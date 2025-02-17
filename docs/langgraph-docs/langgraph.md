Skip to content 
# 🦜🕸️LangGraph¶
![Version](https://img.shields.io/pypi/v/langgraph) ![Downloads](https://static.pepy.tech/badge/langgraph/month) ![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraph) ![Docs](https://img.shields.io/badge/docs-latest-blue)
⚡ Building language agents as graphs ⚡
Note
Looking for the JS version? See the JS repo and the JS docs.
## Overview¶
LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Check out an introductory tutorial here.
LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.
### Why use LangGraph?¶
LangGraph powers production-grade agents, trusted by Linkedin, Uber, Klarna, GitLab, and many more. LangGraph provides fine-grained control over both the flow and state of your agent applications. It implements a central persistence layer, enabling features that are common to most agent architectures:
  * **Memory** : LangGraph persists arbitrary aspects of your application's state, supporting memory of conversations and other updates within and across user interactions;
  * **Human-in-the-loop** : Because state is checkpointed, execution can be interrupted and resumed, allowing for decisions, validation, and corrections at key stages via human input.


Standardizing these components allows individuals and teams to focus on the behavior of their agent, instead of its supporting infrastructure.
Through LangGraph Platform, LangGraph also provides tooling for the development, deployment, debugging, and monitoring of your applications.
LangGraph integrates seamlessly with LangChain and LangSmith (but does not require them).
To learn more about LangGraph, check out our first LangChain Academy course, _Introduction to LangGraph_ , available for free here.
### LangGraph Platform¶
LangGraph Platform is infrastructure for deploying LangGraph agents. It is a commercial solution for deploying agentic applications to production, built on the open-source LangGraph framework. The LangGraph Platform consists of several components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications: LangGraph Server (APIs), LangGraph SDKs (clients for the APIs), LangGraph CLI (command line tool for building the server), and LangGraph Studio (UI/debugger).
See deployment options here (includes a free tier).
Here are some common issues that arise in complex deployments, which LangGraph Platform addresses:
  * **Streaming support** : LangGraph Server provides multiple streaming modes optimized for various application needs
  * **Background runs** : Runs agents asynchronously in the background
  * **Support for long running agents** : Infrastructure that can handle long running processes
  * **Double texting** : Handle the case where you get two messages from the user before the agent can respond
  * **Handle burstiness** : Task queue for ensuring requests are handled consistently without loss, even under heavy loads


## Installation¶
```
pipinstall-Ulanggraph

```

## Example¶
Let's build a tool-calling ReAct-style agent that uses a search tool!
```
pipinstalllangchain-anthropic

```

```
exportANTHROPIC_API_KEY=sk-...

```

Optionally, we can set up LangSmith for best-in-class observability.
```
exportLANGSMITH_TRACING=true
exportLANGSMITH_API_KEY=lsv2_sk_...

```

The simplest way to create a tool-calling agent in LangGraph is to use `create_react_agent`:
High-level implementation
```
fromlanggraph.prebuiltimport create_react_agent
fromlanggraph.checkpoint.memoryimport MemorySaver
fromlangchain_anthropicimport ChatAnthropic
fromlangchain_core.toolsimport tool

# Define the tools for the agent to use
@tool
defsearch(query: str):
"""Call to surf the web."""
  # This is a placeholder, but don't tell the LLM that...
  if "sf" in query.lower() or "san francisco" in query.lower():
    return "It's 60 degrees and foggy."
  return "It's 90 degrees and sunny."


tools = [search]
model = ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()

app = create_react_agent(model, tools, checkpointer=checkpointer)

# Use the agent
final_state = app.invoke(
  {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
  config={"configurable": {"thread_id": 42}}
)
final_state["messages"][-1].content

```

```
"Based on the search results, I can tell you that the current weather in San Francisco is:\n\nTemperature: 60 degrees Fahrenheit\nConditions: Foggy\n\nSan Francisco is known for its microclimates and frequent fog, especially during the summer months. The temperature of 60°F (about 15.5°C) is quite typical for the city, which tends to have mild temperatures year-round. The fog, often referred to as "Karl the Fog" by locals, is a characteristic feature of San Francisco\'s weather, particularly in the mornings and evenings.\n\nIs there anything else you\'d like to know about the weather in San Francisco or any other location?"

```

Now when we pass the same `"thread_id"`, the conversation context is retained via the saved state (i.e. stored list of messages) 
```
final_state = app.invoke(
  {"messages": [{"role": "user", "content": "what about ny"}]},
  config={"configurable": {"thread_id": 42}}
)
final_state["messages"][-1].content

```

```
"Based on the search results, I can tell you that the current weather in New York City is:\n\nTemperature: 90 degrees Fahrenheit (approximately 32.2 degrees Celsius)\nConditions: Sunny\n\nThis weather is quite different from what we just saw in San Francisco. New York is experiencing much warmer temperatures right now. Here are a few points to note:\n\n1. The temperature of 90°F is quite hot, typical of summer weather in New York City.\n2. The sunny conditions suggest clear skies, which is great for outdoor activities but also means it might feel even hotter due to direct sunlight.\n3. This kind of weather in New York often comes with high humidity, which can make it feel even warmer than the actual temperature suggests.\n\nIt's interesting to see the stark contrast between San Francisco's mild, foggy weather and New York's hot, sunny conditions. This difference illustrates how varied weather can be across different parts of the United States, even on the same day.\n\nIs there anything else you'd like to know about the weather in New York or any other location?"

```

Tip
LangGraph is a **low-level** framework that allows you to implement any custom agent architectures. Click on the low-level implementation below to see how to implement a tool-calling agent from scratch.
Low-level implementation
```
fromtypingimport Literal

fromlangchain_anthropicimport ChatAnthropic
fromlangchain_core.toolsimport tool
fromlanggraph.checkpoint.memoryimport MemorySaver
fromlanggraph.graphimport END, START, StateGraph, MessagesState
fromlanggraph.prebuiltimport ToolNode


# Define the tools for the agent to use
@tool
defsearch(query: str):
"""Call to surf the web."""
  # This is a placeholder, but don't tell the LLM that...
  if "sf" in query.lower() or "san francisco" in query.lower():
    return "It's 60 degrees and foggy."
  return "It's 90 degrees and sunny."


tools = [search]

tool_node = ToolNode(tools)

model = ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0).bind_tools(tools)

# Define the function that determines whether to continue or not
defshould_continue(state: MessagesState) -> Literal["tools", END]:
  messages = state['messages']
  last_message = messages[-1]
  # If the LLM makes a tool call, then we route to the "tools" node
  if last_message.tool_calls:
    return "tools"
  # Otherwise, we stop (reply to the user)
  return END


# Define the function that calls the model
defcall_model(state: MessagesState):
  messages = state['messages']
  response = model.invoke(messages)
  # We return a list, because this will get added to the existing list
  return {"messages": [response]}


# Define a new graph
workflow = StateGraph(MessagesState)

# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Set the entrypoint as `agent`
# This means that this node is the first one called
workflow.add_edge(START, "agent")

# We now add a conditional edge
workflow.add_conditional_edges(
  # First, we define the start node. We use `agent`.
  # This means these are the edges taken after the `agent` node is called.
  "agent",
  # Next, we pass in the function that will determine which node is called next.
  should_continue,
)

# We now add a normal edge from `tools` to `agent`.
# This means that after `tools` is called, `agent` node is called next.
workflow.add_edge("tools", 'agent')

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()

# Finally, we compile it!
# This compiles it into a LangChain Runnable,
# meaning you can use it as you would any other runnable.
# Note that we're (optionally) passing the memory when compiling the graph
app = workflow.compile(checkpointer=checkpointer)

# Use the agent
final_state = app.invoke(
  {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
  config={"configurable": {"thread_id": 42}}
)
final_state["messages"][-1].content

```

**Step-by-step Breakdown** :  Initialize the model and tools.
  * We use `ChatAnthropic` as our LLM. **NOTE:** we need to make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the `.bind_tools()` method. 
  * We define the tools we want to use - a search tool in our case. It is really easy to create your own tools - see documentation here on how to do that here. 

Initialize graph with state.
  * We initialize graph (`StateGraph`) by passing state schema (in our case `MessagesState`)
  * `MessagesState` is a prebuilt state schema that has one attribute -- a list of LangChain `Message` objects, as well as logic for merging the updates from each node into the state.

Define graph nodes. There are two main nodes we need: 
  * The `agent` node: responsible for deciding what (if any) actions to take.
  * The `tools` node that invokes tools: if the agent decides to take an action, this node will then execute that action.

Define entry point and graph edges. First, we need to set the entry point for graph execution - `agent` node. Then we define one normal and one conditional edge. Conditional edge means that the destination depends on the contents of the graph's state (`MessagesState`). In our case, the destination is not known until the agent (LLM) decides. 
  * Conditional edge: after the agent is called, we should either: 
    * a. Run tools if the agent said to take an action, OR
    * b. Finish (respond to the user) if the agent did not ask to run tools
  * Normal edge: after the tools are invoked, the graph should always return to the agent to decide what to do next

Compile the graph.
  * When we compile the graph, we turn it into a LangChain Runnable, which automatically enables calling `.invoke()`, `.stream()` and `.batch()` with your inputs 
  * We can also optionally pass checkpointer object for persisting state between graph runs, and enabling memory, human-in-the-loop workflows, time travel and more. In our case we use `MemorySaver` - a simple in-memory checkpointer 

Execute the graph.
  1. LangGraph adds the input message to the internal state, then passes the state to the entrypoint node, `"agent"`.
  2. The `"agent"` node executes, invoking the chat model.
  3. The chat model returns an `AIMessage`. LangGraph adds this to the state.
  4. Graph cycles the following steps until there are no more `tool_calls` on `AIMessage`: 
     * If `AIMessage` has `tool_calls`, `"tools"` node executes
     * The `"agent"` node executes again and returns `AIMessage`
  5. Execution progresses to the special `END` value and outputs the final state. And as a result, we get a list of all our chat messages as output.


## Documentation¶
  * Tutorials: Learn to build with LangGraph through guided examples.
  * How-to Guides: Accomplish specific things within LangGraph, from streaming, to adding memory & persistence, to common design patterns (branching, subgraphs, etc.), these are the place to go if you want to copy and run a specific code snippet.
  * Conceptual Guides: In-depth explanations of the key concepts and principles behind LangGraph, such as nodes, edges, state and more.
  * API Reference: Review important classes and methods, simple examples of how to use the graph and checkpointing APIs, higher-level prebuilt components and more.
  * LangGraph Platform: LangGraph Platform is a commercial solution for deploying agentic applications in production, built on the open-source LangGraph framework.


## Resources¶
  * Built with LangGraph: Hear how industry leaders use LangGraph to ship powerful, production-ready AI applications.


## Contributing¶
For more information on how to contribute, see here.
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
Back to top 
