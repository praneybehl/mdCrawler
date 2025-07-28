Skip to main content
Claude Code installs globally via `npm` with the main application files in your system's global node_modules directory and configuration files stored in the `~/.claude/` directory for easy access and management.
### Installation Locations​
  * **Main Application** : Global npm installation directory (varies by system)
  * **User Settings** : `~/.claude/settings.json` (applies to all projects)
  * **Project Settings** : `.claude/settings.json` (shared with team, checked into source control)
  * **Personal Settings** : `.claude/settings.local.json` (personal preferences, not checked in)


### Configuration Files​
**User Settings** - `~/.claude/settings.json` contains global settings that apply to all projects.
**Project Settings** - `.claude/settings.json` stores project-specific configurations shared with your team.
**Personal Settings** - `.claude/settings.local.json` contains personal preferences that are not checked into source control.
**Project Instructions** - `CLAUDE.md` files provide project-specific guidance and workflow instructions.
### Verification Commands​
```
# Check installation locationwhich claude# View global packagesnpm list -g --depth=0 | grep claude-code# Check user configurationcat ~/.claude/settings.json
```

I store my configuration files in the standard locations to ensure Claude Code can access them consistently across different terminal sessions and projects. The hierarchical settings system allows for global defaults with project-specific overrides.
Configuration Management
Keep your `~/.claude/settings.json` file secure as it may contain sensitive settings. Use `.claude/settings.local.json` for personal API keys that shouldn't be shared with your team.
##### Hierarchical Configuration System
Global npm installation with hierarchical settings system for team and personal configurations. Use ~/.claude/settings.json for global defaults with project-specific overrides for flexibility.
![Custom image](https://www.claudelog.com/img/discovery/013.png)
**See Also** : Download Claude Code|Configuration Guide|Global Settings
  * Installation Locations
  * Configuration Files
  * Verification Commands


