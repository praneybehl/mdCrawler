Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This guide reviews methods to get a model to cite which parts of the source documents it referenced in generating its response.
We will cover five methods:
  1. Using tool-calling to cite document IDs;
  2. Using tool-calling to cite documents IDs and provide text snippets;
  3. Direct prompting;
  4. Retrieval post-processing (i.e., compressing the retrieved context to make it more relevant);
  5. Generation post-processing (i.e., issuing a second LLM call to annotate a generated answer with citations).


We generally suggest using the first item of the list that works for your use-case. That is, if your model supports tool-calling, try methods 1 or 2; otherwise, or if those fail, advance down the list.
Let's first create a simple RAG chain. To start we'll just retrieve from Wikipedia using the WikipediaRetriever. We will use the same LangGraph implementation from the RAG Tutorial.
## Setup​
First we'll need to install some dependencies:
```
%pip install -qU langchain-community wikipedia
```

Let's first select a LLM:
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

We can now load a retriever and construct our prompt:
```
from langchain_community.retrievers import WikipediaRetrieverfrom langchain_core.prompts import ChatPromptTemplatesystem_prompt =("You're a helpful AI assistant. Given a user question ""and some Wikipedia article snippets, answer the user ""question. If none of the articles answer the question, ""just say you don't know.""\n\nHere are the Wikipedia articles: ""{context}")retriever = WikipediaRetriever(top_k_results=6, doc_content_chars_max=2000)prompt = ChatPromptTemplate.from_messages([("system", system_prompt),("human","{question}"),])prompt.pretty_print()
```

**API Reference:**WikipediaRetriever | ChatPromptTemplate
```
================================[1m System Message [0m================================You're a helpful AI assistant. Given a user question and some Wikipedia article snippets, answer the user question. If none of the articles answer the question, just say you don't know.Here are the Wikipedia articles: [33;1m[1;3m{context}[0m================================[1m Human Message [0m=================================[33;1m[1;3m{question}[0m
```

Now that we've got a model, retriver and prompt, let's chain them all together. Following the how-to guide on adding citations to a RAG application, we'll make it so our chain returns both the answer and the retrieved Documents. This uses the same LangGraph implementation as in the RAG Tutorial.
```
from langchain_core.documents import Documentfrom langgraph.graph import START, StateGraphfrom typing_extensions import List, TypedDict# Define state for applicationclassState(TypedDict):  question:str  context: List[Document]  answer:str# Define application stepsdefretrieve(state: State):  retrieved_docs = retriever.invoke(state["question"])return{"context": retrieved_docs}defgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}# Compile application and testgraph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

**API Reference:**Document | StateGraph
```
from IPython.display import Image, displaydisplay(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_citations/)
```
result = graph.invoke({"question":"How fast are cheetahs?"})sources =[doc.metadata["source"]for doc in result["context"]]print(f"Sources: {sources}\n\n")print(f'Answer: {result["answer"]}')
```

```
Sources: ['https://en.wikipedia.org/wiki/Cheetah', 'https://en.wikipedia.org/wiki/Southeast_African_cheetah', 'https://en.wikipedia.org/wiki/Footspeed', 'https://en.wikipedia.org/wiki/Fastest_animals', 'https://en.wikipedia.org/wiki/Pursuit_predation', 'https://en.wikipedia.org/wiki/Gepard-class_fast_attack_craft']Answer: Cheetahs are capable of running at speeds between 93 to 104 km/h (58 to 65 mph).
```

Check out the LangSmith trace.
## Tool-calling​
If your LLM of choice implements a tool-calling feature, you can use it to make the model specify which of the provided documents it's referencing when generating its answer. LangChain tool-calling models implement a `.with_structured_output` method which will force generation adhering to a desired schema (see details here).
### Cite documents​
To cite documents using an identifier, we format the identifiers into the prompt, then use `.with_structured_output` to coerce the LLM to reference these identifiers in its output.
First we define a schema for the output. The `.with_structured_output` supports multiple formats, including JSON schema and Pydantic. Here we will use Pydantic:
```
from pydantic import BaseModel, FieldclassCitedAnswer(BaseModel):"""Answer the user question based only on the given sources, and cite the sources used."""  answer:str= Field(...,    description="The answer to the user question, which is based only on the given sources.",)  citations: List[int]= Field(...,    description="The integer IDs of the SPECIFIC sources which justify the answer.",)
```

