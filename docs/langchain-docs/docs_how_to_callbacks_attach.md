Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Callbacks
  * Custom callback handlers
  * Chaining runnables
  * Attach runtime arguments to a Runnable


If you are composing a chain of runnables and want to reuse callbacks across multiple executions, you can attach callbacks with the `.with_config()` method. This saves you the need to pass callbacks in each time you invoke the chain.
important
`with_config()` binds a configuration which will be interpreted as **runtime** configuration. So these callbacks will propagate to all child components.
Here's an example:
```
from typing import Any, Dict, Listfrom langchain_anthropic import ChatAnthropicfrom langchain_core.callbacks import BaseCallbackHandlerfrom langchain_core.messages import BaseMessagefrom langchain_core.outputs import LLMResultfrom langchain_core.prompts import ChatPromptTemplateclassLoggingHandler(BaseCallbackHandler):defon_chat_model_start(    self, serialized: Dict[str, Any], messages: List[List[BaseMessage]],**kwargs)->None:print("Chat model started")defon_llm_end(self, response: LLMResult,**kwargs)->None:print(f"Chat model ended, response: {response}")defon_chain_start(    self, serialized: Dict[str, Any], inputs: Dict[str, Any],**kwargs)->None:print(f"Chain {serialized.get('name')} started")defon_chain_end(self, outputs: Dict[str, Any],**kwargs)->None:print(f"Chain ended, outputs: {outputs}")callbacks =[LoggingHandler()]llm = ChatAnthropic(model="claude-3-sonnet-20240229")prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")chain = prompt | llmchain_with_callbacks = chain.with_config(callbacks=callbacks)chain_with_callbacks.invoke({"number":"2"})
```

**API Reference:**ChatAnthropic | BaseCallbackHandler | BaseMessage | LLMResult | ChatPromptTemplate
```
Chain RunnableSequence startedChain ChatPromptTemplate startedChain ended, outputs: messages=[HumanMessage(content='What is 1 + 2?')]Chat model startedChat model ended, response: generations=[[ChatGeneration(text='1 + 2 = 3', message=AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01NTYMsH9YxkoWsiPYs4Lemn', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-d6bcfd72-9c94-466d-bac0-f39e456ad6e3-0'))]] llm_output={'id': 'msg_01NTYMsH9YxkoWsiPYs4Lemn', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}} run=NoneChain ended, outputs: content='1 + 2 = 3' response_metadata={'id': 'msg_01NTYMsH9YxkoWsiPYs4Lemn', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}} id='run-d6bcfd72-9c94-466d-bac0-f39e456ad6e3-0'
```

```
AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01NTYMsH9YxkoWsiPYs4Lemn', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-d6bcfd72-9c94-466d-bac0-f39e456ad6e3-0')
```

The bound callbacks will run for all nested module runs.
## Next steps​
You've now learned how to attach callbacks to a chain.
Next, check out the other how-to guides in this section, such as how to pass callbacks in at runtime.
#### Was this page helpful?
  * Next steps


