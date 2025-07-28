Skip to main content
Claude Code provides two methods for updating permissions: the interactive `/permissions` command for real-time management, and manual configuration file editing for persistent setup. Both methods control which tools Claude can use without prompts.
### How to Use It​
**Interactive Method (Recommended):**
```
# Launch the permissions interface/permissions
```

**Manual Configuration:** Edit your `~/.claude.json` file to add or modify allowed tools:
```
{"projects":{"/path/to/your/project":{"allowedTools":["Read","Grep","Bash(git log:*)","Edit","MultiEdit","Write"]}}}
```

### Why Use It​
The `/permissions` interface provides real-time permission management with a fluid, responsive experience that makes configuration changes effortless. No need to restart Claude Code or manually edit configuration files when you need to adjust tool access during active sessions.
**Interactive Benefits:**
  * **Real-Time Updates** - Changes apply immediately without restarting Claude Code
  * **Visual Navigation** - Intuitive UI instead of JSON file editing
  * **Current Status** - View which tools are currently allowed or denied
  * **Explicit Control** - Grant or block access to specific tools or patterns
  * **No Manual Editing** - Avoid syntax errors in configuration files


**Manual Configuration Benefits:**
  * **Bulk Configuration** - Set up multiple projects or complex tool patterns
  * **Documentation** - Clear record of permission decisions and rationale


### Benefits​
**Configuration Flexibility:**
  * **Multiple Locations** - Project-specific `.claude/settings.local.json` or project-specific `~/.claude.json` stored globally (recommended for reliability)
  * **Pattern Matching** - Restrict tools to specific commands like `Bash(git log:*)` for safety
  * **Granular Control** - Allow read operations while requiring prompts for write operations
  * **Tool Categories** - Configure entire tool families or individual commands


Both methods create workflow transparency by making permission decisions explicit and auditable, ensuring you understand exactly which operations are automated versus requiring oversight.
Configuration Priority
Use `~/.claude.json` for reliability as the primary configuration location. Multiple file locations exist due to legacy compatibility.
Safety Patterns
Consider allowing `Read`, `Grep`, and `LS` for research while restricting `Bash` and `Edit` operations to maintain safety controls where needed.
##### Real-Time Permission Management
The /permissions interface enables fluid configuration changes without restarting Claude Code sessions. Use ~/.claude.json for persistent reliability across different projects and configurations.
![Custom image](https://www.claudelog.com/img/discovery/021_happy.png)
**See Also** : Configuration Guide|Allowed Tools|Auto-Accept Permissions
  * How to Use It
  * Why Use It
  * Benefits


