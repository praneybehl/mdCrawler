Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
In order to write valid queries against a database, we need to feed the model the table names, table schemas, and feature values for it to query over. When there are many tables, columns, and/or high-cardinality columns, it becomes impossible for us to dump the full information about our database in every prompt. Instead, we must find ways to dynamically insert into the prompt only the most relevant information.
In this guide we demonstrate methods for identifying such relevant information, and feeding this into a query-generation step. We will cover:
  1. Identifying a relevant subset of tables;
  2. Identifying a relevant subset of column values.


## Setup​
First, get required packages and set environment variables:
```
%pip install --upgrade --quiet langchain langchain-community langchain-openai
```

```
# Uncomment the below to use LangSmith. Not required.# import os# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()# os.environ["LANGSMITH_TRACING"] = "true"
```

The below example will use a SQLite connection with Chinook database. Follow these installation steps to create `Chinook.db` in the same directory as this notebook:
  * Save this file as `Chinook_Sqlite.sql`
  * Run `sqlite3 Chinook.db`
  * Run `.read Chinook_Sqlite.sql`
  * Test `SELECT * FROM Artist LIMIT 10;`


Now, `Chinook.db` is in our directory and we can interface with it using the SQLAlchemy-driven SQLDatabase class:
```
from langchain_community.utilities import SQLDatabasedb = SQLDatabase.from_uri("sqlite:///Chinook.db")print(db.dialect)print(db.get_usable_table_names())print(db.run("SELECT * FROM Artist LIMIT 10;"))
```

**API Reference:**SQLDatabase
```
sqlite['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track'][(1, 'AC/DC'), (2, 'Accept'), (3, 'Aerosmith'), (4, 'Alanis Morissette'), (5, 'Alice In Chains'), (6, 'Antônio Carlos Jobim'), (7, 'Apocalyptica'), (8, 'Audioslave'), (9, 'BackBeat'), (10, 'Billy Cobham')]
```

## Many tables​
One of the main pieces of information we need to include in our prompt is the schemas of the relevant tables. When we have very many tables, we can't fit all of the schemas in a single prompt. What we can do in such cases is first extract the names of the tables related to the user input, and then include only their schemas.
One easy and reliable way to do this is using tool-calling. Below, we show how we can use this feature to obtain output conforming to a desired format (in this case, a list of table names). We use the chat model's `.bind_tools` method to bind a tool in Pydantic format, and feed this into an output parser to reconstruct the object from the model's response.
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

```
from langchain_core.output_parsers.openai_tools import PydanticToolsParserfrom langchain_core.prompts import ChatPromptTemplatefrom pydantic import BaseModel, FieldclassTable(BaseModel):"""Table in SQL database."""  name:str= Field(description="Name of table in SQL database.")table_names ="\n".join(db.get_usable_table_names())system =f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \The tables are:{table_names}Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{input}"),])llm_with_tools = llm.bind_tools([Table])output_parser = PydanticToolsParser(tools=[Table])table_chain = prompt | llm_with_tools | output_parsertable_chain.invoke({"input":"What are all the genres of Alanis Morisette songs"})
```

**API Reference:**PydanticToolsParser | ChatPromptTemplate
```
[Table(name='Genre')]
```

This works pretty well! Except, as we'll see below, we actually need a few other tables as well. This would be pretty difficult for the model to know based just on the user question. In this case, we might think to simplify our model's job by grouping the tables together. We'll just ask the model to choose between categories "Music" and "Business", and then take care of selecting all the relevant tables from there:
```
system ="""Return the names of any SQL tables that are relevant to the user question.The tables are:MusicBusiness"""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{input}"),])category_chain = prompt | llm_with_tools | output_parsercategory_chain.invoke({"input":"What are all the genres of Alanis Morisette songs"})
```

```
[Table(name='Music'), Table(name='Business')]
```

```
from typing import Listdefget_tables(categories: List[Table])-> List[str]:  tables =[]for category in categories:if category.name =="Music":      tables.extend(["Album","Artist","Genre","MediaType","Playlist","PlaylistTrack","Track",])elif category.name =="Business":      tables.extend(["Customer","Employee","Invoice","InvoiceLine"])return tablestable_chain = category_chain | get_tablestable_chain.invoke({"input":"What are all the genres of Alanis Morisette songs"})
```

```
['Album', 'Artist', 'Genre', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track', 'Customer', 'Employee', 'Invoice', 'InvoiceLine']
```

Now that we've got a chain that can output the relevant tables for any query we can combine this with our create_sql_query_chain, which can accept a list of `table_names_to_use` to determine which table schemas are included in the prompt:
```
from operator import itemgetterfrom langchain.chains import create_sql_query_chainfrom langchain_core.runnables import RunnablePassthroughquery_chain = create_sql_query_chain(llm, db)# Convert "question" key to the "input" key expected by current table_chain.table_chain ={"input": itemgetter("question")}| table_chain# Set table_names_to_use using table_chain.full_chain = RunnablePassthrough.assign(table_names_to_use=table_chain)| query_chain
```

