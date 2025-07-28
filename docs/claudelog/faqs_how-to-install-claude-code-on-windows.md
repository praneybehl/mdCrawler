Skip to main content
I use Claude Code on Windows via WSL2 (Windows Subsystem for Linux). The setup requires a few specific steps, but once configured properly, the experience is seamless.
### Prerequisites​
Before installing Claude Code, you'll need:
  * **Windows 10 version 2004 or higher** (or Windows 11)
  * **WSL2 installed and configured**
  * **Node.js 18.0+ in your WSL environment**
  * **Anthropic API key or Claude subscription**


### Step by Step Installation​
**1. Install WSL2**
If you haven't already installed WSL2:
```
wsl --install
```

This installs WSL2 with Ubuntu by default. Restart your computer when prompted.
**2. Set Up Your Linux Environment**
Open your WSL terminal and update packages:
```
sudo apt update && sudo apt upgrade -y
```

**3. Install Node.js**
Install Node.js 18.0+ in your WSL environment:
```
# Download and run NodeSource setup script for LTS versioncurl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -sudo apt-get install -y nodejs
```

Verify the installation:
```
node --versionnpm --version
```

**4. Install Claude Code**
Now install Claude Code globally:
```
npm install -g @anthropic-ai/claude-code
```

**5. Configure Authentication**
Set up your authentication method:
**For API users:**
```
claude config
```

**For subscription users:** You'll authenticate through the browser when you first run `claude`.
### VS Code Integration​
Once Claude Code is installed, you can seamlessly integrate it with Visual Studio Code. I use this setup daily and find it incredibly productive.
  * **Open VS Code on Windows** : Launch Visual Studio Code from your Windows desktop or start menu
  * **Install the WSL extension** : Search for "WSL" in the Extensions panel and install the official Microsoft WSL extension
  * **Open your project in WSL** : Use Ctrl+Shift+P, type "WSL: Open Folder in WSL" and select your project directory
  * **Access WSL terminal** : Open the integrated terminal (Ctrl+`) which will automatically connect to your WSL environment
  * **Launch Claude Code** : Run `claude` in the integrated terminal to start your Claude Code session


This gives you the best of both worlds: familiar VS Code interface with Claude Code's powerful terminal capabilities.
### Testing Your Installation​
Create a simple test to verify everything works:
```
mkdir claude-testcd claude-testecho "# Test Project" > README.mdclaude
```

If Claude Code starts successfully and can read your README.md file, you're all set!
##### WSL2 Integration Excellence
VS Code's Remote-WSL extension provides seamless integration between Windows and Linux environments. This setup delivers the best of both worlds: familiar interface with powerful terminal capabilities.
![Custom image](https://www.claudelog.com/img/discovery/004.png)
**See Also** : Installation Guide|Getting Started
  * Prerequisites
  * Step by Step Installation
  * VS Code Integration
  * Testing Your Installation


