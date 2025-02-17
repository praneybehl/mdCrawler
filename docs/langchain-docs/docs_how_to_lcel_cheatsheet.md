Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This is a quick reference for all the most important LCEL primitives. For more advanced usage see the LCEL how-to guides and the full API reference.
### Invoke a runnable​
#### Runnable.invoke() / Runnable.ainvoke()​
```
from langchain_core.runnables import RunnableLambdarunnable = RunnableLambda(lambda x:str(x))runnable.invoke(5)# Async variant:# await runnable.ainvoke(5)
```

**API Reference:**RunnableLambda
```
'5'
```

### Batch a runnable​
#### Runnable.batch() / Runnable.abatch()​
```
from langchain_core.runnables import RunnableLambdarunnable = RunnableLambda(lambda x:str(x))runnable.batch([7,8,9])# Async variant:# await runnable.abatch([7, 8, 9])
```

**API Reference:**RunnableLambda
```
['7', '8', '9']
```

### Stream a runnable​
#### Runnable.stream() / Runnable.astream()​
```
from langchain_core.runnables import RunnableLambdadeffunc(x):for y in x:yieldstr(y)runnable = RunnableLambda(func)for chunk in runnable.stream(range(5)):print(chunk)# Async variant:# async for chunk in await runnable.astream(range(5)):#   print(chunk)
```

**API Reference:**RunnableLambda
```
01234
```

### Compose runnables​
#### Pipe operator `|`​
```
from langchain_core.runnables import RunnableLambdarunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)chain = runnable1 | runnable2chain.invoke(2)
```

**API Reference:**RunnableLambda
```
[{'foo': 2}, {'foo': 2}]
```

### Invoke runnables in parallel​
#### RunnableParallel​
```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)chain = RunnableParallel(first=runnable1, second=runnable2)chain.invoke(2)
```

**API Reference:**RunnableLambda | RunnableParallel
```
{'first': {'foo': 2}, 'second': [2, 2]}
```

### Turn any function into a runnable​
#### RunnableLambda​
```
from langchain_core.runnables import RunnableLambdadeffunc(x):return x +5runnable = RunnableLambda(func)runnable.invoke(2)
```

**API Reference:**RunnableLambda
```
7
```

### Merge input and output dicts​
#### RunnablePassthrough.assign​
```
from langchain_core.runnables import RunnableLambda, RunnablePassthroughrunnable1 = RunnableLambda(lambda x: x["foo"]+7)chain = RunnablePassthrough.assign(bar=runnable1)chain.invoke({"foo":10})
```

**API Reference:**RunnableLambda | RunnablePassthrough
```
{'foo': 10, 'bar': 17}
```

### Include input dict in output dict​
#### RunnablePassthrough​
```
from langchain_core.runnables import(  RunnableLambda,  RunnableParallel,  RunnablePassthrough,)runnable1 = RunnableLambda(lambda x: x["foo"]+7)chain = RunnableParallel(bar=runnable1, baz=RunnablePassthrough())chain.invoke({"foo":10})
```

**API Reference:**RunnableLambda | RunnableParallel | RunnablePassthrough
```
{'bar': 17, 'baz': {'foo': 10}}
```

### Add default invocation args​
#### Runnable.bind​
```
from typing import Optionalfrom langchain_core.runnables import RunnableLambdadeffunc(main_arg:dict, other_arg: Optional[str]=None)->dict:if other_arg:return{**main_arg,**{"foo": other_arg}}return main_argrunnable1 = RunnableLambda(func)bound_runnable1 = runnable1.bind(other_arg="bye")bound_runnable1.invoke({"bar":"hello"})
```

**API Reference:**RunnableLambda
```
{'bar': 'hello', 'foo': 'bye'}
```

### Add fallbacks​
#### Runnable.with_fallbacks​
```
from langchain_core.runnables import RunnableLambdarunnable1 = RunnableLambda(lambda x: x +"foo")runnable2 = RunnableLambda(lambda x:str(x)+"foo")chain = runnable1.with_fallbacks([runnable2])chain.invoke(5)
```

**API Reference:**RunnableLambda
```
'5foo'
```

### Add retries​
#### Runnable.with_retry​
```
from langchain_core.runnables import RunnableLambdacounter =-1deffunc(x):global counter  counter +=1print(f"attempt with {counter=}")return x / counterchain = RunnableLambda(func).with_retry(stop_after_attempt=2)chain.invoke(2)
```

**API Reference:**RunnableLambda
```
attempt with counter=0attempt with counter=1
```

```
2.0
```

### Configure runnable execution​
#### RunnableConfig​
```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)runnable3 = RunnableLambda(lambda x:str(x))chain = RunnableParallel(first=runnable1, second=runnable2, third=runnable3)chain.invoke(7, config={"max_concurrency":2})
```

