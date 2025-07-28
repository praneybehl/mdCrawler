Skip to main content
On this page
**Reddit content access and analysis for Claude Code workflows**
**Author** : Hawstein | GitHub Repo | 69 Stars|13 Forks|MIT License|Updated Jul 22, 2025
### Overview​
Reddit MCP provides access to Reddit's public API for Claude Code, enabling content analysis, community research, and social media insights through the Model Context Protocol. Browse subreddits, read posts and comments, and analyze Reddit discussions seamlessly.
### Features​
  * **Frontpage Access** - Browse Reddit's frontpage and trending posts
  * **Subreddit Browsing** - Access posts, comments, and community data from any subreddit
  * **Hot Posts Retrieval** - Get the most popular posts from specific communities
  * **Post Details** - Fetch detailed information about specific posts and their metadata
  * **Comment Trees** - Access comment threads and discussion hierarchies
  * **Public API Access** - No authentication required for public content


### Installation​
**Prerequisites**
  * Python environment for the MCP server


**Setup MCP Server**
```
# Install via Pythonpython -m pip install mcp-server-reddit# Or clone and install from sourcegit clone https://github.com/Hawstein/mcp-server-reddit.gitcd mcp-server-redditpip install -e .
```

**Claude Code Configuration**
```
{"projects":{"/path/to/your/project":{"mcpServers":{"reddit":{"type":"stdio","command":"node","args":["/path/to/reddit-mcp-server/build/index.js"],"env":{}}}}}}
```

### Usage​
**Content Discovery**
```
# Browse Reddit frontpageclaude "Show me the current top posts on Reddit's frontpage"# Access specific subreddit contentclaude "Get the top 10 posts from r/programming today"
```

**Community Analysis**
```
# Analyze post engagementclaude "Analyze the comment patterns in r/MachineLearning posts"# Track technology discussionsclaude "Find discussions about AI coding tools across relevant subreddits"
```

**Research and Monitoring**
```
# Competitive researchclaude "Research what developers are saying about different code editors"# Trend analysisclaude "Analyze recent trends in web development discussions"
```

For complete API reference and advanced usage patterns, see the official documentation.
##### Extensibility
Reddit MCP provides a great foundation for additional functionality. The repository can be easily extended to accommodate custom functionality beyond the default API methods.
![Custom image](https://www.claudelog.com/img/discovery/003.png)
_Reddit MCP is developed by Hawstein as a community project. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


