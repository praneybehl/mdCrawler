Skip to main content
Custom system prompts let you guide Claude's behavior for specific tasks. I am exploring using them to make Claude focus on particular aspects like security, algorithm performance, or response constraints depending on what I am working on.
### Understanding System Prompts​
**What they control** - System prompts add specific instructions to Claude's default behavior, letting you customize its expertise level and focus areas.
**How it works** - The `--append-system-prompt` option adds your custom instructions to Claude's existing helpful behavior rather than replacing it entirely.
**Interactive mode support** - As of v1.0.51, `--append-system-prompt` works in interactive mode, not just print mode.
### Basic Usage​
**Print mode with custom focus** - Add specific instructions for single-task sessions:
```
# Add security focus to code reviewclaude -p "Review this authentication code" --append-system-prompt "After analyzing the code, always check for common security vulnerabilities like SQL injection, XSS, and insecure token handling."# Database expertise for design tasksclaude -p "Design a user system" --append-system-prompt "You are a database architect with 10 years PostgreSQL experience. Focus on proper normalization, indexing strategies, and query performance. Always consider data integrity and scalability."
```

**Interactive mode with persistent focus** - Maintain consistent behavior throughout your coding session:
```
# Interactive mode with algorithm performance focusclaude --append-system-prompt "When writing code, prioritize algorithm efficiency and performance optimization. Always analyze time and space complexity and suggest performance improvements."# Start session with security mindsetclaude --append-system-prompt "You are a senior backend engineer specializing in secure API development. Prioritize input validation, authentication, and proper error handling. Always include rate limiting and logging."
```

### Practical Development Examples​
**Code review specialist** - You could use this when you need thorough code analysis:
```
claude --append-system-prompt "You are conducting a senior-level code review. Focus on: 1) Performance bottlenecks, 2) Security vulnerabilities, 3) Code maintainability, 4) Test coverage gaps. Provide specific line-by-line feedback with improvement suggestions."
```

**Legacy code modernization** - Helpful when working with older codebases:
```
claude --append-system-prompt "You are modernizing legacy code. Prioritize backwards compatibility while introducing modern patterns. Always explain migration strategies and potential breaking changes."
```

### When to Use System Prompts​
**Print mode scenarios** :
  * **Single-task focus** - Working on one specific type of problem that needs expert attention
  * **Code review sessions** - Adding consistent review criteria for quality checks
  * **Specialized analysis** - Security audits, performance optimization, or architecture review


**Interactive mode scenarios** :
  * **Long coding sessions** - Maintaining consistent expertise and focus throughout development
  * **Performance optimization** - Focusing on algorithm efficiency and performance improvements across an entire project
  * **Learning sessions** - Having Claude teach specific concepts or patterns consistently


##### Custom Behavior Control
System prompts transform Claude from general assistant to specialized development expert. Use `--append-system-prompt` in interactive mode to maintain focus throughout long coding sessions.
![Custom image](https://www.claudelog.com/img/discovery/032_wind.png)
**See Also** : Configuration Guide
  * Understanding System Prompts
  * Basic Usage
  * Practical Development Examples
  * When to Use System Prompts


