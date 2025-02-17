Skip to content 
# Self-RAG¶
Self-RAG is a strategy for RAG that incorporates self-reflection / self-grading on retrieved documents and generations. 
In the paper, a few decisions are made:
  1. Should I retrieve from retriever, `R` -
  2. Input: `x (question)` OR `x (question)`, `y (generation)`
  3. Decides when to retrieve `D` chunks with `R`
  4. Output: `yes, no, continue`
  5. Are the retrieved passages `D` relevant to the question `x` -
  6.      * Input: (`x (question)`, `d (chunk)`) for `d` in `D`
  7. `d` provides useful information to solve `x`
  8. Output: `relevant, irrelevant`
  9. Are the LLM generation from each chunk in `D` is relevant to the chunk (hallucinations, etc) -
  10. Input: `x (question)`, `d (chunk)`, `y (generation)` for `d` in `D`
  11. All of the verification-worthy statements in `y (generation)` are supported by `d`
  12. Output: `{fully supported, partially supported, no support`
  13. The LLM generation from each chunk in `D` is a useful response to `x (question)` -
  14. Input: `x (question)`, `y (generation)` for `d` in `D`
  15. `y (generation)` is a useful response to `x (question)`.
  16. Output: `{5, 4, 3, 2, 1}`


We will implement some of these ideas from scratch using LangGraph.
![Screenshot 2024-04-01 at 12.41.50 PM.png](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag/)
## Setup¶
First let's install our required packages and set our API keys
```
%pip install -U langchain_community tiktoken langchain-openai langchainhub chromadb langchain langgraph

```

```
importgetpass
importos


def_set_env(key: str):
  if key not in os.environ:
    os.environ[key] = getpass.getpass(f"{key}:")


_set_env("OPENAI_API_KEY")

```

Set up LangSmith for LangGraph development
Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started here. 
## Retriever¶
Let's index 3 blog posts.
```
fromlangchain.text_splitterimport RecursiveCharacterTextSplitter
fromlangchain_community.document_loadersimport WebBaseLoader
fromlangchain_community.vectorstoresimport Chroma
fromlangchain_openaiimport OpenAIEmbeddings

urls = [
  "https://lilianweng.github.io/posts/2023-06-23-agent/",
  "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
  "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_list)

# Add to vectorDB
vectorstore = Chroma.from_documents(
  documents=doc_splits,
  collection_name="rag-chroma",
  embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()

```

API Reference: RecursiveCharacterTextSplitter | WebBaseLoader | Chroma | OpenAIEmbeddings
## LLMs¶
Using Pydantic with LangChain
This notebook uses Pydantic v2 `BaseModel`, which requires `langchain-core >= 0.3`. Using `langchain-core < 0.3` will result in errors due to mixing of Pydantic v1 and v2 `BaseModels`. 
```
### Retrieval Grader


fromlangchain_core.promptsimport ChatPromptTemplate
fromlangchain_openaiimport ChatOpenAI

frompydanticimport BaseModel, Field


# Data model
classGradeDocuments(BaseModel):
"""Binary score for relevance check on retrieved documents."""

  binary_score: str = Field(
    description="Documents are relevant to the question, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeDocuments)

# Prompt
system = """You are a grader assessing relevance of a retrieved document to a user question. \n
  It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
  If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n
  Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "Retrieved document: \n\n{document}\n\n User question: {question}"),
  ]
)

retrieval_grader = grade_prompt | structured_llm_grader
question = "agent memory"
docs = retriever.invoke(question)
doc_txt = docs[1].page_content
print(retrieval_grader.invoke({"question": question, "document": doc_txt}))

```

API Reference: ChatPromptTemplate | ChatOpenAI
```
binary_score='no'

```

```
### Generate

fromlangchainimport hub
fromlangchain_core.output_parsersimport StrOutputParser

# Prompt
prompt = hub.pull("rlm/rag-prompt")

# LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


# Post-processing
defformat_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)


# Chain
rag_chain = prompt | llm | StrOutputParser()

# Run
generation = rag_chain.invoke({"context": docs, "question": question})
print(generation)

```

