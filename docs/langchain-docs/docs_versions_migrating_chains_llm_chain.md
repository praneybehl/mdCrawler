Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
`LLMChain` combined a prompt template, LLM, and output parser into a class.
Some advantages of switching to the LCEL implementation are:
  * Clarity around contents and parameters. The legacy `LLMChain` contains a default output parser and other options.
  * Easier streaming. `LLMChain` only supports streaming via callbacks.
  * Easier access to raw message outputs if desired. `LLMChain` only exposes these via a parameter or via callback.


```
%pip install --upgrade --quiet langchain-openai
```

```
import osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

## Legacy​
Details
```
from langchain.chains import LLMChainfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIprompt = ChatPromptTemplate.from_messages([("user","Tell me a {adjective} joke")],)legacy_chain = LLMChain(llm=ChatOpenAI(), prompt=prompt)legacy_result = legacy_chain({"adjective":"funny"})legacy_result
```

**API Reference:**LLMChain | ChatPromptTemplate | ChatOpenAI
```
{'adjective': 'funny', 'text': "Why couldn't the bicycle stand up by itself?\n\nBecause it was two tired!"}
```

Note that `LLMChain` by default returned a `dict` containing both the input and the output from `StrOutputParser`, so to extract the output, you need to access the `"text"` key.
```
legacy_result["text"]
```

```
"Why couldn't the bicycle stand up by itself?\n\nBecause it was two tired!"
```

## LCEL​
Details
```
from langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIprompt = ChatPromptTemplate.from_messages([("user","Tell me a {adjective} joke")],)chain = prompt | ChatOpenAI()| StrOutputParser()chain.invoke({"adjective":"funny"})
```

**API Reference:**StrOutputParser | ChatPromptTemplate | ChatOpenAI
```
'Why was the math book sad?\n\nBecause it had too many problems.'
```

If you'd like to mimic the `dict` packaging of input and output in `LLMChain`, you can use a `RunnablePassthrough.assign` like:
```
from langchain_core.runnables import RunnablePassthroughouter_chain = RunnablePassthrough().assign(text=chain)outer_chain.invoke({"adjective":"funny"})
```

**API Reference:**RunnablePassthrough
```
{'adjective': 'funny', 'text': 'Why did the scarecrow win an award? Because he was outstanding in his field!'}
```

## Next steps​
See this tutorial for more detail on building with prompt templates, LLMs, and output parsers.
Check out the LCEL conceptual docs for more background information.
#### Was this page helpful?
  * Legacy
  * LCEL
  * Next steps


