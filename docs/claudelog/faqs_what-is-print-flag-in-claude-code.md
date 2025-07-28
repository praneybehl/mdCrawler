Skip to main content
The --print flag (or -p) runs Claude Code in non-interactive mode, executing a single query and outputting results directly to the terminal without the interactive chat interface.
### How to Use It​
Use `--print` or `-p` with a query to execute Claude Code commands in automation-friendly mode that processes one request and exits.
```
claude -p "Fix ESLint errors in src/"claude --print "Generate unit tests for auth.js"claude -p "Review code quality" --model opus
```

### Why Use --print​
The --print flag enables Claude Code integration into scripts, CI/CD pipelines, and automated workflows where interactive sessions aren't suitable or practical.
**Benefits:**
  * **Automation Integration** - Perfect for scripts, CI/CD, and batch processing
  * **Single Query Processing** - Executes one command and exits cleanly
  * **Output Control** - Supports JSON and text formats for programmatic usage
  * **Pipeline Friendly** - Works seamlessly in build and deployment workflows
  * **Resource Efficient** - No persistent session overhead for simple tasks


### Common Use Cases​
**CI/CD Integration** - Automated code analysis and quality checks in build pipelines:
```
claude -p "Check code quality and suggest improvements" --output-format json
```

**Script Automation** - Batch processing multiple files or generating documentation:
```
claude -p "Generate API documentation from source code" > api_docs.md
```

**Error Analysis** - Automated debugging and log analysis:
```
claude -p "Analyze error patterns in application.log" --max-turns 2
```

### Advanced Usage​
**Output Formats** - Control response structure for different use cases:
```
claude -p "List all functions" --output-format json  # Structured dataclaude -p "Explain code flow" --output-format text   # Human readable
```

**Resource Control** - Limit processing scope:
```
claude -p "Quick code review" --max-turns 1      # Fast executionclaude -p "Complex analysis" --max-turns 3       # Thorough analysis
```

Automation Power
--print transforms Claude Code into a powerful automation tool for development workflows. Combine with --output-format json for structured data processing.
##### Pipeline Integration
--print enables Claude Code integration into any automated workflow or script. Execute single commands efficiently without interactive overhead.
![Custom image](https://www.claudelog.com/img/discovery/005_scary.png)
**See Also** : Output Format|Max Turns|Configuration
  * How to Use It
  * Why Use --print
  * Common Use Cases
  * Advanced Usage


