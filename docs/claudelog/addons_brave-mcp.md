Skip to main content
On this page
**Web search capabilities using Brave's Search API for Claude Code**
**Author** : Model Context Protocol | GitHub Repo | 61105 Stars|7081 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Brave Search MCP provides web search capabilities for Claude Code through Brave's Search API. Perform real-time web searches, get up-to-date information, and access current web content directly from your Claude Code conversations.
### Features​
  * **Real-time Web Search** - Access current web information through Brave's search API
  * **Pagination Support** - Navigate through multiple pages of search results
  * **Advanced Filtering** - Filter results by type, date, and relevance
  * **Privacy-Focused** - Leverage Brave's privacy-first search approach
  * **Smart Fallbacks** - Automatic fallback mechanisms for consistent performance


### Installation​
**Prerequisites**
  * Brave Search API key (get from Brave Search API)


**Setup MCP Server**
```
# Install via NPX (recommended)npx -y @modelcontextprotocol/server-brave-search
```

**Claude Code Configuration**
Edit `~/.claude.json`:
```
{"projects":{"/path/to/your/project":{"mcpServers":{"brave-search":{"command":"npx","args":["-y","@modelcontextprotocol/server-brave-search"],"env":{"BRAVE_API_KEY":"YOUR_API_KEY_HERE"}}}}}}
```

### Usage​
**Basic Web Search**
```
# Search for current informationclaude "Search for the latest developments in AI coding tools"# Get specific technical informationclaude "Find recent documentation about React 18 features"
```

**Advanced Search Queries**
```
# Search with filtersclaude "Search for Python tutorial sites from the last month"# Domain-specific searchesclaude "Find GitHub repositories related to Claude Code"
```

For detailed API reference and advanced usage, refer to the official documentation.
##### Community Preference
Many community members report preferring Brave MCP over Claude Code's native web search functionality, citing better search result quality and more reliable performance for development-related queries.
![Custom image](https://www.claudelog.com/img/discovery/012.png)
_Brave Search MCP is part of the official Model Context Protocol servers. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


