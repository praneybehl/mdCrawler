Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Development
Observability
DocumentationCloud API
##### Get Started
  * Introduction
  * Quickstart


##### Customize
  * Supported Models
  * Agent Settings
  * Browser Settings
  * Connect to your Browser
  * Output Format
  * System Prompt
  * Sensitive Data
  * Custom Functions


##### Development
  * Local Setup
  * Telemetry
  * Observability
  * Roadmap


## 
​
Overview
Browser Use has a native integration with Laminar - open-source platform for tracing, evals and labeling of AI agents. Read more about Laminar in the Laminar docs.
Laminar excels at tracing browser agents by providing unified visibility into both browser session recordings and agent execution steps.
## 
​
Setup
To setup Laminar, you need to install the `lmnr` package and set the `LMNR_PROJECT_API_KEY` environment variable.
To get your project API key, you can either:
  * Register on Laminar Cloud and get the key from your project settings
  * Or spin up a local Laminar instance and get the key from the settings page


Copy
```
pip install 'lmnr[all]'
export LMNR_PROJECT_API_KEY=<your-project-api-key>

```

## 
​
Usage
Then, you simply initialize the Laminar at the top of your project and both Browser Use and session recordings will be automatically traced.
Copy
```
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from lmnr import Laminar
# this line auto-instruments Browser Use and any browser you use (local or remote)
Laminar.initialize(project_api_key="...") # you can also pass project api key here
async def main():
  agent = Agent(
    task="open google, search Laminar AI",
    llm=ChatOpenAI(model="gpt-4o-mini"),
  )
  result = await agent.run()
  print(result)
asyncio.run(main())

```

## 
​
Viewing Traces
You can view traces in the Laminar UI by going to the traces tab in your project. When you select a trace, you can see both the browser session recording and the agent execution steps.
Timeline of the browser session is synced with the agent execution steps, timeline highlights indicate the agent’s current step synced with the browser session. In the trace view, you can also see the agent’s current step, the tool it’s using, and the tool’s input and output. Tools are highlighted in the timeline with a yellow color.
![Laminar](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/images/laminar.png)
## 
​
Laminar
To learn more about tracing and evaluating your browser agents, check out the Laminar docs.
Was this page helpful?
YesNo
TelemetryRoadmap
On this page
  * Overview
  * Setup
  * Usage
  * Viewing Traces
  * Laminar


