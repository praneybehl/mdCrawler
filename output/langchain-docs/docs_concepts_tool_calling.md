Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
  * Tools
  * Chat Models


## Overview​
Many AI applications interact directly with humans. In these cases, it is appropriate for models to respond in natural language. But what about cases where we want a model to also interact _directly_ with systems, such as databases or an API? These systems often have a particular input schema; for example, APIs frequently have a required payload structure. This need motivates the concept of _tool calling_. You can use tool calling to request model responses that match a particular schema.
info
You will sometimes hear the term `function calling`. We use this term interchangeably with `tool calling`.
![Conceptual overview of tool calling](https://python.langchain.com/assets/images/tool_calling_concept-552a73031228ff9144c7d59f26dedbbf.png)
## Key concepts​
**(1) Tool Creation:** Use the @tool decorator to create a tool. A tool is an association between a function and its schema. **(2) Tool Binding:** The tool needs to be connected to a model that supports tool calling. This gives the model awareness of the tool and the associated input schema required by the tool. **(3) Tool Calling:** When appropriate, the model can decide to call a tool and ensure its response conforms to the tool's input schema. **(4) Tool Execution:** The tool can be executed using the arguments provided by the model.
![Conceptual parts of tool calling](https://python.langchain.com/assets/images/tool_calling_components-bef9d2bcb9d3706c2fe58b57bf8ccb60.png)
## Recommended usage​
This pseudo-code illustrates the recommended workflow for using tool calling. Created tools are passed to `.bind_tools()` method as a list. This model can be called, as usual. If a tool call is made, model's response will contain the tool call arguments. The tool call arguments can be passed directly to the tool.
```
# Tool creationtools =[my_tool]# Tool bindingmodel_with_tools = model.bind_tools(tools)# Tool calling response = model_with_tools.invoke(user_input)
```

## Tool creation​
The recommended way to create a tool is using the `@tool` decorator.
```
from langchain_core.tools import tool@tooldefmultiply(a:int, b:int)->int:"""Multiply a and b."""return a * b
```

**API Reference:**tool
Further reading
  * See our conceptual guide on tools for more details.
  * See our model integrations that support tool calling.
  * See our how-to guide on tool calling.


## Tool binding​
Many model providers support tool calling.
tip
See our model integration page for a list of providers that support tool calling.
The central concept to understand is that LangChain provides a standardized interface for connecting tools to models. The `.bind_tools()` method can be used to specify which tools are available for a model to call.
```
model_with_tools = model.bind_tools(tools_list)
```

As a specific example, let's take a function `multiply` and bind it as a tool to a model that supports tool calling.
```
defmultiply(a:int, b:int)->int:"""Multiply a and b.  Args:    a: first int    b: second int  """return a * bllm_with_tools = tool_calling_model.bind_tools([multiply])
```

## Tool calling​
![Diagram of a tool call by a model](https://python.langchain.com/assets/images/tool_call_example-2348b869f9a5d0d2a45dfbe614c177a4.png)
A key principle of tool calling is that the model decides when to use a tool based on the input's relevance. The model doesn't always need to call a tool. For example, given an unrelated input, the model would not call the tool:
```
result = llm_with_tools.invoke("Hello world!")
```

The result would be an `AIMessage` containing the model's response in natural language (e.g., "Hello!"). However, if we pass an input _relevant to the tool_ , the model should choose to call it:
```
result = llm_with_tools.invoke("What is 2 multiplied by 3?")
```

As before, the output `result` will be an `AIMessage`. But, if the tool was called, `result` will have a `tool_calls` attribute. This attribute includes everything needed to execute the tool, including the tool name and input arguments:
```
result.tool_calls{'name': 'multiply', 'args': {'a': 2, 'b': 3}, 'id': 'xxx', 'type': 'tool_call'}
```

For more details on usage, see our how-to guides!
## Tool execution​
Tools implement the Runnable interface, which means that they can be invoked (e.g., `tool.invoke(args)`) directly.
LangGraph offers pre-built components (e.g., `ToolNode`) that will often invoke the tool in behalf of the user.
Further reading
  * See our how-to guide on tool calling.
  * See the LangGraph documentation on using ToolNode.


## Best practices​
When designing tools to be used by a model, it is important to keep in mind that:
  * Models that have explicit tool-calling APIs will be better at tool calling than non-fine-tuned models.
  * Models will perform better if the tools have well-chosen names and descriptions.
  * Simple, narrowly scoped tools are easier for models to use than complex tools.
  * Asking the model to select from a large list of tools poses challenges for the model.


#### Was this page helpful?
  * Overview
  * Key concepts
  * Recommended usage
  * Tool creation
  * Tool binding
  * Tool calling
  * Tool execution
  * Best practices


