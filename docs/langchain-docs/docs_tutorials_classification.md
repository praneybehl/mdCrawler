Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)
Tagging means labeling a document with classes such as:
  * Sentiment
  * Language
  * Style (formal, informal etc.)
  * Covered topics
  * Political tendency


![Image description](https://python.langchain.com/assets/images/tagging-93990e95451d92b715c2b47066384224.png)
## Overview​
Tagging has a few components:
  * `function`: Like extraction, tagging uses functions to specify how the model should tag a document
  * `schema`: defines how we want to tag the document


## Quickstart​
Let's see a very straightforward example of how we can use OpenAI tool calling for tagging in LangChain. We'll use the `with_structured_output` method supported by OpenAI models.
```
pip install --upgrade --quiet langchain-core
```

We'll need to load a chat model:
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

Let's specify a Pydantic model with a few properties and their expected type in our schema.
```
from langchain_core.prompts import ChatPromptTemplatefrom langchain_openai import ChatOpenAIfrom pydantic import BaseModel, Fieldtagging_prompt = ChatPromptTemplate.from_template("""Extract the desired information from the following passage.Only extract the properties mentioned in the 'Classification' function.Passage:{input}""")classClassification(BaseModel):  sentiment:str= Field(description="The sentiment of the text")  aggressiveness:int= Field(    description="How aggressive the text is on a scale from 1 to 10")  language:str= Field(description="The language the text is written in")# LLMllm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(  Classification)
```

**API Reference:**ChatPromptTemplate | ChatOpenAI
```
inp ="Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"prompt = tagging_prompt.invoke({"input": inp})response = llm.invoke(prompt)response
```

```
Classification(sentiment='positive', aggressiveness=1, language='Spanish')
```

If we want dictionary output, we can just call `.model_dump()`
```
inp ="Estoy muy enojado con vos! Te voy a dar tu merecido!"prompt = tagging_prompt.invoke({"input": inp})response = llm.invoke(prompt)response.model_dump()
```

```
{'sentiment': 'enojado', 'aggressiveness': 8, 'language': 'es'}
```

As we can see in the examples, it correctly interprets what we want.
The results vary so that we may get, for example, sentiments in different languages ('positive', 'enojado' etc.).
We will see how to control these results in the next section.
## Finer control​
Careful schema definition gives us more control over the model's output.
Specifically, we can define:
  * Possible values for each property
  * Description to make sure that the model understands the property
  * Required properties to be returned


Let's redeclare our Pydantic model to control for each of the previously mentioned aspects using enums:
```
classClassification(BaseModel):  sentiment:str= Field(..., enum=["happy","neutral","sad"])  aggressiveness:int= Field(...,    description="describes how aggressive the statement is, the higher the number the more aggressive",    enum=[1,2,3,4,5],)  language:str= Field(..., enum=["spanish","english","french","german","italian"])
```

```
tagging_prompt = ChatPromptTemplate.from_template("""Extract the desired information from the following passage.Only extract the properties mentioned in the 'Classification' function.Passage:{input}""")llm = ChatOpenAI(temperature=0, model="gpt-4o-mini").with_structured_output(  Classification)
```

Now the answers will be restricted in a way we expect!
```
inp ="Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"prompt = tagging_prompt.invoke({"input": inp})llm.invoke(prompt)
```

```
Classification(sentiment='positive', aggressiveness=1, language='Spanish')
```

```
inp ="Estoy muy enojado con vos! Te voy a dar tu merecido!"prompt = tagging_prompt.invoke({"input": inp})llm.invoke(prompt)
```

```
Classification(sentiment='enojado', aggressiveness=8, language='es')
```

```
inp ="Weather is ok here, I can go outside without much more than a coat"prompt = tagging_prompt.invoke({"input": inp})llm.invoke(prompt)
```

```
Classification(sentiment='neutral', aggressiveness=1, language='English')
```

The LangSmith trace lets us peek under the hood:
![Image description](https://python.langchain.com/assets/images/tagging_trace-de68242b410388c0c3a3b7ca5a95b5ec.png)
### Going deeper​
  * You can use the metadata tagger document transformer to extract metadata from a LangChain `Document`.
  * This covers the same basic functionality as the tagging chain, only applied to a LangChain `Document`.


#### Was this page helpful?
  * Overview
  * Quickstart
  * Finer control
    * Going deeper


