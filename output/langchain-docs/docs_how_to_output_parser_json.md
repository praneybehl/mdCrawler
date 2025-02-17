Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * Output parsers
  * Prompt templates
  * Structured output
  * Chaining runnables together


While some model providers support built-in ways to return structured output, not all do. We can use an output parser to help users to specify an arbitrary JSON schema via the prompt, query a model for outputs that conform to that schema, and finally parse that schema as JSON.
note
Keep in mind that large language models are leaky abstractions! You'll have to use an LLM with sufficient capacity to generate well-formed JSON.
The `JsonOutputParser` is one built-in option for prompting for and then parsing JSON output. While it is similar in functionality to the `PydanticOutputParser`, it also supports streaming back partial JSON objects.
Here's an example of how it can be used alongside Pydantic to conveniently declare the expected schema:
```
%pip install -qU langchain langchain-openaiimport osfrom getpass import getpassif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()
```

```
from langchain_core.output_parsers import JsonOutputParserfrom langchain_core.prompts import PromptTemplatefrom langchain_openai import ChatOpenAIfrom pydantic import BaseModel, Fieldmodel = ChatOpenAI(temperature=0)# Define your desired data structure.classJoke(BaseModel):  setup:str= Field(description="question to set up a joke")  punchline:str= Field(description="answer to resolve the joke")# And a query intented to prompt a language model to populate the data structure.joke_query ="Tell me a joke."# Set up a parser + inject instructions into the prompt template.parser = JsonOutputParser(pydantic_object=Joke)prompt = PromptTemplate(  template="Answer the user query.\n{format_instructions}\n{query}\n",  input_variables=["query"],  partial_variables={"format_instructions": parser.get_format_instructions()},)chain = prompt | model | parserchain.invoke({"query": joke_query})
```

**API Reference:**JsonOutputParser | PromptTemplate | ChatOpenAI
```
{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it was two tired!'}
```

Note that we are passing `format_instructions` from the parser directly into the prompt. You can and should experiment with adding your own formatting hints in the other parts of your prompt to either augment or replace the default instructions:
```
parser.get_format_instructions()
```

```
'The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n\`\`\`\n{"properties": {"setup": {"title": "Setup", "description": "question to set up a joke", "type": "string"}, "punchline": {"title": "Punchline", "description": "answer to resolve the joke", "type": "string"}}, "required": ["setup", "punchline"]}\n\`\`\`'
```

## Streaming​
As mentioned above, a key difference between the `JsonOutputParser` and the `PydanticOutputParser` is that the `JsonOutputParser` output parser supports streaming partial chunks. Here's what that looks like:
```
for s in chain.stream({"query": joke_query}):print(s)
```

```
{}{'setup': ''}{'setup': 'Why'}{'setup': 'Why couldn'}{'setup': "Why couldn't"}{'setup': "Why couldn't the"}{'setup': "Why couldn't the bicycle"}{'setup': "Why couldn't the bicycle stand"}{'setup': "Why couldn't the bicycle stand up"}{'setup': "Why couldn't the bicycle stand up by"}{'setup': "Why couldn't the bicycle stand up by itself"}{'setup': "Why couldn't the bicycle stand up by itself?"}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': ''}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because'}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it'}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it was'}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it was two'}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it was two tired'}{'setup': "Why couldn't the bicycle stand up by itself?", 'punchline': 'Because it was two tired!'}
```

## Without Pydantic​
You can also use the `JsonOutputParser` without Pydantic. This will prompt the model to return JSON, but doesn't provide specifics about what the schema should be.
```
joke_query ="Tell me a joke."parser = JsonOutputParser()prompt = PromptTemplate(  template="Answer the user query.\n{format_instructions}\n{query}\n",  input_variables=["query"],  partial_variables={"format_instructions": parser.get_format_instructions()},)chain = prompt | model | parserchain.invoke({"query": joke_query})
```

```
{'response': "Sure! Here's a joke for you: Why couldn't the bicycle stand up by itself? Because it was two tired!"}
```

## Next steps​
You've now learned one way to prompt a model to return structured JSON. Next, check out the broader guide on obtaining structured output for other techniques.
#### Was this page helpful?
  * Streaming
  * Without Pydantic
  * Next steps


