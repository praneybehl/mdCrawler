Skip to main content
On this page
**Official MCP server providing seamless GitHub API integration for advanced automation and AI-powered development workflows.**
**Author** : GitHub | GitHub Repo | 18820 Stars|1546 Forks|MIT License|Updated Jul 23, 2025
### Overview​
The GitHub MCP Server is the official Model Context Protocol implementation for GitHub integration, enabling AI models to interact directly with GitHub's ecosystem. It provides comprehensive access to repositories, issues, pull requests, actions, and security features through a standardized MCP interface, transforming how developers automate and manage GitHub workflows.
### Features​
  * **Comprehensive GitHub API Access** - Extensive integration with GitHub's REST and GraphQL APIs through curated toolsets
  * **Flexible Deployment Options** - Remote hosted server or local Docker installation
  * **Granular Permissions** - Fine-grained control over tool access and capabilities
  * **Enterprise Support** - GitHub Enterprise Server compatibility with custom configurations
  * **Dynamic Tool Discovery** - Automatically adapts to available GitHub features
  * **Multi-Toolset Support** - Actions, security, issues, PRs, repositories, notifications


### Installation​
**Prerequisites**
  * VS Code 1.101+ (for remote server) or Docker (for local installation)
  * GitHub Personal Access Token with appropriate permissions


**Method 1: Remote Server (Recommended)**
Install directly in VS Code with one-click buttons:
  * Install for Claude Desktop
  * Install for Continue


**Method 2: Claude Desktop Configuration**
```
{"mcpServers":{"github":{"command":"docker","args":["run","-i","--rm","-e","GITHUB_PERSONAL_ACCESS_TOKEN","ghcr.io/github/github-mcp-server"],"env":{"GITHUB_PERSONAL_ACCESS_TOKEN":"<YOUR_TOKEN>"}}}}
```

**Method 3: Local Docker Installation**
```
# Run GitHub MCP server locallydocker run -i --rm \ -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \ -e GITHUB_TOOLSETS="context,repos,issues,pull_requests" \ ghcr.io/github/github-mcp-server
```

**Available GITHUB_TOOLSETS**
  * **`context`**- Repository context (recommended for most use cases)
  * **`repos`**- Repository management and operations
  * **`issues`**- GitHub Issues API access
  * **`pull_requests`**- Pull request management
  * **`actions`**- GitHub Actions workflow integration
  * **`code_security`**- Security scanning and vulnerability management
  * **`notifications`**- GitHub notifications management
  * **`orgs`**- Organization management
  * **`secret_protection`**- Secret scanning and protection
  * **`users`**- User account operations
  * **`experiments`**- Experimental GitHub features (optional)
  * **`all`**- Enable all available toolsets


**Note** : The `context` toolset is recommended for most users. Specify only needed toolsets to help the LLM with tool choice and reduce context size. All toolsets are enabled by default if `GITHUB_TOOLSETS` is not specified.
### Usage​
**Repository Management**
```
# Example interactions through AI client:# "List my repositories and their latest commits"# "Create a new pull request for the feature branch"# "Show me all open issues with bug labels"# "Check the status of GitHub Actions runs"
```

The server enables natural language interaction with GitHub's complete feature set. You can manage repositories, automate issue tracking, review code changes, monitor CI/CD pipelines, and handle security alerts - all through conversational AI interfaces.
**Configuration Options**
  * **Toolset Selection** : Choose specific GitHub features to expose
  * **Read-Only Mode** : Restrict to safe, non-modifying operations
  * **Custom Permissions** : Configure OAuth scopes for security
  * **Enterprise Settings** : Connect to GitHub Enterprise instances


##### Community Insight
The official MCP server has transformed developer workflows with users reporting: "I use it to interact with issues and MRs, looking for related issues when editing code." The official nature ensures reliability that community alternatives often lack.
![Custom image](https://www.claudelog.com/img/discovery/019.png)
_GitHub MCP Server is developed and maintained by the Model Context Protocol organization. For technical support, feature requests, and enterprise configurations, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


