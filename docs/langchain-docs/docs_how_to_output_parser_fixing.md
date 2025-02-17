Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This output parser wraps another output parser, and in the event that the first one fails it calls out to another LLM to fix any errors.
But we can do other things besides throw errors. Specifically, we can pass the misformatted output, along with the formatted instructions, to the model and ask it to fix it.
For this example, we'll use the above Pydantic output parser. Here's what happens if we pass it a result that does not comply with the schema:
```
from typing import Listfrom langchain_core.exceptions import OutputParserExceptionfrom langchain_core.output_parsers import PydanticOutputParserfrom langchain_openai import ChatOpenAIfrom pydantic import BaseModel, Field
```

**API Reference:**OutputParserException | PydanticOutputParser | ChatOpenAI
```
classActor(BaseModel):  name:str= Field(description="name of an actor")  film_names: List[str]= Field(description="list of names of films they starred in")actor_query ="Generate the filmography for a random actor."parser = PydanticOutputParser(pydantic_object=Actor)
```

```
misformatted ="{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"
```

```
try:  parser.parse(misformatted)except OutputParserException as e:print(e)
```

```
Invalid json output: {'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE
```

Now we can construct and use a `OutputFixingParser`. This output parser takes as an argument another output parser but also an LLM with which to try to correct any formatting mistakes.
```
from langchain.output_parsers import OutputFixingParsernew_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
```

**API Reference:**OutputFixingParser
```
new_parser.parse(misformatted)
```

```
Actor(name='Tom Hanks', film_names=['Forrest Gump'])
```

Find out api documentation for OutputFixingParser.
#### Was this page helpful?
