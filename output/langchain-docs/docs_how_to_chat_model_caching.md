Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * LLMs


LangChain provides an optional caching layer for chat models. This is useful for two main reasons:
  * It can save you money by reducing the number of API calls you make to the LLM provider, if you're often requesting the same completion multiple times. This is especially useful during app development.
  * It can speed up your application by reducing the number of API calls you make to the LLM provider.


This guide will walk you through how to enable this in your apps.
Select chat model:
Groq▾
* Groq
* OpenAI
* Anthropic
* Azure
* Google Vertex
* AWS
* Cohere
* NVIDIA
* Fireworks AI
* Mistral AI
* Together AI
* IBM watsonx
* Databricks
```
pip install -qU "langchain[groq]"
```

```
import getpassimport osifnot os.environ.get("GROQ_API_KEY"): os.environ["GROQ_API_KEY"]= getpass.getpass("Enter API key for Groq: ")from langchain.chat_models import init_chat_modelllm = init_chat_model("llama3-8b-8192", model_provider="groq")
```

```
# <!-- ruff: noqa: F821 -->from langchain_core.globalsimport set_llm_cache
```

**API Reference:**set_llm_cache
## In Memory Cache​
This is an ephemeral cache that stores model calls in memory. It will be wiped when your environment restarts, and is not shared across processes.
```
%%timefrom langchain_core.caches import InMemoryCacheset_llm_cache(InMemoryCache())# The first time, it is not yet in cache, so it should take longerllm.invoke("Tell me a joke")
```

**API Reference:**InMemoryCache
```
CPU times: user 645 ms, sys: 214 ms, total: 859 msWall time: 829 ms
```

```
AIMessage(content="Why don't scientists trust atoms?\n\nBecause they make up everything!", response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 11, 'total_tokens': 24}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_c2295e73ad', 'finish_reason': 'stop', 'logprobs': None}, id='run-b6836bdd-8c30-436b-828f-0ac5fc9ab50e-0')
```

```
%%time# The second time it is, so it goes fasterllm.invoke("Tell me a joke")
```

```
CPU times: user 822 µs, sys: 288 µs, total: 1.11 msWall time: 1.06 ms
```

```
AIMessage(content="Why don't scientists trust atoms?\n\nBecause they make up everything!", response_metadata={'token_usage': {'completion_tokens': 13, 'prompt_tokens': 11, 'total_tokens': 24}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_c2295e73ad', 'finish_reason': 'stop', 'logprobs': None}, id='run-b6836bdd-8c30-436b-828f-0ac5fc9ab50e-0')
```

## SQLite Cache​
This cache implementation uses a `SQLite` database to store responses, and will last across process restarts.
```
!rm .langchain.db
```

```
# We can do the same thing with a SQLite cachefrom langchain_community.cache import SQLiteCacheset_llm_cache(SQLiteCache(database_path=".langchain.db"))
```

**API Reference:**SQLiteCache
```
%%time# The first time, it is not yet in cache, so it should take longerllm.invoke("Tell me a joke")
```

```
CPU times: user 9.91 ms, sys: 7.68 ms, total: 17.6 msWall time: 657 ms
```

```
AIMessage(content='Why did the scarecrow win an award? Because he was outstanding in his field!', response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 11, 'total_tokens': 28}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': 'fp_c2295e73ad', 'finish_reason': 'stop', 'logprobs': None}, id='run-39d9e1e8-7766-4970-b1d8-f50213fd94c5-0')
```

```
%%time# The second time it is, so it goes fasterllm.invoke("Tell me a joke")
```

```
CPU times: user 52.2 ms, sys: 60.5 ms, total: 113 msWall time: 127 ms
```

```
AIMessage(content='Why did the scarecrow win an award? Because he was outstanding in his field!', id='run-39d9e1e8-7766-4970-b1d8-f50213fd94c5-0')
```

## Next steps​
You've now learned how to cache model responses to save time and money.
Next, check out the other how-to guides chat models in this section, like how to get a model to return structured output or how to create your own custom chat model.
#### Was this page helpful?
  * In Memory Cache
  * SQLite Cache
  * Next steps


