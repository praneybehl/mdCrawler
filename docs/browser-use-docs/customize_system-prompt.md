Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Customize
System Prompt
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
You can customize the system prompt by extending the `SystemPrompt` class. Internally, this adds extra instructions to the default system prompt.
Custom system prompts allow you to modify the agent’s behavior at a fundamental level. Use this feature carefully as it can significantly impact the agent’s performance and reliability.
## 
​
Basic Customization
Create a custom system prompt by inheriting from the base class.
Copy
```
from browser_use import Agent, SystemPrompt
class MySystemPrompt(SystemPrompt):
  def important_rules(self) -> str:
    # Get existing rules from parent class
    existing_rules = super().important_rules()
    # Add your custom rules
    new_rules = """
9. MOST IMPORTANT RULE:
- ALWAYS open first a new tab and go to wikipedia.com no matter the task!!!
"""
    # Make sure to use this pattern otherwise the exiting rules will be lost
    return f'{existing_rules}\n{new_rules}'

```

## 
​
Using Custom System Prompt
Apply your custom system prompt when creating an agent:
Copy
```
from langchain_openai import ChatOpenAI
# Initialize the model
model = ChatOpenAI(model='gpt-4o')
# Create agent with custom system prompt
agent = Agent(
  task="Your task here",
  llm=model,
  system_prompt_class=MySystemPrompt
)

```

Was this page helpful?
YesNo
Output FormatSensitive Data
On this page
  * Overview
  * Basic Customization
  * Using Custom System Prompt