**API Reference:**RunnableLambda | RunnableParallel
```
{'first': {'foo': 7}, 'second': [7, 7], 'third': '7'}
```

### Add default config to runnable​
#### Runnable.with_config​
```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)runnable3 = RunnableLambda(lambda x:str(x))chain = RunnableParallel(first=runnable1, second=runnable2, third=runnable3)configured_chain = chain.with_config(max_concurrency=2)chain.invoke(7)
```

**API Reference:**RunnableLambda | RunnableParallel
```
{'first': {'foo': 7}, 'second': [7, 7], 'third': '7'}
```

### Make runnable attributes configurable​
#### Runnable.with_configurable_fields​
```
from typing import Any, Optionalfrom langchain_core.runnables import(  ConfigurableField,  RunnableConfig,  RunnableSerializable,)classFooRunnable(RunnableSerializable[dict,dict]):  output_key:strdefinvoke(    self,input: Any, config: Optional[RunnableConfig]=None,**kwargs: Any)->list:return self._call_with_config(self.subtract_seven,input, config,**kwargs)defsubtract_seven(self,input:dict)->dict:return{self.output_key:input["foo"]-7}runnable1 = FooRunnable(output_key="bar")configurable_runnable1 = runnable1.configurable_fields(  output_key=ConfigurableField(id="output_key"))configurable_runnable1.invoke({"foo":10}, config={"configurable":{"output_key":"not bar"}})
```

**API Reference:**ConfigurableField | RunnableConfig | RunnableSerializable
```
{'not bar': 3}
```

```
configurable_runnable1.invoke({"foo":10})
```

```
{'bar': 3}
```

### Make chain components configurable​
#### Runnable.with_configurable_alternatives​
```
from typing import Any, Optionalfrom langchain_core.runnables import RunnableConfig, RunnableLambda, RunnableParallelclassListRunnable(RunnableSerializable[Any,list]):definvoke(    self,input: Any, config: Optional[RunnableConfig]=None,**kwargs: Any)->list:return self._call_with_config(self.listify,input, config,**kwargs)deflistify(self,input: Any)->list:return[input]classStrRunnable(RunnableSerializable[Any,str]):definvoke(    self,input: Any, config: Optional[RunnableConfig]=None,**kwargs: Any)->list:return self._call_with_config(self.strify,input, config,**kwargs)defstrify(self,input: Any)->str:returnstr(input)runnable1 = RunnableLambda(lambda x:{"foo": x})configurable_runnable = ListRunnable().configurable_alternatives(  ConfigurableField(id="second_step"), default_key="list", string=StrRunnable())chain = runnable1 | configurable_runnablechain.invoke(7, config={"configurable":{"second_step":"string"}})
```

**API Reference:**RunnableConfig | RunnableLambda | RunnableParallel
```
"{'foo': 7}"
```

```
chain.invoke(7)
```

```
[{'foo': 7}]
```

### Build a chain dynamically based on input​
```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)chain = RunnableLambda(lambda x: runnable1 if x >6else runnable2)chain.invoke(7)
```

**API Reference:**RunnableLambda | RunnableParallel
```
{'foo': 7}
```

```
chain.invoke(5)
```

```
[5, 5]
```

### Generate a stream of events​
#### Runnable.astream_events​
```
# | echo: falseimport nest_asyncionest_asyncio.apply()
```

```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x}, name="first")asyncdeffunc(x):for _ inrange(5):yield xrunnable2 = RunnableLambda(func, name="second")chain = runnable1 | runnable2asyncfor event in chain.astream_events("bar", version="v2"):print(f"event={event['event']} | name={event['name']} | data={event['data']}")
```

**API Reference:**RunnableLambda | RunnableParallel
```
event=on_chain_start | name=RunnableSequence | data={'input': 'bar'}event=on_chain_start | name=first | data={}event=on_chain_stream | name=first | data={'chunk': {'foo': 'bar'}}event=on_chain_start | name=second | data={}event=on_chain_end | name=first | data={'output': {'foo': 'bar'}, 'input': 'bar'}event=on_chain_stream | name=second | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=RunnableSequence | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=second | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=RunnableSequence | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=second | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=RunnableSequence | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=second | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=RunnableSequence | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=second | data={'chunk': {'foo': 'bar'}}event=on_chain_stream | name=RunnableSequence | data={'chunk': {'foo': 'bar'}}event=on_chain_end | name=second | data={'output': {'foo': 'bar'}, 'input': {'foo': 'bar'}}event=on_chain_end | name=RunnableSequence | data={'output': {'foo': 'bar'}}
```

