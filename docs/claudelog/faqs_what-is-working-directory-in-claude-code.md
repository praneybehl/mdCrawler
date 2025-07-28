Skip to main content
The working directory is Claude Code's primary context location where Claude operates and discovers project configuration. When I launch Claude Code, it uses the current terminal directory as the working directory and automatically reads the CLAUDE.md file if present.
### How to Use It​
**Automatic Discovery** - Claude Code starts in your current terminal location:
```
# Navigate to your project firstcd /path/to/your/project# Launch Claude Code (uses current directory as working directory)claude
```

**CLAUDE.md Integration** - Claude automatically reads `CLAUDE.md` from the working directory for project-specific instructions and context.
**File Access Patterns** - Claude can read, edit, and create files relative to the working directory without specifying full paths.
### Why Use Working Directory Context​
The working directory provides Claude with essential project context and establishes the foundation for all file operations and project understanding.
**Benefits:**
  * **Automatic Configuration** - CLAUDE.md files are discovered and loaded automatically from the working directory
  * **Relative Path Operations** - Simplifies file operations using relative paths instead of absolute paths
  * **Project Context** - Provides Claude with immediate understanding of the current project structure
  * **Tool Integration** - All built-in tools operate relative to the working directory by default
  * **Workspace Boundaries** - Establishes clear boundaries for where Claude should focus its operations


I always ensure I'm in the correct project directory before launching Claude Code. This gives Claude immediate access to my project's CLAUDE.md configuration and establishes the proper context for all subsequent operations.
### Extended Workspace Management​
**Additional Directories** - Expand beyond the working directory using `--add-dir`:
```
# Add additional directories at startupclaude --add-dir ../backend-api --add-dir ~/shared/configs# Add directories mid-session/add-dir /path/to/other/project
```

**Multi-Directory Workflows** - The working directory remains the primary location while additional directories provide supplementary context and access.
Project Organization
Always launch Claude Code from your main project directory. This ensures CLAUDE.md discovery and establishes the proper working context for your development session.
Directory Switching
If you need to work in a different directory, exit Claude Code, navigate to the new location, and restart. This provides cleaner context than trying to work across unrelated directories.
##### Context Foundation
Working directory provides automatic CLAUDE.md discovery and establishes project boundaries. Always launch Claude Code from your main project directory for proper context initialization.
![Custom image](https://www.claudelog.com/img/discovery/020_happy.png)
**See Also** : --add-dir Guide|CLAUDE.md Guide|Configuration
  * How to Use It
  * Why Use Working Directory Context
  * Extended Workspace Management


