Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Sometimes, a query analysis technique may allow for multiple queries to be generated. In these cases, we need to remember to run all queries and then to combine the results. We will show a simple example (using mock data) of how to do that.
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
from langchain_chroma import Chromafrom langchain_openai import OpenAIEmbeddingsfrom langchain_text_splitters import RecursiveCharacterTextSplittertexts =["Harrison worked at Kensho","Ankush worked at Facebook"]embeddings = OpenAIEmbeddings(model="text-embedding-3-small")vectorstore = Chroma.from_texts(  texts,  embeddings,)retriever = vectorstore.as_retriever(search_kwargs={"k":1})
```

**API Reference:**OpenAIEmbeddings | RecursiveCharacterTextSplitter
## Query analysis​
We will use function calling to structure the output. We will let it return multiple queries.
```
from typing import List, Optionalfrom pydantic import BaseModel, FieldclassSearch(BaseModel):"""Search over a database of job records."""  queries: List[str]= Field(...,    description="Distinct queries to search for",)
```

```
from langchain_core.output_parsers.openai_tools import PydanticToolsParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughfrom langchain_openai import ChatOpenAIoutput_parser = PydanticToolsParser(tools=[Search])system ="""You have the ability to issue search queries to get information to help answer user information.If you need to look up two distinct pieces of information, you are allowed to do that!"""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{question}"),])llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)structured_llm = llm.with_structured_output(Search)query_analyzer ={"question": RunnablePassthrough()}| prompt | structured_llm
```

**API Reference:**PydanticToolsParser | ChatPromptTemplate | RunnablePassthrough | ChatOpenAI
We can see that this allows for creating multiple queries
```
query_analyzer.invoke("where did Harrison Work")
```

```
Search(queries=['Harrison Work', 'Harrison employment history'])
```

```
query_analyzer.invoke("where did Harrison and ankush Work")
```

```
Search(queries=['Harrison work history', 'Ankush work history'])
```

## Retrieval with query analysis​
So how would we include this in a chain? One thing that will make this a lot easier is if we call our retriever asyncronously - this will let us loop over the queries and not get blocked on the response time.
```
from langchain_core.runnables import chain
```

**API Reference:**chain
```
@chainasyncdefcustom_chain(question):  response =await query_analyzer.ainvoke(question)  docs =[]for query in response.queries:    new_docs =await retriever.ainvoke(query)    docs.extend(new_docs)# You probably want to think about reranking or deduplicating documents here# But that is a separate topicreturn docs
```

```
await custom_chain.ainvoke("where did Harrison Work")
```

```
[Document(page_content='Harrison worked at Kensho'), Document(page_content='Harrison worked at Kensho')]
```

```
await custom_chain.ainvoke("where did Harrison and ankush Work")
```

```
[Document(page_content='Harrison worked at Kensho'), Document(page_content='Ankush worked at Facebook')]
```

#### Was this page helpful?
  * Setup
    * Create Index
  * Query analysis
  * Retrieval with query analysis


