Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Often in Q&A applications it's important to show users the sources that were used to generate the answer. The simplest way to do this is for the chain to return the Documents that were retrieved in each generation.
We'll work off of the Q&A app we built over the LLM Powered Autonomous Agents blog post by Lilian Weng in the RAG tutorial.
We will cover two approaches:
  1. Using the basic RAG chain covered in Part 1 of the RAG tutorial;
  2. Using a conversational RAG chain as convered in Part 2 of the tutorial.


We will also show how to structure sources into the model response, such that a model can report what specific sources it used in generating its answer.
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

![](https://python.langchain.com/docs/how_to/qa_sources/)
Because we're tracking the retrieved context in our application's state, it is accessible after invoking the application:
```
result = graph.invoke({"question":"What is Task Decomposition?"})print(f'Context: {result["context"]}\n\n')print(f'Answer: {result["answer"]}')
```

```
Context: [Document(id='c8471b37-07d8-4d51-856e-4b2c22bca88d', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.'), Document(id='acb7eb6f-f252-4353-aec2-f459135354ba', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.'), Document(id='4fae6668-7fec-4237-9b2d-78132f4f3f3f', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Resources:\n1. Internet access for searches and information gathering.\n2. Long Term memory management.\n3. GPT-3.5 powered Agents for delegation of simple tasks.\n4. File output.\n\nPerformance Evaluation:\n1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.\n2. Constructively self-criticize your big-picture behavior constantly.\n3. Reflect on past decisions and strategies to refine your approach.\n4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.'), Document(id='3c79dd86-595e-42e8-b64d-404780f9e2d9', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content="(3) Task execution: Expert models execute on the specific tasks and log results.\nInstruction:\n\nWith the input and the inference results, the AI assistant needs to describe the process and results. The previous stages can be formed as - User Input: {{ User Input }}, Task Planning: {{ Tasks }}, Model Selection: {{ Model Assignment }}, Task Execution: {{ Predictions }}. You must first answer the user's request in a straightforward manner. Then describe the task process and show your analysis and model inference results to the user in the first person. If inference results contain a file path, must tell the user the complete file path.")]Answer: Task Decomposition is the process of breaking down a complex task into smaller, manageable steps to facilitate execution. This can be achieved through techniques like Chain of Thought, which encourages step-by-step reasoning, or Tree of Thoughts, which explores multiple reasoning paths for each step. It can be implemented using simple prompts, specific instructions, or human input to effectively tackle the original task.
```

Here, `"context"` contains the sources that the LLM used in generating the response in `"answer"`.
## Structure sources in model response​
Up to this point, we've simply propagated the documents returned from the retrieval step through to the final response. But this may not illustrate what subset of information the model relied on when generating its answer. Below, we show how to structure sources into the model response, allowing the model to report what specific context it relied on for its answer.
It is straightforward to extend the above LangGraph implementation. Below, we make a simple change: we use the model's tool-calling features to generate structured output, consisting of an answer and list of sources. The schema for the response is represented in the `AnswerWithSources` TypedDict, below.
```
from typing import Listfrom typing_extensions import Annotated, TypedDict# Desired schema for responseclassAnswerWithSources(TypedDict):"""An answer to the question, with sources."""  answer:str  sources: Annotated[    List[str],...,"List of sources (author + year) used to answer the question",]classState(TypedDict):  question:str  context: List[Document]  answer: AnswerWithSourcesdefgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  structured_llm = llm.with_structured_output(AnswerWithSources)  response = structured_llm.invoke(messages)return{"answer": response}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

```
import jsonresult = graph.invoke({"question":"What is Chain of Thought?"})print(json.dumps(result["answer"], indent=2))
```

```
{ "answer": "Chain of Thought (CoT) is a prompting technique that enhances model performance by instructing it to think step by step, allowing the decomposition of complex tasks into smaller, manageable steps. This method not only aids in task execution but also provides insights into the model's reasoning process. CoT has become a standard approach in improving how language models handle intricate problem-solving tasks.", "sources": [  "Wei et al. 2022" ]}
```

tip
View LangSmith trace.
## Conversational RAG​
Part 2 of the RAG tutorial implements a different architecture, in which steps in the RAG flow are represented via successive message objects. This leverages additional tool-calling features of chat models, and more naturally accommodates a "back-and-forth" conversational user experience.
In that tutorial (and below), we propagate the retrieved documents as artifacts on the tool messages. That makes it easy to pluck out the retrieved documents. Below, we add them as an additional key in the state, for convenience.
Note that we define the response format of the tool as `"content_and_artifact"`:
```
from langchain_core.tools import tool@tool(response_format="content_and_artifact")defretrieve(query:str):"""Retrieve information related to a query."""  retrieved_docs = vector_store.similarity_search(query, k=2)  serialized ="\n\n".join((f"Source: {doc.metadata}\n"f"Content: {doc.page_content}")for doc in retrieved_docs)return serialized, retrieved_docs
```

**API Reference:**tool
We can now build and compile the exact same application as in Part 2 of the RAG tutorial, with two changes:
  1. We add a `context` key of the state to store retrieved documents;
  2. In the `generate` step, we pluck out the retrieved documents and populate them in the state.


These changes are highlighted below.
```
from langchain_core.messages import SystemMessagefrom langgraph.graph import END, MessagesState, StateGraphfrom langgraph.prebuilt import ToolNode, tools_conditionclassState(MessagesState):  context: List[Document]# Step 1: Generate an AIMessage that may include a tool-call to be sent.defquery_or_respond(state: State):"""Generate tool call for retrieval or respond."""  llm_with_tools = llm.bind_tools([retrieve])  response = llm_with_tools.invoke(state["messages"])# MessagesState appends messages to state instead of overwritingreturn{"messages":[response]}# Step 2: Execute the retrieval.tools = ToolNode([retrieve])# Step 3: Generate a response using the retrieved content.defgenerate(state: MessagesState):"""Generate answer."""# Get generated ToolMessages  recent_tool_messages =[]for message inreversed(state["messages"]):if message.type=="tool":      recent_tool_messages.append(message)else:break  tool_messages = recent_tool_messages[::-1]# Format into prompt  docs_content ="\n\n".join(doc.content for doc in tool_messages)  system_message_content =("You are an assistant for question-answering tasks. ""Use the following pieces of retrieved context to answer ""the question. If you don't know the answer, say that you ""don't know. Use three sentences maximum and keep the ""answer concise.""\n\n"f"{docs_content}")  conversation_messages =[    messagefor message in state["messages"]if message.typein("human","system")or(message.type=="ai"andnot message.tool_calls)]  prompt =[SystemMessage(system_message_content)]+ conversation_messages# Run  response = llm.invoke(prompt)  context =[]for tool_message in tool_messages:    context.extend(tool_message.artifact)return{"messages":[response],"context": context}
```

**API Reference:**SystemMessage | StateGraph | ToolNode | tools_condition
We can compile the application as before:
```
graph_builder = StateGraph(MessagesState)graph_builder.add_node(query_or_respond)graph_builder.add_node(tools)graph_builder.add_node(generate)graph_builder.set_entry_point("query_or_respond")graph_builder.add_conditional_edges("query_or_respond",  tools_condition,{END: END,"tools":"tools"},)graph_builder.add_edge("tools","generate")graph_builder.add_edge("generate", END)graph = graph_builder.compile()
```

```
display(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_sources/)
Invoking our application, we see that the retrieved Document objects are accessible from the application state.
```
input_message ="What is Task Decomposition?"for step in graph.stream({"messages":[{"role":"user","content": input_message}]},  stream_mode="values",):  step["messages"][-1].pretty_print()
```

```
================================[1m Human Message [0m=================================What is Task Decomposition?==================================[1m Ai Message [0m==================================Tool Calls: retrieve (call_oA0XZ5hF70X0oW4ccNUFCFxX) Call ID: call_oA0XZ5hF70X0oW4ccNUFCFxX Args:  query: Task Decomposition=================================[1m Tool Message [0m=================================Name: retrieveSource: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Fig. 1. Overview of a LLM-powered autonomous agent system.Component One: Planning#A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.Task Decomposition#Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}Content: Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.==================================[1m Ai Message [0m==================================Task Decomposition is the process of breaking down a complicated task into smaller, manageable steps. It often utilizes techniques like Chain of Thought (CoT) prompting, which encourages models to think step by step, enhancing performance on complex tasks. This approach helps clarify the model's reasoning and makes it easier to tackle difficult problems.
```

```
step["context"]
```

```
[Document(id='c8471b37-07d8-4d51-856e-4b2c22bca88d', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Fig. 1. Overview of a LLM-powered autonomous agent system.\nComponent One: Planning#\nA complicated task usually involves many steps. An agent needs to know what they are and plan ahead.\nTask Decomposition#\nChain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard tasks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an interpretation of the model’s thinking process.'), Document(id='acb7eb6f-f252-4353-aec2-f459135354ba', metadata={'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}, page_content='Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.\nTask decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.')]
```

tip
Check out the LangSmith trace.
#### Was this page helpful?
  * Setup
    * Dependencies
    * LangSmith
    * Components
  * RAG application
  * Structure sources in model response
  * Conversational RAG


