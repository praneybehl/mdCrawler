Skip to main content
Allowed Tools is part of Claude Code's granular permission system that lets you specify which tools Claude can use without permission. Instead of granting blanket access through dangerous skip permissions, you explicitly configure which operations require permission and which do not.
### How to Use It​
Configure allowed tools in your `~/.claude.json` file or use the interactive `/permissions` command for real-time management without editing JSON files manually.
**JSON Configuration:**
```
{"projects":{"/path/to/your/project":{"allowedTools":["Read","Grep","Bash(git log:*)",// Safer: only git log commands"Edit","MultiEdit"]}}}
```

**Interactive Management:**
```
/permissions
```

### Why Use It​
I use allowed tools configuration to create workflow transparency because I understand exactly which operations are automated. You might allow `Read(*)` and `Grep(*)` for research tasks while maintaining prompts for `Bash(*)` and `Edit(*)` operations that modify your system.
**Benefits:**
  * **Granular Control** - Specify exact tools rather than universal access
  * **Security Transparency** - Clear understanding of automated operations
  * **Persistent Configuration** - Consistent behavior across sessions and projects
  * **Audit Trail** - Visible permission structure in configuration files
  * **Interactive Management** - Real-time updates through `/permissions` interface
  * **Pattern Matching** - Restrict tools to specific commands like `Bash(git log:*)`
  * **Principle of Least Privilege** - Grant only necessary permissions


This explicit configuration approach maintains better security awareness compared to blanket permission bypassing, making it easier to audit and adjust permissions as workflow needs change.
Interactive Interface
The `/permissions` command provides a user-friendly UI to view current permissions, explicitly allow or deny tools, and navigate visually without manual JSON editing.
Configuration Locations
Multiple configuration locations exist for flexibility: project-specific `.claude/settings.local.json`, user-specific `~/.claude/settings.json`, or main `~/.claude.json` (recommended for reliability).
##### Granular Permission Control
Allowed Tools provide explicit workflow transparency with principle of least privilege. Use /permissions command for interactive management without manual JSON configuration editing.
![Custom image](https://www.claudelog.com/img/discovery/032_wind.png)
**See Also** : Configuration Guide|Auto-Accept Permissions|Dangerous Skip Permissions
  * How to Use It
  * Why Use It


