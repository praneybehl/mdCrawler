Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
LLMs can summarize and otherwise distill desired information from text, including large volumes of text. In many cases, especially when the amount of text is large compared to the size of the model's context window, it can be helpful (or necessary) to break up the summarization task into smaller components.
Map-reduce represents one class of strategies for accomplishing this. The idea is to break the text into "sub-documents", and first map each sub-document to an individual summary using an LLM. Then, we reduce or consolidate those summaries into a single global summary.
Note that the map step is typically parallelized over the input documents. This strategy is especially effective when understanding of a sub-document does not rely on preceeding context. For example, when summarizing a corpus of many, shorter documents.
LangGraph, built on top of `langchain-core`, suports map-reduce workflows and is well-suited to this problem:
  * LangGraph allows for individual steps (such as successive summarizations) to be streamed, allowing for greater control of execution;
  * LangGraph's checkpointing supports error recovery, extending with human-in-the-loop workflows, and easier incorporation into conversational applications.
  * The LangGraph implementation is straightforward to modify and extend.


Below, we demonstrate how to summarize text via a map-reduce strategy.
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
First we load in our documents. We will use WebBaseLoader to load a blog post, and split the documents into smaller sub-documents.
```
from langchain_community.document_loaders import WebBaseLoaderfrom langchain_text_splitters import CharacterTextSplittertext_splitter = CharacterTextSplitter.from_tiktoken_encoder(  chunk_size=1000, chunk_overlap=0)loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")docs = loader.load()split_docs = text_splitter.split_documents(docs)print(f"Generated {len(split_docs)} documents.")
```

**API Reference:**WebBaseLoader | CharacterTextSplitter
```
Created a chunk of size 1003, which is longer than the specified 1000``````outputGenerated 14 documents.
```

## Create graph​
### Map step​
Let's first define the prompt associated with the map step, and associated it with the LLM via a chain:
```
from langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatemap_prompt = ChatPromptTemplate.from_messages([("human","Write a concise summary of the following:\\n\\n{context}")])map_chain = map_prompt | llm | StrOutputParser()
```

**API Reference:**StrOutputParser | ChatPromptTemplate
### Reduce step​
We also define a chain that takes the document mapping results and reduces them into a single output.
```
reduce_template ="""The following is a set of summaries:{docs}Take these and distill it into a final, consolidated summaryof the main themes."""reduce_prompt = ChatPromptTemplate([("human", reduce_template)])reduce_chain = reduce_prompt | llm | StrOutputParser()
```

### Orchestration via LangGraph​
Below we implement a simple application that maps the summarization step on a list of documents, then reduces them using the above prompts.
Map-reduce flows are particularly useful when texts are long compared to the context window of a LLM. For long texts, we need a mechanism that ensures that the context to be summarized in the reduce step does not exceed a model's context window size. Here we implement a recursive "collapsing" of the summaries: the inputs are partitioned based on a token limit, and summaries are generated of the partitions. This step is repeated until the total length of the summaries is within a desired limit, allowing for the summarization of arbitrary-length text.
We will need to install `langgraph`:
```
pip install -qU langgraph
```

```
import operatorfrom typing import Annotated, List, Literal, TypedDictfrom langchain.chains.combine_documents.reduceimport(  acollapse_docs,  split_list_of_docs,)from langchain_core.documents import Documentfrom langgraph.constants import Sendfrom langgraph.graph import END, START, StateGraphtoken_max =1000deflength_function(documents: List[Document])->int:"""Get number of tokens for input contents."""returnsum(llm.get_num_tokens(doc.page_content)for doc in documents)# This will be the overall state of the main graph.# It will contain the input document contents, corresponding# summaries, and a final summary.classOverallState(TypedDict):# Notice here we use the operator.add# This is because we want combine all the summaries we generate# from individual nodes back into one list - this is essentially# the "reduce" part  contents: List[str]  summaries: Annotated[list, operator.add]  collapsed_summaries: List[Document]  final_summary:str# This will be the state of the node that we will "map" all# documents to in order to generate summariesclassSummaryState(TypedDict):  content:str# Here we generate a summary, given a documentasyncdefgenerate_summary(state: SummaryState):  response =await map_chain.ainvoke(state["content"])return{"summaries":[response]}# Here we define the logic to map out over the documents# We will use this an edge in the graphdefmap_summaries(state: OverallState):# We will return a list of `Send` objects# Each `Send` object consists of the name of a node in the graph# as well as the state to send to that nodereturn[    Send("generate_summary",{"content": content})for content in state["contents"]]defcollect_summaries(state: OverallState):return{"collapsed_summaries":[Document(summary)for summary in state["summaries"]]}# Add node to collapse summariesasyncdefcollapse_summaries(state: OverallState):  doc_lists = split_list_of_docs(    state["collapsed_summaries"], length_function, token_max)  results =[]for doc_list in doc_lists:    results.append(await acollapse_docs(doc_list, reduce_chain.ainvoke))return{"collapsed_summaries": results}# This represents a conditional edge in the graph that determines# if we should collapse the summaries or notdefshould_collapse(  state: OverallState,)-> Literal["collapse_summaries","generate_final_summary"]:  num_tokens = length_function(state["collapsed_summaries"])if num_tokens > token_max:return"collapse_summaries"else:return"generate_final_summary"# Here we will generate the final summaryasyncdefgenerate_final_summary(state: OverallState):  response =await reduce_chain.ainvoke(state["collapsed_summaries"])return{"final_summary": response}# Construct the graph# Nodes:graph = StateGraph(OverallState)graph.add_node("generate_summary", generate_summary)# same as beforegraph.add_node("collect_summaries", collect_summaries)graph.add_node("collapse_summaries", collapse_summaries)graph.add_node("generate_final_summary", generate_final_summary)# Edges:graph.add_conditional_edges(START, map_summaries,["generate_summary"])graph.add_edge("generate_summary","collect_summaries")graph.add_conditional_edges("collect_summaries", should_collapse)graph.add_conditional_edges("collapse_summaries", should_collapse)graph.add_edge("generate_final_summary", END)app = graph.compile()
```

