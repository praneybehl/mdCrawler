Skip to main content
Complete troubleshooting guide for Claude Code installation, configuration, and usage issues. Get step-by-step solutions for common problems and error messages.
## Installation Issues​
### Node.js Version Problems​
**Problem:** Claude Code installation fails with Node.js version errors **Solution:**
  1. Check your Node.js version: `node --version`
  2. Claude Code requires Node.js 18.0 or higher
  3. Update Node.js from nodejs.org
  4. Restart your terminal after installation
  5. Retry Claude Code installation


### Permission Errors During Installation​
**Problem:** "Permission denied" or "EACCES" errors during npm install **Solution:**
**For macOS/Linux:**
```
# Fix npm permissionssudo chown -R $(whoami) ~/.npm# Or install with sudo (not recommended)sudo npm install -g @anthropic-ai/claude-code
```

**For Windows:**
```
# Run Command Prompt as Administratornpm install -g @anthropic-ai/claude-code
```

### Installation Hangs or Times Out​
**Problem:** Installation process freezes or network timeouts **Solution:**
  1. Check internet connection
  2. Try with different npm registry:


```
npm install -g @anthropic-ai/claude-code --registry https://registry.npmjs.org/
```

  1. Clear npm cache: `npm cache clean --force`
  2. Restart and retry installation


## Authentication and Configuration Issues​
### API Key Problems​
**Problem:** "Invalid API key" or authentication failures **Solution:**
  1. Verify API key at console.anthropic.com
  2. Reconfigure Claude Code: `claude config`
  3. Check environment variables:


```
echo $ANTHROPIC_API_KEY
```

  1. Ensure no extra spaces or characters in API key


### Subscription Authentication Issues​
**Problem:** Can't authenticate with Claude Max/Pro subscription **Solution:**
  1. Ensure you're logged into the correct Claude account
  2. Clear browser cookies and retry authentication
  3. Use incognito/private browsing mode
  4. Contact Anthropic support if subscription isn't recognized


### Configuration File Problems​
**Problem:** Claude Code ignores configuration settings **Solution:**
  1. Check configuration file location: `~/.claude.json`
  2. Verify JSON syntax is valid
  3. Reset configuration: `claude config --reset`
  4. Manually edit `~/.claude.json` if needed


## Connection and Network Issues​
### Claude Code Not Responding​
**Problem:** Claude Code starts but doesn't respond to commands **Solution:**
  1. **Restart Claude Code** - Exit and restart the application
  2. **Check internet connection** - Test with other websites
  3. **Verify API status** - Check status.anthropic.com
  4. **Clear session** - Use `/clear` command to start fresh
  5. **Update Claude Code** - Run `npm update -g @anthropic-ai/claude-code`


### 503 Service Unavailable Errors​
**Problem:** Getting "503 no healthy upstream" errors **Solution:**
  * **Wait 2-5 minutes** - These are temporary server issues
  * **Check service status** - Visit status.anthropic.com
  * **Don't reinstall** - This won't fix server-side problems
  * **Try again later** - Server issues usually resolve quickly


### Internal Server Errors​
**Problem:** "Internal server error" messages **Solution:**
  * **Wait 1-3 minutes** - Backend processing issues resolve automatically
  * **Don't change configuration** - This is a server-side problem
  * **Check community reports** - Visit r/ClaudeAI for widespread issues
  * **Avoid reinstalling** - Won't help with server problems


## Performance Issues​
### Slow Response Times​
**Problem:** Claude Code responses are very slow **Solution:**
  1. **Switch models** - Try Claude 4 Sonnet for better speed
  2. **Reduce context** - Use `/compact` to summarize conversation
  3. **Smaller files** - Break large files into smaller components
  4. **Native platform** - Use Linux/macOS instead of WSL when possible
  5. **Adequate RAM** - Ensure 16GB+ RAM for optimal performance


### High Memory Usage​
**Problem:** Claude Code consuming too much system memory **Solution:**
  1. **Restart Claude Code** regularly for long sessions
  2. **Use`/clear`** to reset conversation history
  3. **Close other applications** to free up RAM
  4. **Monitor usage** with system activity monitor
  5. **Consider upgrading RAM** if consistently hitting limits


### Context Window Issues​
**Problem:** "Context window full" or memory limit errors **Solution:**
  1. **Use`/compact`** with specific instructions:


```
/compact keep only the main function names and error messages
```

  1. **Start fresh** with `/clear` command
  2. **Smaller chunks** - Work on one feature at a time
  3. **Sub-agents** - Use Task tool for parallel processing
  4. **File organization** - Use many small files instead of large ones


## Platform-Specific Issues​
### Windows WSL Problems​
**Problem:** Claude Code performance issues on Windows WSL **Solution:**
  1. **Update WSL2** : `wsl --update`
  2. **Optimize WSL memory** - Configure `.wslconfig`:


