Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Get Started
Quickstart
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
Prepare the environment
Browser Use requires Python 3.11 or higher.
First, we recommend using uv to setup the Python environment.
Copy
```
uv venv --python 3.11

```

and activate it with:
Copy
```
# For Mac/Linux:
source .venv/bin/activate
# For Windows:
.venv\Scripts\activate

```

Install the dependencies:
Copy
```
uv pip install browser-use

```

Then install playwright:
Copy
```
playwright install

```

## 
​
Create an agent
Then you can use the agent as follows:
agent.py
Copy
```
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()
import asyncio
llm = ChatOpenAI(model="gpt-4o")
async def main():
  agent = Agent(
    task="Compare the price of gpt-4o and DeepSeek-V3",
    llm=llm,
  )
  result = await agent.run()
  print(result)
asyncio.run(main())

```

## 
​
Set up your LLM API keys
`ChatOpenAI` and other Langchain chat models require API keys. You should store these in your `.env` file. For example, for OpenAI and Anthropic, you can set the API keys in your `.env` file, such as:
.env
Copy
```
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

```

For other LLM models you can refer to the Langchain documentation to find how to set them up with their specific API keys.
Was this page helpful?
YesNo
IntroductionSupported Models
On this page
  * Prepare the environment
  * Create an agent
  * Set up your LLM API keys


