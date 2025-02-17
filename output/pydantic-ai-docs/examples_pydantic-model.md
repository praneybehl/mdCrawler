Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# Pydantic Model
Simple example of using PydanticAI to construct a Pydantic model from a text input.
Demonstrates:
  * structured `result_type`


## Running the Example
With dependencies installed and environment variables set, run:
pipuv
```
python-mpydantic_ai_examples.pydantic_model

```

```
uvrun-mpydantic_ai_examples.pydantic_model

```

This examples uses `openai:gpt-4o` by default, but it works well with other models, e.g. you can run it with Gemini using:
pipuv
```
PYDANTIC_AI_MODEL=gemini-1.5-propython-mpydantic_ai_examples.pydantic_model

```

```
PYDANTIC_AI_MODEL=gemini-1.5-prouvrun-mpydantic_ai_examples.pydantic_model

```

(or `PYDANTIC_AI_MODEL=gemini-1.5-flash ...`)
## Example Code
pydantic_model.py```
import os
from typing import cast
import logfire
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

class MyModel(BaseModel):
  city: str
  country: str

model = cast(KnownModelName, os.getenv('PYDANTIC_AI_MODEL', 'openai:gpt-4o'))
print(f'Using model: {model}')
agent = Agent(model, result_type=MyModel)
if __name__ == '__main__':
  result = agent.run_sync('The windy city in the US of A.')
  print(result.data)
  print(result.usage())

```

