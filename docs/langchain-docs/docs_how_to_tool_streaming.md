Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
When tools are called in a streaming context, message chunks will be populated with tool call chunk objects in a list via the `.tool_call_chunks` attribute. A `ToolCallChunk` includes optional string fields for the tool `name`, `args`, and `id`, and includes an optional integer field `index` that can be used to join chunks together. Fields are optional because portions of a tool call may be streamed across different chunks (e.g., a chunk that includes a substring of the arguments may have null values for the tool name and id).
Because message chunks inherit from their parent message class, an AIMessageChunk with tool call chunks will also include `.tool_calls` and `.invalid_tool_calls` fields. These fields are parsed best-effort from the message's tool call chunks.
Note that not all providers currently support streaming for tool calls. Before we start let's define our tools and our model.
```
from langchain_core.tools import tool@tooldefadd(a:int, b:int)->int:"""Adds a and b."""return a + b@tooldefmultiply(a:int, b:int)->int:"""Multiplies a and b."""return a * btools =[add, multiply]
```

**API Reference:**tool
```
import osfrom getpass import getpassfrom langchain_openai import ChatOpenAIif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)llm_with_tools = llm.bind_tools(tools)
```

**API Reference:**ChatOpenAI
Now let's define our query and stream our output:
```
query ="What is 3 * 12? Also, what is 11 + 49?"asyncfor chunk in llm_with_tools.astream(query):print(chunk.tool_call_chunks)
```

```
[][{'name': 'Multiply', 'args': '', 'id': 'call_3aQwTP9CYlFxwOvQZPHDu6wL', 'index': 0}][{'name': None, 'args': '{"a"', 'id': None, 'index': 0}][{'name': None, 'args': ': 3, ', 'id': None, 'index': 0}][{'name': None, 'args': '"b": 1', 'id': None, 'index': 0}][{'name': None, 'args': '2}', 'id': None, 'index': 0}][{'name': 'Add', 'args': '', 'id': 'call_SQUoSsJz2p9Kx2x73GOgN1ja', 'index': 1}][{'name': None, 'args': '{"a"', 'id': None, 'index': 1}][{'name': None, 'args': ': 11,', 'id': None, 'index': 1}][{'name': None, 'args': ' "b": ', 'id': None, 'index': 1}][{'name': None, 'args': '49}', 'id': None, 'index': 1}][]
```

Note that adding message chunks will merge their corresponding tool call chunks. This is the principle by which LangChain's various tool output parsers support streaming.
For example, below we accumulate tool call chunks:
```
first =Trueasyncfor chunk in llm_with_tools.astream(query):if first:    gathered = chunk    first =Falseelse:    gathered = gathered + chunkprint(gathered.tool_call_chunks)
```

```
[][{'name': 'Multiply', 'args': '', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}][{'name': 'Multiply', 'args': '{"a"', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, ', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 1', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '{"a"', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '{"a": 11,', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": ', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}][{'name': 'Multiply', 'args': '{"a": 3, "b": 12}', 'id': 'call_AkL3dVeCjjiqvjv8ckLxL3gP', 'index': 0}, {'name': 'Add', 'args': '{"a": 11, "b": 49}', 'id': 'call_b4iMiB3chGNGqbt5SjqqD2Wh', 'index': 1}]
```

```
print(type(gathered.tool_call_chunks[0]["args"]))
```

```
<class 'str'>
```

And below we accumulate tool calls to demonstrate partial parsing:
```
first =Trueasyncfor chunk in llm_with_tools.astream(query):if first:    gathered = chunk    first =Falseelse:    gathered = gathered + chunkprint(gathered.tool_calls)
```

```
[][][{'name': 'Multiply', 'args': {}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}][{'name': 'Multiply', 'args': {'a': 3}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 1}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}, {'name': 'Add', 'args': {}, 'id': 'call_54Hx3DGjZitFlEjgMe1DYonh'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_54Hx3DGjZitFlEjgMe1DYonh'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}, {'name': 'Add', 'args': {'a': 11}, 'id': 'call_54Hx3DGjZitFlEjgMe1DYonh'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_54Hx3DGjZitFlEjgMe1DYonh'}][{'name': 'Multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_4p0D4tHVXSiae9Mu0e8jlI1m'}, {'name': 'Add', 'args': {'a': 11, 'b': 49}, 'id': 'call_54Hx3DGjZitFlEjgMe1DYonh'}]
```

```
print(type(gathered.tool_calls[0]["args"]))
```

```
<class 'dict'>
```

#### Was this page helpful?
