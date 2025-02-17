Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chaining runnables
  * Prompt templates
  * Chat Messages
  * LangGraph persistence


note
This guide previously covered the RunnableWithMessageHistory abstraction. You can access this version of the guide in the v0.2 docs.
As of the v0.3 release of LangChain, we recommend that LangChain users take advantage of LangGraph persistence to incorporate `memory` into new LangChain applications.
If your code is already relying on `RunnableWithMessageHistory` or `BaseChatMessageHistory`, you do **not** need to make any changes. We do not plan on deprecating this functionality in the near future as it works for simple chat applications and any code that uses `RunnableWithMessageHistory` will continue to work as expected.
Please see How to migrate to LangGraph Memory for more details.
Passing conversation state into and out a chain is vital when building a chatbot. LangGraph implements a built-in persistence layer, allowing chain states to be automatically persisted in memory, or external backends such as SQLite, Postgres or Redis. Details can be found in the LangGraph persistence documentation.
In this guide we demonstrate how to add persistence to arbitrary LangChain runnables by wrapping them in a minimal LangGraph application. This lets us persist the message history and other elements of the chain's state, simplifying the development of multi-turn applications. It also supports multiple threads, enabling a single application to interact separately with multiple users.
## Setup​
Let's initialize a chat model:
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

## Example: message inputs​
Adding memory to a chat model provides a simple example. Chat models accept a list of messages as input and output a message. LangGraph includes a built-in `MessagesState` that we can use for this purpose.
Below, we:
  1. Define the graph state to be a list of messages;
  2. Add a single node to the graph that calls a chat model;
  3. Compile the graph with an in-memory checkpointer to store messages between runs.


info
The output of a LangGraph application is its state. This can be any Python type, but in this context it will typically be a `TypedDict` that matches the schema of your runnable.
```
from langchain_core.messages import HumanMessagefrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraph# Define a new graphworkflow = StateGraph(state_schema=MessagesState)# Define the function that calls the modeldefcall_model(state: MessagesState):  response = llm.invoke(state["messages"])# Update message history with response:return{"messages": response}# Define the (single) node in the graphworkflow.add_edge(START,"model")workflow.add_node("model", call_model)# Add memorymemory = MemorySaver()app = workflow.compile(checkpointer=memory)
```

**API Reference:**HumanMessage | MemorySaver | StateGraph
When we run the application, we pass in a configuration `dict` that specifies a `thread_id`. This ID is used to distinguish conversational threads (e.g., between different users).
```
config ={"configurable":{"thread_id":"abc123"}}
```

We can then invoke the application:
```
query ="Hi! I'm Bob."input_messages =[HumanMessage(query)]output = app.invoke({"messages": input_messages}, config)output["messages"][-1].pretty_print()# output contains all messages in state
```

```
==================================[1m Ai Message [0m==================================It's nice to meet you, Bob! I'm Claude, an AI assistant created by Anthropic. How can I help you today?
```

```
query ="What's my name?"input_messages =[HumanMessage(query)]output = app.invoke({"messages": input_messages}, config)output["messages"][-1].pretty_print()
```

```
==================================[1m Ai Message [0m==================================Your name is Bob, as you introduced yourself at the beginning of our conversation.
```

Note that states are separated for different threads. If we issue the same query to a thread with a new `thread_id`, the model indicates that it does not know the answer:
```
query ="What's my name?"config ={"configurable":{"thread_id":"abc234"}}input_messages =[HumanMessage(query)]output = app.invoke({"messages": input_messages}, config)output["messages"][-1].pretty_print()
```

```
==================================[1m Ai Message [0m==================================I'm afraid I don't actually know your name. As an AI assistant, I don't have personal information about you unless you provide it to me directly.
```

## Example: dictionary inputs​
LangChain runnables often accept multiple inputs via separate keys in a single `dict` argument. A common example is a prompt template with multiple parameters.
Whereas before our runnable was a chat model, here we chain together a prompt template and chat model.
```
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderprompt = ChatPromptTemplate.from_messages([("system","Answer in {language}."),    MessagesPlaceholder(variable_name="messages"),])runnable = prompt | llm
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder
For this scenario, we define the graph state to include these parameters (in addition to the message history). We then define a single-node graph in the same way as before.
Note that in the below state:
  * Updates to the `messages` list will append messages;
  * Updates to the `language` string will overwrite the string.


```
from typing import Sequencefrom langchain_core.messages import BaseMessagefrom langgraph.graph.message import add_messagesfrom typing_extensions import Annotated, TypedDictclassState(TypedDict):  messages: Annotated[Sequence[BaseMessage], add_messages]  language:strworkflow = StateGraph(state_schema=State)defcall_model(state: State):  response = runnable.invoke(state)# Update message history with response:return{"messages":[response]}workflow.add_edge(START,"model")workflow.add_node("model", call_model)memory = MemorySaver()app = workflow.compile(checkpointer=memory)
```

**API Reference:**BaseMessage | add_messages
```
config ={"configurable":{"thread_id":"abc345"}}input_dict ={"messages":[HumanMessage("Hi, I'm Bob.")],"language":"Spanish",}output = app.invoke(input_dict, config)output["messages"][-1].pretty_print()
```

```
==================================[1m Ai Message [0m==================================¡Hola, Bob! Es un placer conocerte.
```

## Managing message history​
The message history (and other elements of the application state) can be accessed via `.get_state`:
```
state = app.get_state(config).valuesprint(f'Language: {state["language"]}')for message in state["messages"]:  message.pretty_print()
```

```
Language: Spanish================================[1m Human Message [0m=================================Hi, I'm Bob.==================================[1m Ai Message [0m==================================¡Hola, Bob! Es un placer conocerte.
```

We can also update the state via `.update_state`. For example, we can manually append a new message:
```
from langchain_core.messages import HumanMessage_ = app.update_state(config,{"messages":[HumanMessage("Test")]})
```

**API Reference:**HumanMessage
```
state = app.get_state(config).valuesprint(f'Language: {state["language"]}')for message in state["messages"]:  message.pretty_print()
```

```
Language: Spanish================================[1m Human Message [0m=================================Hi, I'm Bob.==================================[1m Ai Message [0m==================================¡Hola, Bob! Es un placer conocerte.================================[1m Human Message [0m=================================Test
```

For details on managing state, including deleting messages, see the LangGraph documentation:
  * How to delete messages
  * How to view and update past graph state


#### Was this page helpful?
  * Setup
  * Example: message inputs
  * Example: dictionary inputs
  * Managing message history


