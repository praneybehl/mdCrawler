Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
LangChain classes implement standard methods for serialization. Serializing LangChain objects using these methods confer some advantages:
  * Secrets, such as API keys, are separated from other parameters and can be loaded back to the object on de-serialization;
  * De-serialization is kept compatible across package versions, so objects that were serialized with one version of LangChain can be properly de-serialized with another.


To save and load LangChain objects using this system, use the `dumpd`, `dumps`, `load`, and `loads` functions in the load module of `langchain-core`. These functions support JSON and JSON-serializable objects.
All LangChain objects that inherit from Serializable are JSON-serializable. Examples include messages, document objects (e.g., as returned from retrievers), and most Runnables, such as chat models, retrievers, and chains implemented with the LangChain Expression Language.
Below we walk through an example with a simple LLM chain.
caution
De-serialization using `load` and `loads` can instantiate any serializable LangChain object. Only use this feature with trusted inputs!
De-serialization is a beta feature and is subject to change.
```
from langchain_core.load import dumpd, dumps, load, loadsfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIprompt = ChatPromptTemplate.from_messages([("system","Translate the following into {language}:"),("user","{text}"),],)llm = ChatOpenAI(model="gpt-4o-mini", api_key="llm-api-key")chain = prompt | llm
```

**API Reference:**dumpd | dumps | load | loads | ChatPromptTemplate | ChatOpenAI
## Saving objects​
### To json​
```
string_representation = dumps(chain, pretty=True)print(string_representation[:500])
```

```
{ "lc": 1, "type": "constructor", "id": [  "langchain",  "schema",  "runnable",  "RunnableSequence" ], "kwargs": {  "first": {   "lc": 1,   "type": "constructor",   "id": [    "langchain",    "prompts",    "chat",    "ChatPromptTemplate"   ],   "kwargs": {    "input_variables": [     "language",     "text"    ],    "messages": [     {      "lc": 1,      "type": "constructor",
```

### To a json-serializable Python dict​
```
dict_representation = dumpd(chain)print(type(dict_representation))
```

```
<class 'dict'>
```

### To disk​
```
import jsonwithopen("/tmp/chain.json","w")as fp:  json.dump(string_representation, fp)
```

Note that the API key is withheld from the serialized representations. Parameters that are considered secret are specified by the `.lc_secrets` attribute of the LangChain object:
```
chain.last.lc_secrets
```

```
{'openai_api_key': 'OPENAI_API_KEY'}
```

## Loading objects​
Specifying `secrets_map` in `load` and `loads` will load the corresponding secrets onto the de-serialized LangChain object.
### From string​
```
chain = loads(string_representation, secrets_map={"OPENAI_API_KEY":"llm-api-key"})
```

### From dict​
```
chain = load(dict_representation, secrets_map={"OPENAI_API_KEY":"llm-api-key"})
```

### From disk​
```
withopen("/tmp/chain.json","r")as fp:  chain = loads(json.load(fp), secrets_map={"OPENAI_API_KEY":"llm-api-key"})
```

Note that we recover the API key specified at the start of the guide:
```
chain.last.openai_api_key.get_secret_value()
```

```
'llm-api-key'
```

#### Was this page helpful?
  * Saving objects
    * To json
    * To a json-serializable Python dict
    * To disk
  * Loading objects
    * From string
    * From dict
    * From disk


