Skip to main content
Model Context Protocol (MCP) servers extend Claude Code's capabilities by connecting to external APIs and services. I configure MCP servers to give Claude access to real-time web search through Brave's Search API and up-to-date documentation through Context7, enabling current information retrieval and accurate API references during development workflows.
### How to Use It​
**Configuration File Location** - Create MCP configuration in `~/.claude.json` for reliability:
```
{"projects":{"/path/to/your/project":{"mcpServers":{"brave-search":{"command":"npx","args":["-y","@modelcontextprotocol/server-brave-search"]},"context7":{"command":"npx","args":["-y","context7-mcp"]}}}}}
```

**Alternative Configuration Locations** - MCP servers can also be configured in:
  * `.claude/settings.local.json` (project-specific)
  * `~/.claude/settings.local.json` (user-specific local)
  * `~/.claude/settings.json` (user-specific global)
  * `~/.claude/mcp_servers.json` (dedicated MCP file)


### Why Use MCP Servers​
MCP servers bridge the gap between Claude Code's built-in capabilities and external tools, providing Claude with specialized access to systems and services that enhance coding workflows.
**Benefits:**
  * **Project Customization** - Configure different MCP servers for different projects based on specific needs
  * **External API Access** - Connect Claude to specialized services beyond built-in capabilities
  * **Up-to-Date Information** - Get fresh search results instead of relying on training data cutoffs
  * **Modular Architecture** - Add or remove specific capabilities without affecting core Claude Code functionality


I use MCP servers when I need Claude to access current information that isn't in its training data. Brave Search is particularly useful for finding recent documentation and troubleshooting information, while Context7 provides up-to-date, version-specific API references and code examples directly from official sources.
Configuration Reliability
Use `~/.claude.json` as the primary configuration location rather than the various alternative locations. This approach provides the most consistent behavior across different Claude Code versions.
Server Installation
MCP servers using `npx` commands will automatically install when first accessed. Ensure you have Node.js installed for npm-based MCP servers to function properly.
##### Extended Capability Bridge
MCP servers connect Claude to external APIs providing up-to-date information beyond training data. Use ~/.claude.json for reliable configuration across different projects and server combinations.
![Custom image](https://www.claudelog.com/img/discovery/022_excite.png)
**See Also** : Configuration Guide|Brave Search MCP|Context7 MCP|Add-ons
  * How to Use It
  * Why Use MCP Servers


