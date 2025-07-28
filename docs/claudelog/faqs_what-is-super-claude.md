Skip to main content
SuperClaude is a configuration framework that enhances Claude Code with specialized commands and cognitive personas for optimized development workflows. It provides structured guidance through 19 specialized commands and 9 domain-expert personas, transforming Claude Code into a more focused and methodical development assistant.
**Official Repository** : https://github.com/NomenAK/SuperClaude
### Core Capabilities​
**19 Specialized Commands** across four development phases:
  * **Development** - `/build`, `/code`, `/debug` for implementation
  * **Analysis** - `/analyze`, `/optimize`, `/refactor`, `/review`, `/audit` for code improvement
  * **Operations** - `/deploy`, `/test`, `/monitor`, `/backup`, `/scale`, `/migrate` for system management
  * **Design** - `/design`, `/plan`, `/document`, `/workflow`, `/research` for planning


**9 Cognitive Personas** that work as universal flags:
  * **Specialists** - architect, frontend, backend, security, analyzer, qa, performance, refactorer, mentor
  * **Usage** - Apply any persona to any command for domain-specific guidance


### Installation​
Clone the repository and run the installer:
```
git clone https://github.com/NomenAK/SuperClaude.gitcd SuperClaude./install.sh
```

The installer configures your `~/.claude/` directory with the SuperClaude command system.
### How to Use It​
Combine commands with personas for targeted development assistance:
```
# Architecture phase with domain expertise/design --api --ddd --architect# Implementation with testing focus/build --feature --tdd --backend# Security-focused code review/review --security# Performance optimization/optimize --performance
```

### Why Use SuperClaude​
**Structured Development** - Transforms Claude Code from general assistant to specialized development methodologist with consistent, focused responses.
**Domain Expertise** - Cognitive personas provide expert-level guidance for specific development areas without switching contexts.
**Workflow Optimization** - Specialized commands match your development phases, reducing ambiguity and improving task completion.
SuperClaude is particularly useful when you need Claude Code to think like a specialist rather than a generalist, especially for complex development tasks requiring domain expertise.
##### Structured Development Flow
SuperClaude's specialized commands and cognitive personas create consistent, expert-level guidance for every development phase.
![Custom image](https://www.claudelog.com/img/discovery/017.png)
Configuration Framework
SuperClaude uses modular configuration with @include references, allowing flexible customization while maintaining structured development approaches.
**See Also** : SuperClaude Add-on|Configuration|Getting Started
  * Core Capabilities
  * Installation
  * How to Use It
  * Why Use SuperClaude


