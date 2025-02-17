Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Callbacks
  * Custom callback handlers


If you are planning to use the async APIs, it is recommended to use and extend `AsyncCallbackHandler` to avoid blocking the event.
warning
If you use a sync `CallbackHandler` while using an async method to run your LLM / Chain / Tool / Agent, it will still work. However, under the hood, it will be called with `run_in_executor` which can cause issues if your `CallbackHandler` is not thread-safe.
danger
If you're on `python<=3.10`, you need to remember to propagate `config` or `callbacks` when invoking other `runnable` from within a `RunnableLambda`, `RunnableGenerator` or `@tool`. If you do not do this, the callbacks will not be propagated to the child runnables being invoked.
```
import asynciofrom typing import Any, Dict, Listfrom langchain_anthropic import ChatAnthropicfrom langchain_core.callbacks import AsyncCallbackHandler, BaseCallbackHandlerfrom langchain_core.messages import HumanMessagefrom langchain_core.outputs import LLMResultclassMyCustomSyncHandler(BaseCallbackHandler):defon_llm_new_token(self, token:str,**kwargs)->None:print(f"Sync handler being called in a `thread_pool_executor`: token: {token}")classMyCustomAsyncHandler(AsyncCallbackHandler):"""Async callback handler that can be used to handle callbacks from langchain."""asyncdefon_llm_start(    self, serialized: Dict[str, Any], prompts: List[str],**kwargs: Any)->None:"""Run when chain starts running."""print("zzzz....")await asyncio.sleep(0.3)    class_name = serialized["name"]print("Hi! I just woke up. Your llm is starting")asyncdefon_llm_end(self, response: LLMResult,**kwargs: Any)->None:"""Run when chain ends running."""print("zzzz....")await asyncio.sleep(0.3)print("Hi! I just woke up. Your llm is ending")# To enable streaming, we pass in `streaming=True` to the ChatModel constructor# Additionally, we pass in a list with our custom handlerchat = ChatAnthropic(  model="claude-3-sonnet-20240229",  max_tokens=25,  streaming=True,  callbacks=[MyCustomSyncHandler(), MyCustomAsyncHandler()],)await chat.agenerate([[HumanMessage(content="Tell me a joke")]])
```

**API Reference:**ChatAnthropic | AsyncCallbackHandler | BaseCallbackHandler | HumanMessage | LLMResult
```
zzzz....Hi! I just woke up. Your llm is startingSync handler being called in a `thread_pool_executor`: token: HereSync handler being called in a `thread_pool_executor`: token: 'sSync handler being called in a `thread_pool_executor`: token: aSync handler being called in a `thread_pool_executor`: token: littleSync handler being called in a `thread_pool_executor`: token: jokeSync handler being called in a `thread_pool_executor`: token: forSync handler being called in a `thread_pool_executor`: token: youSync handler being called in a `thread_pool_executor`: token: :Sync handler being called in a `thread_pool_executor`: token: WhySync handler being called in a `thread_pool_executor`: token: canSync handler being called in a `thread_pool_executor`: token: 'tSync handler being called in a `thread_pool_executor`: token: aSync handler being called in a `thread_pool_executor`: token: bicycleSync handler being called in a `thread_pool_executor`: token: stanSync handler being called in a `thread_pool_executor`: token: d upSync handler being called in a `thread_pool_executor`: token: bySync handler being called in a `thread_pool_executor`: token: itselfSync handler being called in a `thread_pool_executor`: token: ?Sync handler being called in a `thread_pool_executor`: token: BecauseSync handler being called in a `thread_pool_executor`: token: itSync handler being called in a `thread_pool_executor`: token: 'sSync handler being called in a `thread_pool_executor`: token: twoSync handler being called in a `thread_pool_executor`: token: -Sync handler being called in a `thread_pool_executor`: token: tirezzzz....Hi! I just woke up. Your llm is ending
```

```
LLMResult(generations=[[ChatGeneration(text="Here's a little joke for you:\n\nWhy can't a bicycle stand up by itself? Because it's two-tire", message=AIMessage(content="Here's a little joke for you:\n\nWhy can't a bicycle stand up by itself? Because it's two-tire", id='run-8afc89e8-02c0-4522-8480-d96977240bd4-0'))]], llm_output={}, run=[RunInfo(run_id=UUID('8afc89e8-02c0-4522-8480-d96977240bd4'))])
```

## Next steps​
You've now learned how to create your own custom callback handlers.
Next, check out the other how-to guides in this section, such as how to attach callbacks to a runnable.
#### Was this page helpful?
  * Next steps


