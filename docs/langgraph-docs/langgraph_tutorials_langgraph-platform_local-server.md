Skip to content 
# Quickstart: Launch Local LangGraph Server¶
This is a quick start guide to help you get a LangGraph app up and running locally.
Requirements
  * Python >= 3.11
  * LangGraph CLI: Requires langchain-cli[inmem] >= 0.1.58


## Install the LangGraph CLI¶
```
pipinstall--upgrade"langgraph-cli[inmem]"

```

## 🌱 Create a LangGraph App¶
Create a new app from the `react-agent` template. This template is a simple agent that can be flexibly extended to many tools.
Python ServerNode Server
```
langgraphnewpath/to/your/app--templatereact-agent-python

```

```
langgraphnewpath/to/your/app--templatereact-agent-js

```

Additional Templates
If you use `langgraph new` without specifying a template, you will be presented with an interactive menu that will allow you to choose from a list of available templates.
## Install Dependencies¶
In the root of your new LangGraph app, install the dependencies in `edit` mode so your local changes are used by the server:
```
pipinstall-e.

```

## Create a `.env` file¶
You will find a `.env.example` in the root of your new LangGraph app. Create a `.env` file in the root of your new LangGraph app and copy the contents of the `.env.example` file into it, filling in the necessary API keys:
```
LANGSMITH_API_KEY=lsv2...
TAVILY_API_KEY=tvly-...
ANTHROPIC_API_KEY=sk-
OPENAI_API_KEY=sk-...

```

Get API Keys
  * **LANGSMITH_API_KEY** : Go to the LangSmith Settings page. Then clck **Create API Key**.
  * **ANTHROPIC_API_KEY** : Get an API key from Anthropic.
  * **OPENAI_API_KEY** : Get an API key from OpenAI.
  * **TAVILY_API_KEY** : Get an API key on the Tavily website.


## 🚀 Launch LangGraph Server¶
```
langgraphdev

```

This will start up the LangGraph API server locally. If this runs successfully, you should see something like:
> Ready!
>   * API: http://localhost:2024
>   * Docs: http://localhost:2024/docs
>   * LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
> 

In-Memory Mode
The `langgraph dev` command starts LangGraph Server in an in-memory mode. This mode is suitable for development and testing purposes. For production use, you should deploy LangGraph Server with access to a persistent storage backend.
If you want to test your application with a persistent storage backend, you can use the `langgraph up` command instead of `langgraph dev`. You will need to have `docker` installed on your machine to use this command.
## LangGraph Studio Web UI¶
LangGraph Studio Web is a specialized UI that you can connect to LangGraph API server to enable visualization, interaction, and debugging of your application locally. Test your graph in the LangGraph Studio Web UI by visiting the URL provided in the output of the `langgraph dev` command.
>   * LangGraph Studio Web UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
> 

Connecting to a server with a custom host/port
If you are running the LangGraph API server with a custom host / port, you can point the Studio Web UI at it by changing the `baseUrl` URL param. For example, if you are running your server on port 8000, you can change the above URL to the following:
```
https://smith.langchain.com/studio/baseUrl=http://127.0.0.1:8000

```

Safari Compatibility
Currently, LangGraph Studio Web does not support Safari when running a server locally.
## Test the API¶
Python SDK (Async)Python SDK (Sync)Javascript SDKRest API
**Install the LangGraph Python SDK**
```
pipinstalllanggraph-sdk

```

**Send a message to the assistant (threadless run)**
```
fromlanggraph_sdkimport get_client

client = get_client(url="http://localhost:2024")

async for chunk in client.runs.stream(
  None, # Threadless run
  "agent", # Name of assistant. Defined in langgraph.json.
  input={
    "messages": [{
      "role": "human",
      "content": "What is LangGraph?",
    }],
  },
  stream_mode="updates",
):
  print(f"Receiving new event of type: {chunk.event}...")
  print(chunk.data)
  print("\n\n")

```

**Install the LangGraph Python SDK**
```
pipinstalllanggraph-sdk

```

**Send a message to the assistant (threadless run)**
```
fromlanggraph_sdkimport get_sync_client

client = get_sync_client(url="http://localhost:2024")

for chunk in client.runs.stream(
  None, # Threadless run
  "agent", # Name of assistant. Defined in langgraph.json.
  input={
    "messages": [{
      "role": "human",
      "content": "What is LangGraph?",
    }],
  },
  stream_mode="updates",
):
  print(f"Receiving new event of type: {chunk.event}...")
  print(chunk.data)
  print("\n\n")

```

**Install the LangGraph JS SDK**
```
npminstall@langchain/langgraph-sdk

```

**Send a message to the assistant (threadless run)**
```
const{Client}=awaitimport("@langchain/langgraph-sdk");

// only set the apiUrl if you changed the default port when calling langgraph dev
constclient=newClient({apiUrl:"http://localhost:2024"});

conststreamResponse=client.runs.stream(
null,// Threadless run
"agent",// Assistant ID
{
input:{
"messages":[
{"role":"user","content":"What is LangGraph?"}
]
},
streamMode:"messages",
}
);

forawait(constchunkofstreamResponse){
console.log(`Receiving new event of type: ${chunk.event}...`);
console.log(JSON.stringify(chunk.data));
console.log("\n\n");
}

```

```
curl-s--requestPOST\
--url"http://localhost:2024/runs/stream"\
--header'Content-Type: application/json'\
--data"{
    \"assistant_id\": \"agent\",
    \"input\": {
      \"messages\": [
        {
          \"role\": \"human\",
          \"content\": \"What is LangGraph?\"
        }
      ]
    },
    \"stream_mode\": \"updates\"
  }"

```

Auth
If you're connecting to a remote server, you will need to provide a LangSmith API Key for authorization. Please see the API Reference for the clients for more information.
## Next Steps¶
Now that you have a LangGraph app running locally, take your journey further by exploring deployment and advanced features:
### 🌐 Deploy to LangGraph Cloud¶
  * **LangGraph Cloud Quickstart** : Deploy your LangGraph app using LangGraph Cloud.


### 📚 Learn More about LangGraph Platform¶
Expand your knowledge with these resources:
  * **LangGraph Platform Concepts** : Understand the foundational concepts of the LangGraph Platform. 
  * **LangGraph Platform How-to Guides** : Discover step-by-step guides to build and deploy applications.


### 🛠️ Developer References¶
Access detailed documentation for development and API usage:
  * **LangGraph Server API Reference** : Explore the LangGraph Server API documentation. 
  * **Python SDK Reference** : Explore the Python SDK API Reference.
  * **JS/TS SDK Reference** : Explore the JS/TS SDK API Reference.

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
## Comments
Back to top 
