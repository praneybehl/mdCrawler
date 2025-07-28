Skip to main content
Claude Code issues usually fall into a few common categories: authentication problems, network connectivity, installation issues, or usage limit constraints. Most problems can be resolved with systematic troubleshooting.
## Quick Diagnostic Steps​
**1. Check Authentication**
```
claude config
```

Verify your API key or subscription login is properly configured.
**2. Test Internet Connection** Claude Code requires internet access to Anthropic's servers. Test with a simple request or visit status.anthropic.com.
**3. Verify Installation**
```
claude --versionnode --version
```

Ensure Claude Code is installed and Node.js is 18.0+.
**4. Check Service Status** Visit status.anthropic.com for known outages or maintenance.
## Common Issues and Solutions​
### Authentication Errors​
**"Authentication failed" or "Invalid API key"**
  * Regenerate your API key in the Anthropic Console
  * Check for extra spaces or characters when setting the key
  * For subscription users, try logging out and back in through the browser


**"Subscription not found"**
  * Verify your Claude subscription is active
  * Try switching between API and subscription authentication methods
  * Check if your subscription includes Claude Code access


### Connection Problems​
**"Connection timeout" or "Network error"**
  * Check your internet connection and firewall settings
  * Try a different network to rule out network-specific issues
  * VPN or corporate proxy may block Claude Code traffic


**"503 Service Unavailable"**
  * This indicates Anthropic server issues, not your setup
  * Wait 3-5 minutes and try again
  * Check status.anthropic.com for service updates


### Installation Issues​
**"Command not found: claude"**
  * Reinstall Claude Code: `npm install -g @anthropic-ai/claude-code`
  * Check your npm global path configuration
  * Try using npx: `npx @anthropic-ai/claude-code`


**"Permission denied" errors**
  * Fix npm permissions or use a Node version manager
  * Don't use `sudo` with npm install
  * Configure npm to use a different directory for global packages


### Usage Limit Issues​
**"Rate limit exceeded"**
  * You've hit your API or subscription usage limits
  * Wait for limits to reset (usually hourly or daily)
  * Check usage in Anthropic Console or with CC Usage tool


**"Context window full"**
  * Use `/compact` to summarize the conversation
  * Start a fresh session with `claude` in a new terminal
  * Break large tasks into smaller sessions


## Systematic Troubleshooting​
### Step 1: Environment Check​
```
# Check Node.js version (must be 18.0+)node --version# Check Claude Code installationclaude --version# Test npm global packagesnpm list -g --depth=0
```

### Step 2: Authentication Test​
```
# Reconfigure authenticationclaude config# Test with a simple commandclaude --help
```

### Step 3: Network Verification​
  * Try accessing other web services
  * Test from a different network if possible
  * Check corporate firewall or VPN settings


### Step 4: Clean Reinstall​
```
# Remove existing installationnpm uninstall -g @anthropic-ai/claude-code# Clear npm cachenpm cache clean --force# Reinstallnpm install -g @anthropic-ai/claude-code
```

## Error-Specific Solutions​
### "Module not found" errors​
  * Usually indicates corrupted installation
  * Perform clean reinstall steps above
  * Check Node.js version compatibility


### "Permission denied" on file operations​
  * Check file/directory permissions in your project
  * Ensure Claude Code can read/write to your project directory
  * Run from a directory you own, not system directories


### Slow response times​
  * Check your internet connection speed
  * Try switching to a faster model (Haiku 3.5)
  * Use `/compact` to reduce context size


### Unexpected behavior or wrong responses​
  * Restart Claude Code session
  * Clear context with `/clear` and start fresh
  * Check if you're using the appropriate model for your task


## When to Seek Help​
**After trying basic troubleshooting** : If standard solutions don't work, the issue may be specific to your setup.
**Service-wide issues** : Check r/ClaudeAI for reports of widespread problems.
**Installation problems** : Ensure your Node.js and npm setup is correct before troubleshooting Claude Code specifically.
**Persistent authentication issues** : Contact Anthropic support through their official channels.
##### Systematic Problem Solving
Authentication, network connectivity, and installation issues account for most Claude Code problems. Prevention through Node.js updates and stable connections beats reactive troubleshooting.
![Custom image](https://www.claudelog.com/img/discovery/009.png)
Prevention Strategy
Most Claude Code issues are preventable: keep Node.js updated, use stable internet connections, monitor your usage limits, and restart sessions periodically to avoid context window issues.
**See Also** : Installation Guide|Claude Code Usage Limits|Auto-Compact
  * Quick Diagnostic Steps
  * Common Issues and Solutions
    * Authentication Errors
    * Connection Problems
    * Installation Issues
    * Usage Limit Issues
  * Systematic Troubleshooting
    * Step 1: Environment Check
    * Step 2: Authentication Test
    * Step 3: Network Verification
    * Step 4: Clean Reinstall
  * Error-Specific Solutions
    * "Module not found" errors
    * "Permission denied" on file operations
    * Slow response times
    * Unexpected behavior or wrong responses
  * When to Seek Help


