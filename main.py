import os
import argparse
import logging
import asyncio
from crawl4ai import AsyncWebCrawler
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

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
        # Start crawling
        logger.info("Starting to crawl pages...")
        try:
            # Crawl all pages under the same domain
            base_domain = urlparse(url).netloc
            logger.info(f"Base domain: {base_domain}")
            
            results = await crawler.arun_many(
                url,
                max_pages=1000,  # Adjust this number based on your needs
                same_domain=True,  # Only crawl pages from the same domain
                max_depth=15  # Adjust the depth of crawling
            )
            
            logger.info(f"Successfully retrieved {len(results)} pages")
            
            # Process each page
            for result in results:
                try:
                    # Generate a safe filename from the URL
                    filename = get_safe_filename(result.url)
                    logger.info(f"Processing page: {result.url} -> {filename}")
                    
                    # Save markdown content
                    output_path = output_dir / filename
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(result.markdown)
                    logger.info(f"Successfully saved: {output_path}")
                    
                except Exception as e:
                    logger.error(f"Error processing page {result.url}: {str(e)}")
                    continue
            
        except Exception as e:
            logger.error(f"Error during crawling: {str(e)}")
            raise

    logger.info(f"Crawling completed. Output directory: {output_dir}")

async def async_main():
    parser = argparse.ArgumentParser(description="Crawl documentation and convert to markdown")
    parser.add_argument("url", help="URL of the documentation website")
    parser.add_argument("name", help="Name of the output directory")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--max-pages", type=int, default=100, help="Maximum number of pages to crawl")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of crawling")
    
    args = parser.parse_args()
    
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")

    try:
        await crawl_documentation(args.url, args.name)
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main() 