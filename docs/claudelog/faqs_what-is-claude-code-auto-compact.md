Skip to main content
I observe that auto-compact is Claude Code's intelligent context window management system that automatically summarizes conversations when approaching memory limits, allowing you to continue working without interruption.
### How Auto-Compact Works​
When your conversation approaches the context window limit, Claude Code automatically:
**1. Analyzes the conversation** to identify key information worth preserving **2. Creates a concise summary** of previous interactions, decisions, and code changes **3. Compacts the conversation** by replacing old messages with the summary **4. Continues seamlessly** with the preserved context
### Three Context Management Options​
  * **Auto-Compact (Default)** : Automatic summarization when approaching limits. Best for most users who want hands-off context management
  * **Manual Compact (`/compact`)**: You control when and how to summarize with specific preservation instructions
  * **Clear (`/clear`)**: Starts a completely fresh conversation with no context preservation


**Manual Compact Examples:**
```
# Basic compact/compact# Compact with specific preservation instructions/compact only keep the names of the websites we reviewed# Compact preserving code patterns/compact preserve the coding patterns we established
```

### Controlling Auto-Compact​
You can check or change auto-compact settings in your session:
```
/config
```

This shows whether auto-compact is enabled and your current context usage.
### What Gets Preserved​
Auto-compact typically preserves:
  * **Recent code changes** and file modifications
  * **Project structure** and important architectural decisions
  * **Ongoing task context** and current objectives
  * **Key patterns** and naming conventions established
  * **Important configuration** and setup information


### What Gets Summarized​
Auto-compact condenses:
  * **Detailed explanations** that are no longer immediately relevant
  * **Debugging sessions** that have been resolved
  * **Exploratory discussions** that didn't lead to code changes
  * **Historical context** that's no longer needed for current tasks


### Manual Compact Strategies​
I use manual compact when I want control over what gets preserved:
  * **Before major changes** : `/compact preserve current architecture decisions`
  * **After debugging** : `/compact keep the solution we found, remove debugging steps`
  * **Project transitions** : `/compact focus on the new feature requirements`


The real strategy is to manually compact at strategic times rather than letting auto-compact happen randomly. When auto-compact triggers automatically, it can disrupt your workflow and mess up your current setup. I use `/compact` at natural breakpoints when I control what gets preserved.
##### Memory Management Control
Manual compacting at strategic breakpoints prevents workflow disruption from automatic triggering. Claude's performance degrades when working memory becomes constrained during active development.
![Custom image](https://www.claudelog.com/img/discovery/012.png)
Strategic Compacting
I find it's better to manually compact at logical breakpoints rather than hitting context limits mid-task. Claude's performance degrades significantly when working memory is constrained. See Context Window Depletion for detailed strategies.
**See Also** : Context Window Depletion|Claude Code Usage Limits|Memory Management
  * How Auto-Compact Works
  * Three Context Management Options
  * Controlling Auto-Compact
  * What Gets Preserved
  * What Gets Summarized
  * Manual Compact Strategies


