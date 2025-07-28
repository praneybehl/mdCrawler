Skip to main content
Claude Code can be suspended mid-session and resumed later using standard terminal process control commands.
### How to Suspend​
Press `Ctrl+Z` to suspend Claude Code immediately. This pauses the process and returns control to your terminal prompt.
### How to Resume​
Run `fg` in your terminal to bring Claude Code back to the foreground and resume your session exactly where you left off.
### Alternative: Shell Commands from Within Claude Code​
Use `!` prefix to run shell commands without suspending Claude Code:
```
!git status!npm test!ls -la
```

This executes commands directly from Claude Code's prompt without leaving your session.
### When to Use​
**Use`!` commands for:**
  * **Quick shell commands** - `!git status`, `!npm test`, `!ls` without leaving Claude Code
  * **Simple operations** - Single commands that don't require interaction


**Suspend Claude Code when you need to:**
  * **Interactive commands** - Commands requiring input or extended interaction
  * **Switch between tasks** - Temporarily work on something else without losing your session
  * **Free terminal resources** - Pause Claude Code while running resource-intensive commands
  * **Complex shell work** - Multiple commands or shell navigation


**Benefits:**
  * **Session preservation** - Your conversation history and context remain intact
  * **Quick access** - Instant terminal availability without losing work
  * **Resource management** - Free CPU/memory temporarily while maintaining state


The suspend/resume functionality provides efficient session management for developers who need to switch between Claude Code and other terminal tasks.
**See Also** : Terminal Controls|Session Management|Getting Started
  * How to Suspend
  * How to Resume
  * Alternative: Shell Commands from Within Claude Code
  * When to Use


