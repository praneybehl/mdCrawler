Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * LangChain Expression Language (LCEL)
  * Chaining runnables


Once you create a runnable with LangChain Expression Language, you may often want to inspect it to get a better sense for what is going on. This notebook covers some methods for doing so.
This guide shows some ways you can programmatically introspect the internal steps of chains. If you are instead interested in debugging issues in your chain, see this section instead.
First, let's create an example chain. We will create one that does retrieval:
```
%pip install -qU langchain langchain-openai faiss-cpu tiktoken
```

```
from langchain_community.vectorstores import FAISSfrom langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAI, OpenAIEmbeddingsvectorstore = FAISS.from_texts(["harrison worked at kensho"], embedding=OpenAIEmbeddings())retriever = vectorstore.as_retriever()template ="""Answer the question based only on the following context:{context}Question: {question}"""prompt = ChatPromptTemplate.from_template(template)model = ChatOpenAI()chain =({"context": retriever,"question": RunnablePassthrough()}| prompt| model| StrOutputParser())
```

**API Reference:**FAISS | StrOutputParser | ChatPromptTemplate | RunnablePassthrough | ChatOpenAI | OpenAIEmbeddings
## Get a graph​
You can use the `get_graph()` method to get a graph representation of the runnable:
```
chain.get_graph()
```

## Print a graph​
While that is not super legible, you can use the `print_ascii()` method to show that graph in a way that's easier to understand:
```
chain.get_graph().print_ascii()
```

```
      +---------------------------------+           | Parallel<context,question>Input |           +---------------------------------+               **        **                 ***          ***               **             **      +----------------------+       +-------------+ | VectorStoreRetriever |       | Passthrough | +----------------------+       +-------------+           **        **                   ***     ***                      **   **                 +----------------------------------+          | Parallel<context,question>Output |          +----------------------------------+                   *                            *                            *                      +--------------------+                 | ChatPromptTemplate |                 +--------------------+                       *                            *                            *                        +------------+                     | ChatOpenAI |                     +------------+                         *                            *                            *                       +-----------------+                   | StrOutputParser |                   +-----------------+                        *                            *                            *                     +-----------------------+               | StrOutputParserOutput |               +-----------------------+
```

## Get the prompts​
You may want to see just the prompts that are used in a chain with the `get_prompts()` method:
```
chain.get_prompts()
```

```
[ChatPromptTemplate(input_variables=['context', 'question'], messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], template='Answer the question based only on the following context:\n{context}\n\nQuestion: {question}\n'))])]
```

## Next steps​
You've now learned how to introspect your composed LCEL chains.
Next, check out the other how-to guides on runnables in this section, or the related how-to guide on debugging your chains.
#### Was this page helpful?
  * Get a graph
  * Print a graph
  * Get the prompts
  * Next steps


