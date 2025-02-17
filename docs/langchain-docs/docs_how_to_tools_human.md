Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
There are certain tools that we don't trust a model to execute on its own. One thing we can do in such situations is require human approval before the tool is invoked.
info
This how-to guide shows a simple way to add human-in-the-loop for code running in a jupyter notebook or in a terminal.
To build a production application, you will need to do more work to keep track of application state appropriately.
We recommend using `langgraph` for powering such a capability. For more details, please see this guide.
## Setup​
We'll need to install the following packages:
```
%pip install --upgrade --quiet langchain
```

And set these environment variables:
```
import getpassimport os# If you'd like to use LangSmith, uncomment the below:# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

## Chain​
Let's create a few simple (dummy) tools and a tool-calling chain:
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
from typing import Dict, Listfrom langchain_core.messages import AIMessagefrom langchain_core.runnables import Runnable, RunnablePassthroughfrom langchain_core.tools import tool@tooldefcount_emails(last_n_days:int)->int:"""Dummy function to count number of e-mails. Returns 2 * last_n_days."""return last_n_days *2@tooldefsend_email(message:str, recipient:str)->str:"""Dummy function for sending an e-mail."""returnf"Successfully sent email to {recipient}."tools =[count_emails, send_email]llm_with_tools = llm.bind_tools(tools)defcall_tools(msg: AIMessage)-> List[Dict]:"""Simple sequential tool calling helper."""  tool_map ={tool.name: tool for tool in tools}  tool_calls = msg.tool_calls.copy()for tool_call in tool_calls:    tool_call["output"]= tool_map[tool_call["name"]].invoke(tool_call["args"])return tool_callschain = llm_with_tools | call_toolschain.invoke("how many emails did i get in the last 5 days?")
```

**API Reference:**AIMessage | Runnable | RunnablePassthrough | tool
```
[{'name': 'count_emails', 'args': {'last_n_days': 5}, 'id': 'toolu_01QYZdJ4yPiqsdeENWHqioFW', 'output': 10}]
```

## Adding human approval​
Let's add a step in the chain that will ask a person to approve or reject the tall call request.
On rejection, the step will raise an exception which will stop execution of the rest of the chain.
```
import jsonclassNotApproved(Exception):"""Custom exception."""defhuman_approval(msg: AIMessage)-> AIMessage:"""Responsible for passing through its input or raising an exception.  Args:    msg: output from the chat model  Returns:    msg: original output from the msg  """  tool_strs ="\n\n".join(    json.dumps(tool_call, indent=2)for tool_call in msg.tool_calls)  input_msg =(f"Do you approve of the following tool invocations\n\n{tool_strs}\n\n""Anything except 'Y'/'Yes' (case-insensitive) will be treated as a no.\n >>>")  resp =input(input_msg)if resp.lower()notin("yes","y"):raise NotApproved(f"Tool invocations not approved:\n\n{tool_strs}")return msg
```

```
chain = llm_with_tools | human_approval | call_toolschain.invoke("how many emails did i get in the last 5 days?")
```

```
Do you approve of the following tool invocations{ "name": "count_emails", "args": {  "last_n_days": 5 }, "id": "toolu_01WbD8XeMoQaRFtsZezfsHor"}Anything except 'Y'/'Yes' (case-insensitive) will be treated as a no. >>> yes
```

```
[{'name': 'count_emails', 'args': {'last_n_days': 5}, 'id': 'toolu_01WbD8XeMoQaRFtsZezfsHor', 'output': 10}]
```

```
try:  chain.invoke("Send sally@gmail.com an email saying 'What's up homie'")except NotApproved as e:print()print(e)
```

```
Do you approve of the following tool invocations{ "name": "send_email", "args": {  "recipient": "sally@gmail.com",  "message": "What's up homie" }, "id": "toolu_014XccHFzBiVcc9GV1harV9U"}Anything except 'Y'/'Yes' (case-insensitive) will be treated as a no. >>> no``````outputTool invocations not approved:{ "name": "send_email", "args": {  "recipient": "sally@gmail.com",  "message": "What's up homie" }, "id": "toolu_014XccHFzBiVcc9GV1harV9U"}
```

#### Was this page helpful?
  * Setup
  * Chain
  * Adding human approval


