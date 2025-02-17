Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
In this guide, we will go over the basic ways to create Chains and Agents that call Tools. Tools can be just about anything — APIs, functions, databases, etc. Tools allow us to extend the capabilities of a model beyond just outputting text/messages. The key to using models with tools is correctly prompting a model and parsing its response so that it chooses the right tools and provides the right inputs for them.
## Setup​
We'll need to install the following packages for this guide:
```
%pip install --upgrade --quiet langchain
```

If you'd like to trace your runs in LangSmith uncomment and set the following environment variables:
```
import getpassimport os# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

## Create a tool​
First, we need to create a tool to call. For this example, we will create a custom tool from a function. For more information on creating custom tools, please see this guide.
```
from langchain_core.tools import tool@tooldefmultiply(first_int:int, second_int:int)->int:"""Multiply two integers together."""return first_int * second_int
```

**API Reference:**tool
```
print(multiply.name)print(multiply.description)print(multiply.args)
```

```
multiplymultiply(first_int: int, second_int: int) -> int - Multiply two integers together.{'first_int': {'title': 'First Int', 'type': 'integer'}, 'second_int': {'title': 'Second Int', 'type': 'integer'}}
```

```
multiply.invoke({"first_int":4,"second_int":5})
```

```
20
```

## Chains​
If we know that we only need to use a tool a fixed number of times, we can create a chain for doing so. Let's create a simple chain that just multiplies user-specified numbers.
![chain](https://python.langchain.com/assets/images/tool_chain-3571e7fbc481d648aff93a2630f812ab.svg)
### Tool/function calling​
One of the most reliable ways to use tools with LLMs is with tool calling APIs (also sometimes called function calling). This only works with models that explicitly support tool calling. You can see which models support tool calling here, and learn more about how to use tool calling in this guide.
First we'll define our model and tools. We'll start with just a single tool, `multiply`.
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

We'll use `bind_tools` to pass the definition of our tool in as part of each call to the model, so that the model can invoke the tool when appropriate:
```
llm_with_tools = llm.bind_tools([multiply])
```

When the model invokes the tool, this will show up in the `AIMessage.tool_calls` attribute of the output:
```
msg = llm_with_tools.invoke("whats 5 times forty two")msg.tool_calls
```

```
[{'name': 'multiply', 'args': {'first_int': 5, 'second_int': 42}, 'id': 'call_cCP9oA3tRz7HDrjFn1FdmDaG'}]
```

Check out the LangSmith trace here.
### Invoking the tool​
Great! We're able to generate tool invocations. But what if we want to actually call the tool? To do so we'll need to pass the generated tool args to our tool. As a simple example we'll just extract the arguments of the first tool_call:
```
from operator import itemgetterchain = llm_with_tools |(lambda x: x.tool_calls[0]["args"])| multiplychain.invoke("What's four times 23")
```

```
92
```

Check out the LangSmith trace here.
## Agents​
Chains are great when we know the specific sequence of tool usage needed for any user input. But for certain use cases, how many times we use tools depends on the input. In these cases, we want to let the model itself decide how many times to use tools and in what order. Agents let us do just this.
LangChain comes with a number of built-in agents that are optimized for different use cases. Read about all the agent types here.
We'll use the tool calling agent, which is generally the most reliable kind and the recommended one for most use cases.
![agent](https://python.langchain.com/assets/images/tool_agent-d25fafc271da3ee950ac1fba59cdf490.svg)
```
from langchain import hubfrom langchain.agents import AgentExecutor, create_tool_calling_agent
```

**API Reference:**hub | AgentExecutor | create_tool_calling_agent
```
# Get the prompt to use - can be replaced with any prompt that includes variables "agent_scratchpad" and "input"!prompt = hub.pull("hwchase17/openai-tools-agent")prompt.pretty_print()
```

```
================================[1m System Message [0m================================You are a helpful assistant=============================[1m Messages Placeholder [0m=============================[33;1m[1;3m{chat_history}[0m================================[1m Human Message [0m=================================[33;1m[1;3m{input}[0m=============================[1m Messages Placeholder [0m=============================[33;1m[1;3m{agent_scratchpad}[0m
```

Agents are also great because they make it easy to use multiple tools.
```
@tooldefadd(first_int:int, second_int:int)->int:"Add two integers."return first_int + second_int@tooldefexponentiate(base:int, exponent:int)->int:"Exponentiate the base to the exponent power."return base**exponenttools =[multiply, add, exponentiate]
```

```
# Construct the tool calling agentagent = create_tool_calling_agent(llm, tools, prompt)
```

```
# Create an agent executor by passing in the agent and toolsagent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

With an agent, we can ask questions that require arbitrarily-many uses of our tools:
```
agent_executor.invoke({"input":"Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result"})
```

```
[1m> Entering new AgentExecutor chain...[0m[32;1m[1;3mInvoking: `exponentiate` with `{'base': 3, 'exponent': 5}`[0m[38;5;200m[1;3m243[0m[32;1m[1;3mInvoking: `add` with `{'first_int': 12, 'second_int': 3}`[0m[33;1m[1;3m15[0m[32;1m[1;3mInvoking: `multiply` with `{'first_int': 243, 'second_int': 15}`[0m[36;1m[1;3m3645[0m[32;1m[1;3mInvoking: `exponentiate` with `{'base': 405, 'exponent': 2}`[0m[38;5;200m[1;3m13286025[0m[32;1m[1;3mThe result of taking 3 to the fifth power is 243. The sum of twelve and three is 15. Multiplying 243 by 15 gives 3645. Finally, squaring 3645 gives 13286025.[0m[1m> Finished chain.[0m
```

```
{'input': 'Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result', 'output': 'The result of taking 3 to the fifth power is 243. \n\nThe sum of twelve and three is 15. \n\nMultiplying 243 by 15 gives 3645. \n\nFinally, squaring 3645 gives 13286025.'}
```

Check out the LangSmith trace here.
#### Was this page helpful?
  * Setup
  * Create a tool
  * Chains
    * Tool/function calling
    * Invoking the tool
  * Agents


