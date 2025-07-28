Skip to main content
Utilise the `--add-dir` functionality to work across multiple directories and repositories in a single Claude Code session.
### What is --add-dir​
**Purpose** - Extends Claude Code's workspace beyond your current working directory to include additional directories without changing your primary location.
  * **CLI argument** : `--add-dir` when starting Claude Code
  * **Slash command** : `/add-dir` to expand workspace mid-session


### How to Use --add-dir at Startup​
**Single Additional Directory** - Add one extra directory when launching Claude Code:
```
claude --add-dir /path/to/other/project
```

**Multiple Directories** - Add several directories at once:
```
claude --add-dir ../backend --add-dir ../shared-utils --add-dir ~/company/configs
```

**Combined with Other Options** - Mix with model selection or other flags:
```
claude --model claude-sonnet-4-20250514 --add-dir ../backend-apiclaude --add-dir ~/shared/libraries -p "Compare authentication patterns between current and shared directory"
```

### Mid-Session Directory Addition​
**Slash Command Usage** - Add directories without restarting your session:
```
/add-dir /path/to/other/project/add-dir ../backend-api/add-dir ~/shared/libraries
```

**Dynamic Workflow Expansion** - Start focused, expand as needed:
  * Begin working on frontend project
  * Realize you need backend API reference: `/add-dir ../backend-api`
  * Need shared utilities: `/add-dir ~/company/shared-utils`
  * Access documentation repo: `/add-dir ../project-docs`


### Common Use Cases​
**Multi-Repository Development** - Work on interconnected projects:
```
# Frontend project needs backend API referenceclaude --add-dir ../backend-api# Microservices that share common codeclaude --add-dir ../user-service --add-dir ../auth-service --add-dir ../shared-models
```

**Shared Resources Access** - Reference common configurations or libraries:
```
# Access company-wide shared configurationsclaude --add-dir ~/company/shared-configs# Reference template repositoriesclaude --add-dir ~/templates/react-components --add-dir ~/templates/api-patterns
```

**Legacy Code Integration** - Work with mixed old and new codebases:
```
# Modernizing project while referencing legacy systemclaude --add-dir ../legacy-system --add-dir ../migration-scripts
```

**Documentation and Examples** - Include reference materials:
```
# Access documentation and example codeclaude --add-dir ../project-docs --add-dir ../code-examples
```

##### Workspace Expansion Control
--add-dir transforms Claude Code from single-directory tool into multi-repository orchestrator. Expand your workspace dynamically without losing context or restarting sessions.
![Custom image](https://www.claudelog.com/img/discovery/033_energy.png)
**See Also** : Configuration Guide
  * What is --add-dir
  * How to Use --add-dir at Startup
  * Mid-Session Directory Addition
  * Common Use Cases