**API Reference:**acollapse_docs | split_list_of_docs | Document | Send | StateGraph
LangGraph allows the graph structure to be plotted to help visualize its function:
```
from IPython.display import ImageImage(app.get_graph().draw_mermaid_png())
```

![](https://python.langchain.com/docs/how_to/summarize_map_reduce/)
## Invoke graph​
When running the application, we can stream the graph to observe its sequence of steps. Below, we will simply print out the name of the step.
Note that because we have a loop in the graph, it can be helpful to specify a recursion_limit on its execution. This will raise a specific error when the specified limit is exceeded.
```
asyncfor step in app.astream({"contents":[doc.page_content for doc in split_docs]},{"recursion_limit":10},):print(list(step.keys()))
```

```
['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['generate_summary']['collect_summaries']['collapse_summaries']['collapse_summaries']['generate_final_summary']
```

```
print(step)
```

```
{'generate_final_summary': {'final_summary': 'The consolidated summary of the main themes from the provided documents highlights the advancements and applications of large language models (LLMs) in artificial intelligence, particularly in autonomous agents and software development. Key themes include:\n\n1. **Integration of LLMs**: LLMs play a crucial role in enabling autonomous agents to perform complex tasks through advanced reasoning and decision-making techniques, such as Chain of Thought (CoT) and Tree of Thoughts.\n\n2. **Memory Management**: The categorization of memory into sensory, short-term, and long-term types parallels machine learning concepts, with short-term memory facilitating in-context learning and long-term memory enhanced by external storage solutions.\n\n3. **Tool Use and APIs**: Autonomous agents utilize external APIs to expand their capabilities, demonstrating adaptability and improved problem-solving skills.\n\n4. **Search Algorithms**: Various approximate nearest neighbor search algorithms, including Locality-Sensitive Hashing (LSH) and FAISS, are discussed for enhancing search efficiency in high-dimensional spaces.\n\n5. **Neuro-Symbolic Architectures**: The integration of neuro-symbolic systems, such as the MRKL framework, combines expert modules with LLMs to improve problem-solving, particularly in complex tasks.\n\n6. **Challenges and Innovations**: The documents address challenges like hallucination and inefficient planning in LLMs, alongside innovative methods such as Chain of Hindsight (CoH) and Algorithm Distillation (AD) for performance enhancement.\n\n7. **Software Development Practices**: The use of LLMs in software development is explored, particularly in creating structured applications like a Super Mario game using the model-view-controller (MVC) architecture, emphasizing task management, component organization, and documentation.\n\n8. **Limitations of LLMs**: Constraints such as finite context length and challenges in long-term planning are acknowledged, along with concerns regarding the reliability of natural language as an interface.\n\nOverall, the integration of LLMs and neuro-symbolic architectures signifies a significant evolution in AI, with ongoing research focused on enhancing planning, memory management, and problem-solving capabilities across various applications.'}}
```

## Next steps​
Check out the LangGraph documentation for detail on building with LangGraph, including this guide on the details of map-reduce in LangGraph.
See the summarization how-to guides for additional summarization strategies, including those designed for larger volumes of text.
See also this tutorial for more detail on summarization.
#### Was this page helpful?
  * Load chat model
  * Load documents
  * Create graph
    * Map step
    * Reduce step
    * Orchestration via LangGraph
  * Invoke graph
  * Next steps


