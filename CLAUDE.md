# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

mdCrawler is a documentation-to-markdown converter built with Crawl4AI that transforms entire documentation websites into clean, organized collections of Markdown files. It's designed to help AI coding assistants by providing them with up-to-date documentation context.

## Architecture

The project is a Python command-line tool with:
- **Main entry point**: `main.py` - handles CLI arguments and orchestrates crawling
- **Core crawler**: Uses AsyncWebCrawler from Crawl4AI library with custom configurations
- **Sitemap discovery**: Automatic sitemap.xml discovery and parsing for efficient crawling
- **Markdown generation**: Leverages DefaultMarkdownGenerator with PruningContentFilter for clean output
- **Configuration**: YAML-based configuration files (`libraries.yaml`, `libraries_extended.yaml`) for batch processing

Key architectural decisions:
- Async/await pattern for concurrent crawling
- Sitemap-first approach with fallback to link discovery
- Separate configurations for link extraction vs content extraction
- Domain-based filtering to stay within documentation boundaries
- Extensive tag exclusion list to remove navigation elements

## Common Development Commands

```bash
# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
python -m playwright install

# Run single documentation site (with automatic sitemap discovery)
python main.py https://docs.example.com example-docs
# or
python main.py --url https://docs.example.com --name example-docs

# Disable sitemap and use link crawling only
python main.py --no-sitemap --url https://docs.example.com --name example-docs

# Run multiple sites from config
python main.py --config libraries_extended.yaml

# Enable debug logging
python main.py --debug --url https://docs.example.com --name example-docs
```

## Key Configuration Points

### Sitemap Discovery
The crawler now checks for sitemaps at common locations:
- `/sitemap.xml`
- `/sitemap_index.xml`
- `/sitemap.xml.gz`
- `/sitemap/`
- `/sitemaps.xml`

Handles both regular sitemaps and sitemap indexes. Falls back to link discovery if no sitemap is found.

### Content Filtering
The crawler uses two distinct configurations:
1. **Link extraction**: Minimal filtering to discover all pages
2. **Content extraction**: Aggressive filtering to remove navigation/menus

### Excluded Tags
The system excludes numerous navigation-related tags and selectors to ensure clean content extraction, including:
- Generic navigation elements (nav, header, footer, aside)
- Documentation platform-specific elements (MkDocs, Mintlify, etc.)
- Dynamic selectors using wildcards for navigation patterns

### URL Processing
- Fragment URLs (#) are skipped
- Domain filtering ensures only same-domain links are processed
- Custom filtering rules per documentation site (e.g., Django version filtering)

## Adding New Documentation Sources

To add new documentation sources, edit `libraries_extended.yaml`:
```yaml
libraries:
  - name: your-docs-name
    url: https://docs.your-site.com
```

## Testing & Debugging

When debugging crawling issues:
1. Use `--debug` flag for verbose logging
2. Check the excluded_tags list if navigation is being included
3. Verify the base domain filtering if pages are being skipped
4. Monitor the timeout (default 30 minutes per site)

## Output Structure

Documentation is saved to `docs/{name}/` with:
- Filenames derived from URL paths (replacing `/` with `_`)
- `index.md` for main pages
- Original URL structure preserved in filenames