**API Reference:**create_sql_query_chain | RunnablePassthrough
```
query = full_chain.invoke({"question":"What are all the genres of Alanis Morisette songs"})print(query)
```

```
SELECT DISTINCT "g"."Name"FROM "Genre" gJOIN "Track" t ON "g"."GenreId" = "t"."GenreId"JOIN "Album" a ON "t"."AlbumId" = "a"."AlbumId"JOIN "Artist" ar ON "a"."ArtistId" = "ar"."ArtistId"WHERE "ar"."Name" = 'Alanis Morissette'LIMIT 5;
```

```
db.run(query)
```

```
"[('Rock',)]"
```

We can see the LangSmith trace for this run here.
We've seen how to dynamically include a subset of table schemas in a prompt within a chain. Another possible approach to this problem is to let an Agent decide for itself when to look up tables by giving it a Tool to do so. You can see an example of this in the SQL: Agents guide.
## High-cardinality columns​
In order to filter columns that contain proper nouns such as addresses, song names or artists, we first need to double-check the spelling in order to filter the data correctly.
One naive strategy it to create a vector store with all the distinct proper nouns that exist in the database. We can then query that vector store each user input and inject the most relevant proper nouns into the prompt.
First we need the unique values for each entity we want, for which we define a function that parses the result into a list of elements:
```
import astimport redefquery_as_list(db, query):  res = db.run(query)  res =[el for sub in ast.literal_eval(res)for el in sub if el]  res =[re.sub(r"\b\d+\b","", string).strip()for string in res]return resproper_nouns = query_as_list(db,"SELECT Name FROM Artist")proper_nouns += query_as_list(db,"SELECT Title FROM Album")proper_nouns += query_as_list(db,"SELECT Name FROM Genre")len(proper_nouns)proper_nouns[:5]
```

```
['AC/DC', 'Accept', 'Aerosmith', 'Alanis Morissette', 'Alice In Chains']
```

Now we can embed and store all of our values in a vector database:
```
from langchain_community.vectorstores import FAISSfrom langchain_openai import OpenAIEmbeddingsvector_db = FAISS.from_texts(proper_nouns, OpenAIEmbeddings())retriever = vector_db.as_retriever(search_kwargs={"k":15})
```

**API Reference:**FAISS | OpenAIEmbeddings
And put together a query construction chain that first retrieves values from the database and inserts them into the prompt:
```
from operator import itemgetterfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import RunnablePassthroughsystem ="""You are a SQLite expert. Given an input question, create a syntacticallycorrect SQLite query to run. Unless otherwise specificed, do not return more than{top_k} rows.Only return the SQL query with no markup or explanation.Here is the relevant table info: {table_info}Here is a non-exhaustive list of possible feature values. If filtering on a featurevalue make sure to check its spelling against this list first:{proper_nouns}"""prompt = ChatPromptTemplate.from_messages([("system", system),("human","{input}")])query_chain = create_sql_query_chain(llm, db, prompt=prompt)retriever_chain =(  itemgetter("question")| retriever|(lambda docs:"\n".join(doc.page_content for doc in docs)))chain = RunnablePassthrough.assign(proper_nouns=retriever_chain)| query_chain
```

**API Reference:**ChatPromptTemplate | RunnablePassthrough
To try out our chain, let's see what happens when we try filtering on "elenis moriset", a misspelling of Alanis Morissette, without and with retrieval:
```
# Without retrievalquery = query_chain.invoke({"question":"What are all the genres of elenis moriset songs","proper_nouns":""})print(query)db.run(query)
```

```
SELECT DISTINCT g.Name FROM Track tJOIN Album a ON t.AlbumId = a.AlbumIdJOIN Artist ar ON a.ArtistId = ar.ArtistIdJOIN Genre g ON t.GenreId = g.GenreIdWHERE ar.Name = 'Elenis Moriset';
```

```
''
```

```
# Without retrievalquery = query_chain.invoke({"question":"What are all the genres of elenis moriset songs","proper_nouns":""})print(query)db.run(query)
```

```
SELECT DISTINCT Genre.NameFROM GenreJOIN Track ON Genre.GenreId = Track.GenreIdJOIN Album ON Track.AlbumId = Album.AlbumIdJOIN Artist ON Album.ArtistId = Artist.ArtistIdWHERE Artist.Name = 'Elenis Moriset'
```

```
''
```

```
# With retrievalquery = chain.invoke({"question":"What are all the genres of elenis moriset songs"})print(query)db.run(query)
```

```
SELECT DISTINCT g.NameFROM Genre gJOIN Track t ON g.GenreId = t.GenreIdJOIN Album a ON t.AlbumId = a.AlbumIdJOIN Artist ar ON a.ArtistId = ar.ArtistIdWHERE ar.Name = 'Alanis Morissette';
```

```
"[('Rock',)]"
```

We can see that with retrieval we're able to correct the spelling from "Elenis Moriset" to "Alanis Morissette" and get back a valid result.
Another possible approach to this problem is to let an Agent decide for itself when to look up proper nouns. You can see an example of this in the SQL: Agents guide.
#### Was this page helpful?
  * Setup
  * Many tables
  * High-cardinality columns


