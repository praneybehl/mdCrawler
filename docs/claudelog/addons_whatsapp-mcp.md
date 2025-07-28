Skip to main content
On this page
**Personal WhatsApp messaging and search capabilities for Claude Code**
**Author** : lharries | GitHub Repo | 4528 Stars|653 Forks|MIT License|Updated Jul 23, 2025
### Overview​
WhatsApp MCP enables Claude Code to interact with your personal WhatsApp account through the Model Context Protocol. Search and read your WhatsApp messages (including media), manage contacts, and send messages to individuals or groups using WhatsApp Web's multidevice API.
### Features​
  * **Message Search** - Search through your personal WhatsApp message history
  * **Media Support** - Access images, videos, documents, and audio messages
  * **Contact Management** - Search contacts by name or phone number
  * **Group Messaging** - Send messages to individuals or groups
  * **Local Storage** - All messages stored locally in SQLite database
  * **Privacy-First** - Messages only sent to LLM when actively accessed


### Installation​
**Prerequisites**
  * WhatsApp account with multidevice support
  * Go 1.19+ programming language installed
  * Python 3.6+ installed
  * UV package manager: `pip install uv`
  * FFmpeg (optional, for audio message conversion)
  * **Windows users** : CGO enabled and C compiler installed


**Step 1: Clone and Build**
```
git clone https://github.com/lharries/whatsapp-mcp.gitcd whatsapp-mcpgo build -o whatsapp-mcp-server
```

**Step 2: WhatsApp Bridge Setup**
```
cd whatsapp-bridge# Start the bridge (follow repo instructions for your OS)# Scan QR code with your WhatsApp mobile app when prompted# Wait for initial message history sync to complete
```

**Step 3: Claude Code Configuration**
Edit `~/.claude.json`:
```
{"projects":{"/path/to/your/project":{"mcpServers":{"whatsapp":{"command":"uv","args":["--directory","/path/to/whatsapp-mcp-server","run","main.py"],"env":{}}}}}}
```

**Step 4: Start Services**
  1. Restart Claude Code after configuration
  2. Ensure WhatsApp bridge is running
  3. Test with a simple contact search command


**Troubleshooting**
  * **QR Code Issues** : Ensure WhatsApp multidevice is enabled on your phone
  * **Build Errors** : Verify Go installation and GOPATH configuration
  * **Windows Compilation** : Install TDM-GCC or Visual Studio Build Tools
  * **Bridge Connection** : Check firewall settings and port availability


### Usage​
**Message Search and Analysis**
```
# Search your message historyclaude "Search for messages about the project deadline from last week"# Analyze conversation patternsclaude "What were the main topics discussed with John in the last month?"
```

For detailed setup instructions and advanced configuration, see the official documentation.
Pro Tip
Set up Claude Code to monitor messages sent to your own WhatsApp number. By messaging yourself and starting with "claude", it allows you to access Claude Code remotely from any device with WhatsApp access - including desktop, mobile and smartwatch.
##### Extensibility
WhatsApp MCP provides a great foundation for additional functionality. The repository can be easily extended to accommodate custom functionality beyond the default messaging capabilities.
![Custom image](https://www.claudelog.com/img/discovery/004.png)
_WhatsApp MCP is developed by lharries as a community project. For technical support and setup assistance, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


