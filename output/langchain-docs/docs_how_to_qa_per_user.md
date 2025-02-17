Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This guide demonstrates how to configure runtime properties of a retrieval chain. An example application is to limit the documents available to a retriever based on the user.
When building a retrieval app, you often have to build it with multiple users in mind. This means that you may be storing data not just for one user, but for many different users, and they should not be able to see eachother's data. This means that you need to be able to configure your retrieval chain to only retrieve certain information. This generally involves two steps.
**Step 1: Make sure the retriever you are using supports multiple users**
At the moment, there is no unified flag or filter for this in LangChain. Rather, each vectorstore and retriever may have their own, and may be called different things (namespaces, multi-tenancy, etc). For vectorstores, this is generally exposed as a keyword argument that is passed in during `similarity_search`. By reading the documentation or source code, figure out whether the retriever you are using supports multiple users, and, if so, how to use it.
Note: adding documentation and/or support for multiple users for retrievers that do not support it (or document it) is a GREAT way to contribute to LangChain
**Step 2: Add that parameter as a configurable field for the chain**
This will let you easily call the chain and configure any relevant flags at runtime. See this documentation for more information on configuration.
Now, at runtime you can call this chain with configurable field.
## Code Example​
Let's see a concrete example of what this looks like in code. We will use Pinecone for this example.
To configure Pinecone, set the following environment variable:
  * `PINECONE_API_KEY`: Your Pinecone API key


```
from langchain_openai import OpenAIEmbeddingsfrom langchain_pinecone import PineconeVectorStoreembeddings = OpenAIEmbeddings()vectorstore = PineconeVectorStore(index_name="test-example", embedding=embeddings)vectorstore.add_texts(["I worked at Kensho"], namespace="harrison")vectorstore.add_texts(["I worked at Facebook"], namespace="ankush")
```

**API Reference:**OpenAIEmbeddings | PineconeVectorStore
```
['f907aab7-77c7-4347-acc2-6859f8142f92']
```

The pinecone kwarg for `namespace` can be used to separate documents
```
# This will only get documents for Ankushvectorstore.as_retriever(search_kwargs={"namespace":"ankush"}).invoke("where did i work?")
```

```
[Document(id='f907aab7-77c7-4347-acc2-6859f8142f92', metadata={}, page_content='I worked at Facebook')]
```

```
# This will only get documents for Harrisonvectorstore.as_retriever(search_kwargs={"namespace":"harrison"}).invoke("where did i work?")
```

```
[Document(id='16061fc5-c6fc-4f45-a3b3-23469d7996af', metadata={}, page_content='I worked at Kensho')]
```

We can now create the chain that we will use to do question-answering over.
Let's first select a LLM.
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

This will follow the basic implementation from the RAG tutorial, but we will allow the retrieval step to be configurable.
```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import ConfigurableFieldtemplate ="""Answer the question based only on the following context:{context}Question: {question}"""prompt = ChatPromptTemplate.from_template(template)retriever = vectorstore.as_retriever()
```

**API Reference:**ChatPromptTemplate | ConfigurableField
Here we mark the retriever as having a configurable field. All vectorstore retrievers have `search_kwargs` as a field. This is just a dictionary, with vectorstore specific fields.
This will let us pass in a value for `search_kwargs` when invoking the chain.
```
configurable_retriever = retriever.configurable_fields(  search_kwargs=ConfigurableField(id="search_kwargs",    name="Search Kwargs",    description="The search kwargs to use",))
```

We can now create the chain using our configurable retriever.
```
from langchain_core.documents import Documentfrom langchain_core.runnables import RunnableConfigfrom langgraph.graph import START, StateGraphfrom typing_extensions import List, TypedDictclassState(TypedDict):  question:str  context: List[Document]  answer:strdefretrieve(state: State, config: RunnableConfig):  retrieved_docs = configurable_retriever.invoke(state["question"], config)return{"context": retrieved_docs}defgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

**API Reference:**Document | RunnableConfig | StateGraph
```
from IPython.display import Image, displaydisplay(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_per_user/)
We can now invoke the chain with configurable options. `search_kwargs` is the id of the configurable field. The value is the search kwargs to use for Pinecone.
```
result = graph.invoke({"question":"Where did the user work?"},  config={"configurable":{"search_kwargs":{"namespace":"harrison"}}},)result
```

```
{'question': 'Where did the user work?', 'context': [Document(id='16061fc5-c6fc-4f45-a3b3-23469d7996af', metadata={}, page_content='I worked at Kensho')], 'answer': 'The user worked at Kensho.'}
```

```
result = graph.invoke({"question":"Where did the user work?"},  config={"configurable":{"search_kwargs":{"namespace":"ankush"}}},)result
```

```
{'question': 'Where did the user work?', 'context': [Document(id='f907aab7-77c7-4347-acc2-6859f8142f92', metadata={}, page_content='I worked at Facebook')], 'answer': 'The user worked at Facebook.'}
```

For details operating your specific vector store, see the integration pages.
#### Was this page helpful?
  * Code Example


