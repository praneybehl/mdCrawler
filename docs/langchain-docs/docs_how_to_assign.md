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
  * Passing data through


An alternate way of passing data through steps of a chain is to leave the current values of the chain state unchanged while assigning a new value under a given key. The `RunnablePassthrough.assign()` static method takes an input value and adds the extra arguments passed to the assign function.
This is useful in the common LangChain Expression Language pattern of additively creating a dictionary to use as input to a later step.
Here's an example:
```
%pip install --upgrade --quiet langchain langchain-openaiimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

```
from langchain_core.runnables import RunnableParallel, RunnablePassthroughrunnable = RunnableParallel(  extra=RunnablePassthrough.assign(mult=lambda x: x["num"]*3),  modified=lambda x: x["num"]+1,)runnable.invoke({"num":1})
```

**API Reference:**RunnableParallel | RunnablePassthrough
```
{'extra': {'num': 1, 'mult': 3}, 'modified': 2}
```

Let's break down what's happening here.
  * The input to the chain is `{"num": 1}`. This is passed into a `RunnableParallel`, which invokes the runnables it is passed in parallel with that input.
  * The value under the `extra` key is invoked. `RunnablePassthrough.assign()` keeps the original keys in the input dict (`{"num": 1}`), and assigns a new key called `mult`. The value is `lambda x: x["num"] * 3)`, which is `3`. Thus, the result is `{"num": 1, "mult": 3}`.
  * `{"num": 1, "mult": 3}` is returned to the `RunnableParallel` call, and is set as the value to the key `extra`.
  * At the same time, the `modified` key is called. The result is `2`, since the lambda extracts a key called `"num"` from its input and adds one.


Thus, the result is `{'extra': {'num': 1, 'mult': 3}, 'modified': 2}`.
## Streaming​
One convenient feature of this method is that it allows values to pass through as soon as they are available. To show this off, we'll use `RunnablePassthrough.assign()` to immediately return source docs in a retrieval chain:
```
from langchain_community.vectorstores import FAISSfrom langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAI, OpenAIEmbeddingsvectorstore = FAISS.from_texts(["harrison worked at kensho"], embedding=OpenAIEmbeddings())retriever = vectorstore.as_retriever()template ="""Answer the question based only on the following context:{context}Question: {question}"""prompt = ChatPromptTemplate.from_template(template)model = ChatOpenAI()generation_chain = prompt | model | StrOutputParser()retrieval_chain ={"context": retriever,"question": RunnablePassthrough(),}| RunnablePassthrough.assign(output=generation_chain)stream = retrieval_chain.stream("where did harrison work?")for chunk in stream:print(chunk)
```

**API Reference:**FAISS | StrOutputParser | ChatPromptTemplate | RunnablePassthrough | ChatOpenAI | OpenAIEmbeddings
```
{'question': 'where did harrison work?'}{'context': [Document(page_content='harrison worked at kensho')]}{'output': ''}{'output': 'H'}{'output': 'arrison'}{'output': ' worked'}{'output': ' at'}{'output': ' Kens'}{'output': 'ho'}{'output': '.'}{'output': ''}
```

We can see that the first chunk contains the original `"question"` since that is immediately available. The second chunk contains `"context"` since the retriever finishes second. Finally, the output from the `generation_chain` streams in chunks as soon as it is available.
## Next steps​
Now you've learned how to pass data through your chains to help to help format the data flowing through your chains.
To learn more, see the other how-to guides on runnables in this section.
#### Was this page helpful?
  * Streaming
  * Next steps


