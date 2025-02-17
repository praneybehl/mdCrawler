import os
import asyncio
import logging
from pathlib import Path
from urllib.parse import urlparse
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

async def crawl_documentation(url: str, name: str):
    """
    Crawl a documentation website and save all pages as markdown files.
    
    Args:
        url (str): The URL of the documentation website
        name (str): Name of the output directory where markdown files will be saved
    """
    logger.info(f"Starting crawl process for URL: {url}")
    logger.info(f"Output will be saved in: output/{name}")

    # Create output directory
    output_dir = Path(f"output/{name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Created output directory: {output_dir}")
    
    # Configure browser for better performance
    browser_cfg = BrowserConfig(
        headless=True,
        viewport_width=1920,
        viewport_height=1080
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
        word_count_threshold=15,  # Augmenté pour filtrer les petits blocs de texte comme les menus
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
            # Get base domain for filtering
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain: {base_domain}")
            
            # First get all links from the main page with less restrictive config
            main_result = await crawler.arun(url, config=link_extraction_cfg)
            internal_links = main_result.links.get("internal", [])
            logger.info(f"Found {len(internal_links)} internal links")
            
            # Process the main page with content config
            main_content = await crawler.arun(url, config=content_extraction_cfg)
            main_filename = get_safe_filename(url)
            main_path = output_dir / main_filename
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(main_content.markdown)
            logger.info(f"Saved main page: {main_path}")
            
            # Process each internal link
            processed_urls = {url}  # Keep track of processed URLs to avoid duplicates
            
            for link in internal_links:
                try:
                    link_url = get_url_from_link(link)
                    if not link_url or link_url in processed_urls:
                        continue
                        
                    # Skip fragment URLs (URLs with #)
                    if '#' in link_url:
                        logger.debug(f"Skipping fragment URL: {link_url}")
                        continue
                        
                    # Verify it's from the same domain
                    link_domain = urlparse(link_url).netloc
                    if link_domain != base_domain:
                        logger.debug(f"Skipping external domain: {link_url}")
                        continue
                    
                    logger.info(f"Processing link: {link_url}")
                    # Use content extraction config for the actual page content
                    result = await crawler.arun(link_url, config=content_extraction_cfg)
                    
                    if result and result.success:
                        filename = get_safe_filename(link_url)
                        output_path = output_dir / filename
                        
                        with open(output_path, "w", encoding="utf-8") as f:
                            f.write(result.markdown)
                        logger.info(f"Successfully saved: {output_path}")
                        processed_urls.add(link_url)
                    else:
                        logger.warning(f"Failed to process {link_url}")
                        
                except Exception as e:
                    logger.error(f"Error processing link {link}: {str(e)}")
                    continue
            
            logger.info(f"Total pages processed: {len(processed_urls)}")
            
        except Exception as e:
            logger.error(f"Error during crawling: {str(e)}")
            raise

    logger.info(f"Crawling completed. Output directory: {output_dir}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Crawl documentation and convert to markdown")
    parser.add_argument("url", help="URL of the documentation website")
    parser.add_argument("name", help="Name of the output directory")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        asyncio.run(crawl_documentation(args.url, args.name))
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

if __name__ == "__main__":
    main() 