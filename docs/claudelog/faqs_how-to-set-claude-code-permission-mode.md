Skip to main content
Claude Code permission modes control how Claude handles tool usage permissions. Configure the default mode in settings files to customize permission behavior for your workflow.
### Available Permission Modes​
  * **default** - Standard behavior with prompts for permission on first use of each tool
  * **acceptEdits** - Automatically accepts file edit permissions for the session
  * **plan** - Plan mode where Claude can analyze but not modify files or execute commands
  * **bypassPermissions** - Skips all permission prompts (requires safe environment)


### Configuration Files​
**Settings file hierarchy** (higher priority overrides lower):
  * **Enterprise settings** - `/Library/Application Support/ClaudeCode/managed-settings.json` (macOS) or `/etc/claude-code/managed-settings.json` (Linux/WSL)
  * **Local project settings** - `.claude/settings.local.json` (auto-ignored by git, personal preferences)
  * **Project settings** - `.claude/settings.json` (checked into source control, team defaults)
  * **User settings** - `~/.claude/settings.json` (applies to all projects)


### How to Configure​
**Set the defaultMode in any settings.json file:**
```
{"defaultMode":"acceptEdits"}
```

**Complete configuration example:**
```
{"defaultMode":"plan","permissions":{"allow":["Bash(npm run test:*)","Read(~/.zshrc)"]}}
```

### When to Use Each Mode​
**Use default mode for:**
  * **General development** - Standard workflow with permission control
  * **Learning Claude Code** - Understand what tools Claude wants to use


**Use acceptEdits mode for:**
  * **Trusted projects** - Streamlined editing without constant prompts
  * **Rapid prototyping** - Faster iteration cycles


**Use plan mode for:**
  * **Code review** - Analysis without modifications
  * **Exploration** - Understanding codebases safely


**Use bypassPermissions mode for:**
  * **Automated environments** - CI/CD pipelines and scripts
  * **Sandbox development** - Isolated, safe environments only


##### Safety Warning
Never use bypassPermissions mode in production or with sensitive codebases. This mode skips all safety checks and can lead to unintended modifications or security issues.
Always start with default mode and adjust based on your specific workflow needs.
![Custom image](https://www.claudelog.com/img/discovery/029_wind.png)
**See Also** : Auto-Accept Permissions|Plan Mode|Configuration Guide
  * Available Permission Modes
  * Configuration Files
  * How to Configure
  * When to Use Each Mode


