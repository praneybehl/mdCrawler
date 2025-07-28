Skip to main content
Slash Commands are quick shortcuts you type directly in the Claude Code chat interface to execute specific functions without interrupting your workflow. They start with a forward slash and provide instant access to workspace management, MCP operations, and project controls.
### How to Use It​
Type slash commands directly in the chat interface to execute functions immediately. Commands like `/add-dir` expand your workspace, `/mcp` manages Model Context Protocol servers, and project-specific commands handle repository operations.
```
/add-dir ../backend-api/mcp/project status
```

**Model Specification** - You can specify which model to use for a slash command by adding the model name. This allows you to switch models for specific commands while maintaining your conversation.
**Custom Slash Commands** - You can define your own slash commands as Markdown files in `.claude/commands/` (project-specific with `/project:` prefix) or `~/.claude/commands/` (personal with `/user:` prefix) to automate frequently used prompts.
### Why Use It​
Slash commands eliminate the need to restart Claude Code sessions or navigate complex menus for common operations. They provide instant access to workspace expansion, MCP server management, and project controls while maintaining your current conversation context.
**Benefits:**
  * **Instant Execution** - Commands execute immediately without leaving chat interface
  * **Workflow Continuity** - No need to restart sessions or interrupt conversations
  * **Model Flexibility** - Specify different models for specific commands within same conversation
  * **Workspace Management** - Expand directories and manage project scope dynamically
  * **MCP Integration** - Quick access to Model Context Protocol server operations
  * **Project Controls** - Manage repository operations and project settings efficiently
  * **Custom Automation** - Define your own commands for frequently used workflows and prompts


I use slash commands when I need to expand workspace mid-conversation with `/add-dir`, check MCP server status with `/mcp`, or manage project operations without breaking my development flow.
Discovery Feature
Claude Code v1.0.25 improved slash command discovery reliability, making it easier to find available commands as you type.
##### Instant Workflow Access
Slash commands provide immediate execution without leaving chat interface or restarting sessions. Define custom commands in .claude/commands/ for automated frequently used prompts and workflows.
![Custom image](https://www.claudelog.com/img/discovery/002.png)
Command Categories
Slash commands include "project" and "user" prefixes in descriptions to help organize functionality by scope and access level.
**See Also** : Configuration|MCP Servers|Add Directory Command
  * How to Use It
  * Why Use It


