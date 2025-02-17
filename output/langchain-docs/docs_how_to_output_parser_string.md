Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * Messages
  * Output parsers
  * LangChain Expression Language (LCEL)


LangChain message objects support content in a variety of formats, including text, multimodal data, and a list of content block dicts.
The format of Chat model response content may depend on the provider. For example, the chat model for Anthropic will return string content for typical string input:
```
from langchain_anthropic import ChatAnthropicllm = ChatAnthropic(model="claude-3-5-haiku-latest")response = llm.invoke("Hello")response.content
```

**API Reference:**ChatAnthropic
```
'Hi there! How are you doing today? Is there anything I can help you with?'
```

But when tool calls are generated, the response content is structured into content blocks that convey the model's reasoning process:
```
from langchain_core.tools import tool@tooldefget_weather(location:str)->str:"""Get the weather from a location."""return"Sunny."llm_with_tools = llm.bind_tools([get_weather])response = llm_with_tools.invoke("What's the weather in San Francisco, CA?")response.content
```

**API Reference:**tool
```
[{'text': "I'll help you get the current weather for San Francisco, California. Let me check that for you right away.", 'type': 'text'}, {'id': 'toolu_015PwwcKxWYctKfY3pruHFyy', 'input': {'location': 'San Francisco, CA'}, 'name': 'get_weather', 'type': 'tool_use'}]
```

To automatically parse text from message objects irrespective of the format of the underlying content, we can use StrOutputParser. We can compose it with a chat model as follows:
```
from langchain_core.output_parsers import StrOutputParserchain = llm_with_tools | StrOutputParser()
```

**API Reference:**StrOutputParser
StrOutputParser simplifies the extraction of text from message objects:
```
response = chain.invoke("What's the weather in San Francisco, CA?")print(response)
```

```
I'll help you check the weather in San Francisco, CA right away.
```

This is particularly useful in streaming contexts:
```
for chunk in chain.stream("What's the weather in San Francisco, CA?"):print(chunk, end="|")
```

```
|I'll| help| you get| the current| weather for| San Francisco, California|. Let| me retrieve| that| information for you.||||||||||
```

See the API Reference for more information.
#### Was this page helpful?
