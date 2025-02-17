Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Sometimes, a query analysis technique may allow for selection of which retriever to use. To use this, you will need to add some logic to select the retriever to do. We will show a simple example (using mock data) of how to do that.
## Setup​
#### Install dependencies​
```
%pip install -qU langchain langchain-community langchain-openai langchain-chroma
```

```
Note: you may need to restart the kernel to use updated packages.
```

#### Set environment variables​
We'll use OpenAI in this example:
```
import getpassimport osif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass.getpass()# Optional, uncomment to trace runs with LangSmith. Sign up here: https://smith.langchain.com.# os.environ["LANGSMITH_TRACING"] = "true"# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
```

### Create Index​
We will create a vectorstore over fake information.
```
from langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsfrom langchain_text_splitters import RecursiveCharacterTextSplittertexts =["Harrison worked at Kensho"]embeddings = OpenAIEmbeddings(model="text-embedding-3-small")vectorstore = Chroma.from_texts(texts, embeddings, collection_name="harrison")retriever_harrison = vectorstore.as_retriever(search_kwargs={"k":1})texts =["Ankush worked at Facebook"]embeddings = OpenAIEmbeddings(model="text-embedding-3-small")vectorstore = Chroma.from_texts(texts, embeddings, collection_name="ankush")retriever_ankush = vectorstore.as_retriever(search_kwargs={"k":1})
```

**API Reference:**OpenAIEmbeddings | RecursiveCharacterTextSplitter
## Query analysis​
We will use function calling to structure the output. We will let it return multiple queries.
```
from typing import List, Optionalfrom pydantic import BaseModel, FieldclassSearch(BaseModel):"""Search for information about a person."""  query:str= Field(...,    description="Query to look up",)  person:str= Field(...,    description="Person to look things up for. Should be `HARRISON` or `ANKUSH`.",)
```

```
from langchain_core.output_parsers.openai_tools import PydanticToolsParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAIoutput_parser = PydanticToolsParser(tools=[Search])system ="""You have the ability to issue search queries to get information to help answer user information."""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)structured_llm = llm.with_structured_output(Search)query_analyzer ={"question": RunnablePassthrough()}| prompt | structured_llm
```

**API Reference:**PydanticToolsParser | ChatPromptTemplate | RunnablePassthrough | ChatOpenAI
We can see that this allows for routing between retrievers
```
query_analyzer.invoke("where did Harrison Work")
```

```
Search(query='work history', person='HARRISON')
```

```
query_analyzer.invoke("where did ankush Work")
```

```
Search(query='work history', person='ANKUSH')
```

## Retrieval with query analysis​
So how would we include this in a chain? We just need some simple logic to select the retriever and pass in the search query
```
from langchain_core.runnables import chain
```

**API Reference:**chain
```
retrievers ={"HARRISON": retriever_harrison,"ANKUSH": retriever_ankush,}
```

```
@chaindefcustom_chain(question):  response = query_analyzer.invoke(question)  retriever = retrievers[response.person]return retriever.invoke(response.query)
```

```
custom_chain.invoke("where did Harrison Work")
```

```
[Document(page_content='Harrison worked at Kensho')]
```

```
custom_chain.invoke("where did ankush Work")
```

```
[Document(page_content='Ankush worked at Facebook')]
```

#### Was this page helpful?
  * Setup
    * Create Index
  * Query analysis
  * Retrieval with query analysis


