Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
In this quickstart we'll show you how to build a simple LLM application with LangChain. This application will translate text from English into another language. This is a relatively simple LLM application - it's just a single LLM call plus some prompting. Still, this is a great way to get started with LangChain - a lot of features can be built with just some prompting and an LLM call!
After reading this tutorial, you'll have a high level overview of:
  * Using language models
  * Using prompt templates
  * Debugging and tracing your application using LangSmith


Let's dive in!
## Setup​
### Jupyter Notebook​
This and other tutorials are perhaps most conveniently run in a Jupyter notebooks. Going through guides in an interactive environment is a great way to better understand them. See here for instructions on how to install.
### Installation​
To install LangChain run:
  * Pip
  * Conda


```
pip install langchain
```

```
conda install langchain -c conda-forge
```

For more details, see our Installation guide.
### LangSmith​
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.
After you sign up at the link above, make sure to set your environment variables to start logging traces:
```
export LANGSMITH_TRACING="true"export LANGSMITH_API_KEY="..."
```

Or, if in a notebook, you can set them with:
```
import getpassimport osos.environ["LANGSMITH_TRACING"]="true"os.environ["LANGSMITH_API_KEY"]= getpass.getpass()
```

## Using Language Models​
First up, let's learn how to use a language model by itself. LangChain supports many different language models that you can use interchangeably. For details on getting started with a specific model, refer to supported integrations.
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
import getpassimport osifnot os.environ.get("GROQ_API_KEY"): os.environ["GROQ_API_KEY"]= getpass.getpass("Enter API key for Groq: ")from langchain.chat_models import init_chat_modelmodel = init_chat_model("llama3-8b-8192", model_provider="groq")
```

Let's first use the model directly. ChatModels are instances of LangChain Runnables, which means they expose a standard interface for interacting with them. To simply call the model, we can pass in a list of messages to the `.invoke` method.
```
from langchain_core.messages import HumanMessage, SystemMessagemessages =[  SystemMessage("Translate the following from English into Italian"),  HumanMessage("hi!"),]model.invoke(messages)
```

**API Reference:**HumanMessage | SystemMessage
```
AIMessage(content='Ciao!', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 3, 'prompt_tokens': 20, 'total_tokens': 23, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0705bf87c0', 'finish_reason': 'stop', 'logprobs': None}, id='run-32654a56-627c-40e1-a141-ad9350bbfd3e-0', usage_metadata={'input_tokens': 20, 'output_tokens': 3, 'total_tokens': 23, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})
```

tip
If we've enabled LangSmith, we can see that this run is logged to LangSmith, and can see the LangSmith trace. The LangSmith trace reports token usage information, latency, standard model parameters (such as temperature), and other information.
Note that ChatModels receive message objects as input and generate message objects as output. In addition to text content, message objects convey conversational roles and hold important data, such as tool calls and token usage counts.
LangChain also supports chat model inputs via strings or OpenAI format. The following are equivalent:
```
model.invoke("Hello")model.invoke([{"role":"user","content":"Hello"}])model.invoke([HumanMessage("Hello")])
```

### Streaming​
Because chat models are Runnables, they expose a standard interface that includes async and streaming modes of invocation. This allows us to stream individual tokens from a chat model:
```
for token in model.stream(messages):print(token.content, end="|")
```

```
|C|iao|!||
```

You can find more details on streaming chat model outputs in this guide.
## Prompt Templates​
Right now we are passing a list of messages directly into the language model. Where does this list of messages come from? Usually, it is constructed from a combination of user input and application logic. This application logic usually takes the raw user input and transforms it into a list of messages ready to pass to the language model. Common transformations include adding a system message or formatting a template with the user input.
Prompt templates are a concept in LangChain designed to assist with this transformation. They take in raw user input and return data (a prompt) that is ready to pass into a language model.
Let's create a prompt template here. It will take in two user variables:
  * `language`: The language to translate text into
  * `text`: The text to translate


```
from langchain_core.prompts import ChatPromptTemplatesystem_template ="Translate the following from English into {language}"prompt_template = ChatPromptTemplate.from_messages([("system", system_template),("user","{text}")])
```

**API Reference:**ChatPromptTemplate
Note that `ChatPromptTemplate` supports multiple message roles in a single template. We format the `language` parameter into the system message, and the user `text` into a user message.
The input to this prompt template is a dictionary. We can play around with this prompt template by itself to see what it does by itself
```
prompt = prompt_template.invoke({"language":"Italian","text":"hi!"})prompt
```

```
ChatPromptValue(messages=[SystemMessage(content='Translate the following from English into Italian', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})])
```

We can see that it returns a `ChatPromptValue` that consists of two messages. If we want to access the messages directly we do:
```
prompt.to_messages()
```

```
[SystemMessage(content='Translate the following from English into Italian', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})]
```

Finally, we can invoke the chat model on the formatted prompt:
```
response = model.invoke(prompt)print(response.content)
```

```
Ciao!
```

tip
Message `content` can contain both text and content blocks with additional structure. See this guide for more information.
If we take a look at the LangSmith trace, we can see exactly what prompt the chat model receives, along with token usage information, latency, standard model parameters (such as temperature), and other information.
## Conclusion​
That's it! In this tutorial you've learned how to create your first simple LLM application. You've learned how to work with language models, how to create a prompt template, and how to get great observability into applications you create with LangSmith.
This just scratches the surface of what you will want to learn to become a proficient AI Engineer. Luckily - we've got a lot of other resources!
For further reading on the core concepts of LangChain, we've got detailed Conceptual Guides.
If you have more specific questions on these concepts, check out the following sections of the how-to guides:
  * Chat models
  * Prompt templates


And the LangSmith docs:
  * LangSmith


#### Was this page helpful?
  * Setup
    * Jupyter Notebook
    * Installation
    * LangSmith
  * Using Language Models
    * Streaming
  * Prompt Templates
  * Conclusion


