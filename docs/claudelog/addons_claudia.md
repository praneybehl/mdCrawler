Skip to main content
On this page
**GUI interface for Claude Code offering visual project management, custom AI agents, and usage analytics**
**Author** : getAsterisk | GitHub Repo | 9613 Stars|758 Forks|AGPL-3.0 License|Updated Jul 23, 2025
### Overview​
Claudia provides a graphical interface for Claude Code, perfect for developers who prefer visual tools over terminal workflows. Transform your Claude Code experience with session timelines, custom AI agents, and comprehensive usage analytics in a modern desktop application.
### Features​
  * **Visual Project Browser** - Navigate projects and sessions with rich metadata and thumbnails
  * **Session Timeline** - Visual history with checkpoints, branching, and one-click restoration
  * **Custom AI Agents** - Create specialized assistants with tailored system prompts
  * **Usage Analytics Dashboard** - Real-time tracking of token consumption and costs
  * **MCP Server Management** - Centrally manage all Model Context Protocol servers
  * **Cross-Platform Support** - Windows, macOS, and Linux compatibility


### Installation​
**System Requirements**
  * **RAM** : 4GB minimum (8GB recommended)
  * **Storage** : 1GB free space
  * **OS** : Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)


**Prerequisites**
  * Claude Code CLI installed
  * Rust (1.70.0+) and Bun (latest)
  * Git


**Platform-Specific Setup:**
**Linux (Ubuntu/Debian):**
```
sudo apt updatesudo apt install -y libwebkit2gtk-4.1-dev libgtk-3-dev \ libayatana-appindicator3-dev librsvg2-dev patchelf \ build-essential curl wget file libssl-dev libxdo-dev \ libsoup-3.0-dev libjavascriptcoregtk-4.1-dev
```

**macOS:**
```
xcode-select --install
```

**Quick Setup**
```
# Clone and buildgit clone https://github.com/getAsterisk/claudia.gitcd claudiabun install# Run the applicationbun run tauri dev
```

### Usage​
**Launch Application**
```
# Start development server (full desktop app)bun run tauri dev# Run frontend only (web browser)bun run dev# Or build production versionbun run tauri build
```

**Creating Custom Agents**
  1. Launch Claudia: `bun run tauri dev`
  2. Navigate to "CC Agents" → "Create New Agent"
  3. Configure: Name, System Prompt, Model, Permissions
  4. Execute specialized tasks with your custom agent


For complete documentation, advanced features, and troubleshooting, see the official repository.
While I personally don't use Claudia, I can appreciate how the DX can appeal to different individuals' preferences. It is often name dropped on the Claude subreddit. The perfect developer experience remains an ongoing discovery, and innovation should continue to flourish.
##### Image Tip
![Claudia GUI interface showing Claude Code session management with visual project browser and analytics dashboard](https://www.claudelog.com/assets/images/036_cl-147dc60d4883ea8fc72436a3dfa126e9.png)
Claudia provides a GUI interface for Claude Code, offering a more comfortable developer experience for those who prefer visual tools over terminal-based workflows. The graphical approach makes session management, agent configuration, and usage analytics more accessible.
![Japan discovery](https://www.claudelog.com/img/discovery/026_japan.png)
_Claudia is developed by the getAsterisk team and is open-source under AGPL-3.0 license. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


