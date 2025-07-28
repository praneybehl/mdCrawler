Skip to main content
I have seen a trend amongst developers of opting to use Opus for everything. Not only is this a costly habit, but Claude Opus is not necessarily the best model for every operation. Behind the scenes, Anthropic tactically chooses when to utilise Claude Haiku 3.5 to perform routine grunt work which requires minimal intelligence.
**Model Selection Strategy:**
**Opus (Most Expensive, Highest Capability):**
  * Complex architectural decisions requiring deep reasoning
  * Multi-step logical problems with intricate dependencies
  * Creative tasks requiring nuanced understanding
  * Code reviews requiring architectural judgment
  * Complex refactoring across multiple systems


**Sonnet (Balanced Cost-Performance):**
  * Standard feature implementation and development tasks
  * Most debugging and troubleshooting scenarios
  * Code generation with moderate complexity
  * Documentation writing and editing
  * Task coordination and workflow management


**Haiku (Cheapest, Fastest):**
  * Simple file reads and basic content extraction
  * Routine formatting and style corrections
  * Basic syntax validation and linting
  * Simple text transformations and data parsing
  * Quick status checks and basic analysis


**Cost Optimization Approach:**
I would set Claude 4 Sonnet as the base model and for specific tasks instruct Claude to launch a Claude Opus instance with `claude --model claude-opus-4-20250514`. This would allow specific processes to run Opus as their base model.
This tactic can potentially offer huge cost savings over having Opus drive all processes (assuming Claude Haiku 3.5 is not substituted in). Due to Claude 4 Opus being approximately 5x more expensive than Claude 4 Sonnet, there is substantial financial budget for exploring orchestration configurations with sub-agents to bring costs down whilst retaining performance.
**Note:** When spawning Claude instances in print mode you may need to increase the `max turns` so that the process completes: `claude -p --model claude-opus-4-20250514 --max-turns 20`
##### Cost Optimization
Strategic model selection can reduce Claude Code usage costs by up to 80% while maintaining output quality for most development tasks.
![Custom image](https://www.claudelog.com/img/discovery/019.png)
**See Also** : Model Comparison|Context Window Depletion|Plan Mode
**Author** :![InventorBlack profile](https://www.claudelog.com/img/claudes-greatest-soldier.png)InventorBlack|CTO at Command Stick|Mod at r/ClaudeAi