Let's see what the model output is like when we pass in our functions and a user input:
```
structured_llm = llm.with_structured_output(CitedAnswer)example_q ="""What Brian's height?Source: 1Information: Suzy is 6'2"Source: 2Information: Jeremiah is blondeSource: 3Information: Brian is 3 inches shorter than Suzy"""result = structured_llm.invoke(example_q)result
```

```
CitedAnswer(answer='Brian is 5\'11".', citations=[1, 3])
```

Or as a dict:
```
result.dict()
```

```
{'answer': 'Brian is 5\'11".', 'citations': [1, 3]}
```

Now we structure the source identifiers into the prompt to replicate with our chain. We will make three changes:
  1. Update the prompt to include source identifiers;
  2. Use the `structured_llm` (i.e., `llm.with_structured_output(CitedAnswer)`);
  3. Return the Pydantic object in the output.


```
defformat_docs_with_id(docs: List[Document])->str:  formatted =[f"Source ID: {i}\nArticle Title: {doc.metadata['title']}\nArticle Snippet: {doc.page_content}"for i, doc inenumerate(docs)]return"\n\n"+"\n\n".join(formatted)classState(TypedDict):  question:str  context: List[Document]  answer: CitedAnswerdefgenerate(state: State):  formatted_docs = format_docs_with_id(state["context"])  messages = prompt.invoke({"question": state["question"],"context": formatted_docs})  structured_llm = llm.with_structured_output(CitedAnswer)  response = structured_llm.invoke(messages)return{"answer": response}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

```
result = graph.invoke({"question":"How fast are cheetahs?"})result["answer"]
```

```
CitedAnswer(answer='Cheetahs are capable of running at speeds between 93 to 104 km/h (58 to 65 mph).', citations=[0, 3])
```

We can inspect the document at index 0, which the model cited:
```
print(result["context"][0])
```

```
page_content='The cheetah (Acinonyx jubatus) is a large cat and the fastest land animal. It has a tawny to creamy white or pale buff fur that is marked with evenly spaced, solid black spots. The head is small and rounded, with a short snout and black tear-like facial streaks. It reaches 67–94 cm (26–37 in) at the shoulder, and the head-and-body length is between 1.1 and 1.5 m (3 ft 7 in and 4 ft 11 in). Adults weigh between 21 and 72 kg (46 and 159 lb). The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tail.The cheetah was first described in the late 18th century. Four subspecies are recognised today that are native to Africa and central Iran. An African subspecies was introduced to India in 2022. It is now distributed mainly in small, fragmented populations in northwestern, eastern and southern Africa and central Iran. It lives in a variety of habitats such as savannahs in the Serengeti, arid mountain ranges in the Sahara, and hilly desert terrain.The cheetah lives in three main social groups: females and their cubs, male "coalitions", and solitary males. While females lead a nomadic life searching for prey in large home ranges, males are more sedentary and instead establish much smaller territories in areas with plentiful prey and access to females. The cheetah is active during the day, with peaks during dawn and dusk. It feeds on small- to medium-sized prey, mostly weighing under 40 kg (88 lb), and prefers medium-sized ungulates such as impala, springbok and Thomson's gazelles. The cheetah typically stalks its prey within 60–100 m (200–330 ft) before charging towards it, trips it during the chase and bites its throat to suffocate it to death. It breeds throughout the year. After a gestation of nearly three months, females give birth to a litter of three or four cubs. Cheetah cubs are highly vulnerable to predation by other large carnivores. They are weaned a' metadata={'title': 'Cheetah', 'summary': 'The cheetah (Acinonyx jubatus) is a large cat and the fastest land animal. It has a tawny to creamy white or pale buff fur that is marked with evenly spaced, solid black spots. The head is small and rounded, with a short snout and black tear-like facial streaks. It reaches 67–94 cm (26–37 in) at the shoulder, and the head-and-body length is between 1.1 and 1.5 m (3 ft 7 in and 4 ft 11 in). Adults weigh between 21 and 72 kg (46 and 159 lb). The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tail.\nThe cheetah was first described in the late 18th century. Four subspecies are recognised today that are native to Africa and central Iran. An African subspecies was introduced to India in 2022. It is now distributed mainly in small, fragmented populations in northwestern, eastern and southern Africa and central Iran. It lives in a variety of habitats such as savannahs in the Serengeti, arid mountain ranges in the Sahara, and hilly desert terrain.\nThe cheetah lives in three main social groups: females and their cubs, male "coalitions", and solitary males. While females lead a nomadic life searching for prey in large home ranges, males are more sedentary and instead establish much smaller territories in areas with plentiful prey and access to females. The cheetah is active during the day, with peaks during dawn and dusk. It feeds on small- to medium-sized prey, mostly weighing under 40 kg (88 lb), and prefers medium-sized ungulates such as impala, springbok and Thomson\'s gazelles. The cheetah typically stalks its prey within 60–100 m (200–330 ft) before charging towards it, trips it during the chase and bites its throat to suffocate it to death. It breeds throughout the year. After a gestation of nearly three months, females give birth to a litter of three or four cubs. Cheetah cubs are highly vulnerable to predation by other large carnivores. They are weaned at around four months and are independent by around 20 months of age.\nThe cheetah is threatened by habitat loss, conflict with humans, poaching and high susceptibility to diseases. The global cheetah population was estimated in 2021 at 6,517; it is listed as Vulnerable on the IUCN Red List. It has been widely depicted in art, literature, advertising, and animation. It was tamed in ancient Egypt and trained for hunting ungulates in the Arabian Peninsula and India. It has been kept in zoos since the early 19th century.', 'source': 'https://en.wikipedia.org/wiki/Cheetah'}
```

LangSmith trace: https://smith.langchain.com/public/6f34d136-451d-4625-90c8-2d8decebc21a/r
### Cite snippets​
To return text spans (perhaps in addition to source identifiers), we can use the same approach. The only change will be to build a more complex output schema, here using Pydantic, that includes a "quote" alongside a source identifier.
_Aside: Note that if we break up our documents so that we have many documents with only a sentence or two instead of a few long documents, citing documents becomes roughly equivalent to citing snippets, and may be easier for the model because the model just needs to return an identifier for each snippet instead of the actual text. Probably worth trying both approaches and evaluating._
```
classCitation(BaseModel):  source_id:int= Field(...,    description="The integer ID of a SPECIFIC source which justifies the answer.",)  quote:str= Field(...,    description="The VERBATIM quote from the specified source that justifies the answer.",)classQuotedAnswer(BaseModel):"""Answer the user question based only on the given sources, and cite the sources used."""  answer:str= Field(...,    description="The answer to the user question, which is based only on the given sources.",)  citations: List[Citation]= Field(..., description="Citations from the given sources that justify the answer.")
```

```
classState(TypedDict):  question:str  context: List[Document]  answer: QuotedAnswerdefgenerate(state: State):  formatted_docs = format_docs_with_id(state["context"])  messages = prompt.invoke({"question": state["question"],"context": formatted_docs})  structured_llm = llm.with_structured_output(QuotedAnswer)  response = structured_llm.invoke(messages)return{"answer": response}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

