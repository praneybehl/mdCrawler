Skip to main content
Auto-Approve Mode (also called Auto-Accept Mode) is Claude Code's seamless execution feature that eliminates confirmation prompts, enabling Claude to execute actions immediately without interrupting the workflow for approval. When activated, Claude can edit files, run commands, and perform operations without requesting permission.
### How to Use It​
Press `Shift+Tab` to cycle through modes until you reach "auto-accept edit on" mode. Claude will execute all operations immediately without permission prompts. Press `Shift+Tab` again to cycle back to normal mode when you want confirmation prompts restored.
### Why Use It​
Auto-Approve Mode transforms Claude Code into an uninterrupted execution environment, particularly valuable for repetitive tasks, large refactoring operations, and long autonomous sprints where constant permission requests create friction.
**Benefits:**
  * **Seamless Execution** - No interruptions for file edits or command execution
  * **Faster Iteration** - Dramatically faster workflow cycles without approval delays
  * **Autonomous Operation** - Claude works independently while you focus on other tasks


I use Auto-Approve Mode when I have a clear direction and want Claude to work autonomously on large refactoring operations or when following thoroughly checked plans.
Safety Considerations
Use Auto-Approve Mode cautiously. Claude executes all operations immediately without confirmation, including file modifications, bash commands, and potentially destructive operations. Consider your `allowedTools` configuration carefully.
Mode Cycling
Pressing `Shift+Tab` cycles through: normal-mode → auto-accept edit on → plan mode on. The UI clearly indicates which mode is active.
##### Uninterrupted Execution Environment
Auto-Approve Mode enables seamless autonomous operation for large refactoring and repetitive tasks. Cycle modes with Shift+Tab: normal → auto-accept → plan mode for workflow control.
![Custom image](https://www.claudelog.com/img/discovery/009.png)
**See Also** : Auto-Accept Permissions|Plan Mode|Configuration Guide
  * How to Use It
  * Why Use It


