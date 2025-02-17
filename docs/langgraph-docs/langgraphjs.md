Skip to content 
# 🦜🕸️LangGraph.js¶
![Docs](https://img.shields.io/badge/docs-latest-blue) ![Version](https://img.shields.io/npm/v/@langchain/langgraph?logo=npm) ![Downloads](https://img.shields.io/npm/dm/@langchain/langgraph) ![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langgraphjs)
⚡ Building language agents as graphs ⚡
Note
Looking for the Python version? See the Python repo and the Python docs.
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
npminstall@langchain/langgraph@langchain/core

```

## Example¶
Let's build a tool-calling ReAct-style agent that uses a search tool!
```
npminstall@langchain/anthropiczod

```

```
exportANTHROPIC_API_KEY=sk-...

```

Optionally, we can set up LangSmith for best-in-class observability.
```
exportLANGSMITH_TRACING=true
exportLANGSMITH_API_KEY=lsv2_sk_...

```

The simplest way to create a tool-calling agent in LangGraph is to use `createReactAgent`:
High-level implementation
```
import{createReactAgent}from"@langchain/langgraph/prebuilt";
import{MemorySaver}from"@langchain/langgraph";
import{ChatAnthropic}from"@langchain/anthropic";
import{tool}from"@langchain/core/tools";

import{z}from"zod";

// Define the tools for the agent to use
constsearch=tool(async({query})=>{
// This is a placeholder, but don't tell the LLM that...
if(query.toLowerCase().includes("sf")||query.toLowerCase().includes("san francisco")){
return"It's 60 degrees and foggy."
}
return"It's 90 degrees and sunny."
},{
name:"search",
description:"Call to surf the web.",
schema:z.object({
query:z.string().describe("The query to use in your search."),
}),
});

consttools=[search];
constmodel=newChatAnthropic({
model:"claude-3-5-sonnet-latest"
});

// Initialize memory to persist state between graph runs
constcheckpointer=newMemorySaver();

constapp=createReactAgent({
llm:model,
tools,
checkpointSaver:checkpointer,
});

// Use the agent
constresult=awaitapp.invoke(
{
messages:[{
role:"user",
content:"what is the weather in sf"
}]
},
{configurable:{thread_id:42}}
);
console.log(result.messages.at(-1)?.content);

```

```
"Based on the search results, it's currently 60 degrees Fahrenheit and foggy in San Francisco, which is quite typical weather for the city."

```

Now when we pass the same `"thread_id"`, the conversation context is retained via the saved state (i.e. stored list of messages) 
```
constfollowup=awaitapp.invoke(
{
messages:[{
role:"user",
content:"what about ny"
}]
},
{configurable:{thread_id:42}}
);

console.log(followup.messages.at(-1)?.content);

```

```
"According to the search results, it's currently 90 degrees Fahrenheit and sunny in New York City. That's quite a warm day for New York!"

```

Tip
LangGraph is a **low-level** framework that allows you to implement any custom agent architectures. Click on the low-level implementation below to see how to implement a tool-calling agent from scratch.
Low-level implementation
```
import{AIMessage,BaseMessage,HumanMessage}from"@langchain/core/messages";
import{tool}from"@langchain/core/tools";
import{z}from"zod";
import{ChatAnthropic}from"@langchain/anthropic";
import{StateGraph}from"@langchain/langgraph";
import{MemorySaver,Annotation,messagesStateReducer}from"@langchain/langgraph";
import{ToolNode}from"@langchain/langgraph/prebuilt";

// Define the graph state
// See here for more info: https://langchain-ai.github.io/langgraphjs/how-tos/define-state/
constStateAnnotation=Annotation.Root({
messages:Annotation<BaseMessage[]>({
// `messagesStateReducer` function defines how `messages` state key should be updated
// (in this case it appends new messages to the list and overwrites messages with the same ID)
reducer:messagesStateReducer,
}),
});

// Define the tools for the agent to use
constweatherTool=tool(async({query})=>{
// This is a placeholder for the actual implementation
if(query.toLowerCase().includes("sf")||query.toLowerCase().includes("san francisco")){
return"It's 60 degrees and foggy."
}
return"It's 90 degrees and sunny."
},{
name:"weather",
description:
"Call to get the current weather for a location.",
schema:z.object({
query:z.string().describe("The query to use in your search."),
}),
});

consttools=[weatherTool];
consttoolNode=newToolNode(tools);

constmodel=newChatAnthropic({
model:"claude-3-5-sonnet-20240620",
temperature:0,
}).bindTools(tools);

// Define the function that determines whether to continue or not
// We can extract the state typing via `StateAnnotation.State`
functionshouldContinue(state:typeofStateAnnotation.State){
constmessages=state.messages;
constlastMessage=messages[messages.length-1]asAIMessage;

// If the LLM makes a tool call, then we route to the "tools" node
if(lastMessage.tool_calls?.length){
return"tools";
}
// Otherwise, we stop (reply to the user)
return"__end__";
}

// Define the function that calls the model
asyncfunctioncallModel(state:typeofStateAnnotation.State){
constmessages=state.messages;
constresponse=awaitmodel.invoke(messages);

// We return a list, because this will get added to the existing list
return{messages:[response]};
}

// Define a new graph
constworkflow=newStateGraph(StateAnnotation)
.addNode("agent",callModel)
.addNode("tools",toolNode)
.addEdge("__start__","agent")
.addConditionalEdges("agent",shouldContinue)
.addEdge("tools","agent");

// Initialize memory to persist state between graph runs
constcheckpointer=newMemorySaver();

// Finally, we compile it!
// This compiles it into a LangChain Runnable.
// Note that we're (optionally) passing the memory when compiling the graph
constapp=workflow.compile({checkpointer});

// Use the Runnable
constfinalState=awaitapp.invoke(
{messages:[newHumanMessage("what is the weather in sf")]},
{configurable:{thread_id:"42"}}
);

console.log(finalState.messages[finalState.messages.length-1].content);

```

**Step-by-step Breakdown** :  Initialize the model and tools.
  * We use `ChatAnthropic` as our LLM. **NOTE:** we need to make sure the model knows that it has these tools available to call. We can do this by converting the LangChain tools into the format for OpenAI tool calling using the `.bindTools()` method. 
  * We define the tools we want to use - a search tool in our case. It is really easy to create your own tools - see documentation here on how to do that here. 

Initialize graph with state.
  * We initialize the graph (`StateGraph`) by passing state schema with a reducer that defines how the state should be updated. In our case, we want to append new messages to the list and overwrite messages with the same ID, so we use the prebuilt `messagesStateReducer`.

Define graph nodes. There are two main nodes we need: 
  * The `agent` node: responsible for deciding what (if any) actions to take.
  * The `tools` node that invokes tools: if the agent decides to take an action, this node will then execute that action.

Define entry point and graph edges. First, we need to set the entry point for graph execution - `agent` node. Then we define one normal and one conditional edge. Conditional edge means that the destination depends on the contents of the graph's state. In our case, the destination is not known until the agent (LLM) decides. 
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
