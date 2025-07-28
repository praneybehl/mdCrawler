Skip to main content
On this page
**Web automation with AI vision capabilities for Claude Code**
**Author** : Model Context Protocol | GitHub Repo | 61105 Stars|7081 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Puppeteer MCP brings powerful web automation to Claude Code through the Model Context Protocol. Control headless Chrome browsers, scrape dynamic content, and automate complex web workflows with AI vision capabilities to handle cookies, captchas, and interactive elements automatically.
### Features​
  * **AI Vision Integration** - Automatically handle cookies, captchas, and interactive elements
  * **Headless Browser Control** - Launch and control Chrome/Chromium instances programmatically
  * **Dynamic Content Scraping** - Extract data from JavaScript-heavy and SPA applications
  * **High-Quality Markdown** - Convert web pages to well-formatted markdown
  * **Screenshot & PDF Generation** - Capture visual content and generate documents
  * **Form Automation** - Fill out forms, submit data, and handle user interactions


### Installation​
**Prerequisites**
  * Chrome or Chromium browser installed (auto-installed with NPX method)


**Setup MCP Server**
```
# Install via NPX (recommended)npx -y @modelcontextprotocol/server-puppeteer
```

**Claude Code Configuration**
```
{"projects":{"/path/to/your/project":{"mcpServers":{"puppeteer":{"command":"npx","args":["-y","@modelcontextprotocol/server-puppeteer"]}}}}}
```

### Usage​
**Basic Web Automation**
```
# Navigate and extract content with AI visionclaude "Browse to the product page and extract all pricing information"# Handle complex interactions automaticallyclaude "Navigate the login form and extract user dashboard data"
```

**Advanced Automation**
```
# AI-powered form fillingclaude "Fill out the registration form and handle any captchas"# Markdown conversionclaude "Convert the documentation page to high-quality markdown"
```

For detailed automation examples and API reference, refer to the official documentation.
##### Community Feedback
Developers find Puppeteer MCP valuable for complex web interactions that basic scraping tools can't handle. Particularly useful for navigating dynamic content, JavaScript-heavy sites, and automating multi-step workflows.
![Custom image](https://www.claudelog.com/img/discovery/018.png)
_Puppeteer MCP is part of the official Model Context Protocol servers and is licensed under the MIT License. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


