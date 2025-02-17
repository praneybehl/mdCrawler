Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
LLMs can summarize and otherwise distill desired information from text, including large volumes of text. In many cases, especially for models with larger context windows, this can be adequately achieved via a single LLM call.
LangChain implements a simple pre-built chain that "stuffs" a prompt with the desired context for summarization and other purposes. In this guide we demonstrate how to use the chain.
## Load chat model​
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

## Load documents​
Next, we need some documents to summarize. Below, we generate some toy documents for illustrative purposes. See the document loader how-to guides and integration pages for additional sources of data. The summarization tutorial also includes an example summarizing a blog post.
```
from langchain_core.documents import Documentdocuments =[  Document(page_content="Apples are red", metadata={"title":"apple_book"}),  Document(page_content="Blueberries are blue", metadata={"title":"blueberry_book"}),  Document(page_content="Bananas are yelow", metadata={"title":"banana_book"}),]
```

**API Reference:**Document
## Load chain​
Below, we define a simple prompt and instantiate the chain with our chat model and documents:
```
from langchain.chains.combine_documents import create_stuff_documents_chainfrom langchain_core.prompts import ChatPromptTemplateprompt = ChatPromptTemplate.from_template("Summarize this content: {context}")chain = create_stuff_documents_chain(llm, prompt)
```

**API Reference:**create_stuff_documents_chain | ChatPromptTemplate
## Invoke chain​
Because the chain is a Runnable, it implements the usual methods for invocation:
```
result = chain.invoke({"context": documents})result
```

```
'The content describes the colors of three fruits: apples are red, blueberries are blue, and bananas are yellow.'
```

### Streaming​
Note that the chain also supports streaming of individual output tokens:
```
for chunk in chain.stream({"context": documents}):print(chunk, end="|")
```

```
|The| content| describes| the| colors| of| three| fruits|:| apples| are| red|,| blueberries| are| blue|,| and| bananas| are| yellow|.||
```

## Next steps​
See the summarization how-to guides for additional summarization strategies, including those designed for larger volumes of text.
See also this tutorial for more detail on summarization.
#### Was this page helpful?
  * Load chat model
  * Load documents
  * Load chain
  * Invoke chain
    * Streaming
  * Next steps


