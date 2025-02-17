Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Callbacks
  * Custom callback handlers


Most LangChain modules allow you to pass `callbacks` directly into the constructor (i.e., initializer). In this case, the callbacks will only be called for that instance (and any nested runs).
warning
Constructor callbacks are scoped only to the object they are defined on. They are **not** inherited by children of the object. This can lead to confusing behavior, and it's generally better to pass callbacks as a run time argument.
Here's an example:
```
from typing import Any, Dict, Listfrom langchain_anthropic import ChatAnthropicfrom langchain_core.callbacks import BaseCallbackHandlerfrom langchain_core.messages import BaseMessagefrom langchain_core.outputs import LLMResultfrom langchain_core.prompts import ChatPromptTemplateclassLoggingHandler(BaseCallbackHandler):defon_chat_model_start(    self, serialized: Dict[str, Any], messages: List[List[BaseMessage]],**kwargs)->None:print("Chat model started")defon_llm_end(self, response: LLMResult,**kwargs)->None:print(f"Chat model ended, response: {response}")defon_chain_start(    self, serialized: Dict[str, Any], inputs: Dict[str, Any],**kwargs)->None:print(f"Chain {serialized.get('name')} started")defon_chain_end(self, outputs: Dict[str, Any],**kwargs)->None:print(f"Chain ended, outputs: {outputs}")callbacks =[LoggingHandler()]llm = ChatAnthropic(model="claude-3-sonnet-20240229", callbacks=callbacks)prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")chain = prompt | llmchain.invoke({"number":"2"})
```

**API Reference:**ChatAnthropic | BaseCallbackHandler | BaseMessage | LLMResult | ChatPromptTemplate
```
Chat model startedChat model ended, response: generations=[[ChatGeneration(text='1 + 2 = 3', message=AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01CdKsRmeS9WRb8BWnHDEHm7', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-2d7fdf2a-7405-4e17-97c0-67e6b2a65305-0'))]] llm_output={'id': 'msg_01CdKsRmeS9WRb8BWnHDEHm7', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}} run=None
```

```
AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01CdKsRmeS9WRb8BWnHDEHm7', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-2d7fdf2a-7405-4e17-97c0-67e6b2a65305-0')
```

You can see that we only see events from the chat model run - no chain events from the prompt or broader chain.
## Next steps​
You've now learned how to pass callbacks into a constructor.
Next, check out the other how-to guides in this section, such as how to pass callbacks at runtime.
#### Was this page helpful?
  * Next steps


