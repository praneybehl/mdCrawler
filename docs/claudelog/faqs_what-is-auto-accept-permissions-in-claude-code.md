Skip to main content
Auto-Accept Permissions is Claude Code's seamless execution mode that eliminates confirmation prompts, enabling Claude to execute actions immediately without interrupting the flow for approval. When activated, the UI displays "auto-accept edit on" and Claude proceeds with file edits, commands, and operations automatically.
### How to Use It​
Press `Shift+Tab` repeatedly to cycle through permission modes: normal-mode, auto-accept edit on, and plan mode on. The UI clearly indicates which mode is active as you cycle through each state.
### Why Use It​
I use auto-accept permissions when I have a clear direction and want Claude working autonomously while I focus on other tasks. This mode transforms Claude Code into a seamless execution environment, particularly valuable during research phases, large refactoring operations, and following thoroughly checked implementation plans.
**Benefits:**
  * **Uninterrupted Flow** - No constant approval decisions breaking your concentration
  * **Autonomous Execution** - Claude works independently while you focus on other tasks
  * **Faster Iterations** - Dramatically faster iteration cycles without permission friction
  * **Maintained Focus** - Attention stays on the problem rather than approval management
  * **Extended Sessions** - Enables 10-40 minute agentic sprints for complex tasks


I observe this creates a distinctly different workflow rhythm compared to the deliberate verification pace of normal mode, allowing for continuous execution momentum.
Safety Configuration
Configure your `allowedTools` in `~/.claude.json` to control which operations auto-accept can execute without prompts. See Configuration for specific tool patterns.
Bell Notifications
Use terminal bell notifications to stay informed when Claude completes tasks in auto-accept mode.
##### Seamless Execution Flow
Auto-accept mode eliminates approval friction for uninterrupted autonomous development sprints. Use Shift+Tab to cycle between normal mode, auto-accept, and plan mode for workflow control.
![Custom image](https://www.claudelog.com/img/discovery/028_fire.png)
**See Also** : Auto-Accept Permissions Mechanics|Plan Mode|Configuration
  * How to Use It
  * Why Use It


