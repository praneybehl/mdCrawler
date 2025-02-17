Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This guide explains how to stream results from a RAG application. It covers streaming tokens from the final output as well as intermediate steps of a chain (e.g., from query re-writing).
We'll work off of the Q&A app with sources we built over the LLM Powered Autonomous Agents blog post by Lilian Weng in the RAG tutorial.
## Setup​
### Dependencies​
We'll use the following packages:
```
%pip install --upgrade --quiet langchain langchain-community langchainhub beautifulsoup4
```

### LangSmith​
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.
Note that LangSmith is not needed, but it is helpful. If you do want to use LangSmith, after you sign up at the link above, make sure to set your environment variables to start logging traces:
```
os.environ["LANGSMITH_TRACING"]="true"os.environ["LANGSMITH_API_KEY"]= getpass.getpass()
```

### Components​
We will need to select three components from LangChain's suite of integrations.
A chat model:
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

An embedding model:
Select embeddings model:
OpenAI▾
* OpenAI
* Azure
* Google
* AWS
* HuggingFace
* Ollama
* Cohere
* MistralAI
* Nomic
* NVIDIA
* Voyage AI
* IBM watsonx
* Fake
```
pip install -qU langchain-openai
```

```
import getpassimport osifnot os.environ.get("OPENAI_API_KEY"): os.environ["OPENAI_API_KEY"]= getpass.getpass("Enter API key for OpenAI: ")from langchain_openai import OpenAIEmbeddingsembeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

And a vector store:
Select vector store:
In-memory▾
* In-memory
* AstraDB
* Chroma
* FAISS
* Milvus
* MongoDB
* PGVector
* Pinecone
* Qdrant
```
pip install -qU langchain-core
```

```
from langchain_core.vectorstores import InMemoryVectorStorevector_store = InMemoryVectorStore(embeddings)
```

## RAG application​
Let's reconstruct the Q&A app with sources we built over the LLM Powered Autonomous Agents blog post by Lilian Weng in the RAG tutorial.
First we index our documents:
```
import bs4from langchain import hubfrom langchain_community.document_loaders import WebBaseLoaderfrom langchain_core.documents import Documentfrom langchain_text_splitters import RecursiveCharacterTextSplitterfrom typing_extensions import List, TypedDict# Load and chunk contents of the blogloader = WebBaseLoader(  web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),  bs_kwargs=dict(    parse_only=bs4.SoupStrainer(      class_=("post-content","post-title","post-header"))),)docs = loader.load()text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)all_splits = text_splitter.split_documents(docs)
```

**API Reference:**hub | WebBaseLoader | Document | RecursiveCharacterTextSplitter
```
# Index chunks_ = vector_store.add_documents(documents=all_splits)
```

Next we build the application:
```
from langchain import hubfrom langchain_core.documents import Documentfrom langgraph.graph import START, StateGraphfrom typing_extensions import List, TypedDict# Define prompt for question-answeringprompt = hub.pull("rlm/rag-prompt")# Define state for applicationclassState(TypedDict):  question:str  context: List[Document]  answer:str# Define application stepsdefretrieve(state: State):  retrieved_docs = vector_store.similarity_search(state["question"])return{"context": retrieved_docs}defgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}# Compile application and testgraph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

**API Reference:**hub | Document | StateGraph
```
from IPython.display import Image, displaydisplay(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_streaming/)
## Streaming final outputs​
LangGraph supports several streaming modes, which can be controlled by specifying the `stream_mode` parameter. Setting `stream_mode="messages"` allows us to stream tokens from chat model invocations.
In general there can be multiple chat model invocations in an application (although here there is just one). Below, we filter to only the last step using the name of the corresponding node:
```
input_message ="What is Task Decomposition?"for message, metadata in graph.stream({"question":"What is Task Decomposition?"},  stream_mode="messages",):if metadata["langgraph_node"]=="generate":print(message.content, end="|")
```

```
|Task| De|composition| is| a| technique| used| to| break| down| complex| tasks| into| smaller|,| more| manageable| steps|.| It| often| involves| prompting| models| to| "|think| step| by| step|,"| allowing| for| clearer| reasoning| and| better| performance| on| intricate| problems|.| This| can| be| achieved| through| various| methods|,| including| simple| prompts|,| task|-specific| instructions|,| or| human| input|.||
```

## Streaming intermediate steps​
Other streaming modes will generally stream steps from our invocation-- i.e., state updates from individual nodes. In this case, each node is just appending a new key to the state:
```
for step in graph.stream({"question":"What is Task Decomposition?"},  stream_mode="updates",):print(f"{step}\n\n----------------\n")
```

```
{'retrieve': {'context': [Document(id='5bf5e308-6ccb-4f09-94d2-d0c36b8c9980', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.'), Document(id='d8aed221-7943-414d-8ed7-63c2b0e7523b', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.'), Document(id='bfa87007-02ef-4f81-a008-4522ecea1025', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Resources:\n1. Internet access for searches and information gathering.\n2. Long Term memory management.\n3. GPT-3.5 powered Agents for delegation of simple tasks.\n4. File output.\n\nPerformance Evaluation:\n1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.\n2. Constructively self-criticize your big-picture behavior constantly.\n3. Reflect on past decisions and strategies to refine your approach.\n4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.'), Document(id='6aff7fc0-5c21-4986-9f1e-91e89715d934', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content="(3) Task execution: Expert models execute on the specific tasks and log results.\nInstruction:\n\nWith the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.")]}}----------------{'generate': {'answer': 'Task Decomposition is the process of breaking down a complex task into smaller, manageable steps to enhance understanding and execution. Techniques like Chain of Thought (CoT) and Tree of Thoughts (ToT) guide models to think through steps systematically, allowing for better problem-solving. It can be achieved through simple prompting, task-specific instructions, or human input.'}}----------------
```

For more on streaming with LangGraph, check out its streaming documentation. For more information on streaming individual LangChain Runnables, refer to this guide.
#### Was this page helpful?
  * Setup
    * Dependencies
    * LangSmith
    * Components
  * RAG application
  * Streaming final outputs
  * Streaming intermediate steps


