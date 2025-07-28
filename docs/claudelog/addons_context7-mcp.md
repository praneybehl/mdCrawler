Skip to main content
On this page
**Up-to-date code documentation and examples injected directly into your prompts**
**Author** : Upstash | GitHub Repo | 21843 Stars|1108 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Context7 MCP dynamically fetches up-to-date, version-specific documentation and code examples from official sources and injects them directly into your Claude Code prompts. No more outdated API references or hallucinated methods.
### Features​
  * **Real-time Documentation** - Fetches current official documentation from library sources
  * **Version-Specific Content** - Gets documentation for the exact version you're using
  * **Automatic Integration** - Seamlessly injects relevant docs into AI context
  * **Universal Compatibility** - Works with Claude Code, Cursor, Windsurf, and more
  * **Millisecond Response** - Fast documentation lookup and injection


### Installation​
**Prerequisites**
  * Internet connection for documentation fetching


**Setup MCP Server**
```
# Install via NPX (recommended)npx -y @upstash/context7-mcp
```

**Claude Code Configuration**
```
{"projects":{"/path/to/your/project":{"mcpServers":{"Context7":{"command":"npx","args":["-y","@upstash/context7-mcp"]}}}}}
```

### Usage​
**Automatic Documentation Injection**
```
# Context7 automatically detects library referencesclaude "use context7 to help me implement FastAPI authentication"# Gets current FastAPI auth documentationclaude "Show me how to use React hooks with TypeScript"
```

**How It Works**
  1. **Library Detection** - Identifies the library being referenced (e.g., FastAPI, React)
  2. **Version Lookup** - Finds the latest version of official documentation
  3. **Content Parsing** - Extracts relevant documentation and examples
  4. **Context Injection** - Injects current, accurate information into the AI prompt
  5. **Response Generation** - AI responds with up-to-date, version-accurate code


For complete setup guides and supported libraries, see the official documentation.
##### Community Insight
Developers share that Context7 MCP eliminates frustration from outdated AI code suggestions. Instead of debugging deprecated methods, Context7 ensures Claude Code provides current, working examples on first try.
![Custom image](https://www.claudelog.com/img/discovery/009.png)
_Context7 MCP is developed by Upstash and is open-source and free to use. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


