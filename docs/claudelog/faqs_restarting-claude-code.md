Skip to main content
Choose between `/clear` and restart based on your specific context management needs.
### Use /clear First​
**Primary recommendation** - Use `/clear` command instead of restarting Claude Code:
  * **Clears context window** : Removes all previous context and starts fresh
  * **Preserves session** : Keeps Claude Code running without reinitialization costs
  * **Faster than restart** : No startup overhead
  * **Retains`CLAUDE.md`** : Project instructions remain active without re-reading


### When to Actually Restart​
Restart when switching projects, dealing with major `CLAUDE.md` changes, or experiencing session corruption.
Both `/clear` and restart clear the context window completely. The main difference is that restart also re-reads `CLAUDE.md`.
### When NOT to Restart​
Preserve accumulated knowledge that helps with future tasks. Claude builds understanding of your codebase patterns, preferences, and workflow over time.
Only clear or restart when transitioning to unrelated work that won't benefit from previous task learnings. Avoid "just in case" restarts that destroy valuable context unnecessarily.
### Token and Memory Considerations​
Every restart triggers `CLAUDE.md` re-reading and context rebuilding. The `/clear` command preserves project instructions but clears the context window while retaining previous memory updates.
Subscription Considerations
Claude Max users can restart freely due to high usage limits. API users should monitor token costs and use `/clear` strategically.
##### Context Management Strategy
Use /clear instead of restart to preserve accumulated project knowledge and patterns. Only restart when switching projects or dealing with major CLAUDE.md configuration changes.
![Custom image](https://www.claudelog.com/img/discovery/019.png)
**See Also** : Context Window Depletion|CLAUDE.md Supremacy|Getting Started
  * Use /clear First
  * When to Actually Restart
  * When NOT to Restart
  * Token and Memory Considerations


