Skip to main content
On this page
**Social media posting and search capabilities for Claude Code**
**Author** : EnesCinr | GitHub Repo | 252 Stars|30 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Twitter/X MCP enables Claude Code to interact with Twitter through the Model Context Protocol. Post tweets, search for content, and manage social media interactions directly from your Claude Code conversations using Twitter's official API.
### Features​
  * **Tweet Posting** - Create and publish tweets directly from Claude Code
  * **Content Search** - Search Twitter for specific topics, hashtags, and trends
  * **Real-time Integration** - Access current Twitter data and conversations
  * **API-based Access** - Uses official Twitter Developer API for reliable functionality
  * **Secure Authentication** - OAuth-based authentication with API key management


### Installation​
**Prerequisites**
  * Twitter Developer Account and API access
  * Node.js for running the MCP server


**Step 1: Get Twitter API Credentials**
  1. Create a Twitter Developer Account
  2. Create a new app in the Twitter Developer Portal
  3. Generate API keys and access tokens: 
     * API Key
     * API Secret Key
     * Access Token
     * Access Token Secret


**Step 2: Clone and Setup Twitter MCP Server**
```
# Clone the repositorygit clone https://github.com/EnesCinr/twitter-mcp.gitcd twitter-mcp# Install dependenciesnpm install# Build the projectnpm run build
```

**Step 3: Claude Code Configuration**
Edit `~/.claude.json`:
```
{"projects":{"/path/to/your/project":{"mcpServers":{"twitter":{"command":"uv","args":["--directory","/path/to/twitter-mcp-server","run","x-mcp"],"env":{"API_KEY":"your_api_key_here","API_SECRET_KEY":"your_api_secret_key_here","ACCESS_TOKEN":"your_access_token_here","ACCESS_TOKEN_SECRET":"your_access_token_secret_here"}}}}}}
```

**Step 4: Restart and Test**
  1. Restart Claude Code after configuration
  2. Test with a simple search or tweet command


### Usage​
**Tweet Posting**
```
# Post a simple tweetclaude "Post a tweet saying 'Hello from Claude Code!'"# Tweet with hashtagsclaude "Tweet about the latest AI developments with relevant hashtags"
```

**Content Search**
```
# Search for specific topicsclaude "Search Twitter for recent discussions about AI coding tools"# Find trending hashtagsclaude "What are people saying about #ClaudeCode on Twitter?"
```

For detailed API capabilities and advanced usage, refer to the official documentation.
##### Social Media Automation
Transform Twitter into a seamless extension of your development workflow, posting updates and monitoring discussions without leaving your terminal.
![Custom image](https://www.claudelog.com/img/discovery/002.png)
_Twitter/X MCP is developed by EnesCinr as a community project. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


