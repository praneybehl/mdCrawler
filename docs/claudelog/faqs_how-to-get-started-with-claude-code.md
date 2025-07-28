Skip to main content
Getting started with Claude Code is straightforward - most developers are up and running within 10 minutes. The key is understanding the conversation-based workflow that makes it different from traditional coding tools.
### Quick Start​
**1. Install Claude Code**
```
npm install -g @anthropic-ai/claude-code
```

**2. Navigate to Your Project**
```
cd your-project-directory
```

**3. Start Claude Code**
```
claude
```

**4. Have Your First Conversation**
```
You: Can you read my package.json and tell me what this project does?Claude: I'll read your package.json file to understand your project...
```

That's it! Claude Code will analyze your project and start helping immediately.
### Understanding the Workflow​
Claude Code works through natural conversation. Instead of memorizing commands, you describe what you want to accomplish:
  * **Be Specific** : "Add error handling to the login function" vs "improve the code"
  * **Provide Context** : "I'm building a React app" helps Claude understand your environment
  * **Iterate Naturally** : Ask follow-up questions and refine solutions through conversation


### Setting Up Your Environment​
  * **Authentication** : Claude Code will prompt you to authenticate on first run. You can use either an Anthropic API key or Claude subscription
  * **Project Configuration** : Use `/init` to create a `CLAUDE.md` file for your project. Claude will analyze your codebase and generate documentation about your project structure and coding preferences
  * **Editor Integration** : Claude Code works great with VS Code, Vim, or any editor. Many developers run Claude in one terminal while editing in their preferred environment


Understanding New Repos
Start your first session by asking Claude to "explain what this repo is about." This gives you immediate, project-specific guidance and demonstrates Claude Code's contextual understanding. This is incredibly useful when you git clone a new repo and want to understand it or perform security checks.
##### First Session Success
Start with "explain what this repo is about" to unlock immediate project-specific insights. This simple question demonstrates Claude's contextual understanding and security analysis capabilities.
![Custom image](https://www.claudelog.com/img/discovery/002.png)
**See Also** : Installation Guide|What is Claude Code|Configuration Guide|CLAUDE.md Supremacy
  * Quick Start
  * Understanding the Workflow
  * Setting Up Your Environment


