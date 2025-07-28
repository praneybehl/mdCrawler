import os
import asyncio
import logging
import yaml
import aiohttp
from pathlib import Path
from urllib.parse import urlparse, urljoin
from xml.etree import ElementTree
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def get_safe_filename(url: str) -> str:
    """Convert URL to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path:
        return 'index.md'
    
    # Replace unsafe characters
    safe_name = path.replace('/', '_').replace('\\', '_')
    return f"{safe_name}.md"

def get_url_from_link(link) -> str:
    """Extract URL from a link object."""
    if isinstance(link, str):
        return link
    elif isinstance(link, dict):
        return link.get('href', '')
    return ''

def should_process_url(url: str, base_domain: str) -> bool:
    """Determine if a URL should be processed based on filtering rules."""
    parsed = urlparse(url)
    
    # Skip if not from same domain
    if parsed.netloc != base_domain:
        return False
        
    # Skip fragment URLs
    if '#' in url:
        return False
        
    # For Django docs, skip old versions (customize per documentation site)
    if 'djangoproject.com' in base_domain:
        path_parts = parsed.path.strip('/').split('/')
        if len(path_parts) >= 2 and path_parts[0] == 'en':
            try:
                version = float(path_parts[1])
                if version < 4.0:  # Only process Django 4.0+ docs
                    return False
            except ValueError:
                pass
    
    return True

async def discover_sitemap_urls(base_url: str) -> list:
    """
    Discover and parse sitemap URLs from a website.
    Checks common sitemap locations and returns all found URLs.
    """
    parsed = urlparse(base_url)
    base_domain = f"{parsed.scheme}://{parsed.netloc}"
    
    # Common sitemap locations
    sitemap_locations = [
        urljoin(base_domain, "/sitemap.xml"),
        urljoin(base_domain, "/sitemap_index.xml"),
        urljoin(base_domain, "/sitemap.xml.gz"),
        urljoin(base_domain, "/sitemap/"),
        urljoin(base_domain, "/sitemaps.xml"),
    ]
    
    all_urls = []
    
    async with aiohttp.ClientSession() as session:
        for sitemap_url in sitemap_locations:
            try:
                logger.debug(f"Checking sitemap at: {sitemap_url}")
                async with session.get(sitemap_url, timeout=10) as response:
                    if response.status == 200:
                        content = await response.text()
                        logger.info(f"Found sitemap at: {sitemap_url}")
                        
                        # Parse sitemap XML
                        urls = parse_sitemap_content(content, base_domain)
                        
                        # Check if this is a sitemap index
                        if is_sitemap_index(content):
                            logger.info(f"Processing sitemap index at: {sitemap_url}")
                            # Get all sitemap URLs from index
                            sitemap_urls = parse_sitemap_index(content, base_domain)
                            for sub_sitemap_url in sitemap_urls:
                                try:
                                    async with session.get(sub_sitemap_url, timeout=10) as sub_response:
                                        if sub_response.status == 200:
                                            sub_content = await sub_response.text()
                                            sub_urls = parse_sitemap_content(sub_content, base_domain)
                                            all_urls.extend(sub_urls)
                                            logger.info(f"Found {len(sub_urls)} URLs in {sub_sitemap_url}")
                                except Exception as e:
                                    logger.warning(f"Error fetching sub-sitemap {sub_sitemap_url}: {str(e)}")
                        else:
                            all_urls.extend(urls)
                            logger.info(f"Found {len(urls)} URLs in sitemap")
                        
                        # If we found a sitemap, don't check other locations
                        break
                        
            except Exception as e:
                logger.debug(f"No sitemap found at {sitemap_url}: {str(e)}")
                continue
    
    # Remove duplicates while preserving order
    seen = set()
    unique_urls = []
    for url in all_urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)
    
    return unique_urls

def is_sitemap_index(content: str) -> bool:
    """Check if the XML content is a sitemap index."""
    return '<sitemapindex' in content

def parse_sitemap_index(content: str, base_domain: str) -> list:
    """Parse sitemap index XML and extract sitemap URLs."""
    urls = []
    try:
        root = ElementTree.fromstring(content)
        # Handle namespace
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # Find all sitemap locations
        for sitemap in root.findall('.//ns:sitemap', namespace):
            loc = sitemap.find('ns:loc', namespace)
            if loc is not None and loc.text:
                urls.append(loc.text.strip())
    except Exception as e:
        logger.error(f"Error parsing sitemap index: {str(e)}")
    
    return urls

def parse_sitemap_content(content: str, base_domain: str) -> list:
    """Parse sitemap XML content and extract URLs."""
    urls = []
    try:
        root = ElementTree.fromstring(content)
        # Handle namespace
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # Find all URL locations
        for url_elem in root.findall('.//ns:url', namespace):
            loc = url_elem.find('ns:loc', namespace)
            if loc is not None and loc.text:
                url = loc.text.strip()
                # Only include URLs from the same domain
                if urlparse(url).netloc == urlparse(base_domain).netloc:
                    urls.append(url)
    except Exception as e:
        logger.error(f"Error parsing sitemap: {str(e)}")
    
    return urls

async def crawl_documentation(url: str, name: str, timeout: int = 1800, use_sitemap: bool = True):  # 30 minute timeout
    """
    Crawl a documentation website and save all pages as markdown files.
    
    Args:
        url (str): The URL of the documentation website
        name (str): Name of the output directory where markdown files will be saved
        timeout (int): Maximum time in seconds to spend crawling (default: 30 minutes)
        use_sitemap (bool): Whether to attempt to discover and use sitemap (default: True)
    """
    logger.info(f"Starting crawl process for URL: {url}")
    logger.info(f"Output will be saved in: docs/{name}")
    logger.info(f"Sitemap discovery: {'enabled' if use_sitemap else 'disabled'}")

    # Create output directory
    output_dir = Path(f"docs/{name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created output directory: {output_dir}")

    start_time = datetime.now()
    
    # Get base domain for filtering
    base_domain = urlparse(url).netloc
    logger.info(f"Base domain: {base_domain}")
    
    # Try to discover URLs from sitemap first
    sitemap_urls = []
    if use_sitemap:
        logger.info("Attempting to discover sitemap URLs...")
        sitemap_urls = await discover_sitemap_urls(url)
        if sitemap_urls:
            logger.info(f"Discovered {len(sitemap_urls)} URLs from sitemap")
            # Filter sitemap URLs based on our rules
            filtered_sitemap_urls = [u for u in sitemap_urls if should_process_url(u, base_domain)]
            logger.info(f"Filtered to {len(filtered_sitemap_urls)} URLs after applying rules")
            sitemap_urls = filtered_sitemap_urls
        else:
            logger.info("No sitemap found, falling back to link discovery mode")
    
    # Configure browser for better performance and reliability
    browser_cfg = BrowserConfig(
        headless=True
    )
    
    # Configure crawler with less restrictive filtering
    link_extraction_cfg = CrawlerRunConfig(
        word_count_threshold=0,  # No minimum word count for link extraction
        excluded_tags=[],  # Don't exclude any tags for link discovery
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.1),  # Very permissive threshold
            options={"ignore_links": False}
        ),
        cache_mode="BYPASS"
    )

    content_extraction_cfg = CrawlerRunConfig(
        word_count_threshold=15,  # Higher threshold to filter small text blocks like menus
        excluded_tags=[
            # Base HTML elements
            "script", "style", "nav", "header", "footer", "aside",
            # Navigation and menu selectors
            ".sidebar", "#sidebar", ".menu", "#menu", ".navigation", "#navigation",
            # Documentation specific selectors
            "[role='navigation']", ".nav-menu", ".nav-list", ".table-of-contents",
            ".toc", "#toc", ".site-nav", ".site-menu", ".docs-nav", ".docs-menu",
            # Specific to documentation platforms
            # Mintlify (firecrawl)
            ".mintlify-nav", ".docs-sidebar", ".navigation-menu", ".nav-groups",
            ".nav-wrapper", ".nav-container", ".navigation-wrapper",
            # MkDocs (crawl4ai)
            ".md-nav", ".md-sidebar", ".md-header", ".md-footer", ".md-tabs",
            ".md-search", ".md-search-result", ".md-source", ".md-header-nav",
            ".md-main__inner > nav", ".md-nav__title", ".md-nav__list",
            ".terminal-mkdocs", ".terminal-mkdocs-nav", ".terminal-mkdocs-sidebar",
            # Generic doc elements
            ".search-box", ".search-wrapper", ".ctrl-key", ".keyboard-shortcut",
            ".version-selector", ".version-info", ".metadata-bar",
            # Additional navigation patterns
            "*[class*='sidebar']", "*[class*='navigation']", "*[class*='nav-']",
            "*[id*='sidebar']", "*[id*='navigation']", "*[id*='nav-']",
            "*[class*='menu']", "*[id*='menu']"
        ],
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(threshold=0.3),
            options={
                "ignore_links": True,
                "ignore_navigation": True,
                "main_content_only": True,
                "remove_navigation_elements": True,
                "clean_documentation_artifacts": True,
                "strip_empty_headings": True,
                "remove_duplicate_content": True
            }
        ),
        cache_mode="BYPASS"
    )
    
    # Initialize crawler
    logger.info("Initializing AsyncWebCrawler...")
    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        try:
            processed_urls = set()  # Keep track of processed URLs to avoid duplicates
            
            # If we have sitemap URLs, use them
            if sitemap_urls:
                logger.info(f"Processing {len(sitemap_urls)} URLs from sitemap...")
                urls_to_process = sitemap_urls
                
                # Still process the main page if it's not in the sitemap
                if url not in sitemap_urls:
                    urls_to_process = [url] + sitemap_urls
            else:
                # Fall back to the original link discovery approach
                logger.info("Using link discovery mode...")
                
                # First get all links from the main page with less restrictive config
                main_result = await crawler.arun(url, config=link_extraction_cfg)
                internal_links = main_result.links.get("internal", [])
                logger.info(f"Found {len(internal_links)} internal links")
                
                # Start with the main URL
                urls_to_process = [url]
                
                # Add discovered links
                for link in internal_links:
                    link_url = get_url_from_link(link)
                    if link_url and should_process_url(link_url, base_domain):
                        urls_to_process.append(link_url)
            
            # Process all URLs
            for idx, current_url in enumerate(urls_to_process, 1):
                # Check timeout
                if (datetime.now() - start_time).total_seconds() > timeout:
                    logger.warning(f"Timeout reached after {timeout} seconds. Stopping crawl.")
                    break

                try:
                    if current_url in processed_urls:
                        continue
                    
                    logger.info(f"Processing [{idx}/{len(urls_to_process)}]: {current_url}")
                    
                    # Add delay between requests to be polite
                    await asyncio.sleep(0.5)  # 500ms delay between requests
                    
                    # Use content extraction config for the actual page content
                    result = await crawler.arun(current_url, config=content_extraction_cfg)
                    
                    if result and result.success:
                        filename = get_safe_filename(current_url)
                        output_path = output_dir / filename
                        
                        with open(output_path, "w", encoding="utf-8") as f:
                            f.write(result.markdown)
                        logger.info(f"Successfully saved: {output_path}")
                        processed_urls.add(current_url)
                    else:
                        logger.warning(f"Failed to process {current_url}")
                        
                except Exception as e:
                    logger.error(f"Error processing URL {current_url}: {str(e)}")
                    continue
            
            logger.info(f"Total pages processed: {len(processed_urls)}")
            
        except Exception as e:
            logger.error(f"Error during crawling: {str(e)}")
            raise

    logger.info(f"Crawling completed. Output directory: {output_dir}")

async def crawl_multiple_libraries(config_file: str):
    """
    Crawl multiple documentation websites based on a configuration file.
    
    Args:
        config_file (str): Path to the YAML configuration file containing library definitions
    """
    logger.info(f"Loading library configuration from: {config_file}")
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading configuration file: {str(e)}")
        raise

    if not config or 'libraries' not in config:
        raise ValueError("Invalid configuration file: 'libraries' section not found")

    libraries = config['libraries']
    if not libraries:
        logger.warning("No libraries defined in configuration file")
        return

    total_libraries = len(libraries)
    for idx, library in enumerate(libraries, 1):
        if not isinstance(library, dict) or 'name' not in library or 'url' not in library:
            logger.warning(f"Skipping invalid library entry: {library}")
            continue

        name = library['name']
        url = library['url']
        
        logger.info(f"\n{'='*50}")
        logger.info(f"Processing library {idx}/{total_libraries}: {name}")
        logger.info(f"{'='*50}")
        
        try:
            await crawl_documentation(url, name, use_sitemap=True)
        except Exception as e:
            logger.error(f"Error processing library {name}: {str(e)}")
            logger.error("Moving to next library...")
            # Sleep for a few seconds before trying the next library
            await asyncio.sleep(5)
            continue

    logger.info(f"\nCompleted processing all libraries ({total_libraries} total)")
    logger.info("Check the 'docs' directory for the generated documentation")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Crawl documentation and convert to markdown")
    parser.add_argument("--config", help="Path to libraries configuration file (YAML)")
    parser.add_argument("--url", help="URL of a single documentation website")
    parser.add_argument("--name", help="Name of the output directory for single website")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--no-sitemap", action="store_true", help="Disable sitemap discovery and use link crawling only")
    
    # Add support for positional arguments
    parser.add_argument("url_pos", nargs="?", help="URL of documentation website (positional)")
    parser.add_argument("name_pos", nargs="?", help="Output directory name (positional)")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        use_sitemap = not args.no_sitemap
        
        if args.config:
            # Process multiple libraries from config file
            asyncio.run(crawl_multiple_libraries(args.config))
        elif args.url and args.name:
            # Process single library with named parameters
            asyncio.run(crawl_documentation(args.url, args.name, use_sitemap=use_sitemap))
        elif args.url_pos and args.name_pos:
            # Process single library with positional parameters
            asyncio.run(crawl_documentation(args.url_pos, args.name_pos, use_sitemap=use_sitemap))
        else:
            parser.error("Either --config or URL and name must be provided (either as named or positional arguments)")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main()