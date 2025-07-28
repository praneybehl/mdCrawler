Skip to main content
The --continue flag automatically loads the most recent Claude Code conversation from your current directory, preserving full conversation history and accumulated context for seamless workflow resumption.
### How to Use It​
Use `--continue` when launching Claude Code to automatically resume your most recent session from the current directory. No session ID required - Claude finds and loads the latest conversation automatically.
```
cd /path/to/your/projectclaude --continueclaude --continue --model opus
```

### Why Use --continue​
The --continue flag eliminates the friction of starting fresh sessions when working on ongoing projects. It preserves conversation history, accumulated knowledge, and project context, making it ideal for multi-day development work.
**Benefits:**
  * **Context Preservation** - Maintains full conversation history and accumulated knowledge
  * **Directory-Specific** - Each project directory maintains its own session history
  * **Automatic Discovery** - No need to remember or specify session IDs
  * **Workflow Continuity** - Natural resumption of interrupted work
  * **CLAUDE.md Integration** - Preserves project-specific instructions and context


##### Seamless Workflow
--continue preserves conversation history and project context for natural workflow resumption. Ideal for multi-day projects where accumulated knowledge accelerates development.
![Custom image](https://www.claudelog.com/img/discovery/001_calm.png)
**See Also** : --resume Flag|Session Management|Context Management
  * How to Use It
  * Why Use --continue