Here we see that the model has extracted a relevant snippet of text from source 0:
```
result = graph.invoke({"question":"How fast are cheetahs?"})result["answer"]
```

```
QuotedAnswer(answer='Cheetahs are capable of running at speeds of 93 to 104 km/h (58 to 65 mph).', citations=[Citation(source_id=0, quote='The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed.')])
```

LangSmith trace: https://smith.langchain.com/public/e16dc72f-4261-4f25-a9a7-906238737283/r
## Direct prompting​
Some models don't support function-calling. We can achieve similar results with direct prompting. Let's try instructing a model to generate structured XML for its output:
```
xml_system ="""You're a helpful AI assistant. Given a user question and some Wikipedia article snippets, \answer the user question and provide citations. If none of the articles answer the question, just say you don't know.Remember, you must return both an answer and citations. A citation consists of a VERBATIM quote that \justifies the answer and the ID of the quote article. Return a citation for every quote across all articles \that justify the answer. Use the following format for your final output:<cited_answer>  <answer></answer>  <citations>    <citation><source_id></source_id><quote></quote></citation>    <citation><source_id></source_id><quote></quote></citation>    ...  </citations></cited_answer>Here are the Wikipedia articles:{context}"""xml_prompt = ChatPromptTemplate.from_messages([("system", xml_system),("human","{question}")])
```

