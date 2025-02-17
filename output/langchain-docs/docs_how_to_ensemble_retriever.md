Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The EnsembleRetriever supports ensembling of results from multiple retrievers. It is initialized with a list of BaseRetriever objects. EnsembleRetrievers rerank the results of the constituent retrievers based on the Reciprocal Rank Fusion algorithm.
By leveraging the strengths of different algorithms, the `EnsembleRetriever` can achieve better performance than any single algorithm.
The most common pattern is to combine a sparse retriever (like BM25) with a dense retriever (like embedding similarity), because their strengths are complementary. It is also known as "hybrid search". The sparse retriever is good at finding relevant documents based on keywords, while the dense retriever is good at finding relevant documents based on semantic similarity.
## Basic usage​
Below we demonstrate ensembling of a BM25Retriever with a retriever derived from the FAISS vector store.
```
%pip install --upgrade --quiet rank_bm25 >/dev/null
```

```
from langchain.retrievers import EnsembleRetrieverfrom langchain_community.retrievers import BM25Retrieverfrom langchain_community.vectorstores import FAISSfrom langchain_openai import OpenAIEmbeddingsdoc_list_1 =["I like apples","I like oranges","Apples and oranges are fruits",]# initialize the bm25 retriever and faiss retrieverbm25_retriever = BM25Retriever.from_texts(  doc_list_1, metadatas=[{"source":1}]*len(doc_list_1))bm25_retriever.k =2doc_list_2 =["You like apples","You like oranges",]embedding = OpenAIEmbeddings()faiss_vectorstore = FAISS.from_texts(  doc_list_2, embedding, metadatas=[{"source":2}]*len(doc_list_2))faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k":2})# initialize the ensemble retrieverensemble_retriever = EnsembleRetriever(  retrievers=[bm25_retriever, faiss_retriever], weights=[0.5,0.5])
```

**API Reference:**EnsembleRetriever | BM25Retriever | FAISS | OpenAIEmbeddings
```
docs = ensemble_retriever.invoke("apples")docs
```

```
[Document(page_content='I like apples', metadata={'source': 1}), Document(page_content='You like apples', metadata={'source': 2}), Document(page_content='Apples and oranges are fruits', metadata={'source': 1}), Document(page_content='You like oranges', metadata={'source': 2})]
```

## Runtime Configuration​
We can also configure the individual retrievers at runtime using configurable fields. Below we update the "top-k" parameter for the FAISS retriever specifically:
```
from langchain_core.runnables import ConfigurableFieldfaiss_retriever = faiss_vectorstore.as_retriever(  search_kwargs={"k":2}).configurable_fields(  search_kwargs=ConfigurableField(id="search_kwargs_faiss",    name="Search Kwargs",    description="The search kwargs to use",))ensemble_retriever = EnsembleRetriever(  retrievers=[bm25_retriever, faiss_retriever], weights=[0.5,0.5])
```

**API Reference:**ConfigurableField
```
config ={"configurable":{"search_kwargs_faiss":{"k":1}}}docs = ensemble_retriever.invoke("apples", config=config)docs
```

```
[Document(page_content='I like apples', metadata={'source': 1}), Document(page_content='You like apples', metadata={'source': 2}), Document(page_content='Apples and oranges are fruits', metadata={'source': 1})]
```

Notice that this only returns one source from the FAISS retriever, because we pass in the relevant configuration at run time
#### Was this page helpful?
  * Basic usage
  * Runtime Configuration


