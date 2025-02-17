Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
In this tutorial, we will use tool-calling features of chat models to extract structured information from unstructured text. We will also demonstrate how to use few-shot prompting in this context to improve performance.
important
This tutorial requires `langchain-core>=0.3.20` and will only work with models that support **tool calling**.
## Setup​
### Jupyter Notebook​
This and other tutorials are perhaps most conveniently run in a Jupyter notebooks. Going through guides in an interactive environment is a great way to better understand them. See here for instructions on how to install.
### Installation​
To install LangChain run:
  * Pip
  * Conda


```
pip install --upgrade langchain-core
```

```
conda install langchain-core -c conda-forge
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

## The Schema​
First, we need to describe what information we want to extract from the text.
We'll use Pydantic to define an example schema to extract personal information.
```
from typing import Optionalfrom pydantic import BaseModel, FieldclassPerson(BaseModel):"""Information about a person."""# ^ Doc-string for the entity Person.# This doc-string is sent to the LLM as the description of the schema Person,# and it can help to improve extraction results.# Note that:# 1. Each field is an `optional` -- this allows the model to decline to extract it!# 2. Each field has a `description` -- this description is used by the LLM.# Having a good description can help improve extraction results.  name: Optional[str]= Field(default=None, description="The name of the person")  hair_color: Optional[str]= Field(    default=None, description="The color of the person's hair if known")  height_in_meters: Optional[str]= Field(    default=None, description="Height measured in meters")
```

There are two best practices when defining schema:
  1. Document the **attributes** and the **schema** itself: This information is sent to the LLM and is used to improve the quality of information extraction.
  2. Do not force the LLM to make up information! Above we used `Optional` for the attributes allowing the LLM to output `None` if it doesn't know the answer.


important
For best performance, document the schema well and make sure the model isn't force to return results if there's no information to be extracted in the text.
## The Extractor​
Let's create an information extractor using the schema we defined above.
```
from typing import Optionalfrom langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholderfrom pydantic import BaseModel, Field# Define a custom prompt to provide instructions and any additional context.# 1) You can add examples into the prompt template to improve extraction quality# 2) Introduce additional parameters to take context into account (e.g., include metadata#  about the document from which the text was extracted.)prompt_template = ChatPromptTemplate.from_messages([("system","You are an expert extraction algorithm. ""Only extract relevant information from the text. ""If you do not know the value of an attribute asked to extract, ""return null for the attribute's value.",),# Please see the how-to about improving performance with# reference examples.# MessagesPlaceholder('examples'),("human","{text}"),])
```

**API Reference:**ChatPromptTemplate | MessagesPlaceholder
We need to use a model that supports function/tool calling.
Please review the documentation for all models that can be used with this API.
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
structured_llm = llm.with_structured_output(schema=Person)
```

Let's test it out:
```
text ="Alan Smith is 6 feet tall and has blond hair."prompt = prompt_template.invoke({"text": text})structured_llm.invoke(prompt)
```

```
Person(name='Alan Smith', hair_color='blond', height_in_meters='1.83')
```

important
Extraction is Generative 🤯
LLMs are generative models, so they can do some pretty cool things like correctly extract the height of the person in meters even though it was provided in feet!
We can see the LangSmith trace here. Note that the chat model portion of the trace reveals the exact sequence of messages sent to the model, tools invoked, and other metadata.
## Multiple Entities​
In **most cases** , you should be extracting a list of entities rather than a single entity.
This can be easily achieved using pydantic by nesting models inside one another.
```
from typing import List, Optionalfrom pydantic import BaseModel, FieldclassPerson(BaseModel):"""Information about a person."""# ^ Doc-string for the entity Person.# This doc-string is sent to the LLM as the description of the schema Person,# and it can help to improve extraction results.# Note that:# 1. Each field is an `optional` -- this allows the model to decline to extract it!# 2. Each field has a `description` -- this description is used by the LLM.# Having a good description can help improve extraction results.  name: Optional[str]= Field(default=None, description="The name of the person")  hair_color: Optional[str]= Field(    default=None, description="The color of the person's hair if known")  height_in_meters: Optional[str]= Field(    default=None, description="Height measured in meters")classData(BaseModel):"""Extracted data about people."""# Creates a model so that we can extract multiple entities.  people: List[Person]
```

important
Extraction results might not be perfect here. Read on to see how to use **Reference Examples** to improve the quality of extraction, and check out our extraction how-to guides for more detail.
```
structured_llm = llm.with_structured_output(schema=Data)text ="My name is Jeff, my hair is black and i am 6 feet tall. Anna has the same color hair as me."prompt = prompt_template.invoke({"text": text})structured_llm.invoke(prompt)
```

```
Data(people=[Person(name='Jeff', hair_color='black', height_in_meters='1.83'), Person(name='Anna', hair_color='black', height_in_meters=None)])
```

