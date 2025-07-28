Skip to main content
Quick guide to check Claude AI service status and resolve common connectivity issues. Get real-time updates and troubleshooting steps for Claude service problems.
## Quick Status Check​
### Official Status Sources​
**Primary Status Page:**
  * **Anthropic Status:** status.anthropic.com
  * **Real-time updates** on service incidents and maintenance
  * **Historical data** on past outages and resolutions


**Community Reports:**
  * **Reddit:** r/ClaudeAI for user reports
  * **Real-time discussions** during widespread issues
  * **Community troubleshooting** and workaround sharing


### Common Signs Claude is Down​
**Service Unavailable Errors:**
  * **503 Service Unavailable** - Most common during outages
  * **502 Bad Gateway** - Server connection issues
  * **504 Gateway Timeout** - Server response timeouts


**Authentication Issues:**
  * **Login failures** - Can't access Claude web interface
  * **API authentication errors** - Token validation problems
  * **Session timeouts** - Unexpected disconnections


**Performance Problems:**
  * **Very slow responses** - Significantly delayed replies
  * **Partial failures** - Some features work, others don't
  * **Inconsistent availability** - Works intermittently


## Troubleshooting Steps​
### First Steps - Check Your Connection​
**1. Verify Internet Connection:**
```
# Test general connectivityping google.com# Test Claude domainping claude.ai
```

**2. Try Different Device/Network:**
  * **Mobile data** vs WiFi
  * **Different device** (phone, laptop)
  * **Incognito/private mode** to rule out browser issues


**3. Check Other Services:**
  * **Test other websites** to confirm internet works
  * **Try Claude web interface** if using Claude Code
  * **Check related services** (OpenAI, ChatGPT) for broader issues


### Claude Code Specific Troubleshooting​
**1. Restart Claude Code:**
```
# Exit current sessionexit# Restart Claude Codeclaude
```

**2. Check Configuration:**
```
# Verify configurationclaude config# Test API connectionclaude --version
```

**3. Try Different Model:**
```
# Switch to different modelclaude --model claude-3-5-haiku-20241022# Or try Sonnet if using Opusclaude --model claude-sonnet-4-20250514
```

### When to Wait vs. Troubleshoot​
**Wait it out (2-5 minutes) if:**
  * **503 errors** are appearing
  * **Multiple users reporting** issues on Reddit
  * **Status page shows** ongoing incident
  * **Errors started suddenly** during normal operation


**Troubleshoot immediately if:**
  * **Only you're affected** (no community reports)
  * **Specific to Claude Code** (web interface works)
  * **Authentication problems** persist
  * **Been failing for 10+ minutes** with no status updates


## Common Error Messages​
### 503 Service Unavailable​
**What it means:** Server temporarily overloaded or down **Typical duration:** 2-5 minutes **Action:** Wait and retry, don't reinstall Claude Code
### Internal Server Error​
**What it means:** Backend processing issue **Typical duration:** 1-3 minutes **Action:** Wait for automatic resolution
### Authentication Failed​
**What it means:** Login or API key problem **Possible causes:**
  * Expired session
  * API key issues
  * Account problems **Action:** Try logging out/in, check API key, contact support


### Rate Limit Exceeded​
**What it means:** Too many requests too quickly **Typical duration:** Few minutes to hours **Action:** Wait for limit reset, check usage patterns
## Prevention and Monitoring​
### Stay Informed​
**Subscribe to Updates:**
  * **Anthropic status page** email notifications
  * **Reddit notifications** for r/ClaudeAI posts
  * **Community Discord** servers for real-time updates


**Monitor Usage:**
  * **Track your patterns** to identify personal vs service issues
  * **Use status tools** like CC Usage for insights
  * **Plan around known maintenance** windows


### Best Practices During Outages​
**Save Your Work:**
  * **Copy important conversations** before they're lost
  * **Document solutions** you were working on
  * **Have backup plans** for critical development work


**Alternative Workflows:**
  * **Continue with non-Claude tasks** during outages
  * **Review and plan** next steps for when service returns
  * **Local development** that doesn't require AI assistance


## When to Contact Support​
**Contact Anthropic Support if:**
  * **Personal account issues** persist after status shows "operational"
  * **API key problems** that configuration doesn't resolve
  * **Billing or subscription** problems during outages
  * **Service works for others** but not your account specifically


**Include in Support Requests:**
  * **Error messages** (exact text)
  * **Timestamps** when issues started
  * **Your configuration** (without API keys)
  * **Steps you've tried** to resolve


##### Service Disruption Alert
When Claude goes dark, check status pages first before diving into local troubleshooting. Server issues resolve themselves faster than your debugging efforts can complete.
![Custom image](https://www.claudelog.com/img/discovery/005_scary.png)
**See Also** : Troubleshooting Guide|Configuration|FAQs
_Most Claude service issues resolve automatically within minutes. Check the official status page first, then try basic troubleshooting steps before assuming the problem is on your end._
  * Quick Status Check
    * Official Status Sources
    * Common Signs Claude is Down
  * Troubleshooting Steps
    * First Steps - Check Your Connection
    * Claude Code Specific Troubleshooting
    * When to Wait vs. Troubleshoot
  * Common Error Messages
    * 503 Service Unavailable
    * Internal Server Error
    * Authentication Failed
    * Rate Limit Exceeded
  * Prevention and Monitoring
    * Stay Informed
    * Best Practices During Outages
  * When to Contact Support


