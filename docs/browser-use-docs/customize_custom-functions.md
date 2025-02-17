Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Customize
Custom Functions
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
Basic Function Registration
Functions can be either `sync` or `async`. Keep them focused and single-purpose.
Copy
```
from browser_use import Controller, ActionResult
# Initialize the controller
controller = Controller()
@controller.action('Ask user for information')
def ask_human(question: str) -> str:
  answer = input(f'\n{question}\nInput: ')
  return ActionResult(extracted_content=answer)

```

Basic `Controller` has all basic functionality you might need to interact with the browser already implemented.
Copy
```
# ... then pass controller to the agent
agent = Agent(
  task=task,
  llm=llm,
  controller=controller
)

```

Keep the function name and description short and concise. The Agent use the function solely based on the name and description. The stringified output of the action is passed to the Agent.
## 
​
Browser-Aware Functions
For actions that need browser access, simply add the `browser` parameter inside the function parameters:
Copy
```
from browser_use import Browser, Controller, ActionResult
controller = Controller()
@controller.action('Open website')
async def open_website(url: str, browser: Browser):
  page = browser.get_current_page()
  await page.goto(url)
  return ActionResult(extracted_content='Website opened')

```

## 
​
Structured Parameters with Pydantic
For complex actions, you can define parameter schemas using Pydantic models:
Copy
```
from pydantic import BaseModel
from typing import Optional
from browser_use import Controller, ActionResult, Browser
controller = Controller()
class JobDetails(BaseModel):
  title: str
  company: str
  job_link: str
  salary: Optional[str] = None
@controller.action(
  'Save job details which you found on page',
  param_model=JobDetails
)
async def save_job(params: JobDetails, browser: Browser):
  print(f"Saving job: {params.title} at {params.company}")
  # Access browser if needed
  page = browser.get_current_page()
  await page.goto(params.job_link)

```

## 
​
Using Custom Actions with multiple agents
You can use the same controller for multiple agents.
Copy
```
controller = Controller()
# ... register actions to the controller
agent = Agent(
  task="Go to website X and find the latest news",
  llm=llm,
  controller=controller
)
# Run the agent
await agent.run()
agent2 = Agent(
  task="Go to website Y and find the latest news",
  llm=llm,
  controller=controller
)
await agent2.run()

```

The controller is stateless and can be used to register multiple actions and multiple agents.
## 
​
Exclude functions
If you want less actions to be used by the agent, you can exclude them from the controller.
Copy
```
controller = Controller(exclude_actions=['open_tab', 'google_search'])

```

For more examples like file upload or notifications, visit examples/custom-functions.
Was this page helpful?
YesNo
Sensitive DataLocal Setup
On this page
  * Basic Function Registration
  * Browser-Aware Functions
  * Structured Parameters with Pydantic
  * Using Custom Actions with multiple agents
  * Exclude functions


