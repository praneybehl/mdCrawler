Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
StuffDocumentsChain combines documents by concatenating them into a single context window. It is a straightforward and effective strategy for combining documents for question-answering, summarization, and other purposes.
create_stuff_documents_chain is the recommended alternative. It functions the same as `StuffDocumentsChain`, with better support for streaming and batch functionality. Because it is a simple combination of LCEL primitives, it is also easier to extend and incorporate into other LangChain applications.
Below we will go through both `StuffDocumentsChain` and `create_stuff_documents_chain` on a simple example for illustrative purposes.
Let's first load a chat model:
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

## Example​
Let's go through an example where we analyze a set of documents. We first generate some simple documents for illustrative purposes:
```
from langchain_core.documents import Documentdocuments =[  Document(page_content="Apples are red", metadata={"title":"apple_book"}),  Document(page_content="Blueberries are blue", metadata={"title":"blueberry_book"}),  Document(page_content="Bananas are yelow", metadata={"title":"banana_book"}),]
```

**API Reference:**Document
### Legacy​
Details
Below we show an implementation with `StuffDocumentsChain`. We define the prompt template for a summarization task and instantiate a LLMChain object for this purpose. We define how documents are formatted into the prompt and ensure consistency among the keys in the various prompts.
```
from langchain.chains import LLMChain, StuffDocumentsChainfrom langchain_core.prompts import ChatPromptTemplate, PromptTemplate# This controls how each document will be formatted. Specifically,# it will be passed to `format_document` - see that function for more# details.document_prompt = PromptTemplate(  input_variables=["page_content"], template="{page_content}")document_variable_name ="context"# The prompt here should take as an input variable the# `document_variable_name`prompt = ChatPromptTemplate.from_template("Summarize this content: {context}")llm_chain = LLMChain(llm=llm, prompt=prompt)chain = StuffDocumentsChain(  llm_chain=llm_chain,  document_prompt=document_prompt,  document_variable_name=document_variable_name,)
```

**API Reference:**LLMChain | StuffDocumentsChain | ChatPromptTemplate | PromptTemplate
We can now invoke our chain:
```
result = chain.invoke(documents)result["output_text"]
```

```
'This content describes the colors of different fruits: apples are red, blueberries are blue, and bananas are yellow.'
```

```
for chunk in chain.stream(documents):print(chunk)
```

```
{'input_documents': [Document(metadata={'title': 'apple_book'}, page_content='Apples are red'), Document(metadata={'title': 'blueberry_book'}, page_content='Blueberries are blue'), Document(metadata={'title': 'banana_book'}, page_content='Bananas are yelow')], 'output_text': 'This content describes the colors of different fruits: apples are red, blueberries are blue, and bananas are yellow.'}
```

### LCEL​
Details
Below we show an implementation using `create_stuff_documents_chain`:
```
from langchain.chains.combine_documents import create_stuff_documents_chainfrom langchain_core.prompts import ChatPromptTemplateprompt = ChatPromptTemplate.from_template("Summarize this content: {context}")chain = create_stuff_documents_chain(llm, prompt)
```

**API Reference:**create_stuff_documents_chain | ChatPromptTemplate
Invoking the chain, we obtain a similar result as before:
```
result = chain.invoke({"context": documents})result
```

```
'This content describes the colors of different fruits: apples are red, blueberries are blue, and bananas are yellow.'
```

Note that this implementation supports streaming of output tokens:
```
for chunk in chain.stream({"context": documents}):print(chunk, end=" | ")
```

```
 | This | content | describes | the | colors | of | different | fruits | : | apples | are | red | , | blue | berries | are | blue | , | and | bananas | are | yellow | . | |
```

## Next steps​
Check out the LCEL conceptual docs for more background information.
See these how-to guides for more on question-answering tasks with RAG.
See this tutorial for more LLM-based summarization strategies.
#### Was this page helpful?
  * Example
    * Legacy
    * LCEL
  * Next steps


