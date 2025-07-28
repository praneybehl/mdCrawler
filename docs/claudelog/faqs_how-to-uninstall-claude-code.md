Skip to main content
Completely remove Claude Code from your system when you no longer need it or want to perform a clean reinstall. The process is straightforward and removes all traces of the installation.
### Basic Uninstall​
**Remove Claude Code globally**
```
npm uninstall -g @anthropic-ai/claude-code
```

This removes the Claude Code package from your system's global npm packages.
### Clean Up Configuration​
**Remove configuration files** (optional if you might reinstall)
```
# Remove main configuration filerm ~/.claude.json# Remove Claude Code directory and all settingsrm -rf ~/.claude/
```

Permanent Deletion
These `rm` commands permanently delete files - there's no recycle bin or undo. If you might reinstall Claude Code later, consider backing up your configuration files first.
These commands remove:
  * **Main config** : `~/.claude.json` with API keys and project settings
  * **Settings directory** : `~/.claude/` containing MCP configurations, local settings, and cached data


**For safer removal** with confirmation prompts:
```
rm -i ~/.claude.jsonrm -ri ~/.claude/
```

### Verify Removal​
**Check that Claude Code is gone**
```
claude --version
```

This should return "command not found" or similar error, confirming successful removal.
##### Clean Removal Process
Complete uninstall includes removing both the npm package and all configuration files. Backup configuration files before permanent deletion if you might reinstall Claude Code later.
![Custom image](https://www.claudelog.com/img/discovery/014.png)
**See Also** : Installation Guide|Getting Started
  * Basic Uninstall
  * Clean Up Configuration
  * Verify Removal