We now make similar small updates to our chain:
  1. We update the formatting function to wrap the retrieved context in XML tags;
  2. We do not use `.with_structured_output` (e.g., because it does not exist for a model);
  3. We use XMLOutputParser to parse the answer into a dict.


```
from langchain_core.output_parsers import XMLOutputParserdefformat_docs_xml(docs: List[Document])->str:  formatted =[]for i, doc inenumerate(docs):    doc_str =f"""\  <source id=\"{i}\">    <title>{doc.metadata['title']}</title>    <article_snippet>{doc.page_content}</article_snippet>  </source>"""    formatted.append(doc_str)return"\n\n<sources>"+"\n".join(formatted)+"</sources>"classState(TypedDict):  question:str  context: List[Document]  answer:dictdefgenerate(state: State):  formatted_docs = format_docs_xml(state["context"])  messages = xml_prompt.invoke({"question": state["question"],"context": formatted_docs})  response = llm.invoke(messages)  parsed_response = XMLOutputParser().invoke(response)return{"answer": parsed_response}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

**API Reference:**XMLOutputParser
Note that citations are again structured into the answer:
```
result = graph.invoke({"question":"How fast are cheetahs?"})result["answer"]
```

```
{'cited_answer': [{'answer': 'Cheetahs can run at speeds of 93 to 104 km/h (58 to 65 mph).'}, {'citations': [{'citation': [{'source_id': '0'},   {'quote': 'The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph);'}]},  {'citation': [{'source_id': '3'},   {'quote': 'The fastest land animal is the cheetah.'}]}]}]}
```

LangSmith trace: https://smith.langchain.com/public/0c45f847-c640-4b9a-a5fa-63559e413527/r
## Retrieval post-processing​
Another approach is to post-process our retrieved documents to compress the content, so that the source content is already minimal enough that we don't need the model to cite specific sources or spans. For example, we could break up each document into a sentence or two, embed those and keep only the most relevant ones. LangChain has some built-in components for this. Here we'll use a RecursiveCharacterTextSplitter, which creates chunks of a specified size by splitting on separator substrings, and an EmbeddingsFilter, which keeps only the texts with the most relevant embeddings.
This approach effectively updates our `retrieve` step to compress the documents. Let's first select an embedding model:
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

We can now rewrite the `retrieve` step:
```
from langchain.retrievers.document_compressors import EmbeddingsFilterfrom langchain_core.runnables import RunnableParallelfrom langchain_text_splitters import RecursiveCharacterTextSplittersplitter = RecursiveCharacterTextSplitter(  chunk_size=400,  chunk_overlap=0,  separators=["\n\n","\n","."," "],  keep_separator=False,)compressor = EmbeddingsFilter(embeddings=embeddings, k=10)classState(TypedDict):  question:str  context: List[Document]  answer:strdefretrieve(state: State):  retrieved_docs = retriever.invoke(state["question"])  split_docs = splitter.split_documents(retrieved_docs)  stateful_docs = compressor.compress_documents(split_docs, state["question"])return{"context": stateful_docs}
```

**API Reference:**EmbeddingsFilter | RunnableParallel | RecursiveCharacterTextSplitter
Let's test this out:
```
retrieval_result = retrieve({"question":"How fast are cheetahs?"})for doc in retrieval_result["context"]:print(f"{doc.page_content}\n\n")
```

```
Adults weigh between 21 and 72 kg (46 and 159 lb). The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tailThe cheetah (Acinonyx jubatus) is a large cat and the fastest land animal. It has a tawny to creamy white or pale buff fur that is marked with evenly spaced, solid black spots. The head is small and rounded, with a short snout and black tear-like facial streaks. It reaches 67–94 cm (26–37 in) at the shoulder, and the head-and-body length is between 1.1 and 1.5 m (3 ft 7 in and 4 ft 11 in)2 mph), or 171 body lengths per second. The cheetah, the fastest land mammal, scores at only 16 body lengths per secondIt feeds on small- to medium-sized prey, mostly weighing under 40 kg (88 lb), and prefers medium-sized ungulates such as impala, springbok and Thomson's gazelles. The cheetah typically stalks its prey within 60–100 m (200–330 ft) before charging towards it, trips it during the chase and bites its throat to suffocate it to death. It breeds throughout the yearThe cheetah was first described in the late 18th century. Four subspecies are recognised today that are native to Africa and central Iran. An African subspecies was introduced to India in 2022. It is now distributed mainly in small, fragmented populations in northwestern, eastern and southern Africa and central IranThe cheetah lives in three main social groups: females and their cubs, male "coalitions", and solitary males. While females lead a nomadic life searching for prey in large home ranges, males are more sedentary and instead establish much smaller territories in areas with plentiful prey and access to females. The cheetah is active during the day, with peaks during dawn and duskThe Southeast African cheetah (Acinonyx jubatus jubatus) is the nominate cheetah subspecies native to East and Southern Africa. The Southern African cheetah lives mainly in the lowland areas and deserts of the Kalahari, the savannahs of Okavango Delta, and the grasslands of the Transvaal region in South Africa. In Namibia, cheetahs are mostly found in farmlandsSubpopulations have been called "South African cheetah" and "Namibian cheetah."In India, four cheetahs of the subspecies are living in Kuno National Park in Madhya Pradesh after having been introduced thereAcinonyx jubatus velox proposed in 1913 by Edmund Heller on basis of a cheetah that was shot by Kermit Roosevelt in June 1909 in the Kenyan highlands.Acinonyx rex proposed in 1927 by Reginald Innes Pocock on basis of a specimen from the Umvukwe Range in Rhodesia.
```

Next, we assemble it into our chain as before:
```
# This step is unchanged from our original RAG implementationdefgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}graph_builder = StateGraph(State).add_sequence([retrieve, generate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

