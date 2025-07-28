Skip to main content
On this page
Plan mode is a feature in Claude Code that separates research and analysis from execution, significantly improving the safety.
When activated, Claude will not edit files, run commands, or change anything until you approve the plan.
You activate it by pressing `shift+tab` twice. To exit Plan Mode you can press `shift+tab` again. (I must say the UX of Claude Code is seamless, well done Anthropic)
This feature dropped (in stealth in v1.0.16) one month after I was using Claude Code daily and yet it instantly changed my workflow especially when working with Claude 4 Opus.
### Prior to Plan Mode​
I would frequently start or end prompts with:
> Do not code, just make suggestions
And generally speaking this worked. However, when Claude did provide suggestions it was unfortunately inconsistent in format and verbosity.
Other folks on r/ClaudeAI have mentioned similar inconsistent results when requesting inaction from Claude. This led to an unpredictable UX and feedback loop.
### With Plan Mode​
Plan Mode not only provides security but it 'forces' Claude to deliver consistently formatted responses in a reasonable verbosity.
When I asked for suggestions on improving shader time complexity, Claude elegantly provided multiple numbered options with clear benefits outlined for each approach (e.g. speed delta, amount of changes required, etc.). No more guessing whether Claude will edit files or just suggest. The output is structured, predictable, and you get to approve before execution.
I have also observed plan mode is incredibly fast! This in combination with the compactness of the plan's produced has made using Opus much more efficient in terms of speed and token usage.
### Available Tools & Restricted Tools​
In plan mode, Claude has access to read-only and research tools:
**Available tools:**
  * **Read** - Files and content viewing
  * **LS** - Directory listings
  * **Glob** - File pattern searches
  * **Grep** - Content searches
  * **Task** - Research agents
  * **TodoRead/TodoWrite** - Task management
  * **WebFetch** - Web content analysis
  * **WebSearch** - Web searches
  * **NotebookRead** - Jupyter notebooks


**Restricted tools:**
  * **Edit/MultiEdit** - File edits
  * **Write** - File creation
  * **Bash** - Command execution
  * **NotebookEdit** - Notebook edits
  * MCP tools that modify state


Claude can research and plan without touching anything until you approve.
##### Extra Cautious
When exiting plan mode, Claude is extra cautious and will ask for additional confirmation about the task he is about to execute. It's a nice touch that further ensures safety is maintained.
![Custom image](https://www.claudelog.com/img/discovery/035_plan.png)
**See Also** : Auto-Accept Permissions|Dangerous Skip Permissions|Configuration
**Author** :![InventorBlack profile](https://www.claudelog.com/img/claudes-greatest-soldier.png)InventorBlack|CTO at Command Stick|Mod at r/ClaudeAi
  * Prior to Plan Mode
  * With Plan Mode
  * Available Tools & Restricted Tools


