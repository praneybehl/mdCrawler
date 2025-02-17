Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
`ConversationChain` incorporated a memory of previous messages to sustain a stateful conversation.
Some advantages of switching to the Langgraph implementation are:
  * Innate support for threads/separate sessions. To make this work with `ConversationChain`, you'd need to instantiate a separate memory class outside the chain.
  * More explicit parameters. `ConversationChain` contains a hidden default prompt, which can cause confusion.
  * Streaming support. `ConversationChain` only supports streaming via callbacks.


Langgraph's checkpointing system supports multiple threads or sessions, which can be specified via the `"thread_id"` key in its configuration parameters.
```
%pip install --upgrade --quiet langchain langchain-openai
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

## Legacy​
Details
```
from langchain.chains import ConversationChainfrom langchain.memory import ConversationBufferMemoryfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAItemplate ="""You are a pirate. Answer the following questions as best you can.Chat history: {history}Question: {input}"""prompt = ChatPromptTemplate.from_template(template)memory = ConversationBufferMemory()chain = ConversationChain(  llm=ChatOpenAI(),  memory=memory,  prompt=prompt,)chain({"input":"I'm Bob, how are you?"})
```

**API Reference:**ConversationChain | ConversationBufferMemory | ChatPromptTemplate | ChatOpenAI
```
{'input': "I'm Bob, how are you?", 'history': '', 'response': "Arrr matey, I be a pirate sailin' the high seas. What be yer business with me?"}
```

```
chain({"input":"What is my name?"})
```

```
{'input': 'What is my name?', 'history': "Human: I'm Bob, how are you?\nAI: Arrr matey, I be a pirate sailin' the high seas. What be yer business with me?", 'response': 'Your name be Bob, matey.'}
```

## Langgraph​
Details
```
import uuidfrom langchain_openai import ChatOpenAIfrom langgraph.checkpoint.memory import MemorySaverfrom langgraph.graph import START, MessagesState, StateGraphmodel = ChatOpenAI(model="gpt-4o-mini")# Define a new graphworkflow = StateGraph(state_schema=MessagesState)# Define the function that calls the modeldefcall_model(state: MessagesState):  response = model.invoke(state["messages"])return{"messages": response}# Define the two nodes we will cycle betweenworkflow.add_edge(START,"model")workflow.add_node("model", call_model)# Add memorymemory = MemorySaver()app = workflow.compile(checkpointer=memory)# The thread id is a unique key that identifies# this particular conversation.# We'll just generate a random uuid here.thread_id = uuid.uuid4()config ={"configurable":{"thread_id": thread_id}}
```

**API Reference:**ChatOpenAI | MemorySaver | StateGraph
```
query ="I'm Bob, how are you?"input_messages =[{"role":"system","content":"You are a pirate. Answer the following questions as best you can.",},{"role":"user","content": query},]for event in app.stream({"messages": input_messages}, config, stream_mode="values"):  event["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================I'm Bob, how are you?==================================[1m Ai Message [0m==================================Ahoy, Bob! I be feelin' as lively as a ship in full sail! How be ye on this fine day?
```

```
query ="What is my name?"input_messages =[{"role":"user","content": query}]for event in app.stream({"messages": input_messages}, config, stream_mode="values"):  event["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is my name?==================================[1m Ai Message [0m==================================Ye be callin' yerself Bob, I reckon! A fine name for a swashbuckler like yerself!
```

## Next steps​
See this tutorial for a more end-to-end guide on building with `RunnableWithMessageHistory`.
Check out the LCEL conceptual docs for more background information.
#### Was this page helpful?
  * Legacy
  * Langgraph
  * Next steps


