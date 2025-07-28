Skip to main content
On this page
Get Claude Code up and running on your system in just a few steps. This complete Claude Code installation and setup guide covers download, installation, configuration, and model selection for Windows, Mac, and Linux systems.
**Note:** For the most up-to-date installation instructions, visit the official Claude Code documentation.
## Claude Code System Requirements and Prerequisites​
Claude Code supports the following operating systems:
  * **macOS** 10.15 (Catalina) or later
  * **Windows** 10 or later
  * **Linux** (Ubuntu 18.04+, CentOS 7+, or equivalent)


**Hardware Requirements:**
  * 4GB RAM minimum (16GB is my recommendation)
  * 500MB available disk space
  * Internet connection for API communication


## Prerequisites​
Before installing Claude Code, make sure you have:
  * **Node.js** version 18.0 or higher
  * An **Anthropic API key** (get one from console.anthropic.com)
  * A terminal or command prompt


## How to Install Claude Code: Step-by-Step Methods​
### Option 1: npm (Recommended)​
```
npm install -g @anthropic-ai/claude-code
```

### Option 2: Direct Download​
Download the latest binary from the GitHub releases page.
## Claude Code Setup and Configuration Guide​
### API Key Configuration​
After installation, configure Claude Code with your API key:
```
claude config
```

You'll complete a one-time OAuth process with your Claude Max or Anthropic Console account.
### Alternative: Environment Variable​
You can also set your API key using an environment variable:
```
export ANTHROPIC_API_KEY="your-api-key-here"
```

Add this to your shell profile (`.bashrc`, `.zshrc`, etc.) to make it persistent.
### Claude Max Subscription​
**Important:** The Anthropic API is pay-per-use and can become expensive with frequent usage. For regular Claude Code users, a Claude Max subscription is likely the more economical option. Claude Max provides higher usage limits at a fixed monthly cost, making it ideal for developers using Claude Code extensively.
Consider Claude Max if you plan to:
  * Use Claude Code for multiple hours per day
  * Work on large codebases
  * Perform complex multi-file operations regularly


**Getting Started:** If you're unsure about your usage patterns, consider starting with ~$20 in API credits to test Claude Code with your typical workflows. This will help you determine whether the Claude Max subscription is worth the investment for your specific use case.
For complete pricing breakdown and plan comparison, see our Claude AI Pricing Guide.
_Disclaimer: The author uses Claude Max 5x._
### Claude Code Model Selection and Configuration​
Claude Code supports multiple models. You can specify which model to use for optimal performance:
**Claude 4 Sonnet:** Latest balanced performance and speed
```
export ANTHROPIC_MODEL="claude-sonnet-4-20250514"
```

**Claude 4 Opus:** Maximum capability for complex tasks
```
export ANTHROPIC_MODEL="claude-opus-4-20250514"
```

**Claude 3.5 Haiku:** Fastest and most cost-effective
```
export ANTHROPIC_MODEL="claude-3-5-haiku-20241022"
```

Important limitations: Claude 3.5 Haiku
While Haiku is cost-effective, it has significant limitations for Claude Code usage:
  * **Reduced reasoning capabilities** - Struggles with complex multi-step planning and architectural decisions
  * **Limited context understanding** - Less effective at analyzing large codebases and maintaining context across multiple files
  * **Simplified code analysis** - May miss subtle bugs, dependencies, or complex patterns that modern models catch
  * **Basic refactoring only** - Not suitable for sophisticated restructuring or feature implementations
  * **Limited framework knowledge** - Less effective with complex frameworks or novel coding patterns


**Recommended use cases for Haiku:**
  * Simple single-file edits
  * Basic syntax corrections
  * Quick code questions
  * Learning Claude Code basics before upgrading


For serious development work, Claude 4 Sonnet or Opus provide substantially better results and are worth the additional cost.
**Alternative Method:** You can also specify the model directly when starting Claude Code:
```
claude --model claude-sonnet-4-20250514claude --model claude-opus-4-20250514claude --model claude-3-5-haiku-20241022
```

To monitor your usage and costs, consider the cc-usage add-on.
For detailed model comparison and selection guidance, see our Complete Model Comparison Guide.
## Platform-Specific Claude Code Setup: Windows, Mac, and Linux​
### Claude Code Windows Setup​
For the best Claude Code experience on Windows, follow these optimization steps:
#### WSL2 Installation and Configuration​
**1. Install WSL2** (if not already installed):
```
wsl --install
```

**2. Install a Linux distribution** (Ubuntu recommended):
```
wsl --install -d Ubuntu
```

**3. WSL2 Performance Optimization:**
Set WSL2 memory limit by creating `.wslconfig` in your Windows user directory:
```
# In Windows: %USERPROFILE%\.wslconfig[wsl2]memory=8GB     # Limit WSL2 memory usageprocessors=4    # Limit CPU coresswap=2GB      # Set swap sizelocalhostForwarding=true
```

**4. Update WSL2 to latest version:**
```
wsl --update
```

#### Terminal Recommendation​
I personally use Windows Terminal app for Claude Code development. You can download it from the Microsoft Store or GitHub releases.
#### Claude Code VS Code Integration​
**1. Install VS Code Extensions:**
  * **WSL Extension:** `ms-vscode-remote.remote-wsl`
  * **Remote Development Extension Pack:** `ms-vscode-remote.vscode-remote-extensionpack`


**2. Connect VS Code to WSL:**
```
# From WSL terminal in your project directorycode .
```

**3. Install Claude Code VS Code Extension:** Install the official Claude Code extension from the VS Code Marketplace or search for "Claude Code" in VS Code's Extensions panel.
**4. Restart VS Code** completely for the extension to take effect.
**5. Use Claude Code with VS Code:**
```
# In VS Code integrated terminal (WSL)claude# Or use /ide command from any external terminal to connect
```

**6. VS Code Integration Features:**
  * Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open Claude Code directly
  * File references: `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Windows/Linux) to insert file references
  * View proposed changes in VS Code's diff viewer


## Verify Claude Code Installation: Testing Your Setup​
Verify your Claude Code installation by running:
```
claude --version
```

You should see the current version of Claude Code printed to the terminal.
##### Installation Complete
With Claude Code successfully installed, you now have access to one of the most powerful AI development tools available. Every great development journey begins with a solid foundation.
![Custom image](https://www.claudelog.com/img/discovery/014.png)
**Next:** Head to the Getting Started section to learn about Claude Code project setup, basic commands, and workflow optimization.
  * Claude Code System Requirements and Prerequisites
  * Prerequisites
  * How to Install Claude Code: Step-by-Step Methods
    * Option 1: npm (Recommended)
    * Option 2: Direct Download
  * Claude Code Setup and Configuration Guide
    * API Key Configuration
    * Alternative: Environment Variable
    * Claude Max Subscription
    * Claude Code Model Selection and Configuration
  * Platform-Specific Claude Code Setup: Windows, Mac, and Linux
    * Claude Code Windows Setup
  * Verify Claude Code Installation: Testing Your Setup


