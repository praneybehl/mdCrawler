Skip to main content
On this page
Now that you have Claude Code installed, let's set up your project and learn the basics of using Claude Code to enhance your development workflow. This beginner-friendly Claude Code tutorial covers essential commands, examples, best practices, and workflow optimization for new users.
## Claude Code Project Setup and Configuration​
### CLAUDE.md Configuration​
Create a `CLAUDE.md` file in your project root to help Claude understand your project. This is one of the most important Claude Code best practices:
```
# CLAUDE.md## Project OverviewBrief description of your project, its purpose, and main technologies.## Development Guidelines- Coding standards and conventions- File structure preferences- Testing approaches## Important Commands- Build commands- Test commands- Development server commands
```

Claude Code automatically reads this file when it starts to provide project context.
## Your First Claude Code Session: Step-by-Step Tutorial​
Claude Code provides two main ways to interact:
**Interactive mode:** Run `claude` to start a REPL session **One-shot mode:** Use `claude -p "query"` for quick commands
### Interactive Mode​
Start Claude Code in your project directory:
```
cd your-projectclaude
```

You'll see the Claude Code prompt, ready to assist with your development tasks.
### One-shot Mode​
For quick queries without starting a full session:
```
claude -p "Show me the files in this directory"claude -p "What kind of project is this?"
```

This mode is perfect for quick questions or when you need fast answers without entering an interactive session.
## Claude Code Examples: Quick Wins for Beginners​
Here are some simple requests to get you comfortable with Claude Code:
### Understanding Your Project​
```
Show me the files in this directory
```

Claude Code will list your project files and explain what it found.
```
What kind of project is this?
```

Claude will analyze your project structure and tell you what type of application it is.
```
Explain what this project does
```

Based on your files and documentation, Claude will summarize the project's purpose.
### Quick Analysis​
```
Show me the main entry point
```

Claude will identify and show you the primary file that starts your application.
```
What dependencies does this project have?
```

Claude will read your package.json, requirements.txt, or similar files and list dependencies.
```
How do I run this project?
```

Claude will look for scripts and documentation to tell you how to start the project.
### Your First File Creation​
Let's create your first file with Claude Code:
```
Create a hello_world.txt file with a greeting message
```

Claude Code will create the file, show you what it wrote, and confirm the creation. This demonstrates Claude's ability to understand natural language and take real actions in your project.
## Essential Claude Code Commands and Examples​
### File Operations​
```
# Read a fileread src/components/Button.js# Edit a fileedit src/components/Button.js# Create a new filewrite src/components/NewComponent.js
```

### Code Analysis​
```
# Analyze code structureanalyze this codebase# Find specific patternsfind all React components# Explain codeexplain how authentication works
```

### Development Tasks​
```
# Add new featuresadd a dark mode toggle to the app# Fix bugsfix the memory leak in the data fetcher# Refactor coderefactor the user service to use TypeScript# Write testswrite unit tests for the Button component
```

## How to Use Claude Code: Natural Language Commands​
Claude Code understands natural language requests, making it easier than traditional development tools:
```
# Instead of complex git commands"Create a commit with all the changes I made to the user authentication"# Instead of manual file operations"Update all components to use the new theme system"# Instead of searching through documentation"How do I set up database migrations in this project?"
```

##### Welcome to the Future
You've just taken your first steps into AI-powered development with Claude Code. The journey ahead leads to unprecedented productivity and creativity in software development.
![Custom image](https://www.claudelog.com/img/discovery/022_excite.png)
## Next Steps​
Now that you know the basics, proceed to Configuration for advanced setup and optimization.
  * Claude Code Project Setup and Configuration
    * CLAUDE.md Configuration
  * Your First Claude Code Session: Step-by-Step Tutorial
    * Interactive Mode
    * One-shot Mode
  * Claude Code Examples: Quick Wins for Beginners
    * Understanding Your Project
    * Quick Analysis
    * Your First File Creation
  * Essential Claude Code Commands and Examples
    * File Operations
    * Code Analysis
    * Development Tasks
  * How to Use Claude Code: Natural Language Commands
  * Next Steps


