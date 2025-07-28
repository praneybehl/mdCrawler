Skip to main content
Adding MCP (Model Context Protocol) servers to Claude Code extends its capabilities with external tools, APIs, and resources. I add MCP servers to give Claude access to web search, documentation, and specialized services during development.
### Quick Steps to Add MCP​
**Step 1: Create Configuration File**
```
# Navigate to your home directorycd ~# Create or edit the Claude configurationnano .claude.json
```

**Step 2: Add MCP Server Configuration**
```
{"projects":{"/your/project/path":{"mcpServers":{"brave-search":{"command":"npx","args":["-y","@modelcontextprotocol/server-brave-search"]}}}}}
```

**Step 3: Restart Claude Code**
```
# Exit current sessionexit# Start Claude Code againclaude --continue
```

That's it! Claude now has access to the MCP server capabilities.
### Popular MCP Servers to Add​
**Web Search Access** - Add Brave Search for real-time information:
```
"brave-search":{"command":"npx","args":["-y","@modelcontextprotocol/server-brave-search"]}
```

**Documentation Access** - Add Context7 for up-to-date API references:
```
"context7":{"command":"npx","args":["-y","context7-mcp"]}
```

**File System Access** - Add filesystem MCP for broader file operations:
```
"filesystem":{"command":"npx","args":["-y","@modelcontextprotocol/server-filesystem","/path/to/allowed/directory"]}
```

### Verify MCP is Working​
**Test the connection** - Ask Claude to use the new capability:
```
"Search for the latest React 19 features"
```

##### Extended Capability Integration
MCP servers add external functionality like web search and API access through simple JSON configuration. Start with Brave Search for immediate visible benefits to development workflows.
![Custom image](https://www.claudelog.com/img/discovery/019.png)
**See Also** : MCP Server Setup|What is MCP|Context7 MCP|Brave Search MCP|Configuration Guide
Start Simple
Add one MCP server at a time to test functionality. I recommend starting with Brave Search since it provides immediate, visible benefits for development workflows.
  * Quick Steps to Add MCP
  * Popular MCP Servers to Add
  * Verify MCP is Working


