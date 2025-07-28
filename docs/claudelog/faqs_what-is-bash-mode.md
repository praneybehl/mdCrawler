Skip to main content
Bash Mode refers to Claude Code's ability to execute shell commands through the Bash tool, enabling system integration, automation, and development workflow enhancement. Unlike Plan Mode or Auto-Approve Mode, bash mode isn't a specific toggle but rather Claude's capability to run terminal commands when granted permission.
### How to Use It​
Claude Code uses the Bash tool to execute shell commands directly in your terminal environment. You can grant permission for individual commands or configure allowed tools for automated execution.
**Basic Usage:**
```
# Claude can run git commandsgit statusgit log --oneline -10# System operationsls -lamkdir new-directorynpm install
```

**Permission Configuration:**
```
{"projects":{"/path/to/project":{"allowedTools":["Bash(git log:*)",// Only git log commands"Bash(npm install:*)",// Only npm install operations"Bash(*)"// All bash commands (use cautiously)]}}}
```

### Why Use It​
I use bash mode functionality when I need Claude Code to integrate deeply with my development environment. The Bash tool enables Claude to perform system operations that would otherwise require manual intervention, creating seamless automation workflows.
**Benefits:**
  * **System Integration** - Direct access to command line tools and utilities
  * **Development Automation** - Automated git operations, package management, and build processes
  * **Workflow Continuity** - No need to switch between Claude Code and terminal manually
  * **Environment Awareness** - Claude can check system state and respond accordingly
  * **Script Execution** - Run custom bash scripts and development tools
  * **Granular Permissions** - Configure exactly which commands are allowed without confirmation


The Bash tool transforms Claude Code from a code assistant into a comprehensive development environment manager that can interact with your entire system stack.
### Configuration and Safety​
Configure bash access through allowed tools in your `~/.claude.json` file or use the `/permissions` command for interactive management. I recommend starting with specific command patterns rather than blanket bash access.
**Safe Pattern Examples:**
  * `Bash(git *:*)` - All git operations
  * `Bash(npm run:*)` - Package scripts only
  * `Bash(ls:*)` - Directory listing commands
  * `Bash(docker ps:*)` - Docker status commands


**Security Considerations:**
  * **Principle of Least Privilege** - Grant only necessary command access
  * **Command Pattern Matching** - Use specific patterns rather than `Bash(*)`
  * **Project Isolation** - Configure permissions per project directory
  * **Regular Auditing** - Review and update allowed commands periodically


Interactive Management
Use the `/permissions` command to manage bash tool access visually without manually editing JSON configuration files.
Automation Scripts
Claude Code can create and execute custom bash scripts for complex multi-step operations, reducing API overhead compared to individual tool calls.
##### System Integration Power
Bash mode enables seamless development environment integration through controlled terminal access. Configure granular permissions to balance automation benefits with security requirements.
![Custom image](https://www.claudelog.com/img/discovery/014.png)
**See Also** : Configuration Guide|Bash Scripts|Allowed Tools
  * How to Use It
  * Why Use It
  * Configuration and Safety


