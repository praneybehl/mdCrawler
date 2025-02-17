Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Expression Language (LCEL)
  * Chaining runnables


You can use arbitrary functions as Runnables. This is useful for formatting or when you need functionality not provided by other LangChain components, and custom functions used as Runnables are called `RunnableLambdas`.
Note that all inputs to these functions need to be a SINGLE argument. If you have a function that accepts multiple arguments, you should write a wrapper that accepts a single dict input and unpacks it into multiple arguments.
This guide will cover:
  * How to explicitly create a runnable from a custom function using the `RunnableLambda` constructor and the convenience `@chain` decorator
  * Coercion of custom functions into runnables when used in chains
  * How to accept and use run metadata in your custom function
  * How to stream with custom functions by having them return generators


## Using the constructor​
Below, we explicitly wrap our custom logic using the `RunnableLambda` constructor:
```
%pip install -qU langchain langchain_openaiimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

```
from operator import itemgetterfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnableLambdafrom langchain_openai import ChatOpenAIdeflength_function(text):returnlen(text)def_multiple_length_function(text1, text2):returnlen(text1)*len(text2)defmultiple_length_function(_dict):return _multiple_length_function(_dict["text1"], _dict["text2"])model = ChatOpenAI()prompt = ChatPromptTemplate.from_template("what is {a} + {b}")chain =({"a": itemgetter("foo")| RunnableLambda(length_function),"b":{"text1": itemgetter("foo"),"text2": itemgetter("bar")}| RunnableLambda(multiple_length_function),}| prompt| model)chain.invoke({"foo":"bar","bar":"gah"})
```

**API Reference:**ChatPromptTemplate | RunnableLambda | ChatOpenAI
```
AIMessage(content='3 + 9 equals 12.', response_metadata={'token_usage': {'completion_tokens': 8, 'prompt_tokens': 14, 'total_tokens': 22}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_c2295e73ad', 'finish_reason': 'stop', 'logprobs': None}, id='run-73728de3-e483-49e3-ad54-51bd9570e71a-0')
```

## The convenience `@chain` decorator​
You can also turn an arbitrary function into a chain by adding a `@chain` decorator. This is functionally equivalent to wrapping the function in a `RunnableLambda` constructor as shown above. Here's an example:
```
from langchain_core.output_parsers import StrOutputParserfrom langchain_core.runnables import chainprompt1 = ChatPromptTemplate.from_template("Tell me a joke about {topic}")prompt2 = ChatPromptTemplate.from_template("What is the subject of this joke: {joke}")@chaindefcustom_chain(text):  prompt_val1 = prompt1.invoke({"topic": text})  output1 = ChatOpenAI().invoke(prompt_val1)  parsed_output1 = StrOutputParser().invoke(output1)  chain2 = prompt2 | ChatOpenAI()| StrOutputParser()return chain2.invoke({"joke": parsed_output1})custom_chain.invoke("bears")
```

**API Reference:**StrOutputParser | chain
```
'The subject of the joke is the bear and his girlfriend.'
```

Above, the `@chain` decorator is used to convert `custom_chain` into a runnable, which we invoke with the `.invoke()` method.
If you are using a tracing with LangSmith, you should see a `custom_chain` trace in there, with the calls to OpenAI nested underneath.
## Automatic coercion in chains​
When using custom functions in chains with the pipe operator (`|`), you can omit the `RunnableLambda` or `@chain` constructor and rely on coercion. Here's a simple example with a function that takes the output from the model and returns the first five letters of it:
```
prompt = ChatPromptTemplate.from_template("tell me a story about {topic}")model = ChatOpenAI()chain_with_coerced_function = prompt | model |(lambda x: x.content[:5])chain_with_coerced_function.invoke({"topic":"bears"})
```

```
'Once '
```

Note that we didn't need to wrap the custom function `(lambda x: x.content[:5])` in a `RunnableLambda` constructor because the `model` on the left of the pipe operator is already a Runnable. The custom function is **coerced** into a runnable. See this section for more information.
## Passing run metadata​
Runnable lambdas can optionally accept a RunnableConfig parameter, which they can use to pass callbacks, tags, and other configuration information to nested runs.
```
import jsonfrom langchain_core.runnables import RunnableConfigdefparse_or_fix(text:str, config: RunnableConfig):  fixing_chain =(    ChatPromptTemplate.from_template("Fix the following text:\n\n\`\`\`text\n{input}\n\`\`\`\nError: {error}"" Don't narrate, just respond with the fixed data.")| model| StrOutputParser())for _ inrange(3):try:return json.loads(text)except Exception as e:      text = fixing_chain.invoke({"input": text,"error": e}, config)return"Failed to parse"from langchain_community.callbacks import get_openai_callbackwith get_openai_callback()as cb:  output = RunnableLambda(parse_or_fix).invoke("{foo: bar}",{"tags":["my-tag"],"callbacks":[cb]})print(output)print(cb)
```

**API Reference:**RunnableConfig | get_openai_callback
```
{'foo': 'bar'}Tokens Used: 62	Prompt Tokens: 56	Completion Tokens: 6Successful Requests: 1Total Cost (USD): $9.6e-05
```

```
from langchain_community.callbacks import get_openai_callbackwith get_openai_callback()as cb:  output = RunnableLambda(parse_or_fix).invoke("{foo: bar}",{"tags":["my-tag"],"callbacks":[cb]})print(output)print(cb)
```

**API Reference:**get_openai_callback
```
{'foo': 'bar'}Tokens Used: 62	Prompt Tokens: 56	Completion Tokens: 6Successful Requests: 1Total Cost (USD): $9.6e-05
```

## Streaming​
note
RunnableLambda is best suited for code that does not need to support streaming. If you need to support streaming (i.e., be able to operate on chunks of inputs and yield chunks of outputs), use RunnableGenerator instead as in the example below.
You can use generator functions (ie. functions that use the `yield` keyword, and behave like iterators) in a chain.
The signature of these generators should be `Iterator[Input] -> Iterator[Output]`. Or for async generators: `AsyncIterator[Input] -> AsyncIterator[Output]`.
These are useful for:
  * implementing a custom output parser
  * modifying the output of a previous step, while preserving streaming capabilities


Here's an example of a custom output parser for comma-separated lists. First, we create a chain that generates such a list as text:
```
from typing import Iterator, Listprompt = ChatPromptTemplate.from_template("Write a comma-separated list of 5 animals similar to: {animal}. Do not include numbers")str_chain = prompt | model | StrOutputParser()for chunk in str_chain.stream({"animal":"bear"}):print(chunk, end="", flush=True)
```

```
lion, tiger, wolf, gorilla, panda
```

Next, we define a custom function that will aggregate the currently streamed output and yield it when the model generates the next comma in the list:
```
# This is a custom parser that splits an iterator of llm tokens# into a list of strings separated by commasdefsplit_into_list(input: Iterator[str])-> Iterator[List[str]]:# hold partial input until we get a commabuffer=""for chunk ininput:# add current chunk to bufferbuffer+= chunk# while there are commas in the bufferwhile","inbuffer:# split buffer on comma      comma_index =buffer.index(",")# yield everything before the commayield[buffer[:comma_index].strip()]# save the rest for the next iterationbuffer=buffer[comma_index +1:]# yield the last chunkyield[buffer.strip()]list_chain = str_chain | split_into_listfor chunk in list_chain.stream({"animal":"bear"}):print(chunk, flush=True)
```

```
['lion']['tiger']['wolf']['gorilla']['raccoon']
```

Invoking it gives a full array of values:
```
list_chain.invoke({"animal":"bear"})
```

```
['lion', 'tiger', 'wolf', 'gorilla', 'raccoon']
```

## Async version​
If you are working in an `async` environment, here is an `async` version of the above example:
```
from typing import AsyncIteratorasyncdefasplit_into_list(input: AsyncIterator[str],)-> AsyncIterator[List[str]]:# async defbuffer=""asyncfor(    chunk)ininput:# `input` is a `async_generator` object, so use `async for`buffer+= chunkwhile","inbuffer:      comma_index =buffer.index(",")yield[buffer[:comma_index].strip()]buffer=buffer[comma_index +1:]yield[buffer.strip()]list_chain = str_chain | asplit_into_listasyncfor chunk in list_chain.astream({"animal":"bear"}):print(chunk, flush=True)
```

```
['lion']['tiger']['wolf']['gorilla']['panda']
```

```
await list_chain.ainvoke({"animal":"bear"})
```

```
['lion', 'tiger', 'wolf', 'gorilla', 'panda']
```

## Next steps​
Now you've learned a few different ways to use custom logic within your chains, and how to implement streaming.
To learn more, see the other how-to guides on runnables in this section.
#### Was this page helpful?
  * Using the constructor
  * The convenience `@chain` decorator
  * Automatic coercion in chains
  * Passing run metadata
  * Streaming
  * Async version
  * Next steps


