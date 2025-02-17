Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following:
  * LangChain Expression Language (LCEL)
  * How to turn any function into a runnable


Sometimes we want to construct parts of a chain at runtime, depending on the chain inputs (routing is the most common example of this). We can create dynamic chains like this using a very useful property of RunnableLambda's, which is that if a RunnableLambda returns a Runnable, that Runnable is itself invoked. Let's see an example.
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
# | echo: falsefrom langchain_anthropic import ChatAnthropicllm = ChatAnthropic(model="claude-3-sonnet-20240229")
```

**API Reference:**ChatAnthropic
```
from operator import itemgetterfrom langchain_core.output_parsers import StrOutputParserfrom langchain_core.prompts import ChatPromptTemplatefrom langchain_core.runnables import Runnable, RunnablePassthrough, chaincontextualize_instructions ="""Convert the latest user question into a standalone question given the chat history. Don't answer the question, return the question and nothing else (no descriptive text)."""contextualize_prompt = ChatPromptTemplate.from_messages([("system", contextualize_instructions),("placeholder","{chat_history}"),("human","{question}"),])contextualize_question = contextualize_prompt | llm | StrOutputParser()qa_instructions =("""Answer the user question given the following context:\n\n{context}.""")qa_prompt = ChatPromptTemplate.from_messages([("system", qa_instructions),("human","{question}")])@chaindefcontextualize_if_needed(input_:dict)-> Runnable:if input_.get("chat_history"):# NOTE: This is returning another Runnable, not an actual output.return contextualize_questionelse:return RunnablePassthrough()| itemgetter("question")@chaindeffake_retriever(input_:dict)->str:return"egypt's population in 2024 is about 111 million"full_chain =(  RunnablePassthrough.assign(question=contextualize_if_needed).assign(    context=fake_retriever)| qa_prompt| llm| StrOutputParser())full_chain.invoke({"question":"what about egypt","chat_history":[("human","what's the population of indonesia"),("ai","about 276 million"),],})
```

**API Reference:**StrOutputParser | ChatPromptTemplate | Runnable | RunnablePassthrough | chain
```
"According to the context provided, Egypt's population in 2024 is estimated to be about 111 million."
```

The key here is that `contextualize_if_needed` returns another Runnable and not an actual output. This returned Runnable is itself run when the full chain is executed.
Looking at the trace we can see that, since we passed in chat_history, we executed the contextualize_question chain as part of the full chain: https://smith.langchain.com/public/9e0ae34c-4082-4f3f-beed-34a2a2f4c991/r
Note that the streaming, batching, etc. capabilities of the returned Runnable are all preserved
```
for chunk in contextualize_if_needed.stream({"question":"what about egypt","chat_history":[("human","what's the population of indonesia"),("ai","about 276 million"),],}):print(chunk)
```

```
What is the population of Egypt?
```

#### Was this page helpful?
