Skip to main content
On this page
**Revolutionary AI-powered 3D modeling that connects Blender to Claude AI for natural language scene creation and object manipulation.**
**Author** : ahujasid | GitHub Repo | 12592 Stars|1166 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Blender MCP creates a bidirectional bridge between Blender and Claude AI through the Model Context Protocol, enabling prompt-assisted 3D modeling and scene creation. This integration allows users to create, modify, and manipulate 3D objects using natural language instructions, democratizing 3D design for users of all skill levels.
### Features​
  * **Natural Language 3D Modeling** - Create and modify 3D objects using conversational prompts
  * **Two-Way Communication** - Socket-based server enabling real-time interaction with Blender
  * **Scene Management** - Comprehensive control over lighting, cameras, and scene properties
  * **Asset Integration** - Direct access to Poly Haven HDRIs, textures, and 3D models
  * **Python Code Execution** - Run arbitrary Python scripts in Blender through AI prompts
  * **Material Control** - Apply and modify materials, colors, and textures with AI assistance


### Installation​
**Prerequisites**
  * Blender 3.0 or newer (3.6+ recommended for full functionality)
  * Python 3.10 or newer
  * uv package manager


**Setup Commands**
```
# Install uv package manager (macOS)curl -LsSf https://astral.sh/uv/install.sh | sh# Install uv package manager (Windows)powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"# Install uv package manager (Linux)curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Blender Configuration**
```
# 1. Download addon.py from the repository# 2. Open Blender → Edit → Preferences → Add-ons# 3. Click "Install..." and select addon.py# 4. Enable "MCP Blender Bridge" addon
```

**Claude Desktop Configuration**
```
{"mcpServers":{"blender":{"command":"uvx","args":["blender-mcp"]}}}
```

### Usage​
**Scene Creation Examples**
```
# Natural language commands through Claude:# "Create a beach scene with palm trees and rocks"# "Add a sunset HDRI and adjust the lighting"# "Generate a low-poly character model"# "Apply ocean materials to the water plane"
```

The integration supports complex 3D workflows through conversational interaction. Users can describe scenes, modify object properties, download assets from integrated libraries, and execute advanced modeling operations without deep Blender knowledge.
**Advanced Capabilities**
  * **Asset Download** : Automatic integration with Poly Haven and Hyper3D libraries
  * **Scene Analysis** : AI can inspect and describe current Blender scenes
  * **Code Generation** : Python scripts generated and executed for complex operations
  * **Reference-Based Creation** : Generate 3D scenes from reference images


##### Community Insight
Blender MCP has been called "a game-changer for 3D artists" with users reporting "amateur users who barely know Blender can use natural language to describe models." The integration represents "text-to-3D workflow playing out in real time" as similar servers emerge for Unity and Unreal Engine.
![Custom image](https://www.claudelog.com/img/discovery/021_happy.png)
_Blender MCP is developed by ahujasid and sponsored by Warp. For technical support, contributions, and community discussions, please refer to the official GitHub repository and Discord community._
  * Overview
  * Features
  * Installation
  * Usage


