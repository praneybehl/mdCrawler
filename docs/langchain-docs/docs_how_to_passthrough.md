Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Expression Language (LCEL)
  * Chaining runnables
  * Calling runnables in parallel
  * Custom functions


When composing chains with several steps, sometimes you will want to pass data from previous steps unchanged for use as input to a later step. The `RunnablePassthrough` class allows you to do just this, and is typically is used in conjunction with a RunnableParallel to pass data through to a later step in your constructed chains.
See the example below:
```
%pip install -qU langchain langchain-openaiimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

```
from langchain_core.runnables import RunnableParallel, RunnablePassthroughrunnable = RunnableParallel(  passed=RunnablePassthrough(),  modified=lambda x: x["num"]+1,)runnable.invoke({"num":1})
```

**API Reference:**RunnableParallel | RunnablePassthrough
```
{'passed': {'num': 1}, 'modified': 2}
```

As seen above, `passed` key was called with `RunnablePassthrough()` and so it simply passed on `{'num': 1}`.
We also set a second key in the map with `modified`. This uses a lambda to set a single value adding 1 to the num, which resulted in `modified` key with the value of `2`.
## Retrieval Example​
In the example below, we see a more real-world use case where we use `RunnablePassthrough` along with `RunnableParallel` in a chain to properly format inputs to a prompt:
```
from langchain_community.vectorstores import FAISSfrom langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAI, OpenAIEmbeddingsvectorstore = FAISS.from_texts(["harrison worked at kensho"], embedding=OpenAIEmbeddings())retriever = vectorstore.as_retriever()template ="""Answer the question based only on the following context:{context}Question: {question}"""prompt = ChatPromptTemplate.from_template(template)model = ChatOpenAI()retrieval_chain =({"context": retriever,"question": RunnablePassthrough()}| prompt| model| StrOutputParser())retrieval_chain.invoke("where did harrison work?")
```

**API Reference:**FAISS | StrOutputParser | ChatPromptTemplate | RunnablePassthrough | ChatOpenAI | OpenAIEmbeddings
```
'Harrison worked at Kensho.'
```

Here the input to prompt is expected to be a map with keys "context" and "question". The user input is just the question. So we need to get the context using our retriever and passthrough the user input under the "question" key. The `RunnablePassthrough` allows us to pass on the user's question to the prompt and model.
## Next steps​
Now you've learned how to pass data through your chains to help format the data flowing through your chains.
To learn more, see the other how-to guides on runnables in this section.
#### Was this page helpful?
  * Retrieval Example
  * Next steps


