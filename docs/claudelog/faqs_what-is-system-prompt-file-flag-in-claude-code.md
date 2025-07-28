Skip to main content
The --system-prompt-file flag overrides Claude Code's default system prompt with custom instructions from a file, enabling specialized workflows and consistent prompting behavior.
### How to Use It​
Use `--system-prompt-file` with a file path containing your custom prompt instructions. This flag only works in print mode, not interactive mode.
```
claude --system-prompt-file path/to/prompt.txt "Review this code"claude --system-prompt-file prompts/reviewer.txt --model opus "Analyze security"
```

### Creating Custom Prompt Files​
**File Format** - Plain text files with clear instructions:
```
You are a Python code reviewer. Focus on:- Performance optimizations - Security vulnerabilities- PEP 8 complianceBe concise and provide specific suggestions.
```

**Benefits:**
  * **Complete Control** : Replaces default Claude Code behavior entirely
  * **Specialized Workflows** : Tailored prompts for code review, documentation, testing
  * **Team Consistency** : Share standardized prompts across development teams
  * **Print Mode Only** : Works exclusively with non-interactive Claude Code usage


### Relationship to --append-system-prompt​
**Key Differences** - Two distinct approaches to prompt customization:
  * **--system-prompt-file** : Completely replaces the default system prompt
  * **--append-system-prompt** : Adds instructions to the existing default prompt


##### Custom System Prompts
--system-prompt-file enables complete prompt customization for specialized workflows. Perfect for code review, documentation generation, and team standardization.
![Custom image](https://www.claudelog.com/img/discovery/036_cl.png)
**See Also** : --print Flag|--append-system-prompt
  * How to Use It
  * Creating Custom Prompt Files
  * Relationship to --append-system-prompt


