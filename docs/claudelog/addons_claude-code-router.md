Skip to main content
On this page
**Use Claude Code without an Anthropic account through intelligent AI provider routing**
**Author** : @musistudio | GitHub Repo | 7108 Stars|520 Forks|MIT License|Updated Jul 23, 2025
### Overview​
Claude Code Router is a proxy tool that enables Claude Code functionality without requiring an Anthropic account. It intercepts Claude Code requests and routes them to alternative AI providers like OpenRouter, DeepSeek, Ollama, and Gemini, giving you access to Claude Code's interface while using any supported AI model.
### Features​
  * **No Anthropic Account Required** - Use Claude Code interface with alternative AI providers
  * **8+ Supported Providers** - OpenRouter, DeepSeek, Ollama, Gemini, VolcEngine, SiliconFlow, ModelScope, DashScope
  * **Dynamic Model Switching** - Change models mid-session with `/model provider,model_name` commands
  * **Context-Based Routing** - Automatic routing for default, background, reasoning, and long-context tasks
  * **Custom Transformers** - Configure request/response transformations for provider compatibility
  * **GitHub Actions Integration** - CI/CD workflow support with automated model routing


### Installation​
**Prerequisites**
  * Node.js runtime environment
  * Claude Code: `npm install -g @anthropic-ai/claude-code`


**Install Router**
```
# Install the router globallynpm install -g @musistudio/claude-code-router
```

**Configuration Setup** Create `~/.claude-code-router/config.json` with your preferred AI providers:
```
{"Providers":[{"name":"openrouter","api_base_url":"https://openrouter.ai/api/v1/chat/completions","api_key":"sk-xxx","models":["anthropic/claude-3.5-sonnet","google/gemini-2.5-pro-preview"]},{"name":"deepseek","api_base_url":"https://api.deepseek.com/chat/completions","api_key":"sk-xxx","models":["deepseek-chat","deepseek-reasoner"]}],"Router":{"default":"deepseek,deepseek-chat","background":"deepseek,deepseek-chat","think":"deepseek,deepseek-reasoner","longContext":"openrouter,google/gemini-2.5-pro-preview"}}
```

### Usage​
**Start Claude Code with Router**
```
# Use this command instead of regular Claude Codeccr code
```

**Dynamic Model Switching** During your session, switch models with:
```
# Switch to different provider and model/model deepseek,deepseek-chat/model openrouter,anthropic/claude-3.5-sonnet/model ollama,qwen2.5-coder:latest
```

**Context-Based Routing** The router automatically selects models based on task context:
  * **Default** : General development tasks
  * **Background** : Simple, cost-effective operations
  * **Think** : Complex reasoning and analysis
  * **Long Context** : Tasks requiring extensive context windows


For detailed configuration options and routing rules, read the official documentation.
##### No Anthropic Account Needed
Access Claude Code's interface using alternative AI providers without requiring an Anthropic subscription.
![Custom image](https://www.claudelog.com/img/discovery/004.png)
_Claude Code Router is an independent community project. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage


