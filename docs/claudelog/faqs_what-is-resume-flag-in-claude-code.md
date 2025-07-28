Skip to main content
The --resume flag loads specific Claude Code conversations by session ID, providing precise control over which session to restore regardless of current directory or when it was created.
### How to Use It​
Use `--resume` with a session ID to load a specific conversation, or use it without an ID to interactively select from available sessions.
```
claude --resume abc123def456claude --resumeclaude --resume session_id --model opus
```

### Why Use --resume​
The --resume flag provides precise session control when you need to access specific conversations rather than just the most recent one. It enables cross-directory session access and session archaeology for finding older valuable conversations.
**Benefits:**
  * **Precise Control** : Load exact sessions by ID, not just most recent
  * **Cross-Directory Access** : Access any session from any directory
  * **Session Archaeology** : Find and load older conversations with valuable context
  * **Interactive Selection** : Browse available sessions when you don't know the ID
  * **Team Collaboration** : Share specific session IDs for collaborative work


##### Precise Session Access
--resume enables exact session targeting across directories and time periods. Perfect for accessing specific debugging contexts or feature discussions.
![Custom image](https://www.claudelog.com/img/discovery/000.png)
**See Also** : --continue Flag|Session Management|Context Management|Changelog
  * How to Use It
  * Why Use --resume


