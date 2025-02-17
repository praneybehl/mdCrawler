Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Tracking token usage to calculate cost is an important part of putting your app in production. This guide goes over how to obtain this information from your LangChain model calls.
Prerequisites
This guide assumes familiarity with the following concepts:
  * LLMs


## Using LangSmith​
You can use LangSmith to help track token usage in your LLM application. See the LangSmith quick start guide.
## Using callbacks​
There are some API-specific callback context managers that allow you to track token usage across multiple calls. You'll need to check whether such an integration is available for your particular model.
If such an integration is not available for your model, you can create a custom callback manager by adapting the implementation of the OpenAI callback manager.
### OpenAI​
Let's first look at an extremely simple example of tracking token usage for a single Chat model call.
danger
The callback handler does not currently support streaming token counts for legacy language models (e.g., `langchain_openai.OpenAI`). For support in a streaming context, refer to the corresponding guide for chat models here.
### Single call​
```
from langchain_community.callbacks import get_openai_callbackfrom langchain_openai import OpenAIllm = OpenAI(model_name="gpt-3.5-turbo-instruct")with get_openai_callback()as cb:  result = llm.invoke("Tell me a joke")print(result)print("---")print()print(f"Total Tokens: {cb.total_tokens}")print(f"Prompt Tokens: {cb.prompt_tokens}")print(f"Completion Tokens: {cb.completion_tokens}")print(f"Total Cost (USD): ${cb.total_cost}")
```

**API Reference:**get_openai_callback | OpenAI
```
Why don't scientists trust atoms?Because they make up everything.---Total Tokens: 18Prompt Tokens: 4Completion Tokens: 14Total Cost (USD): $3.4e-05
```

### Multiple calls​
Anything inside the context manager will get tracked. Here's an example of using it to track multiple calls in sequence to a chain. This will also work for an agent which may use multiple steps.
```
from langchain_community.callbacks import get_openai_callbackfrom langchain_core.prompts import PromptTemplatefrom langchain_openai import OpenAIllm = OpenAI(model_name="gpt-3.5-turbo-instruct")template = PromptTemplate.from_template("Tell me a joke about {topic}")chain = template | llmwith get_openai_callback()as cb:  response = chain.invoke({"topic":"birds"})print(response)  response = chain.invoke({"topic":"fish"})print("--")print(response)print()print("---")print(f"Total Tokens: {cb.total_tokens}")print(f"Prompt Tokens: {cb.prompt_tokens}")print(f"Completion Tokens: {cb.completion_tokens}")print(f"Total Cost (USD): ${cb.total_cost}")
```

**API Reference:**get_openai_callback | PromptTemplate | OpenAI
```
Why did the chicken go to the seance?To talk to the other side of the road!--Why did the fish need a lawyer?Because it got caught in a net!---Total Tokens: 50Prompt Tokens: 12Completion Tokens: 38Total Cost (USD): $9.400000000000001e-05
```

## Streaming​
danger
`get_openai_callback` does not currently support streaming token counts for legacy language models (e.g., `langchain_openai.OpenAI`). If you want to count tokens correctly in a streaming context, there are a number of options:
  * Use chat models as described in this guide;
  * Implement a custom callback handler that uses appropriate tokenizers to count the tokens;
  * Use a monitoring platform such as LangSmith.


Note that when using legacy language models in a streaming context, token counts are not updated:
```
from langchain_community.callbacks import get_openai_callbackfrom langchain_openai import OpenAIllm = OpenAI(model_name="gpt-3.5-turbo-instruct")with get_openai_callback()as cb:for chunk in llm.stream("Tell me a joke"):print(chunk, end="", flush=True)print(result)print("---")print()print(f"Total Tokens: {cb.total_tokens}")print(f"Prompt Tokens: {cb.prompt_tokens}")print(f"Completion Tokens: {cb.completion_tokens}")print(f"Total Cost (USD): ${cb.total_cost}")
```

**API Reference:**get_openai_callback | OpenAI
```
Why don't scientists trust atoms?Because they make up everything!Why don't scientists trust atoms?Because they make up everything.---Total Tokens: 0Prompt Tokens: 0Completion Tokens: 0Total Cost (USD): $0.0
```

#### Was this page helpful?
  * Using LangSmith
  * Using callbacks
    * OpenAI
    * Single call
    * Multiple calls
  * Streaming


