Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * Tool calling
  * Tools
  * Output parsers


Tool calling allows a chat model to respond to a given prompt by "calling a tool".
Remember, while the name "tool calling" implies that the model is directly performing some action, this is actually not the case! The model only generates the arguments to a tool, and actually running the tool (or not) is up to the user.
Tool calling is a general technique that generates structured output from a model, and you can use it even when you don't intend to invoke any tools. An example use-case of that is extraction from unstructured text.
![Diagram of calling a tool](https://python.langchain.com/assets/images/tool_call-8d4a8b18e90cacd03f62e94071eceace.png)
If you want to see how to use the model-generated tool call to actually run a tool check out this guide.
Supported models
Tool calling is not universal, but is supported by many popular LLM providers. You can find a list of all models that support tool calling here.
LangChain implements standard interfaces for defining tools, passing them to LLMs, and representing tool calls. This guide will cover how to bind tools to an LLM, then invoke the LLM to generate these arguments.
## Defining tool schemas​
For a model to be able to call tools, we need to pass in tool schemas that describe what the tool does and what it's arguments are. Chat models that support tool calling features implement a `.bind_tools()` method for passing tool schemas to the model. Tool schemas can be passed in as Python functions (with typehints and docstrings), Pydantic models, TypedDict classes, or LangChain Tool objects. Subsequent invocations of the model will pass in these tool schemas along with the prompt.
### Python functions​
Our tool schemas can be Python functions:
```
# The function name, type hints, and docstring are all part of the tool# schema that's passed to the model. Defining good, descriptive schemas# is an extension of prompt engineering and is an important part of# getting models to perform well.defadd(a:int, b:int)->int:"""Add two integers.  Args:    a: First integer    b: Second integer  """return a + bdefmultiply(a:int, b:int)->int:"""Multiply two integers.  Args:    a: First integer    b: Second integer  """return a * b
```

### LangChain Tool​
LangChain also implements a `@tool` decorator that allows for further control of the tool schema, such as tool names and argument descriptions. See the how-to guide here for details.
### Pydantic class​
You can equivalently define the schemas without the accompanying functions using Pydantic.
Note that all fields are `required` unless provided a default value.
```
from pydantic import BaseModel, Fieldclassadd(BaseModel):"""Add two integers."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")classmultiply(BaseModel):"""Multiply two integers."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")
```

### TypedDict class​
Requires `langchain-core>=0.2.25`
Or using TypedDicts and annotations:
```
from typing_extensions import Annotated, TypedDictclassadd(TypedDict):"""Add two integers."""# Annotations must have the type and can optionally include a default value and description (in that order).  a: Annotated[int,...,"First integer"]  b: Annotated[int,...,"Second integer"]classmultiply(TypedDict):"""Multiply two integers."""  a: Annotated[int,...,"First integer"]  b: Annotated[int,...,"Second integer"]tools =[add, multiply]
```

To actually bind those schemas to a chat model, we'll use the `.bind_tools()` method. This handles converting the `add` and `multiply` schemas to the proper format for the model. The tool schema will then be passed it in each time the model is invoked.
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
import getpassimport osifnot os.environ.get("GROQ_API_KEY"): os.environ["GROQ_API_KEY"]= getpass.getpass("Enter API key for Groq: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("llama3-8b-8192", model_provider="groq")
```

```
llm_with_tools = llm.bind_tools(tools)query ="What is 3 * 12?"llm_with_tools.invoke(query)
```

```
AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_iXj4DiW1p7WLjTAQMRO0jxMs', 'function': {'arguments': '{"a":3,"b":12}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 80, 'total_tokens': 97}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_483d39d857', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-0b620986-3f62-4df7-9ba3-4595089f9ad4-0', tool_calls=[{'name': 'multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_iXj4DiW1p7WLjTAQMRO0jxMs', 'type': 'tool_call'}], usage_metadata={'input_tokens': 80, 'output_tokens': 17, 'total_tokens': 97})
```

As we can see our LLM generated arguments to a tool! You can look at the docs for bind_tools() to learn about all the ways to customize how your LLM selects tools, as well as this guide on how to force the LLM to call a tool rather than letting it decide.
## Tool calls​
If tool calls are included in a LLM response, they are attached to the corresponding message or message chunk as a list of tool call objects in the `.tool_calls` attribute.
Note that chat models can call multiple tools at once.
A `ToolCall` is a typed dict that includes a tool name, dict of argument values, and (optionally) an identifier. Messages with no tool calls default to an empty list for this attribute.
```
query ="What is 3 * 12? Also, what is 11 + 49?"llm_with_tools.invoke(query).tool_calls
```

```
[{'name': 'multiply', 'args': {'a': 3, 'b': 12}, 'id': 'call_1fyhJAbJHuKQe6n0PacubGsL', 'type': 'tool_call'}, {'name': 'add', 'args': {'a': 11, 'b': 49}, 'id': 'call_fc2jVkKzwuPWyU7kS9qn1hyG', 'type': 'tool_call'}]
```

The `.tool_calls` attribute should contain valid tool calls. Note that on occasion, model providers may output malformed tool calls (e.g., arguments that are not valid JSON). When parsing fails in these cases, instances of InvalidToolCall are populated in the `.invalid_tool_calls` attribute. An `InvalidToolCall` can have a name, string arguments, identifier, and error message.
## Parsing​
If desired, output parsers can further process the output. For example, we can convert existing values populated on the `.tool_calls` to Pydantic objects using the PydanticToolsParser:
```
from langchain_core.output_parsers import PydanticToolsParserfrom pydantic import BaseModel, Fieldclassadd(BaseModel):"""Add two integers."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")classmultiply(BaseModel):"""Multiply two integers."""  a:int= Field(..., description="First integer")  b:int= Field(..., description="Second integer")chain = llm_with_tools | PydanticToolsParser(tools=[add, multiply])chain.invoke(query)
```

**API Reference:**PydanticToolsParser
```
[multiply(a=3, b=12), add(a=11, b=49)]
```

## Next steps​
Now you've learned how to bind tool schemas to a chat model and have the model call the tool.
Next, check out this guide on actually using the tool by invoking the function and passing the results back to the model:
  * Pass tool results back to model


You can also check out some more specific uses of tool calling:
  * Getting structured outputs from models
  * Few shot prompting with tools
  * Stream tool calls
  * Pass runtime values to tools


#### Was this page helpful?
  * Defining tool schemas
    * Python functions
    * LangChain Tool
    * Pydantic class
    * TypedDict class
  * Tool calls
  * Parsing
  * Next steps