API Reference: StrOutputParser
```
The design of generative agents combines LLM with memory, planning, and reflection mechanisms to enable agents to behave conditioned on past experience. Memory stream is a long-term memory module that records a comprehensive list of agents' experience in natural language. LLM functions as the agent's brain in an autonomous agent system.

```

```
### Hallucination Grader


# Data model
classGradeHallucinations(BaseModel):
"""Binary score for hallucination present in generation answer."""

  binary_score: str = Field(
    description="Answer is grounded in the facts, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeHallucinations)

# Prompt
system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n
   Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
hallucination_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "Set of facts: \n\n{documents}\n\n LLM generation: {generation}"),
  ]
)

hallucination_grader = hallucination_prompt | structured_llm_grader
hallucination_grader.invoke({"documents": docs, "generation": generation})

```

```
GradeHallucinations(binary_score='yes')

```

```
### Answer Grader


# Data model
classGradeAnswer(BaseModel):
"""Binary score to assess answer addresses question."""

  binary_score: str = Field(
    description="Answer addresses the question, 'yes' or 'no'"
  )


# LLM with function call
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)

# Prompt
system = """You are a grader assessing whether an answer addresses / resolves a question \n
   Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
answer_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    ("human", "User question: \n\n{question}\n\n LLM generation: {generation}"),
  ]
)

answer_grader = answer_prompt | structured_llm_grader
answer_grader.invoke({"question": question, "generation": generation})

```

```
GradeAnswer(binary_score='yes')

```

```
### Question Re-writer

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt
system = """You a question re-writer that converts an input question to a better version that is optimized \n
   for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""
re_write_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", system),
    (
      "human",
      "Here is the initial question: \n\n{question}\n Formulate an improved question.",
    ),
  ]
)

question_rewriter = re_write_prompt | llm | StrOutputParser()
question_rewriter.invoke({"question": question})

```

```
"What is the role of memory in an agent's functioning?"

```

# Graph¶
Capture the flow in as a graph.
## Graph state¶
```
fromtypingimport List

fromtyping_extensionsimport TypedDict


classGraphState(TypedDict):
"""
  Represents the state of our graph.

  Attributes:
    question: question
    generation: LLM generation
    documents: list of documents
  """

  question: str
  generation: str
  documents: List[str]

```

```
### Nodes


defretrieve(state):
"""
  Retrieve documents

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): New key added to state, documents, that contains retrieved documents
  """
  print("---RETRIEVE---")
  question = state["question"]

  # Retrieval
  documents = retriever.invoke(question)
  return {"documents": documents, "question": question}


defgenerate(state):
"""
  Generate answer

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): New key added to state, generation, that contains LLM generation
  """
  print("---GENERATE---")
  question = state["question"]
  documents = state["documents"]

  # RAG generation
  generation = rag_chain.invoke({"context": documents, "question": question})
  return {"documents": documents, "question": question, "generation": generation}


defgrade_documents(state):
"""
  Determines whether the retrieved documents are relevant to the question.

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): Updates documents key with only filtered relevant documents
  """

  print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
  question = state["question"]
  documents = state["documents"]

  # Score each doc
  filtered_docs = []
  for d in documents:
    score = retrieval_grader.invoke(
      {"question": question, "document": d.page_content}
    )
    grade = score.binary_score
    if grade == "yes":
      print("---GRADE: DOCUMENT RELEVANT---")
      filtered_docs.append(d)
    else:
      print("---GRADE: DOCUMENT NOT RELEVANT---")
      continue
  return {"documents": filtered_docs, "question": question}


deftransform_query(state):
"""
  Transform the query to produce a better question.

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): Updates question key with a re-phrased question
  """

  print("---TRANSFORM QUERY---")
  question = state["question"]
  documents = state["documents"]

  # Re-write question
  better_question = question_rewriter.invoke({"question": question})
  return {"documents": documents, "question": better_question}


### Edges


defdecide_to_generate(state):
"""
  Determines whether to generate an answer, or re-generate a question.

  Args:
    state (dict): The current graph state

  Returns:
    str: Binary decision for next node to call
  """

  print("---ASSESS GRADED DOCUMENTS---")
  state["question"]
  filtered_documents = state["documents"]

  if not filtered_documents:
    # All documents have been filtered check_relevance
    # We will re-generate a new query
    print(
      "---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---"
    )
    return "transform_query"
  else:
    # We have relevant documents, so generate answer
    print("---DECISION: GENERATE---")
    return "generate"


defgrade_generation_v_documents_and_question(state):
"""
  Determines whether the generation is grounded in the document and answers question.

  Args:
    state (dict): The current graph state

  Returns:
    str: Decision for next node to call
  """

  print("---CHECK HALLUCINATIONS---")
  question = state["question"]
  documents = state["documents"]
  generation = state["generation"]

  score = hallucination_grader.invoke(
    {"documents": documents, "generation": generation}
  )
  grade = score.binary_score

  # Check hallucination
  if grade == "yes":
    print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
    # Check question-answering
    print("---GRADE GENERATION vs QUESTION---")
    score = answer_grader.invoke({"question": question, "generation": generation})
    grade = score.binary_score
    if grade == "yes":
      print("---DECISION: GENERATION ADDRESSES QUESTION---")
      return "useful"
    else:
      print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
      return "not useful"
  else:
    pprint("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
    return "not supported"

```

