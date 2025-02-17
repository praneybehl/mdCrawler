Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
While in some cases it is possible to fix any parsing mistakes by only looking at the output, in other cases it isn't. An example of this is when the output is not just in the incorrect format, but is partially complete. Consider the below example.
```
from langchain.output_parsers import OutputFixingParserfrom langchain_core.exceptions import OutputParserExceptionfrom langchain_core.output_parsers import PydanticOutputParserfrom langchain_core.prompts import PromptTemplatefrom langchain_openai import ChatOpenAI, OpenAIfrom pydantic import BaseModel, Field
```

**API Reference:**OutputFixingParser | OutputParserException | PydanticOutputParser | PromptTemplate | ChatOpenAI | OpenAI
```
template ="""Based on the user question, provide an Action and Action Input for what step should be taken.{format_instructions}Question: {query}Response:"""classAction(BaseModel):  action:str= Field(description="action to take")  action_input:str= Field(description="input to the action")parser = PydanticOutputParser(pydantic_object=Action)
```

```
prompt = PromptTemplate(  template="Answer the user query.\n{format_instructions}\n{query}\n",  input_variables=["query"],  partial_variables={"format_instructions": parser.get_format_instructions()},)
```

```
prompt_value = prompt.format_prompt(query="who is leo di caprios gf?")
```

```
bad_response ='{"action": "search"}'
```

If we try to parse this response as is, we will get an error:
```
try:  parser.parse(bad_response)except OutputParserException as e:print(e)
```

```
Failed to parse Action from completion {"action": "search"}. Got: 1 validation error for Actionaction_input Field required [type=missing, input_value={'action': 'search'}, input_type=dict]  For further information visit https://errors.pydantic.dev/2.9/v/missingFor troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/OUTPUT_PARSING_FAILURE
```

If we try to use the `OutputFixingParser` to fix this error, it will be confused - namely, it doesn't know what to actually put for action input.
```
fix_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
```

```
fix_parser.parse(bad_response)
```

```
Action(action='search', action_input='input')
```

Instead, we can use the RetryOutputParser, which passes in the prompt (as well as the original output) to try again to get a better response.
```
from langchain.output_parsers import RetryOutputParser
```

**API Reference:**RetryOutputParser
```
retry_parser = RetryOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0))
```

```
retry_parser.parse_with_prompt(bad_response, prompt_value)
```

```
Action(action='search', action_input='leo di caprio girlfriend')
```

We can also add the RetryOutputParser easily with a custom chain which transform the raw LLM/ChatModel output into a more workable format.
```
from langchain_core.runnables import RunnableLambda, RunnableParallelcompletion_chain = prompt | OpenAI(temperature=0)main_chain = RunnableParallel(  completion=completion_chain, prompt_value=prompt)| RunnableLambda(lambda x: retry_parser.parse_with_prompt(**x))main_chain.invoke({"query":"who is leo di caprios gf?"})
```

**API Reference:**RunnableLambda | RunnableParallel
```
Action(action='search', action_input='leo di caprio girlfriend')
```

Find out api documentation for RetryOutputParser.
#### Was this page helpful?
