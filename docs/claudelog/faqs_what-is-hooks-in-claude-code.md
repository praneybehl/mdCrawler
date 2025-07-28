Skip to main content
Hooks are user-defined shell commands that automatically execute at specific points in Claude Code's lifecycle, providing deterministic control over behavior and ensuring certain actions always happen without relying on Claude to choose.
For the most up-to-date know-how, see the official hooks documentation.
### How Hooks Work​
Configure hooks in your `~/.claude/settings.json` file to trigger shell commands during specific events like before tool execution, after file edits, or when notifications are sent.
```
{"hooks":{"PreToolUse":[{"matcher":"Bash","hooks":[{"type":"command","command":"echo 'About to run bash command'"}]}]}}
```

### Why Use Hooks​
Hooks provide automated workflow control that happens regardless of Claude's decisions. They enable consistent behavior patterns and integrate Claude Code seamlessly into existing development workflows.
**Benefits:**
  * **Deterministic Control** : Actions happen automatically without Claude choosing
  * **Notification Integration** : Get alerts about tool usage and permission requests
  * **Code Quality** : Auto-format code after edits or enforce conventions
  * **Audit Trail** : Log all executed commands for security and debugging
  * **Workflow Integration** : Connect Claude Code to existing development tools


### Common Hook Events​
**PreToolUse** - Executes before Claude uses any tool (file operations, bash commands, etc.)
**PostToolUse** - Runs after tool completion for cleanup or notifications
**UserPromptSubmit** - Triggers when user submits a prompt
**Notification** - Triggers when Claude sends notifications or requests permissions
**Stop** - Executes when Claude finishes responding to complete workflows
### Simple Example​
Auto-format Python files after Claude edits them:
```
{"hooks":{"PostToolUse":[{"matcher":"Edit","hooks":[{"type":"command","command":"black *.py"}]}]}}
```

### Debugging Hooks​
You can debug your hooks with `claude --debug` or `claude -d`. This provides detailed information about hook execution including actions, errors, and timing data to help troubleshoot hook behavior.
Security Notice
Hooks execute shell commands with full user permissions without confirmation. Ensure your hooks are safe and secure before implementing them.
##### Workflow Automation
Hooks provide deterministic control over Claude Code behavior through automated shell commands. Perfect for notifications, formatting, logging, and workflow integration.
![Custom image](https://www.claudelog.com/img/discovery/006.png)
Early Days
It's early days for hooks! I'm excited to see and document what the community does with this powerful new feature.
**See Also** : Official Hooks Documentation|Configuration|Changelog
  * How Hooks Work
  * Why Use Hooks
  * Common Hook Events
  * Simple Example
  * Debugging Hooks


