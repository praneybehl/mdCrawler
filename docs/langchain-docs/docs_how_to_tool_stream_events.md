Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Tools
  * Custom tools
  * Using stream events
  * Accessing RunnableConfig within a custom tool


If you have tools that call chat models, retrievers, or other runnables, you may want to access internal events from those runnables or configure them with additional properties. This guide shows you how to manually pass parameters properly so that you can do this using the `astream_events()` method.
Compatibility
LangChain cannot automatically propagate configuration, including callbacks necessary for `astream_events()`, to child runnables if you are running `async` code in `python&lt;=3.10`. This is a common reason why you may fail to see events being emitted from custom runnables or tools.
If you are running python<=3.10, you will need to manually propagate the `RunnableConfig` object to the child runnable in async environments. For an example of how to manually propagate the config, see the implementation of the `bar` RunnableLambda below.
If you are running python>=3.11, the `RunnableConfig` will automatically propagate to child runnables in async environment. However, it is still a good idea to propagate the `RunnableConfig` manually if your code may run in older Python versions.
This guide also requires `langchain-core>=0.2.16`.
Say you have a custom tool that calls a chain that condenses its input by prompting a chat model to return only 10 words, then reversing the output. First, define it in a naive way:
Select chat model:
Groq▾
* Groq
* OpenAI
* Anthropic
* Azure
* Google Vertex
* AWS
* Cohere
* NVIDIA
* Fireworks AI
* Mistral AI
* Together AI
* IBM watsonx
* Databricks
```
pip install -qU "langchain[groq]"
```

```
import getpassimport osifnot os.environ.get("GROQ_API_KEY"): os.environ["GROQ_API_KEY"]= getpass.getpass("Enter API key for Groq: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("llama3-8b-8192", model_provider="groq")
```

```
from langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.tools import tool@toolasyncdefspecial_summarization_tool(long_text:str)->str:"""A tool that summarizes input text using advanced techniques."""  prompt = ChatPromptTemplate.from_template("You are an expert writer. Summarize the following text in 10 words or less:\n\n{long_text}")defreverse(x:str):return x[::-1]  chain = prompt | model | StrOutputParser()| reverse  summary =await chain.ainvoke({"long_text": long_text})return summary
```

**API Reference:**StrOutputParser | ChatPromptTemplate | tool
Invoking the tool directly works just fine:
```
LONG_TEXT ="""NARRATOR:(Black screen with text; The sound of buzzing bees can be heard)According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.BARRY BENSON:(Barry is picking out a shirt)Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.JANET BENSON:Barry! Breakfast is ready!BARRY:Coming! Hang on a second."""await special_summarization_tool.ainvoke({"long_text": LONG_TEXT})
```

```
'.yad noitaudarg rof tiftuo sesoohc yrraB ;scisyhp seifed eeB'
```

But if you wanted to access the raw output from the chat model rather than the full tool, you might try to use the `astream_events()` method and look for an `on_chat_model_end` event. Here's what happens:
```
stream = special_summarization_tool.astream_events({"long_text": LONG_TEXT}, version="v2")asyncfor event in stream:if event["event"]=="on_chat_model_end":# Never triggers in python<=3.10!print(event)
```

You'll notice (unless you're running through this guide in `python>=3.11`) that there are no chat model events emitted from the child run!
This is because the example above does not pass the tool's config object into the internal chain. To fix this, redefine your tool to take a special parameter typed as `RunnableConfig` (see this guide for more details). You'll also need to pass that parameter through into the internal chain when executing it:
```
from langchain_core.runnables import RunnableConfig@toolasyncdefspecial_summarization_tool_with_config(  long_text:str, config: RunnableConfig)->str:"""A tool that summarizes input text using advanced techniques."""  prompt = ChatPromptTemplate.from_template("You are an expert writer. Summarize the following text in 10 words or less:\n\n{long_text}")defreverse(x:str):return x[::-1]  chain = prompt | model | StrOutputParser()| reverse# Pass the "config" object as an argument to any executed runnables  summary =await chain.ainvoke({"long_text": long_text}, config=config)return summary
```

**API Reference:**RunnableConfig
And now try the same `astream_events()` call as before with your new tool:
```
stream = special_summarization_tool_with_config.astream_events({"long_text": LONG_TEXT}, version="v2")asyncfor event in stream:if event["event"]=="on_chat_model_end":print(event)
```

```
{'event': 'on_chat_model_end', 'data': {'output': AIMessage(content='Bee defies physics; Barry chooses outfit for graduation day.', response_metadata={'stop_reason': 'end_turn', 'stop_sequence': None}, id='run-d23abc80-0dce-4f74-9d7b-fb98ca4f2a9e', usage_metadata={'input_tokens': 182, 'output_tokens': 16, 'total_tokens': 198}), 'input': {'messages': [[HumanMessage(content="You are an expert writer. Summarize the following text in 10 words or less:\n\n\nNARRATOR:\n(Black screen with text; The sound of buzzing bees can be heard)\nAccording to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.\nBARRY BENSON:\n(Barry is picking out a shirt)\nYellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.\nJANET BENSON:\nBarry! Breakfast is ready!\nBARRY:\nComing! Hang on a second.\n")]]}}, 'run_id': 'd23abc80-0dce-4f74-9d7b-fb98ca4f2a9e', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['f25c41fe-8972-4893-bc40-cecf3922c1fa']}
```

Awesome! This time there's an event emitted.
For streaming, `astream_events()` automatically calls internal runnables in a chain with streaming enabled if possible, so if you wanted to a stream of tokens as they are generated from the chat model, you could simply filter to look for `on_chat_model_stream` events with no other changes:
```
stream = special_summarization_tool_with_config.astream_events({"long_text": LONG_TEXT}, version="v2")asyncfor event in stream:if event["event"]=="on_chat_model_stream":print(event)
```

```
{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42', usage_metadata={'input_tokens': 182, 'output_tokens': 0, 'total_tokens': 182})}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='Bee', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' def', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='ies physics', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=';', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' Barry', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' cho', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='oses outfit', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' for', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' graduation', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content=' day', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='.', id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42')}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}{'event': 'on_chat_model_stream', 'data': {'chunk': AIMessageChunk(content='', response_metadata={'stop_reason': 'end_turn', 'stop_sequence': None}, id='run-f24ab147-0b82-4e63-810a-b12bd8d1fb42', usage_metadata={'input_tokens': 0, 'output_tokens': 16, 'total_tokens': 16})}, 'run_id': 'f24ab147-0b82-4e63-810a-b12bd8d1fb42', 'name': 'ChatAnthropic', 'tags': ['seq:step:2'], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-5-sonnet-20240620', 'ls_model_type': 'chat', 'ls_temperature': 0.0, 'ls_max_tokens': 1024}, 'parent_ids': ['385f3612-417c-4a70-aae0-cce3a5ba6fb6']}
```

## Next steps​
You've now seen how to stream events from within a tool. Next, check out the following guides for more on using tools:
  * Pass runtime values to tools
  * Pass tool results back to a model
  * Dispatch custom callback events


You can also check out some more specific uses of tool calling:
  * Building tool-using chains and agents
  * Getting structured outputs from models


#### Was this page helpful?
  * Next steps


