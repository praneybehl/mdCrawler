Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat History
  * RunnableWithMessageHistory
  * LangGraph
  * Memory


We recommend that new LangChain applications take advantage of the built-in LangGraph peristence to implement memory.
In some situations, users may need to keep using an existing persistence solution for chat message history.
Here, we will show how to use LangChain chat message histories (implementations of BaseChatMessageHistory) with LangGraph.
## Set up​
```
%%capture --no-stderr%pip install --upgrade --quiet langchain-anthropic langgraph
```

```
import osfrom getpass import getpassif"ANTHROPIC_API_KEY"notin os.environ:  os.environ["ANTHROPIC_API_KEY"]= getpass()
```

## ChatMessageHistory​
A message history needs to be parameterized by a conversation ID or maybe by the 2-tuple of (user ID, conversation ID).
Many of the LangChain chat message histories will have either a `session_id` or some `namespace` to allow keeping track of different conversations. Please refer to the specific implementations to check how it is parameterized.
The built-in `InMemoryChatMessageHistory` does not contains such a parameterization, so we'll create a dictionary to keep track of the message histories.
```
import uuidfrom langchain_core.chat_history import InMemoryChatMessageHistorychats_by_session_id ={}defget_chat_history(session_id:str)-> InMemoryChatMessageHistory:  chat_history = chats_by_session_id.get(session_id)if chat_history isNone:    chat_history = InMemoryChatMessageHistory()    chats_by_session_id[session_id]= chat_historyreturn chat_history
```

**API Reference:**InMemoryChatMessageHistory
## Use with LangGraph​
Next, we'll set up a basic chat bot using LangGraph. If you're not familiar with LangGraph, you should look at the following Quick Start Tutorial.
We'll create a LangGraph node for the chat model, and manually manage the conversation history, taking into account the conversation ID passed as part of the RunnableConfig.
The conversation ID can be passed as either part of the RunnableConfig (as we'll do here), or as part of the graph state.
```
import uuidfrom langchain_anthropic import ChatAnthropicfrom langchain_core.messages import BaseMessage, HumanMessagefrom langchain_core.runnables import RunnableConfigfrom langgraph.graph import START, MessagesState, StateGraph# Define a new graphbuilder = StateGraph(state_schema=MessagesState)# Define a chat modelmodel = ChatAnthropic(model="claude-3-haiku-20240307")# Define the function that calls the modeldefcall_model(state: MessagesState, config: RunnableConfig)->list[BaseMessage]:# Make sure that config is populated with the session idif"configurable"notin config or"session_id"notin config["configurable"]:raise ValueError("Make sure that the config includes the following information: {'configurable': {'session_id': 'some_value'}}")# Fetch the history of messages and append to it any new messages.  chat_history = get_chat_history(config["configurable"]["session_id"])  messages =list(chat_history.messages)+ state["messages"]  ai_message = model.invoke(messages)# Finally, update the chat message history to include# the new input message from the user together with the# repsonse from the model.  chat_history.add_messages(state["messages"]+[ai_message])return{"messages": ai_message}# Define the two nodes we will cycle betweenbuilder.add_edge(START,"model")builder.add_node("model", call_model)graph = builder.compile()# Here, we'll create a unique session ID to identify the conversationsession_id = uuid.uuid4()config ={"configurable":{"session_id": session_id}}input_message = HumanMessage(content="hi! I'm bob")for event in graph.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()# Here, let's confirm that the AI remembers our name!input_message = HumanMessage(content="what was my name?")for event in graph.stream({"messages":[input_message]}, config, stream_mode="values"):  event["messages"][-1].pretty_print()
```

**API Reference:**ChatAnthropic | BaseMessage | HumanMessage | RunnableConfig | StateGraph
```
================================[1m Human Message [0m=================================hi! I'm bob==================================[1m Ai Message [0m==================================Hello Bob! It's nice to meet you. I'm Claude, an AI assistant created by Anthropic. How are you doing today?================================[1m Human Message [0m=================================what was my name?==================================[1m Ai Message [0m==================================You introduced yourself as Bob when you said "hi! I'm bob".
```

tip
This also supports streaming LLM content token by token if using langgraph >= 0.2.28.
```
from langchain_core.messages import AIMessageChunkfirst =Truefor msg, metadata in graph.stream({"messages": input_message}, config, stream_mode="messages"):if msg.content andnotisinstance(msg, HumanMessage):print(msg.content, end="|", flush=True)
```

**API Reference:**AIMessageChunk
```
You| sai|d your| name was Bob.|
```

## Using With RunnableWithMessageHistory​
This how-to guide used the `messages` and `add_messages` interface of `BaseChatMessageHistory` directly.
Alternatively, you can use RunnableWithMessageHistory, as LCEL can be used inside any LangGraph node.
To do that replace the following code:
```
defcall_model(state: MessagesState, config: RunnableConfig)->list[BaseMessage]:# Make sure that config is populated with the session idif"configurable"notin config or"session_id"notin config["configurable"]:raise ValueError("You make sure that the config includes the following information: {'configurable': {'session_id': 'some_value'}}")# Fetch the history of messages and append to it any new messages.  chat_history = get_chat_history(config["configurable"]["session_id"])  messages =list(chat_history.messages)+ state["messages"]  ai_message = model.invoke(messages)# Finally, update the chat message history to include# the new input message from the user together with the# repsonse from the model.  chat_history.add_messages(state["messages"]+[ai_message])# hilight-endreturn{"messages": ai_message}
```

With the corresponding instance of `RunnableWithMessageHistory` defined in your current application.
```
runnable = RunnableWithMessageHistory(...)# From existing codedefcall_model(state: MessagesState, config: RunnableConfig)->list[BaseMessage]:# RunnableWithMessageHistory takes care of reading the message history# and updating it with the new human message and ai response.  ai_message = runnable.invoke(state['messages'], config)return{"messages": ai_message}
```

#### Was this page helpful?
  * Set up
  * ChatMessageHistory
  * Use with LangGraph
  * Using With RunnableWithMessageHistory


