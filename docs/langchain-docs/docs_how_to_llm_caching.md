Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
LangChain provides an optional caching layer for LLMs. This is useful for two reasons:
It can save you money by reducing the number of API calls you make to the LLM provider, if you're often requesting the same completion multiple times. It can speed up your application by reducing the number of API calls you make to the LLM provider.
```
%pip install -qU langchain_openai langchain_communityimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()# Please manually enter OpenAI Key
```

```
from langchain_core.globalsimport set_llm_cachefrom langchain_openai import OpenAI# To make the caching really obvious, lets use a slower and older model.# Caching supports newer chat models as well.llm = OpenAI(model="gpt-3.5-turbo-instruct", n=2, best_of=2)
```

**API Reference:**set_llm_cache | OpenAI
```
%%timefrom langchain_core.caches import InMemoryCacheset_llm_cache(InMemoryCache())# The first time, it is not yet in cache, so it should take longerllm.invoke("Tell me a joke")
```

**API Reference:**InMemoryCache
```
CPU times: user 546 ms, sys: 379 ms, total: 925 msWall time: 1.11 s
```

```
"\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"
```

```
%%time# The second time it is, so it goes fasterllm.invoke("Tell me a joke")
```

```
CPU times: user 192 µs, sys: 77 µs, total: 269 µsWall time: 270 µs
```

```
"\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"
```

## SQLite Cache​
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
CPU times: user 10.6 ms, sys: 4.21 ms, total: 14.8 msWall time: 851 ms
```

```
"\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"
```

```
%%time# The second time it is, so it goes fasterllm.invoke("Tell me a joke")
```

```
CPU times: user 59.7 ms, sys: 63.6 ms, total: 123 msWall time: 134 ms
```

```
"\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"
```

#### Was this page helpful?
  * SQLite Cache