tip
When the schema accommodates the extraction of **multiple entities** , it also allows the model to extract **no entities** if no relevant information is in the text by providing an empty list.
This is usually a **good** thing! It allows specifying **required** attributes on an entity without necessarily forcing the model to detect this entity.
We can see the LangSmith trace here.
## Reference examples​
The behavior of LLM applications can be steered using few-shot prompting. For chat models, this can take the form of a sequence of pairs of input and response messages demonstrating desired behaviors.
For example, we can convey the meaning of a symbol with alternating `user` and `assistant` messages:
```
messages =[{"role":"user","content":"2 🦜 2"},{"role":"assistant","content":"4"},{"role":"user","content":"2 🦜 3"},{"role":"assistant","content":"5"},{"role":"user","content":"3 🦜 4"},]response = llm.invoke(messages)print(response.content)
```

```
7
```

Structured output often uses tool calling under-the-hood. This typically involves the generation of AI messages containing tool calls, as well as tool messages containing the results of tool calls. What should a sequence of messages look like in this case?
Different chat model providers impose different requirements for valid message sequences. Some will accept a (repeating) message sequence of the form:
  * User message
  * AI message with tool call
  * Tool message with result


Others require a final AI message containing some sort of response.
LangChain includes a utility function tool_example_to_messages that will generate a valid sequence for most model providers. It simplifies the generation of structured few-shot examples by just requiring Pydantic representations of the corresponding tool calls.
Let's try this out. We can convert pairs of input strings and desired Pydantic objects to a sequence of messages that can be provided to a chat model. Under the hood, LangChain will format the tool calls to each provider's required format.
Note: this version of `tool_example_to_messages` requires `langchain-core>=0.3.20`.
```
from langchain_core.utils.function_calling import tool_example_to_messagesexamples =[("The ocean is vast and blue. It's more than 20,000 feet deep.",    Data(people=[]),),("Fiona traveled far from France to Spain.",    Data(people=[Person(name="Fiona", height_in_meters=None, hair_color=None)]),),]messages =[]for txt, tool_call in examples:if tool_call.people:# This final message is optional for some providers    ai_response ="Detected people."else:    ai_response ="Detected no people."  messages.extend(tool_example_to_messages(txt,[tool_call], ai_response=ai_response))
```

**API Reference:**tool_example_to_messages
Inspecting the result, we see these two example pairs generated eight messages:
```
for message in messages:  message.pretty_print()
```

```
================================[1m Human Message [0m=================================The ocean is vast and blue. It's more than 20,000 feet deep.==================================[1m Ai Message [0m==================================Tool Calls: Data (d8f2e054-7fb9-417f-b28f-0447a775b2c3) Call ID: d8f2e054-7fb9-417f-b28f-0447a775b2c3 Args:  people: []=================================[1m Tool Message [0m=================================You have correctly called this tool.==================================[1m Ai Message [0m==================================Detected no people.================================[1m Human Message [0m=================================Fiona traveled far from France to Spain.==================================[1m Ai Message [0m==================================Tool Calls: Data (0178939e-a4b1-4d2a-a93e-b87f665cdfd6) Call ID: 0178939e-a4b1-4d2a-a93e-b87f665cdfd6 Args:  people: [{'name': 'Fiona', 'hair_color': None, 'height_in_meters': None}]=================================[1m Tool Message [0m=================================You have correctly called this tool.==================================[1m Ai Message [0m==================================Detected people.
```

Let's compare performance with and without these messages. For example, let's pass a message for which we intend no people to be extracted:
```
message_no_extraction ={"role":"user","content":"The solar system is large, but earth has only 1 moon.",}structured_llm = llm.with_structured_output(schema=Data)structured_llm.invoke([message_no_extraction])
```

```
Data(people=[Person(name='Earth', hair_color='None', height_in_meters='0.00')])
```

In this example, the model is liable to erroneously generate records of people.
Because our few-shot examples contain examples of "negatives", we encourage the model to behave correctly in this case:
```
structured_llm.invoke(messages +[message_no_extraction])
```

```
Data(people=[])
```

tip
The LangSmith trace for the run reveals the exact sequence of messages sent to the chat model, tool calls generated, latency, token counts, and other metadata.
See this guide for more detail on extraction workflows with reference examples, including how to incorporate prompt templates and customize the generation of example messages.
## Next steps​
Now that you understand the basics of extraction with LangChain, you're ready to proceed to the rest of the how-to guides:
  * Add Examples: More detail on using **reference examples** to improve performance.
  * Handle Long Text: What should you do if the text does not fit into the context window of the LLM?
  * Use a Parsing Approach: Use a prompt based approach to extract with models that do not support **tool/function calling**.


#### Was this page helpful?
  * Setup
    * Jupyter Notebook
    * Installation
    * LangSmith
  * The Schema
  * The Extractor
  * Multiple Entities
  * Reference examples
  * Next steps


