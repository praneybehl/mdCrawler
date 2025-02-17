Skip to content 
# Quickstart: Deploy on LangGraph Cloud¶
Prerequisites
Before you begin, ensure you have the following:
  * GitHub account
  * LangSmith account


## Create a repository on GitHub¶
To deploy a LangGraph application to **LangGraph Cloud** , your application code must reside in a GitHub repository. Both public and private repositories are supported.
You can deploy any LangGraph Application to LangGraph Cloud.
For this guide, we'll use the pre-built Python **ReAct Agent** template.
Get Required API Keys for the ReAct Agent template
This **ReAct Agent** application requires an API key from Anthropic and Tavily. You can get these API keys by signing up on their respective websites.
**Alternative** : If you'd prefer a scaffold application that doesn't require API keys, use the **New LangGraph Project** template instead of the **ReAct Agent** template.
  1. Go to the ReAct Agent repository.
  2. Fork the repository to your GitHub account by clicking the `Fork` button in the top right corner.


## Deploy to LangGraph Cloud¶
1. Log in to LangSmith ![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/01_login.png) Go to LangSmith and log in. If you don't have an account, you can sign up for free.  2. Click on _LangGraph Platform_ (the left sidebar) ![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/02_langgraph_platform.png) Select **LangGraph Platform** from the left sidebar.  3. Click on + New Deployment (top right corner) ![Login to LangSmith](https://langchain-ai.github.io/langgraph/cloud/deployment/img/03_deployments_page.png) Click on **+ New Deployment** to create a new deployment. This button is located in the top right corner. It'll open a new modal where you can fill out the required fields.  4. Click on Import from GitHub (first time users) ![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/04_create_new_deployment.png) Click on **Import from GitHub** and follow the instructions to connect your GitHub account. This step is needed for **first-time users** or to add private repositories that haven't been connected before. 5. Select the repository, configure ENV vars etc ![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png) Select the **repository** , add env variables and secrets, and set other configuration options. 
  * **Repository** : Select the repository you forked earlier (or any other repository you want to deploy).
  * Set the secrets and environment variables required by your application. For the **ReAct Agent** template, you need to set the following secrets:
    * **ANTHROPIC_API_KEY** : Get an API key from Anthropic.
    * **TAVILY_API_KEY** : Get an API key on the Tavily website.

6. Click Submit to Deploy! ![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/05_configure_deployment.png) Please note that this step may ~15 minutes to complete. You can check the status of your deployment in the **Deployments** view. Click the **Submit** button at the top right corner to deploy your application. 
## LangGraph Studio Web UI¶
Once your application is deployed, you can test it in **LangGraph Studio**. 
1. Click on an existing deployment ![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/07_deployments_page.png) Click on the deployment you just created to view more details.  2. Click on LangGraph Studio ![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/08_deployment_view.png) Click on the **LangGraph Studio** button to open LangGraph Studio. 
![image](https://langchain-ai.github.io/langgraph/cloud/deployment/img/09_langgraph_studio.png)
Sample graph run in LangGraph Studio. 
## Test the API¶
Note
The API calls below are for the **ReAct Agent** template. If you're deploying a different application, you may need to adjust the API calls accordingly.
Before using, you need to get the `URL` of your LangGraph deployment. You can find this in the `Deployment` view. Click the `URL` to copy it to the clipboard.
You also need to make sure you have set up your API key properly, so you can authenticate with LangGraph Cloud.
```
exportLANGSMITH_API_KEY=...

```

Python SDK (Async)Python SDK (Sync)Javascript SDKRest API
**Install the LangGraph Python SDK**
```
pipinstalllanggraph-sdk

```

**Send a message to the assistant (threadless run)**
```
fromlanggraph_sdkimport get_client

client = get_client(url="your-deployment-url", api_key="your-langsmith-api-key")

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

client = get_sync_client(url="your-deployment-url", api_key="your-langsmith-api-key")

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

constclient=newClient({apiUrl:"your-deployment-url",apiKey:"your-langsmith-api-key"});

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
--url<DEPLOYMENT_URL>\
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

## Next Steps¶
Congratulations! If you've worked your way through this tutorial you are well on your way to becoming a LangGraph Cloud expert. Here are some other resources to check out to help you out on the path to expertise:
### LangGraph Framework¶
  * **LangGraph Tutorial** : Get started with LangGraph framework.
  * **LangGraph Concepts** : Learn the foundational concepts of LangGraph.
  * **LangGraph How-to Guides** : Guides for common tasks with LangGraph.


### 📚 Learn More about LangGraph Platform¶
Expand your knowledge with these resources:
  * **LangGraph Platform Concepts** : Understand the foundational concepts of the LangGraph Platform.
  * **LangGraph Platform How-to Guides** : Discover step-by-step guides to build and deploy applications.
  * **Launch Local LangGraph Server** : This quick start guide shows how to start a LangGraph Server locally for the **ReAct Agent** template. The steps are similar for other templates.

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
## Comments
Back to top 
