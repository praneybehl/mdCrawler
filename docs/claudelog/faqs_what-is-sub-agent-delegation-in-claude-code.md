Skip to main content
Sub-agent delegation uses Claude's Task tool to spawn parallel agents that handle operations while the main agent focuses on coordination. This creates faster, more efficient workflows.
### How to Use It​
**Delegate Operations** - Use sub-agents for file reads, writes, edits, searches, analysis, and web content fetching. The main agent handles coordination.
**Parallel Processing** - Create multiple sub-agents to work simultaneously on different aspects of a task for efficient feature implementation.
**Explicit Orchestration** - Provide Claude with clear steps showing which operations will be delegated to sub-agents.
### Why Use Sub-Agent Delegation​
Sub-agent delegation distributes work across multiple agents that run asynchronously, avoiding the need to wait for one task to finish before starting another. I can initiate multiple tasks simultaneously rather than waiting sequentially.
**Benefits:**
  * **Faster Execution** - Asynchronous processing avoids waiting for sequential task completion
  * **Reduced Waiting** - Multiple tasks initiate simultaneously instead of one-by-one
  * **Comprehensive Coverage** - Multiple agents can research different areas simultaneously
  * **Organized Workflow** - Main agent coordinates while sub-agents handle specific tasks
  * **Efficient Resource Use** - Parallel execution maximizes throughput despite individual task overhead


I use sub-agent delegation for comprehensive research, feature analysis, and any workflow where I can avoid sequential waiting by initiating multiple tasks simultaneously.
Orchestration Strategy
Provide explicit steps showing which tasks will be delegated to sub-agents. The better you orchestrate the workflow, the faster your overall completion time.
Balance Costs
Group related tasks together rather than creating separate agents for every operation. Balance token costs with performance gains through strategic grouping.
##### Parallel Processing Power
Sub-agent delegation enables asynchronous task execution avoiding sequential waiting patterns. Use Task tool for operations while main agent coordinates comprehensive workflow coverage.
![Custom image](https://www.claudelog.com/img/discovery/006.png)
**See Also** : Task Agent Tools|You Are the Main Thread|Context Window Depletion
  * How to Use It
  * Why Use Sub-Agent Delegation


