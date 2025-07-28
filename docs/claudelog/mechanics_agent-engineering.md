Skip to main content
On this page
We've evolved through three distinct eras of AI interaction: from Prompt Engineering (crafting perfect individual prompts) to Context Engineering (optimizing the context, what goes into it and what remains in it through `CLAUDE.md` files) and now to Agent Engineering (designing specialized, reusable, efficient AI agents). At each stage, our ability to share deliverables and grow as a community has expanded: from sharing individual prompts, to sharing comprehensive context configurations and tactics, to now sharing complete portable agent definitions that work across any project.
`Custom agents` represent this latest paradigm shift in Claude Code workflows from manual orchestration to automatic delegation, from project-specific solutions to portable specialist tools. This guide covers the essential foundations you need to understand before diving into advanced tactics.
## Understanding the Agent Ecosystem​
Comparison: Custom Agents vs. Sub-agents vs. Task Tools
Aspect| Custom Agents| Split Role Sub-agents| Task/Agent Tools  
---|---|---|---  
**Token Efficiency**  
**Activation**|  Automatic delegation| Manual delegation| Manual delegation  
**Shared System Prompt**|  No| Yes| Yes  
**Portability**|  Highly portable (single .md file)| Impractical| Impractical  
**Configuration**|  YAML frontmatter + system prompt| Task description only| Task description only  
**System Prompt**|  Custom system prompt access| Inherits system prompt| Inherits system prompt  
**Custom Tool Selection**|  Yes| No| No  
**Claude.md Inheritance**|  No| Yes| Yes  
**Use Case**|  Specialized repeatable tasks| Multi-perspective analysis| Parallel task execution  
`Custom agents` deliver **automatic activation** , **isolated contexts** , and **surgical tool selection** , eliminating the token bloat and manual orchestration of previous approaches.
## Custom Agent Design​
I believe one of the most important aspects when designing `custom agents` is to carefully engineer how many tokens your `custom agent` needs to initialize. Optimizing this serves multiple purposes: to improve initialization speed, reduce cost, maintain peak performance, and enable efficient chaining.
Each `custom agent` invocation carries a **variable initialization cost** based on tool count and configuration complexity. Design decisions should account for this:
**Performance Analysis by Tool Count (Anecdotal experiment):**
Tool Count| Token Usage| Relative Initialization Time| Claude.md Empty  
---|---|---|---  
0| 640| 2.6s| true  
1| 2.6k| 3.9s| false  
2| 2.9k| 4.3s| false  
3| 3.2k| 6.0s| false  
4| 3.4k| 6.1s| false  
5| 3.9k| 5.1s| false  
6| 4.1k| 7.0s| false  
7| 5.0k| 6.9s| false  
8| 7.1k| 5.6s| false  
9| 7.5k| 5.1s| false  
10| 7.9k| 6.2s| false  
15+| 13.9k - 25k| 6.4s| false  
_Note: The 0 tool experiment was conducted with a completely empty`Claude.md` and thus reflects the best case scenario. Experiments for 1-15+ tools were conducted with a non-empty `Claude.md`. Token cost and initialization time were affected by the specific tools which were added._
**Agent Weight Classifications:**
  * **Lightweight agents** : Under 3k tokens - Low initialization cost
  * **Medium-weight agents** : 10-15k tokens - Moderate initialization cost
  * **Heavy agents** : 25k+ tokens - High initialization cost


**Subscription and Model Optimization:** A lightweight, performant `custom agent` will be used and experimented with more than a heavyweight `custom agent` due to subscription constraints. They are by far the most composable and effortless to use. We should strive to make our `custom agents` as performant and composable as possible. It would be logical to pair `Claude 4 Opus` with a lightweight `custom agent` due to its high token efficiency, which helps balance out `Claude 4 Opus's` 5X cost.
**Agent Chainability Impact:** The complexity of a `custom agent` significantly affects its chainability due to startup time and token usage. Heavy `custom agents` (25k+ tokens) create bottlenecks in multi-agent workflows, while lightweight `custom agents` (under 3k tokens) enable fluid orchestration. As future **Agent Engineers** , we must optimize both individual `custom agent` metrics and their composability:
  * **Individual Optimization** : Minimize tool count while preserving capability
  * **Composition Strategy** : Balance specialized high-cost `custom agents` with efficient ones (Similar to the big.LITTLE concept from CPU design)
  * **Workflow Design** : Consider cumulative token costs when chaining multiple `custom agents`
  * **Performance Monitoring** : Track `custom agent` efficiency metrics across different use cases


## When to Use Custom Agents​
`Custom agents` excel in the same scenarios as split role sub-agents, but with enhanced portability and automatic activation:
### Specialized Domain Tasks​
  * **Code Review** - Security, performance, maintainability analysis
  * **Research Tasks** - API documentation, library comparison, best practices
  * **Quality Assurance** - Testing strategies, edge case identification
  * **Documentation** - Technical writing, SEO optimization, accessibility
  * **Design Analysis** - UX review, layout assessment, design consistency
  * **Content Quality** - Legibility expert, grammar expert, brand voice expert