```
result = graph.invoke({"question":"How fast are cheetahs?"})print(result["answer"])
```

```
Cheetahs are capable of running at speeds between 93 to 104 km/h (58 to 65 mph). They are known as the fastest land animals.
```

Note that the document content is now compressed, although the document objects retain the original content in a "summary" key in their metadata. These summaries are not passed to the model; only the condensed content is.
```
result["context"][0].page_content # passed to model
```

```
'Adults weigh between 21 and 72 kg (46 and 159 lb). The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tail'
```

```
result["context"][0].metadata["summary"]# original document # original document
```

```
'The cheetah (Acinonyx jubatus) is a large cat and the fastest land animal. It has a tawny to creamy white or pale buff fur that is marked with evenly spaced, solid black spots. The head is small and rounded, with a short snout and black tear-like facial streaks. It reaches 67–94 cm (26–37 in) at the shoulder, and the head-and-body length is between 1.1 and 1.5 m (3 ft 7 in and 4 ft 11 in). Adults weigh between 21 and 72 kg (46 and 159 lb). The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph); it has evolved specialized adaptations for speed, including a light build, long thin legs and a long tail.\nThe cheetah was first described in the late 18th century. Four subspecies are recognised today that are native to Africa and central Iran. An African subspecies was introduced to India in 2022. It is now distributed mainly in small, fragmented populations in northwestern, eastern and southern Africa and central Iran. It lives in a variety of habitats such as savannahs in the Serengeti, arid mountain ranges in the Sahara, and hilly desert terrain.\nThe cheetah lives in three main social groups: females and their cubs, male "coalitions", and solitary males. While females lead a nomadic life searching for prey in large home ranges, males are more sedentary and instead establish much smaller territories in areas with plentiful prey and access to females. The cheetah is active during the day, with peaks during dawn and dusk. It feeds on small- to medium-sized prey, mostly weighing under 40 kg (88 lb), and prefers medium-sized ungulates such as impala, springbok and Thomson\'s gazelles. The cheetah typically stalks its prey within 60–100 m (200–330 ft) before charging towards it, trips it during the chase and bites its throat to suffocate it to death. It breeds throughout the year. After a gestation of nearly three months, females give birth to a litter of three or four cubs. Cheetah cubs are highly vulnerable to predation by other large carnivores. They are weaned at around four months and are independent by around 20 months of age.\nThe cheetah is threatened by habitat loss, conflict with humans, poaching and high susceptibility to diseases. The global cheetah population was estimated in 2021 at 6,517; it is listed as Vulnerable on the IUCN Red List. It has been widely depicted in art, literature, advertising, and animation. It was tamed in ancient Egypt and trained for hunting ungulates in the Arabian Peninsula and India. It has been kept in zoos since the early 19th century.'
```

