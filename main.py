import os
import asyncio
import logging
from pathlib import Path
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'crawler_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
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
    
    # Initialize crawler
    logger.info("Initializing AsyncWebCrawler...")
    async with AsyncWebCrawler() as crawler:
        try:
            # Get base domain for filtering
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain: {base_domain}")
            
            # First get all links from the main page
            main_result = await crawler.arun(url)
            internal_links = main_result.links.get("internal", [])
            logger.info(f"Found {len(internal_links)} internal links")
            
            # Process the main page
            main_filename = get_safe_filename(url)
            main_path = output_dir / main_filename
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(main_result.markdown)
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
                    result = await crawler.arun(link_url)
                    
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