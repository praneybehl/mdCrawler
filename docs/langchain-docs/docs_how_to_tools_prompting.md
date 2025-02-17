Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
caution
Some models have been fine-tuned for tool calling and provide a dedicated API for tool calling. Generally, such models are better at tool calling than non-fine-tuned models, and are recommended for use cases that require tool calling. Please see the how to use a chat model to call tools guide for more information.
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Tools
  * Function/tool calling
  * Chat models
  * LLMs


In this guide, we'll see how to add **ad-hoc** tool calling support to a chat model. This is an alternative method to invoke tools if you're using a model that does not natively support tool calling.
We'll do this by simply writing a prompt that will get the model to invoke the appropriate tools. Here's a diagram of the logic:
![chain](https://python.langchain.com/assets/images/tool_chain-3571e7fbc481d648aff93a2630f812ab.svg)
## Setup​
We'll need to install the following packages:
```
%pip install --upgrade --quiet langchain langchain-community
```

If you'd like to use LangSmith, uncomment the below:
```
import getpassimport os# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

You can select any of the given models for this how-to guide. Keep in mind that most of these models already support native tool calling, so using the prompting strategy shown here doesn't make sense for these models, and instead you should follow the how to use a chat model to call tools guide.
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

To illustrate the idea, we'll use `phi3` via Ollama, which does **NOT** have native support for tool calling. If you'd like to use `Ollama` as well follow these instructions.
```
from langchain_community.llms import Ollamamodel = Ollama(model="phi3")
```

**API Reference:**Ollama
## Create a tool​
First, let's create an `add` and `multiply` tools. For more information on creating custom tools, please see this guide.
```
from langchain_core.tools import tool@tooldefmultiply(x:float, y:float)->float:"""Multiply two numbers together."""return x * y@tooldefadd(x:int, y:int)->int:"Add two numbers."return x + ytools =[multiply, add]# Let's inspect the toolsfor t in tools:print("--")print(t.name)print(t.description)print(t.args)
```

**API Reference:**tool
```
--multiplyMultiply two numbers together.{'x': {'title': 'X', 'type': 'number'}, 'y': {'title': 'Y', 'type': 'number'}}--addAdd two numbers.{'x': {'title': 'X', 'type': 'integer'}, 'y': {'title': 'Y', 'type': 'integer'}}
```

```
multiply.invoke({"x":4,"y":5})
```

```
20.0
```

## Creating our prompt​
We'll want to write a prompt that specifies the tools the model has access to, the arguments to those tools, and the desired output format of the model. In this case we'll instruct it to output a JSON blob of the form `{"name": "...", "arguments": {...}}`.
```
from langchain_core.output_parsers import JsonOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.tools import render_text_descriptionrendered_tools = render_text_description(tools)print(rendered_tools)
```

**API Reference:**JsonOutputParser | ChatPromptTemplate | render_text_description
```
multiply(x: float, y: float) -> float - Multiply two numbers together.add(x: int, y: int) -> int - Add two numbers.
```

```
system_prompt =f"""\You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool:{rendered_tools}Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys.The `arguments` should be a dictionary, with keys corresponding to the argument names and the values corresponding to the requested values."""prompt = ChatPromptTemplate.from_messages([("system", system_prompt),("user","{input}")])
```

```
chain = prompt | modelmessage = chain.invoke({"input":"what's 3 plus 1132"})# Let's take a look at the output from the model# if the model is an LLM (not a chat model), the output will be a string.ifisinstance(message,str):print(message)else:# Otherwise it's a chat modelprint(message.content)
```

```
{  "name": "add",  "arguments": {    "x": 3,    "y": 1132  }}
```

## Adding an output parser​
We'll use the `JsonOutputParser` for parsing our models output to JSON.
```
from langchain_core.output_parsers import JsonOutputParserchain = prompt | model | JsonOutputParser()chain.invoke({"input":"what's thirteen times 4"})
```

**API Reference:**JsonOutputParser
```
{'name': 'multiply', 'arguments': {'x': 13.0, 'y': 4.0}}
```

important
🎉 Amazing! 🎉 We now instructed our model on how to **request** that a tool be invoked.
Now, let's create some logic to actually run the tool!
## Invoking the tool 🏃​
Now that the model can request that a tool be invoked, we need to write a function that can actually invoke the tool.
The function will select the appropriate tool by name, and pass to it the arguments chosen by the model.
```
from typing import Any, Dict, Optional, TypedDictfrom langchain_core.runnables import RunnableConfigclassToolCallRequest(TypedDict):"""A typed dict that shows the inputs into the invoke_tool function."""  name:str  arguments: Dict[str, Any]definvoke_tool(  tool_call_request: ToolCallRequest, config: Optional[RunnableConfig]=None):"""A function that we can use the perform a tool invocation.  Args:    tool_call_request: a dict that contains the keys name and arguments.      The name must match the name of a tool that exists.      The arguments are the arguments to that tool.    config: This is configuration information that LangChain uses that contains      things like callbacks, metadata, etc.See LCEL documentation about RunnableConfig.  Returns:    output from the requested tool  """  tool_name_to_tool ={tool.name: tool for tool in tools}  name = tool_call_request["name"]  requested_tool = tool_name_to_tool[name]return requested_tool.invoke(tool_call_request["arguments"], config=config)
```

**API Reference:**RunnableConfig
Let's test this out 🧪!
```
invoke_tool({"name":"multiply","arguments":{"x":3,"y":5}})
```

```
15.0
```

## Let's put it together​
Let's put it together into a chain that creates a calculator with add and multiplication capabilities.
```
chain = prompt | model | JsonOutputParser()| invoke_toolchain.invoke({"input":"what's thirteen times 4.14137281"})
```

```
53.83784653
```

## Returning tool inputs​
It can be helpful to return not only tool outputs but also tool inputs. We can easily do this with LCEL by `RunnablePassthrough.assign`-ing the tool output. This will take whatever the input is to the RunnablePassrthrough components (assumed to be a dictionary) and add a key to it while still passing through everything that's currently in the input:
```
from langchain_core.runnables import RunnablePassthroughchain =(  prompt | model | JsonOutputParser()| RunnablePassthrough.assign(output=invoke_tool))chain.invoke({"input":"what's thirteen times 4.14137281"})
```

**API Reference:**RunnablePassthrough
```
{'name': 'multiply', 'arguments': {'x': 13, 'y': 4.14137281}, 'output': 53.83784653}
```

## What's next?​
This how-to guide shows the "happy path" when the model correctly outputs all the required tool information.
In reality, if you're using more complex tools, you will start encountering errors from the model, especially for models that have not been fine tuned for tool calling and for less capable models.
You will need to be prepared to add strategies to improve the output from the model; e.g.,
  1. Provide few shot examples.
  2. Add error handling (e.g., catch the exception and feed it back to the LLM to ask it to correct its previous output).


#### Was this page helpful?
  * Setup
  * Create a tool
  * Creating our prompt
  * Adding an output parser
  * Invoking the tool 🏃
  * Let's put it together
  * Returning tool inputs
  * What's next?