LangSmith trace: https://smith.langchain.com/public/21b0dc15-d70a-4293-9402-9c70f9178e66/r
## Generation post-processing​
Another approach is to post-process our model generation. In this example we'll first generate just an answer, and then we'll ask the model to annotate it's own answer with citations. The downside of this approach is of course that it is slower and more expensive, because two model calls need to be made.
Let's apply this to our initial chain. If desired, we can implement this via a third step in our application.
```
classCitation(BaseModel):  source_id:int= Field(...,    description="The integer ID of a SPECIFIC source which justifies the answer.",)  quote:str= Field(...,    description="The VERBATIM quote from the specified source that justifies the answer.",)classAnnotatedAnswer(BaseModel):"""Annotate the answer to the user question with quote citations that justify the answer."""  citations: List[Citation]= Field(..., description="Citations from the given sources that justify the answer.")structured_llm = llm.with_structured_output(AnnotatedAnswer)
```

```
classState(TypedDict):  question:str  context: List[Document]  answer:str  annotations: AnnotatedAnswerdefretrieve(state: State):  retrieved_docs = retriever.invoke(state["question"])return{"context": retrieved_docs}defgenerate(state: State):  docs_content ="\n\n".join(doc.page_content for doc in state["context"])  messages = prompt.invoke({"question": state["question"],"context": docs_content})  response = llm.invoke(messages)return{"answer": response.content}defannotate(state: State):  formatted_docs = format_docs_with_id(state["context"])  messages =[("system", system_prompt.format(context=formatted_docs)),("human", state["question"]),("ai", state["answer"]),("human","Annotate your answer with citations."),]  response = structured_llm.invoke(messages)return{"annotations": response}graph_builder = StateGraph(State).add_sequence([retrieve, generate, annotate])graph_builder.add_edge(START,"retrieve")graph = graph_builder.compile()
```

```
display(Image(graph.get_graph().draw_mermaid_png()))
```

![](https://python.langchain.com/docs/how_to/qa_citations/)
```
result = graph.invoke({"question":"How fast are cheetahs?"})print(result["answer"])
```

```
Cheetahs are capable of running at speeds between 93 to 104 km/h (58 to 65 mph).
```

```
result["annotations"]
```

```
AnnotatedAnswer(citations=[Citation(source_id=0, quote='The cheetah is capable of running at 93 to 104 km/h (58 to 65 mph)')])
```

LangSmith trace: https://smith.langchain.com/public/b8257417-573b-47c4-a750-74e542035f19/r
#### Was this page helpful?
  * Setup
  * Tool-calling
    * Cite documents
    * Cite snippets
  * Direct prompting
  * Retrieval post-processing
  * Generation post-processing