## Build Graph¶
The just follows the flow we outlined in the figure above.
```
fromlanggraph.graphimport END, StateGraph, START

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("retrieve", retrieve) # retrieve
workflow.add_node("grade_documents", grade_documents) # grade documents
workflow.add_node("generate", generate) # generatae
workflow.add_node("transform_query", transform_query) # transform_query

# Build graph
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
  "grade_documents",
  decide_to_generate,
  {
    "transform_query": "transform_query",
    "generate": "generate",
  },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_conditional_edges(
  "generate",
  grade_generation_v_documents_and_question,
  {
    "not supported": "generate",
    "useful": END,
    "not useful": "transform_query",
  },
)

# Compile
app = workflow.compile()

```

API Reference: END | StateGraph | START
```
frompprintimport pprint

# Run
inputs = {"question": "Explain how the different types of agent memory work?"}
for output in app.stream(inputs):
  for key, value in output.items():
    # Node
    pprint(f"Node '{key}':")
    # Optional: print full state at each node
    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
  pprint("\n---\n")

# Final generation
pprint(value["generation"])

```

```
---RETRIEVE---
"Node 'retrieve':"
'\n---\n'
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---ASSESS GRADED DOCUMENTS---
---DECISION: GENERATE---
"Node 'grade_documents':"
'\n---\n'
---GENERATE---
---CHECK HALLUCINATIONS---
---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
---GRADE GENERATION vs QUESTION---
---DECISION: GENERATION ADDRESSES QUESTION---
"Node 'generate':"
'\n---\n'
('Short-term memory is used for in-context learning in agents, allowing them '
 'to learn quickly. Long-term memory enables agents to retain and recall vast '
 'amounts of information over extended periods. Agents can also utilize '
 'external tools like APIs to access additional information beyond what is '
 'stored in their memory.')

```

```
inputs = {"question": "Explain how chain of thought prompting works?"}
for output in app.stream(inputs):
  for key, value in output.items():
    # Node
    pprint(f"Node '{key}':")
    # Optional: print full state at each node
    # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
  pprint("\n---\n")

# Final generation
pprint(value["generation"])

```

```
---RETRIEVE---
"Node 'retrieve':"
'\n---\n'
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT NOT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---ASSESS GRADED DOCUMENTS---
---DECISION: GENERATE---
"Node 'grade_documents':"
'\n---\n'
---GENERATE---
---CHECK HALLUCINATIONS---
---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---
---GRADE GENERATION vs QUESTION---
---DECISION: GENERATION ADDRESSES QUESTION---
"Node 'generate':"
'\n---\n'
('Chain of thought prompting works by repeatedly prompting the model to ask '
 'follow-up questions to construct the thought process iteratively. This '
 'method can be combined with queries to search for relevant entities and '
 'content to add back into the context. It extends the thought process by '
 'exploring multiple reasoning possibilities at each step, creating a tree '
 'structure of thoughts.')

```

Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! Please help us improve this page by adding to the discussion below. 
## Comments
Back to top 
