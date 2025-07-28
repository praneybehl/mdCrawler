Skip to main content
On this page
**Comprehensive browser automation and monitoring toolkit providing real-time web debugging, performance analysis, and automated testing through MCP integration.**
**Author** : AgentDeskAI | GitHub Repo | 5925 Stars|441 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Browser Tools MCP provides a comprehensive suite for browser automation and monitoring through Model Context Protocol integration. It enables real-time browser log monitoring, automated performance analysis, and seamless IDE integration for web development workflows. The server combines browser automation capabilities with detailed debugging tools for enhanced development productivity.
### Features​
  * **Real-Time Browser Monitoring** - Monitor console logs, network requests, and errors directly from IDE
  * **Comprehensive Audit Suite** - SEO, performance, accessibility analysis via Lighthouse integration
  * **Chrome Extension Integration** - Browser extension for seamless data collection and auto-paste functionality
  * **WCAG Compliance Checking** - Automated accessibility testing and compliance reporting
  * **Cursor Integration** - Primarily designed for Cursor with auto-paste functionality
  * **Automated Testing** - Puppeteer-based automation for end-to-end testing scenarios


### Installation​
**Prerequisites**
  * Node.js 14 or higher
  * Chrome browser for extension functionality
  * MCP-compatible IDE (Cursor recommended, VS Code, Claude Desktop)


**Chrome Extension Setup**
  1. Download the extension ZIP from: https://github.com/AgentDeskAI/browser-tools-mcp/releases/download/v1.2.0/BrowserTools-1.2.0-extension.zip
  2. Extract the ZIP file
  3. Open Chrome → Extensions → Enable "Developer mode"
  4. Click "Load unpacked" and select the extracted extension folder
  5. Enable the extension for browser automation features


**MCP Server Setup**
```
# Install and run MCP server (Terminal 1)npx @agentdeskai/browser-tools-mcp@1.2.0# Start local server (Terminal 2) npx @agentdeskai/browser-tools-server@1.2.0
```

**Claude Desktop Configuration**
```
{"mcpServers":{"browser-tools":{"command":"npx","args":["@agentdeskai/browser-tools-mcp@1.2.0"]}}}
```

**Important Notes**
  * Keep both servers running simultaneously
  * Ensure only one Chrome DevTools panel is open
  * Restart Chrome if connectivity issues occur


### Usage​
**Development Workflow**
```
# Example MCP interactions through AI:# "Monitor console errors on the current page"# "Run a Lighthouse audit for performance analysis"# "Check accessibility compliance for form elements"# "Capture network requests for the login flow"
```

The server provides seamless integration between browser debugging and AI-assisted development. You can monitor real-time browser activity, automate testing procedures, and analyze web performance - all through natural language interactions with your AI coding assistant.
**Advanced Features**
  * **Auto-Paste Integration** : Browser extension automatically pastes captured data into Cursor
  * **Performance Monitoring** : Real-time metrics collection and analysis
  * **Error Tracking** : Comprehensive JavaScript error monitoring and reporting
  * **Accessibility Auditing** : WCAG 2.1 compliance checking with detailed reports


##### Community Insight
Browser Tools MCP has earned a 4.8/5 star rating with users praising the auto-paste functionality that "streamlines debugging workflow by automatically sending browser data to Cursor." Real-time monitoring has proven invaluable for frontend developers.
![Custom image](https://www.claudelog.com/img/discovery/022_excite.png)
_Browser Tools MCP is developed by AgentDeskAI and is open-source. For technical support, feature requests, and community discussions, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


