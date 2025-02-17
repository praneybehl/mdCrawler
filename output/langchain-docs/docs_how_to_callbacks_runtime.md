Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Callbacks
  * Custom callback handlers


In many cases, it is advantageous to pass in handlers instead when running the object. When we pass through `CallbackHandlers` using the `callbacks` keyword arg when executing a run, those callbacks will be issued by all nested objects involved in the execution. For example, when a handler is passed through to an Agent, it will be used for all callbacks related to the agent and all the objects involved in the agent's execution, in this case, the Tools and LLM.
This prevents us from having to manually attach the handlers to each individual nested object. Here's an example:
```
from typing import Any, Dict, Listfrom langchain_anthropic import ChatAnthropicfrom langchain_core.callbacks import BaseCallbackHandlerfrom langchain_core.messages import BaseMessagefrom langchain_core.outputs import LLMResultfrom langchain_core.prompts import ChatPromptTemplateclassLoggingHandler(BaseCallbackHandler):defon_chat_model_start(    self, serialized: Dict[str, Any], messages: List[List[BaseMessage]],**kwargs)->None:print("Chat model started")defon_llm_end(self, response: LLMResult,**kwargs)->None:print(f"Chat model ended, response: {response}")defon_chain_start(    self, serialized: Dict[str, Any], inputs: Dict[str, Any],**kwargs)->None:print(f"Chain {serialized.get('name')} started")defon_chain_end(self, outputs: Dict[str, Any],**kwargs)->None:print(f"Chain ended, outputs: {outputs}")callbacks =[LoggingHandler()]llm = ChatAnthropic(model="claude-3-sonnet-20240229")prompt = ChatPromptTemplate.from_template("What is 1 + {number}?")chain = prompt | llmchain.invoke({"number":"2"}, config={"callbacks": callbacks})
```

**API Reference:**ChatAnthropic | BaseCallbackHandler | BaseMessage | LLMResult | ChatPromptTemplate
```
Chain RunnableSequence startedChain ChatPromptTemplate startedChain ended, outputs: messages=[HumanMessage(content='What is 1 + 2?')]Chat model startedChat model ended, response: generations=[[ChatGeneration(text='1 + 2 = 3', message=AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01D8Tt5FdtBk5gLTfBPm2tac', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-bb0dddd8-85f3-4e6b-8553-eaa79f859ef8-0'))]] llm_output={'id': 'msg_01D8Tt5FdtBk5gLTfBPm2tac', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}} run=NoneChain ended, outputs: content='1 + 2 = 3' response_metadata={'id': 'msg_01D8Tt5FdtBk5gLTfBPm2tac', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}} id='run-bb0dddd8-85f3-4e6b-8553-eaa79f859ef8-0'
```

```
AIMessage(content='1 + 2 = 3', response_metadata={'id': 'msg_01D8Tt5FdtBk5gLTfBPm2tac', 'model': 'claude-3-sonnet-20240229', 'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 16, 'output_tokens': 13}}, id='run-bb0dddd8-85f3-4e6b-8553-eaa79f859ef8-0')
```

If there are already existing callbacks associated with a module, these will run in addition to any passed in at runtime.
## Next steps​
You've now learned how to pass callbacks at runtime.
Next, check out the other how-to guides in this section, such as how to pass callbacks into a module constructor.
#### Was this page helpful?
  * Next steps


