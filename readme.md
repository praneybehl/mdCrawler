# 📚 mdCrawler - Documentation to Markdown Converter

Transform entire documentation websites into a clean, organized collection of Markdown files with a single command. mdCrawler automatically crawls through all pages of a documentation site and converts each page into a well-formatted Markdown file while preserving the original structure.

## 💬 Join Our Community!

Join our vibrant Discord community [AiCodingBattle](https://discord.gg/TH8V5b5rGR) where we:
- Share daily news about AI and coding tools
- Exchange expertise and best practices
- Connect with fellow AI enthusiasts

## 🎯 What it Does

Give it a documentation URL, and mdCrawler will:
1. 🔍 Automatically discover all documentation pages
2. 📥 Download and process each page
3. ✨ Convert the content to clean Markdown
4. 📁 Save everything in an organized folder structure

Perfect for:
- 📖 Offline documentation reading
- 📝 Content migration projects
- 🔄 Documentation backups
- 🎨 Custom documentation styling

## 🚀 Quick Start

```bash
# Install and run in 3 simple steps:
git clone https://github.com/yourusername/mdCrawler.git
python -m playwright install
pip install -r requirements.txt

# Convert an entire documentation site:
python main.py https://docs.python.org/fr/3/ python-docs
```

Your converted documentation will be available in `output/python-docs/`!

## 📋 Requirements

- Python 3.8 or higher (Install via Windows Store for Windows users)
- pip (Python package manager)

## 📂 Output Structure

```
output/
└── your-docs/
    ├── index.md              # Main documentation page
    ├── getting-started.md    # Each page becomes a Markdown file
    └── api/                  # Original structure is preserved
        ├── overview.md
        └── reference.md
```

## 🛠️ Built With

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Powerful web crawling engine
- [Playwright](https://playwright.dev/) - Browser automation
- Python 3.8+

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Support

If you find this tool useful, please consider giving it a star on GitHub!