```
[wsl2]memory=8GBprocessors=4
```

  1. **Use Windows Terminal** for better performance
  2. **Store files in Linux filesystem** (`/home/` not `/mnt/c/`)
  3. **Consider native Linux** for best performance


### VS Code Integration Issues​
**Problem:** Claude Code VS Code extension not working **Solution:**
  1. **Install extension** from VS Code Marketplace
  2. **Restart VS Code** completely after installation
  3. **Check WSL connection** - Ensure VS Code connects to WSL
  4. **Use`/ide` command** from external terminal to connect
  5. **Verify file paths** - Ensure working in correct directory


## File and Project Issues​
### Permission Denied on File Operations​
**Problem:** Can't read/write files in project directory **Solution:**
  1. **Check file permissions** : `ls -la`
  2. **Fix ownership** : `sudo chown -R $(whoami) .`
  3. **Verify directory access** - Ensure Claude Code can access project folder
  4. **Use`--add-dir`** flag for multiple directories
  5. **Configure allowed tools** in `~/.claude.json`


### Large File Handling Problems​
**Problem:** Claude Code struggles with large files **Solution:**
  1. **Split large files** into smaller, logical components
  2. **Use specific ranges** when reading large files
  3. **Exclude build artifacts** - Don't process generated files
  4. **Focus requests** - Ask about specific functions, not entire files
  5. **Create summaries** of large codebases in CLAUDE.md


## Model and Feature Issues​
### Model Switching Problems​
**Problem:** Can't switch between Claude models **Solution:**
  1. **Use correct syntax** : `claude --model claude-sonnet-4-20250514`
  2. **Check subscription** - Ensure access to requested model
  3. **Restart session** after model change
  4. **Verify model names** - Use exact model identifiers
  5. **Update Claude Code** - Newer versions support more models


### Sub-agent Issues​
**Problem:** Sub-agents not working or hanging **Solution:**
  1. **Check internet connection** - Sub-agents need network access
  2. **Simplify tasks** - Break complex requests into smaller parts
  3. **Monitor progress** - Look for flashing bubbles in UI
  4. **Manual tasks** - Do critical work in main thread
  5. **Restart if stuck** - Exit and restart Claude Code


## Advanced Troubleshooting​
### Complete Reset Procedure​
If all else fails, try a complete reset:
  1. **Uninstall Claude Code** :


```
npm uninstall -g @anthropic-ai/claude-code
```

  1. **Remove configuration** :


```
rm ~/.claude.jsonrm -rf ~/.claude/
```

  1. **Clear npm cache** :


```
npm cache clean --force
```

  1. **Reinstall fresh** :


```
npm install -g @anthropic-ai/claude-codeclaude config
```

### Log Collection for Support​
To get help from support, collect these details:
  1. **Claude Code version** : `claude --version`
  2. **Node.js version** : `node --version`
  3. **Operating system** : `uname -a` (Linux/Mac) or `ver` (Windows)
  4. **Error messages** - Copy exact error text
  5. **Configuration** - Share `~/.claude.json` (remove API keys)


## Getting Additional Help​
### Community Resources​
  * **Reddit** : r/ClaudeAI for community support
  * **Awesome Claude Code** : GitHub repository for tools and tips
  * **Status page** : status.anthropic.com for service updates


### Official Support​
  * **Documentation** : docs.anthropic.com
  * **Console** : console.anthropic.com for API issues
  * **Contact** : Use official Anthropic support channels for account problems


### Prevention Tips​
  * **Keep updated** - Regularly update Claude Code and Node.js
  * **Monitor status** - Check service status before major sessions
  * **Backup configuration** - Save working `~/.claude.json` files
  * **Test changes** - Verify configuration changes in small projects first
  * **Regular restarts** - Restart Claude Code periodically in long sessions


**See Also** : Installation Guide|Configuration|Getting Started|Windows Installation|FAQ
_This troubleshooting guide covers the most common Claude Code issues. For additional help, check the community resources above._
  * Installation Issues
    * Node.js Version Problems
    * Permission Errors During Installation
    * Installation Hangs or Times Out
  * Authentication and Configuration Issues
    * API Key Problems
    * Subscription Authentication Issues
    * Configuration File Problems
  * Connection and Network Issues
    * Claude Code Not Responding
    * 503 Service Unavailable Errors
    * Internal Server Errors
  * Performance Issues
    * Slow Response Times
    * High Memory Usage
    * Context Window Issues
  * Platform-Specific Issues
    * Windows WSL Problems
    * VS Code Integration Issues
  * File and Project Issues
    * Permission Denied on File Operations
    * Large File Handling Problems
  * Model and Feature Issues
    * Model Switching Problems
    * Sub-agent Issues
  * Advanced Troubleshooting
    * Complete Reset Procedure
    * Log Collection for Support
  * Getting Additional Help
    * Community Resources
    * Official Support
    * Prevention Tips


