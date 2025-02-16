# 📚 mdCrawler - Documentation Crawler

A powerful documentation crawler built on top of [Crawl4AI](https://github.com/unclecode/crawl4ai) that converts documentation websites into well-structured Markdown files.

## 💬 Join Our Community!

Join our vibrant Discord community [AiCodingBattle](https://discord.gg/TH8V5b5rGR) where we:
- Share daily news about AI and coding tools
- Exchange expertise and best practices
- Connect with fellow AI enthusiasts
- Get early access to updates and features

## 🌟 Features

- 🔄 Automatically crawls entire documentation websites
- 📝 Converts HTML documentation to clean Markdown format
- 📁 Maintains the original site structure in the output
- 🎯 Specifically optimized for documentation sites
- 🌐 Works with most modern documentation platforms

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher (Install via Windows Store for Windows users)
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mdCrawler.git
cd mdCrawler
```

2. Install Playwright:
```bash
python -m playwright install
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

The basic syntax to run the crawler is:

```bash
python main.py <documentation-url> <output-name>
```

Example:
```bash
python main.py https://docs.python.org/fr/3/ python-docs
```

The crawler will:
1. Visit the specified documentation URL
2. Crawl all related documentation pages
3. Convert the content to Markdown format
4. Save the files in `output/<output-name>/`

## 📂 Output Structure

The converted documentation will be saved in the `output` directory with the following structure:

```
output/
└── <output-name>/
    ├── page1.md
    ├── page2.md
    └── subdirectory/
        └── page3.md
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