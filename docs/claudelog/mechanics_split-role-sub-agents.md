Skip to main content
On this page
A fascinating mechanic the Reddit community brought to my attention is the ability to designate different roles to sub-agents.
### The Role Foundation​
Anthropic have openly discussed providing Claude with a `Role` which helps get him in the zone for the task at hand, for example:
> Your role is as a seasoned security expert which specialises in pen testing.
Multiple members of the community have created sophisticated tools for orchestrating sub-agent roles. SuperClaude provides **9 cognitive personas** (architect, frontend, backend, security, analyzer, qa, performance, refactorer, mentor) that can be applied as universal flags to any command. Claudia offers **custom AI agents** with tailored system prompts through a GUI interface for coordinating different agent roles.
### Native Implementation​
However, I am old school and love exploring a tool's raw mechanics without third-party dependencies. So I experimented with asking Claude to `Utilise multiple sub-agents to validate this code from multiple perspectives`.
**Sub-Agent Coordination Strategy:**
  1. **Setup Phase** - Ensure Claude is in Plan Mode and that ultrathink is instantiated
  2. **Role Suggestion** - Claude automatically suggests various relevant roles applicable to the task
  3. **Perspective Selection** - Select the kind of perspectives you want the task reviewed from
  4. **Parallel Analysis** - Sub-agents complete their review using their specialized approaches
  5. **Consolidation** - Findings are consolidated and presented by Claude


**Perspective Selection Examples:**
After multiple successful attempts it becomes second nature to suggest quirky perspectives for Claude to analyse tasks/problems from different perspectives.
**Code Review Tasks:**
```
Create sub-agents and analyse the problem from the following perspectives: factual, senior engineer, security expert, consistency reviewer, redundancy checker
```

**User Experience Tasks:**
```
Create sub-agents and analyse the problem from a: creative, nooby user, designer, marketing, seo perspective
```

**Documentation Tasks:**
```
Create sub-agents to review this documentation from the following perspectives:technical accuracy, beginner accessibility, SEO optimization, content clarity
```

Interestingly enough each perspective naturally gravitates toward different tools based on their role and problem-solving approach. This creates a more comprehensive analysis as different agents instinctively choose the most relevant combination of tools for their domain of expertise.
**Performance & Cost Optimization:**
This mechanic delivers exceptional value by maximizing Claude 4 Sonnet's capabilities through strategic orchestration. Rather than reaching for the 5x more expensive Opus model, split role sub-agents combined with ultrathink unlock sophisticated analysis at Sonnet pricing. The parallel nature of Task execution means multiple expert roles can analyze the same problem simultaneously, creating multiple insights that would be difficult to achieve through single-role analysis (due to previous roles and context influencing the context window).
### Beyond Coding Applications​
This mechanic applies beyond coding! I have used noob, seo, engineer, vibe coder, non-coder perspectives to get additional opinions on aspects of ClaudeLog and it all happens in parallel safely within Plan Mode.
The beauty of split role sub-agents lies in their scalability - you can adapt the perspective combinations to any domain or problem type. Start with the fundamental technical perspectives, then experiment with creative combinations as you discover what insights each role type reveals. A.B.E (Always be experimenting)
##### Multi-Perspective Analysis
The power of split role sub-agents lies in their ability to surface insights you neither a single Claude instance could surface alone. Each perspective uses different tools and approaches, creating a comprehensive analysis that dramatically improves decision quality.
![Custom image](https://www.claudelog.com/img/discovery/023_excite.png)
##### Pushing the Limit
Utilise `Claude 4 Sonnet` + Plan Mode + `ultrathink` + `role sub-agents` to extract the maximum performance from the Claude 4 Sonnet model, prior to reaching for the 5x more expensive and often overkill Claude 4 Opus model.
![Custom image](https://www.claudelog.com/img/discovery/037_sonnet.png)
**See Also** : Plan Mode|Task Agent Tools|Tactical Model Selection|Always Be Experimenting
**Author** :![InventorBlack profile](https://www.claudelog.com/img/claudes-greatest-soldier.png)InventorBlack|CTO at Command Stick|Mod at r/ClaudeAi
  * The Role Foundation
  * Native Implementation
  * Beyond Coding Applications