### Yield batched outputs as they complete​
#### Runnable.batch_as_completed / Runnable.abatch_as_completed​
```
import timefrom langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x: time.sleep(x)orprint(f"slept {x}"))for idx, result in runnable1.batch_as_completed([5,1]):print(idx, result)# Async variant:# async for idx, result in runnable1.abatch_as_completed([5, 1]):#   print(idx, result)
```

**API Reference:**RunnableLambda | RunnableParallel
```
slept 11 Noneslept 50 None
```

### Return subset of output dict​
#### Runnable.pick​
```
from langchain_core.runnables import RunnableLambda, RunnablePassthroughrunnable1 = RunnableLambda(lambda x: x["baz"]+5)chain = RunnablePassthrough.assign(foo=runnable1).pick(["foo","bar"])chain.invoke({"bar":"hi","baz":2})
```

**API Reference:**RunnableLambda | RunnablePassthrough
```
{'foo': 7, 'bar': 'hi'}
```

### Declaratively make a batched version of a runnable​
#### Runnable.map​
```
from langchain_core.runnables import RunnableLambdarunnable1 = RunnableLambda(lambda x:list(range(x)))runnable2 = RunnableLambda(lambda x: x +5)chain = runnable1 | runnable2.map()chain.invoke(3)
```

**API Reference:**RunnableLambda
```
[5, 6, 7]
```

### Get a graph representation of a runnable​
#### Runnable.get_graph​
```
from langchain_core.runnables import RunnableLambda, RunnableParallelrunnable1 = RunnableLambda(lambda x:{"foo": x})runnable2 = RunnableLambda(lambda x:[x]*2)runnable3 = RunnableLambda(lambda x:str(x))chain = runnable1 | RunnableParallel(second=runnable2, third=runnable3)chain.get_graph().print_ascii()
```

**API Reference:**RunnableLambda | RunnableParallel
```
               +-------------+                              | LambdaInput |                              +-------------+                                 *                                     *                                     *                             +------------------------------+                     | Lambda(lambda x: {'foo': x}) |                     +------------------------------+                             *                                     *                                     *                              +-----------------------------+                      | Parallel<second,third>Input |                      +-----------------------------+                       ****         ***                       ****             ****                    **                 **          +---------------------------+        +--------------------------+ | Lambda(lambda x: [x] * 2) |        | Lambda(lambda x: str(x)) | +---------------------------+        +--------------------------+             ****         ***                           ****     ****                              **   **                          +------------------------------+                     | Parallel<second,third>Output |                     +------------------------------+
```

### Get all prompts in a chain​
#### Runnable.get_prompts​
```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnableLambdaprompt1 = ChatPromptTemplate.from_messages([("system","good ai"),("human","{input}")])prompt2 = ChatPromptTemplate.from_messages([("system","really good ai"),("human","{input}"),("ai","{ai_output}"),("human","{input2}"),])fake_llm = RunnableLambda(lambda prompt:"i am good ai")chain = prompt1.assign(ai_output=fake_llm)| prompt2 | fake_llmfor i, prompt inenumerate(chain.get_prompts()):print(f"**prompt {i=}**\n")print(prompt.pretty_repr())print("\n"*3)
```

**API Reference:**ChatPromptTemplate | RunnableLambda
```
**prompt i=0**================================ System Message ================================good ai================================ Human Message ================================={input}**prompt i=1**================================ System Message ================================really good ai================================ Human Message ================================={input}================================== AI Message =================================={ai_output}================================ Human Message ================================={input2}
```

### Add lifecycle listeners​
#### Runnable.with_listeners​
```
import timefrom langchain_core.runnables import RunnableLambdafrom langchain_core.tracers.schemas import Rundefon_start(run_obj: Run):print("start_time:", run_obj.start_time)defon_end(run_obj: Run):print("end_time:", run_obj.end_time)runnable1 = RunnableLambda(lambda x: time.sleep(x))chain = runnable1.with_listeners(on_start=on_start, on_end=on_end)chain.invoke(2)
```

**API Reference:**RunnableLambda | Run
```
start_time: 2024-05-17 23:04:00.951065+00:00end_time: 2024-05-17 23:04:02.958765+00:00
```

#### Was this page helpful?
  * Invoke a runnable
  * Batch a runnable
  * Stream a runnable
  * Compose runnables
  * Invoke runnables in parallel
  * Turn any function into a runnable
  * Merge input and output dicts
  * Include input dict in output dict
  * Add default invocation args
  * Add fallbacks
  * Add retries
  * Configure runnable execution
  * Add default config to runnable
  * Make runnable attributes configurable
  * Make chain components configurable
  * Build a chain dynamically based on input
  * Generate a stream of events
  * Yield batched outputs as they complete
  * Return subset of output dict
  * Declaratively make a batched version of a runnable
  * Get a graph representation of a runnable
  * Get all prompts in a chain
  * Add lifecycle listeners


