Skip to main content
On this page
**Multi-AI orchestration platform that enables Claude Code to collaborate seamlessly with Gemini Pro, OpenAI O3, Grok, and other leading AI models for enhanced development workflows.**
**Author** : BeehiveInnovations | GitHub Repo | 5091 Stars|461 Forks|Other|Updated Jul 23, 2025
### Overview​
Zen MCP Server creates a unified orchestration layer that enables Claude Code to collaborate with multiple AI models simultaneously. By intelligently routing tasks to the most suitable AI model, it dramatically enhances development workflows through specialized expertise and cross-model validation. The platform maintains context continuity across different models while providing specialized developer workflows for debugging, code review, and analysis.
### Features​
  * **Multi-Model Orchestration** - Seamlessly integrate Claude, Gemini 2.5 Pro, OpenAI O3, Grok, OpenRouter, and Ollama
  * **Intelligent Model Selection** - Automatic routing to optimal models based on task requirements
  * **Context Preservation** - Maintain conversation context across different AI models and sessions
  * **Specialized Dev Workflows** - Built-in tools for code review, debugging, pre-commit validation, and analysis
  * **Cross-Model Validation** - Compare outputs and approaches from different AI models for enhanced reliability
  * **Expert Mode Routing** - Route complex problems to specialized models (O3 for logic, Gemini for architecture)


### Installation​
**Prerequisites**
  * Python 3.10+ (3.12 recommended) with UV package manager
  * API keys for desired AI services (at least one required: OpenAI, Gemini, OpenRouter, etc.)
  * Claude Code or compatible MCP client
  * For Windows: WSL2 required


**Recommended: UVX Quick Install**
```
# One-line installation - no manual setup requiredexec $(which uvx || echo uvx) --from git+https://github.com/BeehiveInnovations/zen-mcp-server.git zen-mcp-server
```

**Claude Code Configuration** Add to your Claude Code configuration:
```
{"mcpServers":{"zen":{"command":"sh","args":["-c","exec $(which uvx || echo uvx) --from git+https://github.com/BeehiveInnovations/zen-mcp-server.git zen-mcp-server"],"env":{"PATH":"/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:~/.local/bin","OPENAI_API_KEY":"your_api_key_here","GEMINI_API_KEY":"your_gemini_key_here"}}}}
```

**API Key Configuration** Create a `.env` file in your project directory or set environment variables:
```
# Option 1: Environment variablesexport OPENAI_API_KEY="your-openai-key"export GEMINI_API_KEY="your-gemini-key"export ANTHROPIC_API_KEY="your-claude-key"# Option 2: .env file (recommended)echo "OPENAI_API_KEY=your-openai-key" > .envecho "GEMINI_API_KEY=your-gemini-key" >> .env
```

**Alternative: Traditional Installation**
```
# Only if uvx method doesn't workgit clone https://github.com/BeehiveInnovations/zen-mcp-server.gitcd zen-mcp-server./run-server.sh # or ./run-server.ps1 on Windows
```

### Usage​
**Multi-Model Development Workflows**
```
# Example AI orchestration commands:# "Use Gemini for architecture review and O3 for logic validation"# "Compare debugging approaches from Claude and GPT-4"# "Route this complex algorithm to the best mathematical reasoning model"# "Run pre-commit validation using multiple model perspectives"
```

The platform intelligently manages model selection and context flow, enabling developers to leverage the unique strengths of different AI models within a single conversation. Zen MCP maintains conversation continuity while providing access to specialized capabilities from each model.
**Specialized Developer Tools**
  * **Code Review** : Multi-model code review with diverse perspectives
  * **Debug Analysis** : Route debugging tasks to models with specific strengths
  * **Pre-commit Validation** : Comprehensive validation using optimal models
  * **Architecture Planning** : Leverage Gemini's architectural reasoning capabilities


##### Community Insight
Zen MCP Server gained massive attention with a Reddit post receiving 800+ upvotes. Users report multi-model orchestration provides "different perspectives that catch issues single models miss."
![Custom image](https://www.claudelog.com/img/discovery/024_excite.png)
_Zen MCP Server is developed by BeehiveInnovations and is open-source. For technical support, multi-model configuration, and community discussions, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


