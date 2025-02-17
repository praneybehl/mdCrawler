Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This retriever uses a combination of semantic similarity and a time decay.
The algorithm for scoring them is:
```
semantic_similarity + (1.0 - decay_rate) ^ hours_passed
```

Notably, `hours_passed` refers to the hours passed since the object in the retriever **was last accessed** , not since it was created. This means that frequently accessed objects remain "fresh".
```
from datetime import datetime, timedeltaimport faissfrom langchain.retrievers import TimeWeightedVectorStoreRetrieverfrom langchain_community.docstore import InMemoryDocstorefrom langchain_community.vectorstores import FAISSfrom langchain_core.documents import Documentfrom langchain_openai import OpenAIEmbeddings
```

**API Reference:**TimeWeightedVectorStoreRetriever | InMemoryDocstore | FAISS | Document | OpenAIEmbeddings
## Low decay rate​
A low `decay rate` (in this, to be extreme, we will set it close to 0) means memories will be "remembered" for longer. A `decay rate` of 0 means memories never be forgotten, making this retriever equivalent to the vector lookup.
```
# Define your embedding modelembeddings_model = OpenAIEmbeddings()# Initialize the vectorstore as emptyembedding_size =1536index = faiss.IndexFlatL2(embedding_size)vectorstore = FAISS(embeddings_model, index, InMemoryDocstore({}),{})retriever = TimeWeightedVectorStoreRetriever(  vectorstore=vectorstore, decay_rate=0.0000000000000000000000001, k=1)
```

```
yesterday = datetime.now()- timedelta(days=1)retriever.add_documents([Document(page_content="hello world", metadata={"last_accessed_at": yesterday})])retriever.add_documents([Document(page_content="hello foo")])
```

```
['73679bc9-d425-49c2-9d74-de6356c73489']
```

```
# "Hello World" is returned first because it is most salient, and the decay rate is close to 0., meaning it's still recent enoughretriever.invoke("hello world")
```

```
[Document(metadata={'last_accessed_at': datetime.datetime(2024, 10, 22, 16, 37, 40, 818583), 'created_at': datetime.datetime(2024, 10, 22, 16, 37, 37, 975074), 'buffer_idx': 0}, page_content='hello world')]
```

## High decay rate​
With a high `decay rate` (e.g., several 9's), the `recency score` quickly goes to 0! If you set this all the way to 1, `recency` is 0 for all objects, once again making this equivalent to a vector lookup.
```
# Define your embedding modelembeddings_model = OpenAIEmbeddings()# Initialize the vectorstore as emptyembedding_size =1536index = faiss.IndexFlatL2(embedding_size)vectorstore = FAISS(embeddings_model, index, InMemoryDocstore({}),{})retriever = TimeWeightedVectorStoreRetriever(  vectorstore=vectorstore, decay_rate=0.999, k=1)
```

```
yesterday = datetime.now()- timedelta(days=1)retriever.add_documents([Document(page_content="hello world", metadata={"last_accessed_at": yesterday})])retriever.add_documents([Document(page_content="hello foo")])
```

```
['379631f0-42c2-4773-8cc2-d36201e1e610']
```

```
# "Hello Foo" is returned first because "hello world" is mostly forgottenretriever.invoke("hello world")
```

```
[Document(metadata={'last_accessed_at': datetime.datetime(2024, 10, 22, 16, 37, 46, 553633), 'created_at': datetime.datetime(2024, 10, 22, 16, 37, 43, 927429), 'buffer_idx': 1}, page_content='hello foo')]
```

## Virtual time​
Using some utils in LangChain, you can mock out the time component.
```
from langchain_core.utils import mock_now
```

**API Reference:**mock_now
```
# Notice the last access time is that date timetomorrow = datetime.now()+ timedelta(days=1)with mock_now(tomorrow):print(retriever.invoke("hello world"))
```

```
[Document(metadata={'last_accessed_at': MockDateTime(2024, 10, 23, 16, 38, 19, 66711), 'created_at': datetime.datetime(2024, 10, 22, 16, 37, 43, 599877), 'buffer_idx': 0}, page_content='hello world')]
```

#### Was this page helpful?
  * Low decay rate
  * High decay rate
  * Virtual time


