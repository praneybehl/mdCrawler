Skip to main content
The --add-dir command extends Claude Code's workspace beyond your current working directory to include additional directories without changing your primary location. You can use it as a CLI argument at startup or as a slash command mid-session.
### How to Use It​
Use `--add-dir` when launching Claude Code to include additional directories from the start, or use `/add-dir` during your session to expand workspace dynamically. You can add multiple directories at once or one at a time as needed.
```
claude --add-dir /path/to/other/projectclaude --add-dir ../backend --add-dir ../shared-utils/add-dir ../backend-api
```

### Why Use It​
The --add-dir command enables multi-repository development where you need to reference code across different projects, access shared libraries, or work with interconnected services. Instead of switching between separate Claude Code sessions, you work across multiple codebases simultaneously.
**Benefits:**
  * **Multi-Repository Development** - Work on interconnected projects in one session
  * **Shared Resources Access** - Reference common configurations and libraries
  * **Dynamic Workspace Expansion** - Add directories as needed without restarting
  * **Legacy Code Integration** - Access old codebases while working on new projects
  * **Documentation Access** - Include reference materials and examples


I use it to access requirements from other directories temporarily.
Dynamic Workflow
Start focused on one project and use `/add-dir` to expand workspace as you discover dependencies, rather than predicting all needed directories upfront.
Multi-Project Strategy
For comprehensive multi-directory workflows and use cases, see the --add-dir Guide.
##### Multi-Repository Development
Extend workspace beyond current directory for interconnected projects and shared resources. Use /add-dir dynamically to expand workspace as dependencies emerge during development.
![Custom image](https://www.claudelog.com/img/discovery/000.png)
**See Also** : --add-dir Guide|Working Directory|Configuration|Getting Started
  * How to Use It
  * Why Use It


