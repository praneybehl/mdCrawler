# 📚 mdCrawler - Documentation to Markdown Converter

🤖 **Perfect for AI Coding Assistants!**
 
Want to supercharge your AI coding experience? mdCrawler helps you provide the perfect context to your AI coding agents:
1. Run mdCrawler to download documentation for the technologies you're using
2. Place the generated Markdown docs in your project's `/docs` folder
3. Now tools like Cursor, Augment, Windsurf, Traycer, Codebuff and others can access the full context of your dependencies!

No more incomplete or outdated context - give your AI the documentation it needs to help you code better!
PSSTTT : We already have fetched some docs for you :), check out our output folder to see the result
PSSSTTT2 : Don't know where to begin ? Check out our easycommand.txt

> Built with ❤️ using [Crawl4AI](https://github.com/unclecode/crawl4ai), the powerful open-source web crawler (30.5k+ ⭐)

Transform entire documentation websites into a clean, organized collection of Markdown files with a single command. mdCrawler leverages the power of Crawl4AI to automatically process documentation sites and convert them into well-structured Markdown files while preserving the original structure.

## 💬 Join Our Community!

Join our vibrant Discord community [AiCodingBattle](https://discord.gg/TH8V5b5rGR) where we:
- Share daily news about AI and coding tools
- Exchange expertise and best practices
- Connect with fellow AI enthusiasts

## 🎯 What it Does

Give it a documentation URL, and mdCrawler will:
1. 🗺️ Check for sitemaps to discover all documentation pages efficiently
2. 🔍 Automatically discover pages through link crawling (if no sitemap)
3. 📥 Download and process each page
4. ✨ Convert the content to clean Markdown
5. 📁 Save everything in an organized folder structure

Perfect for:
- 📖 Offline documentation reading
- 📝 Content migration projects
- 🔄 Documentation backups
- 🎨 Custom documentation styling
    
## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/AiCodingBattle/mdCrawler.git
cd mdCrawler

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install browser dependencies
python -m playwright install
```

### Single Documentation Site

You can use either format:
```bash
# Using positional arguments (original format)
python main.py https://docs.python.org/fr/3/ python-docs

# Using named arguments
python main.py --url https://docs.python.org/fr/3/ --name python-docs

# Disable sitemap discovery (use link crawling only)
python main.py --no-sitemap --url https://docs.python.org/fr/3/ --name python-docs
```

### Multiple Documentation Sites

```bash
# Convert multiple documentation sites using a YAML config
python main.py --config libraries_extended.yaml
```

Your converted documentation will be available in the `docs/` directory!

### 🗺️ Sitemap Support

mdCrawler now automatically discovers and uses sitemaps for more efficient crawling:

- **Automatic Discovery**: Checks common sitemap locations (`/sitemap.xml`, `/sitemap_index.xml`, etc.)
- **Sitemap Index Support**: Handles sites with multiple sitemaps
- **Efficient Crawling**: Gets all URLs upfront instead of discovering incrementally
- **Fallback Mode**: Automatically falls back to link discovery if no sitemap is found
- **Manual Override**: Use `--no-sitemap` to force link discovery mode

Benefits of sitemap crawling:
- ⚡ Faster - knows all pages upfront
- 📊 More complete - ensures no pages are missed
- 🎯 More efficient - no need to crawl pages just to find links
- 📈 Progress tracking - shows accurate progress (e.g., "Processing [23/150]")

## 📖 Examples

Here are some examples of how to use mdCrawler with popular documentation sites:

### Claudelog
```bash
# Convert Claudelog docs to Markdown
python main.py https://claudelog.com/ claudelog
```

### Pocketbase Documentation
```bash
# Convert Pocketbase docs to Markdown
python main.py https://claudelog.com/ pocketbase
```

### Supabase Documentation
```bash
# Convert Supabase docs to Markdown
python main.py https://supabase.com/docs supabase-docs
```
This will create a complete Markdown version of Supabase's documentation, including:
- Authentication guides
- Database documentation
- API references
- Getting started guides

### Stripe Documentation
```bash
# Convert Stripe docs to Markdown
python main.py https://docs.stripe.com stripe-docs
```
Perfect for creating offline copies of:
- Payment integration guides
- API documentation
- Product documentation
- Testing guides

### Crawl4AI Documentation
```bash
# Convert Crawl4AI docs to Markdown
python main.py https://docs.crawl4ai.com crawl4ai-docs
```
Useful for:
- Offline reference
- Contributing to the project
- Custom documentation styling

### SvelteKit Documentation
```bash
# Convert SvelteKit docs to Markdown
python main.py https://svelte.dev/docs/kit sveltekit-docs
```
Great for:
- Learning materials
- Framework documentation
- Component guides

Each conversion will maintain the original documentation structure and create clean, well-formatted Markdown files in their respective output directories.

## 📋 Requirements

- Python 3.8 or higher (Install via Windows Store for Windows users)
- pip (Python package manager)

## 📋 Extended Library Support

mdCrawler now includes an extensive library of pre-configured documentation sources covering:

- **Programming Languages**: Python, Java, C++, Rust, Go
- **Web Frameworks**: Django, Flask, FastAPI, Express.js, Rails
- **Database Systems**: PostgreSQL, MySQL, MongoDB, Redis
- **AI/ML Frameworks**: TensorFlow, PyTorch, Hugging Face, LangChain
- **Cloud & DevOps**: Docker, Kubernetes, Terraform
- **Frontend Frameworks**: React, Vue, Angular, Svelte
- **And many more!**

To use the extended library:

1. Check `libraries_extended.yaml` for available documentation sources
2. Run with the config file to process multiple sites:
```bash
python main.py --config libraries_extended.yaml
```

## 📂 Output Structure

```
docs/
└── your-docs/
    ├── index.md              # Main documentation page
    ├── getting-started.md    # Each page becomes a Markdown file
    └── api/                  # Original structure is preserved
        ├── overview.md
        └── reference.md
```

## 🛠️ Built With

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - The backbone of our crawler, providing powerful web crawling capabilities
- [Playwright](https://playwright.dev/) - Browser automation
- Python 3.8+

## 🙏 Acknowledgments

This project would not be possible without:
- [Crawl4AI](https://github.com/unclecode/crawl4ai) and its amazing community
- The incredible work of [@unclecode](https://github.com/unclecode) and all Crawl4AI contributors
- Everyone who has contributed to making web crawling more accessible

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Support

If you find this tool useful, please consider giving it a star on GitHub!