Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
When working with files, like PDFs, you're likely to encounter text that exceeds your language model's context window. To process this text, consider these strategies:
  1. **Change LLM** Choose a different LLM that supports a larger context window.
  2. **Brute Force** Chunk the document, and extract content from each chunk.
  3. **RAG** Chunk the document, index the chunks, and only extract content from a subset of chunks that look "relevant".


Keep in mind that these strategies have different trade off and the best strategy likely depends on the application that you're designing!
This guide demonstrates how to implement strategies 2 and 3.
## Setup​
First we'll install the dependencies needed for this guide:
```
%pip install -qU langchain-community lxml faiss-cpu langchain-openai
```

```
Note: you may need to restart the kernel to use updated packages.
```

Now we need some example data! Let's download an article about cars from wikipedia and load it as a LangChain Document.
```
import reimport requestsfrom langchain_community.document_loaders import BSHTMLLoader# Download the contentresponse = requests.get("https://en.wikipedia.org/wiki/Car")# Write it to a filewithopen("car.html","w", encoding="utf-8")as f:  f.write(response.text)# Load it with an HTML parserloader = BSHTMLLoader("car.html")document = loader.load()[0]# Clean up code# Replace consecutive new lines with a single new linedocument.page_content = re.sub("\n\n+","\n", document.page_content)
```

**API Reference:**BSHTMLLoader
```
print(len(document.page_content))
```

```
78865
```

