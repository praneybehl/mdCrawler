Skip to main content
The --allowedTools flag specifies which Claude Code operations can proceed without permission prompts, providing granular control over automation scope while maintaining security boundaries.
### How to Use It​
Use `--allowedTools` with specific tool names and command patterns to grant automatic permission for trusted operations while requiring prompts for other actions.
```
claude --allowedTools "Read" "Edit" "Bash(git status)"claude --allowedTools "Bash(npm *)" "Grep" "Glob"claude --allowedTools "Read" "Edit" "Bash(git *)" --model sonnet
```

### Why Use --allowedTools​
The --allowedTools flag enables secure automation by providing granular permission control without the security risks of blanket permission bypass flags.
**Benefits:**
  * **Granular Security** - Specify exact tools and commands that can run automatically
  * **Workflow Optimization** - Streamline trusted operations while maintaining safety controls
  * **Selective Automation** - Allow specific git commands or file operations without full automation
  * **Team Standards** - Enforce consistent permission patterns across development teams
  * **Safe CI/CD** - Enable automation for specific operations without security compromise


### Common Patterns​
**Development Workflow** - Allow git inspection and file operations:
```
claude --allowedTools "Read" "Edit" "Bash(git status)" "Bash(git diff)"
```

**Code Review** - Enable analysis tools without modification capability:
```
claude --allowedTools "Read" "Grep" "Glob" "Bash(git diff)"
```

**Testing Workflow** - Allow testing and limited file operations:
```
claude --allowedTools "Read" "Edit" "Bash(npm test)" "Bash(npm run lint)"
```

### Security Considerations​
**Start Restrictive** - Begin with minimal permissions and add as needed.
**Avoid Dangerous Commands** - Never include `sudo`, `rm`, or network operations in allowedTools.
**Use Patterns Carefully** - Wildcards like `Bash(*)` can be overly permissive.
Security Best Practice
--allowedTools provides the security benefits of granular permissions without the risks of --dangerously-skip-permissions. Start restrictive and add permissions as needed.
##### Granular Security
--allowedTools grants specific tool access without compromising security. Perfect for workflow automation with granular permission boundaries.
![Custom image](https://www.claudelog.com/img/discovery/004.png)
**See Also** : Auto-Accept Permissions|Configuration|Print Mode
  * How to Use It
  * Why Use --allowedTools
  * Common Patterns
  * Security Considerations


