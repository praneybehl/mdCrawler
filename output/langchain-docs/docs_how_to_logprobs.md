Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * Tokens


Certain chat models can be configured to return token-level log probabilities representing the likelihood of a given token. This guide walks through how to get this information in LangChain.
## OpenAI​
Install the LangChain x OpenAI package and set your API key
```
%pip install -qU langchain-openai
```

```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

For the OpenAI API to return log probabilities we need to configure the `logprobs=True` param. Then, the logprobs are included on each output `AIMessage` as part of the `response_metadata`:
```
from langchain_openai import ChatOpenAIllm = ChatOpenAI(model="gpt-4o-mini").bind(logprobs=True)msg = llm.invoke(("human","how are you today"))msg.response_metadata["logprobs"]["content"][:5]
```

**API Reference:**ChatOpenAI
```
[{'token': 'I', 'bytes': [73], 'logprob': -0.26341408, 'top_logprobs': []}, {'token': "'m", 'bytes': [39, 109], 'logprob': -0.48584133, 'top_logprobs': []}, {'token': ' just', 'bytes': [32, 106, 117, 115, 116], 'logprob': -0.23484154, 'top_logprobs': []}, {'token': ' a', 'bytes': [32, 97], 'logprob': -0.0018291725, 'top_logprobs': []}, {'token': ' computer', 'bytes': [32, 99, 111, 109, 112, 117, 116, 101, 114], 'logprob': -0.052299336, 'top_logprobs': []}]
```

And are part of streamed Message chunks as well:
```
ct =0full =Nonefor chunk in llm.stream(("human","how are you today")):if ct <5:    full = chunk if full isNoneelse full + chunkif"logprobs"in full.response_metadata:print(full.response_metadata["logprobs"]["content"])else:break  ct +=1
```

```
[][{'token': 'I', 'bytes': [73], 'logprob': -0.26593843, 'top_logprobs': []}][{'token': 'I', 'bytes': [73], 'logprob': -0.26593843, 'top_logprobs': []}, {'token': "'m", 'bytes': [39, 109], 'logprob': -0.3238896, 'top_logprobs': []}][{'token': 'I', 'bytes': [73], 'logprob': -0.26593843, 'top_logprobs': []}, {'token': "'m", 'bytes': [39, 109], 'logprob': -0.3238896, 'top_logprobs': []}, {'token': ' just', 'bytes': [32, 106, 117, 115, 116], 'logprob': -0.23778509, 'top_logprobs': []}][{'token': 'I', 'bytes': [73], 'logprob': -0.26593843, 'top_logprobs': []}, {'token': "'m", 'bytes': [39, 109], 'logprob': -0.3238896, 'top_logprobs': []}, {'token': ' just', 'bytes': [32, 106, 117, 115, 116], 'logprob': -0.23778509, 'top_logprobs': []}, {'token': ' a', 'bytes': [32, 97], 'logprob': -0.0022134194, 'top_logprobs': []}]
```

## Next steps​
You've now learned how to get logprobs from OpenAI models in LangChain.
Next, check out the other how-to guides chat models in this section, like how to get a model to return structured output or how to track token usage.
#### Was this page helpful?
  * OpenAI
  * Next steps