### Portable Workflows​
Unlike `sub-agents` tied to specific projects, `custom agents` can be refined once and utilized across multiple projects, making them ideal for:
  * Cross-project standards enforcement
  * Team workflow standardization
  * Personal expertise amplification
  * Community knowledge sharing


## Essential Features​
### No CLAUDE.md Inheritance​
**Major Advantage** : Unlike traditional sub-agents, custom agents are designed to not automatically inherit the project's `CLAUDE.md` configuration. This prevents context pollution and ensures consistent behavior across projects. You can verify this with a sanity check.
### Coloring Your Custom Agent​
Custom agents can be visually distinguished through terminal color formatting in their indicator, making it easier to track which agent is responding during complex workflows. This helps maintain clarity when multiple agents are active or when reviewing conversation history.
### Agent Nicknaming for Efficiency​
Configure short nicknames for frequently used agents:
  * **UX agent (`A1`)** - Quick UX analysis
  * **Security agent (`S1`)** - Rapid security review
  * **Performance agent (`P1`)** - Performance optimization


Example configuration with nickname:
```
---name: UX Agent (A1)description: UX specialist for user experience analysis. Use this agent when evaluating interfaces and user workflows.tools: Read, Grep, Glob---You are a UX specialist focused on user experience analysis and interface evaluation.When invoked:1. Analyze user interface elements and workflows2. Identify usability issues and improvement opportunities3. Provide actionable UX recommendations4. Consider accessibility and user journey optimization
```

**Calling the agent with nickname:**
```
ask agent a1 to review the navigation menu UX
```

or:
```
ask a1 to review the navigation menu UX
```

### Advanced Nickname Workflows​
The ability to provide nicknames to `custom agents` helps to improve manual invocation and opens up possibilities like calling `custom agents` via nicknames `A1, P2, C1`.
```
ask A1, P2, C1 to review the changes
```

### Configuring Automatic Delegation​
`Custom agents` are automatically utilized by the `delegating agent` based on the task description within your prompt, the description field within your `custom agent` configuration, the current context and available tools.
When crafting your `custom agents` you will need to evaluate Claude's reliability at invoking your `custom agent`. If you need to improve the reliability, explore updating your agent's name, description or system prompt. Configuring your `custom agent` to be promptly utilized by Claude is a form of `Tool SEO`.
Anthropic has mentioned that to encourage proactive `custom agent` use we should include terms like `use PROACTIVELY` or `MUST BE USED` in the `description` fields of our `custom agents`. This functions similarly to how you would use such terms to get good adherence out of Claude by correctly formatting your `Claude.md`.
## Design Considerations​
### Getting Started Strategy​
**Token-First Design:**
  * Create focused, single-purpose agents initially
  * Start with lightweight agents (minimal or no tools) for maximum composability
  * Carefully engineer how many tokens your custom agent needs to initialize
  * Prioritize efficiency over capability for frequent-use agents


**Configuration Best Practices:**
  * Use clear, specific descriptions for reliable auto-activation
  * Grant only necessary tools initially, expand as needed
  * Test agent reliability before expanding
  * Include examples in system prompts for better pattern recognition
  * Test agents in isolation before deploying in workflows
  * Design for chainability and multi-agent piping
  * Frequently test agents and share them with others to help validate effectiveness


Getting Started
Start with one simple, focused custom agent that solves a specific problem you encounter regularly. Test its effectiveness and refine its description based on how reliably Claude invokes it automatically.
Token Efficiency
Stay lean with your agent design. Lightweight agents are faster to initialize, more cost-effective, and highly composable for chaining workflows. Expand tool selection only when the specialized capability justifies the higher initialization cost.
##### Foundation First
Master the fundamentals of custom agents before diving into complex chaining. A solid understanding of these foundations will enable more effective chaining and increased usage frequency.
![Custom image](https://www.claudelog.com/img/discovery/028_fire.png)
**See Also** : Custom Agents|Task Agent Tools
**Author** :![InventorBlack profile](https://www.claudelog.com/img/claudes-greatest-soldier.png)InventorBlack|CTO at Command Stick|Mod at r/ClaudeAi
  * Understanding the Agent Ecosystem
  * Custom Agent Design
  * When to Use Custom Agents
    * Specialized Domain Tasks
    * Portable Workflows
  * Essential Features
    * No CLAUDE.md Inheritance
    * Coloring Your Custom Agent
    * Agent Nicknaming for Efficiency
    * Advanced Nickname Workflows
    * Configuring Automatic Delegation
  * Design Considerations
    * Getting Started Strategy


