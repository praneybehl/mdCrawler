Skip to main content
Claude Code stores configuration settings in multiple JSON files depending on scope and priority. Understanding these locations helps you configure permissions, MCP servers, and tool access across different projects and user environments.
### Configuration File Locations​
**Global Configuration Files** - Claude Code uses a hierarchy of configuration files with different scopes and priorities:
```
# Main global configuration (highest priority)~/.claude.json# User-specific global settings~/.claude/settings.json# User-specific local settings~/.claude/settings.local.json# Project-specific settings (in your project directory).claude/settings.local.json
```

### Why Multiple Configuration Files​
**Flexible Configuration Hierarchy** - Multiple configuration files allow you to set global defaults while overriding specific settings for individual projects or local environments.
**Security and Permissions** - Different configuration scopes enable you to maintain secure global settings while allowing project-specific tool access and MCP server configurations.
**Environment Management** - Separate configuration files help manage different development environments, from local testing to production deployments.
**Benefits:**
  * **Hierarchical Priority** - Project-specific settings override user settings, which override global settings
  * **Security Isolation** - Dangerous permissions can be limited to specific projects rather than global access
  * **Environment Flexibility** - Different configurations for development, testing, and production environments
  * **Team Collaboration** - Project-specific settings can be shared while maintaining individual user preferences
  * **MCP Server Management** - Configure different MCP servers for different projects and environments
  * **Tool Access Control** - Granular control over which tools are available in different contexts


**Common Configuration Examples:**
```
// ~/.claude.json (recommended for global settings){"projects":{"/path/to/project":{"allowedTools":["Task","Bash","Read","Edit"],"mcpServers":{"filesystem":{"command":"npx","args":["-y","@modelcontextprotocol/server-filesystem"]}}}}}
```

Configuration Priority
Settings are applied in order of specificity: project-specific → user local → user global → main global. More specific settings override broader ones.
Security Recommendation
Use `~/.claude.json` for global settings and project-specific `.claude/settings.local.json` for dangerous permissions like unrestricted Bash access.
##### Configuration Hierarchy
Multiple configuration files enable global defaults with project-specific overrides for security isolation. Use ~/.claude.json for global settings and project-specific files for dangerous permissions.
![Custom image](https://www.claudelog.com/img/discovery/027_japan.png)
**See Also** : Configuration Guide|Update Permissions|Allowed Tools
  * Configuration File Locations
  * Why Multiple Configuration Files