## Define the schema​
Following the extraction tutorial, we will use Pydantic to define the schema of information we wish to extract. In this case, we will extract a list of "key developments" (e.g., important historical events) that include a year and description.
Note that we also include an `evidence` key and instruct the model to provide in verbatim the relevant sentences of text from the article. This allows us to compare the extraction results to (the model's reconstruction of) text from the original document.
```
from typing import List, Optionalfrom langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderfrom pydantic import BaseModel, FieldclassKeyDevelopment(BaseModel):"""Information about a development in the history of cars."""  year:int= Field(..., description="The year when there was an important historic development.")  description:str= Field(..., description="What happened in this year? What was the development?")  evidence:str= Field(...,    description="Repeat in verbatim the sentence(s) from which the year and description information were extracted",)classExtractionData(BaseModel):"""Extracted information about key developments in the history of cars."""  key_developments: List[KeyDevelopment]# Define a custom prompt to provide instructions and any additional context.# 1) You can add examples into the prompt template to improve extraction quality# 2) Introduce additional parameters to take context into account (e.g., include metadata#  about the document from which the text was extracted.)prompt = ChatPromptTemplate.from_messages([("system","You are an expert at identifying key historic development in text. ""Only extract important historic developments. Extract nothing if no important information can be found in the text.",),("human","{text}"),])
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder
## Create an extractor​
Let's select an LLM. Because we are using tool-calling, we will need a model that supports a tool-calling feature. See this table for available LLMs.
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
extractor = prompt | llm.with_structured_output(  schema=ExtractionData,  include_raw=False,)
```

## Brute force approach​
Split the documents into chunks such that each chunk fits into the context window of the LLMs.
```
from langchain_text_splitters import TokenTextSplittertext_splitter = TokenTextSplitter(# Controls the size of each chunk  chunk_size=2000,# Controls overlap between chunks  chunk_overlap=20,)texts = text_splitter.split_text(document.page_content)
```

**API Reference:**TokenTextSplitter
Use batch functionality to run the extraction in **parallel** across each chunk!
tip
You can often use .batch() to parallelize the extractions! `.batch` uses a threadpool under the hood to help you parallelize workloads.
If your model is exposed via an API, this will likely speed up your extraction flow!
```
# Limit just to the first 3 chunks# so the code can be re-run quicklyfirst_few = texts[:3]extractions = extractor.batch([{"text": text}for text in first_few],{"max_concurrency":5},# limit the concurrency by passing max concurrency!)
```

### Merge results​
After extracting data from across the chunks, we'll want to merge the extractions together.
```
key_developments =[]for extraction in extractions:  key_developments.extend(extraction.key_developments)key_developments[:10]
```

```
[KeyDevelopment(year=1769, description='Nicolas-Joseph Cugnot built the first steam-powered road vehicle.', evidence='The French inventor Nicolas-Joseph Cugnot built the first steam-powered road vehicle in 1769, while the Swiss inventor François Isaac de Rivaz designed and constructed the first internal combustion-powered automobile in 1808.'), KeyDevelopment(year=1808, description='François Isaac de Rivaz designed and constructed the first internal combustion-powered automobile.', evidence='The French inventor Nicolas-Joseph Cugnot built the first steam-powered road vehicle in 1769, while the Swiss inventor François Isaac de Rivaz designed and constructed the first internal combustion-powered automobile in 1808.'), KeyDevelopment(year=1886, description='Carl Benz invented the modern car, a practical, marketable automobile for everyday use, and patented his Benz Patent-Motorwagen.', evidence='The modern car—a practical, marketable automobile for everyday use—was invented in 1886, when the German inventor Carl Benz patented his Benz Patent-Motorwagen.'), KeyDevelopment(year=1901, description='The Oldsmobile Curved Dash became the first mass-produced car.', evidence='The 1901 Oldsmobile Curved Dash and the 1908 Ford Model T, both American cars, are widely considered the first mass-produced[3][4] and mass-affordable[5][6][7] cars, respectively.'), KeyDevelopment(year=1908, description='The Ford Model T became the first mass-affordable car.', evidence='The 1901 Oldsmobile Curved Dash and the 1908 Ford Model T, both American cars, are widely considered the first mass-produced[3][4] and mass-affordable[5][6][7] cars, respectively.'), KeyDevelopment(year=1885, description='Carl Benz built the original Benz Patent-Motorwagen, the first modern car.', evidence='The original Benz Patent-Motorwagen, the first modern car, built in 1885 and awarded the patent for the concept'), KeyDevelopment(year=1881, description='Gustave Trouvé demonstrated a three-wheeled car powered by electricity.', evidence='In November 1881, French inventor Gustave Trouvé demonstrated a three-wheeled car powered by electricity at the International Exposition of Electricity.'), KeyDevelopment(year=1888, description="Bertha Benz undertook the first road trip by car to prove the road-worthiness of her husband's invention.", evidence="In August 1888, Bertha Benz, the wife and business partner of Carl Benz, undertook the first road trip by car, to prove the road-worthiness of her husband's invention."), KeyDevelopment(year=1896, description='Benz designed and patented the first internal-combustion flat engine, called boxermotor.', evidence='In 1896, Benz designed and patented the first internal-combustion flat engine, called boxermotor.'), KeyDevelopment(year=1897, description='The first motor car in central Europe and one of the first factory-made cars in the world was produced by Czech company Nesselsdorfer Wagenbau (later renamed to Tatra), the Präsident automobil.', evidence='The first motor car in central Europe and one of the first factory-made cars in the world, was produced by Czech company Nesselsdorfer Wagenbau (later renamed to Tatra) in 1897, the Präsident automobil.')]
```

## RAG based approach​
Another simple idea is to chunk up the text, but instead of extracting information from every chunk, just focus on the the most relevant chunks.
caution
It can be difficult to identify which chunks are relevant.
For example, in the `car` article we're using here, most of the article contains key development information. So by using **RAG** , we'll likely be throwing out a lot of relevant information.
We suggest experimenting with your use case and determining whether this approach works or not.
To implement the RAG based approach:
  1. Chunk up your document(s) and index them (e.g., in a vectorstore);
  2. Prepend the `extractor` chain with a retrieval step using the vectorstore.


Here's a simple example that relies on the `FAISS` vectorstore.
```
from langchain_community.vectorstores import FAISSfrom langchain_core.documents import Documentfrom langchain_core.runnables import RunnableLambdafrom langchain_openai import OpenAIEmbeddingsfrom langchain_text_splitters import CharacterTextSplittertexts = text_splitter.split_text(document.page_content)vectorstore = FAISS.from_texts(texts, embedding=OpenAIEmbeddings())retriever = vectorstore.as_retriever(  search_kwargs={"k":1})# Only extract from first document
```

**API Reference:**FAISS | Document | RunnableLambda | OpenAIEmbeddings | CharacterTextSplitter
In this case the RAG extractor is only looking at the top document.
```
rag_extractor ={"text": retriever |(lambda docs: docs[0].page_content)# fetch content of top doc}| extractor
```

```
results = rag_extractor.invoke("Key developments associated with cars")
```

```
for key_development in results.key_developments:print(key_development)
```

```
year=2006 description='Car-sharing services in the US experienced double-digit growth in revenue and membership.' evidence='in the US, some car-sharing services have experienced double-digit growth in revenue and membership growth between 2006 and 2007.'year=2020 description='56 million cars were manufactured worldwide, with China producing the most.' evidence='In 2020, there were 56 million cars manufactured worldwide, down from 67 million the previous year. The automotive industry in China produces by far the most (20 million in 2020).'
```

## Common issues​
Different methods have their own pros and cons related to cost, speed, and accuracy.
Watch out for these issues:
  * Chunking content means that the LLM can fail to extract information if the information is spread across multiple chunks.
  * Large chunk overlap may cause the same information to be extracted twice, so be prepared to de-duplicate!
  * LLMs can make up data. If looking for a single fact across a large text and using a brute force approach, you may end up getting more made up data.


#### Was this page helpful?
  * Setup
  * Define the schema
  * Create an extractor
  * Brute force approach
    * Merge results
  * RAG based approach
  * Common issues


