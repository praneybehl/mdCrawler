Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
tip
You are probably looking for the Chat Model Concept Guide page for more information.
LangChain has implementations for older language models that take a string as input and return a string as output. These models are typically named without the "Chat" prefix (e.g., `Ollama`, `Anthropic`, `OpenAI`, etc.), and may include the "LLM" suffix (e.g., `OllamaLLM`, `AnthropicLLM`, `OpenAILLM`, etc.). These models implement the BaseLLM interface.
Users should be using almost exclusively the newer Chat Models as most model providers have adopted a chat like interface for interacting with language models.
#### Was this page helpful?
