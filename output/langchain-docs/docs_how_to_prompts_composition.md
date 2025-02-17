Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Prompt templates


LangChain provides a user friendly interface for composing different parts of prompts together. You can do this with either string prompts or chat prompts. Constructing prompts this way allows for easy reuse of components.
## String prompt composition​
When working with string prompts, each template is joined together. You can work with either prompts directly or strings (the first element in the list needs to be a prompt).
```
from langchain_core.prompts import PromptTemplateprompt =(  PromptTemplate.from_template("Tell me a joke about {topic}")+", make it funny"+"\n\nand in {language}")prompt
```

**API Reference:**PromptTemplate
```
PromptTemplate(input_variables=['language', 'topic'], template='Tell me a joke about {topic}, make it funny\n\nand in {language}')
```

```
prompt.format(topic="sports", language="spanish")
```

```
'Tell me a joke about sports, make it funny\n\nand in spanish'
```

## Chat prompt composition​
A chat prompt is made up a of a list of messages. Similarly to the above example, we can concatenate chat prompt templates. Each new element is a new message in the final prompt.
First, let's initialize the a `ChatPromptTemplate` with a `SystemMessage`.
```
from langchain_core.messages import AIMessage, HumanMessage, SystemMessageprompt = SystemMessage(content="You are a nice pirate")
```

**API Reference:**AIMessage | HumanMessage | SystemMessage
You can then easily create a pipeline combining it with other messages _or_ message templates. Use a `Message` when there is no variables to be formatted, use a `MessageTemplate` when there are variables to be formatted. You can also use just a string (note: this will automatically get inferred as a `HumanMessagePromptTemplate`.)
```
new_prompt =(  prompt + HumanMessage(content="hi")+ AIMessage(content="what?")+"{input}")
```

Under the hood, this creates an instance of the ChatPromptTemplate class, so you can use it just as you did before!
```
new_prompt.format_messages(input="i said hi")
```

```
[SystemMessage(content='You are a nice pirate'), HumanMessage(content='hi'), AIMessage(content='what?'), HumanMessage(content='i said hi')]
```

## Using PipelinePrompt​
LangChain includes a class called `PipelinePromptTemplate`, which can be useful when you want to reuse parts of prompts. A PipelinePrompt consists of two main parts:
  * Final prompt: The final prompt that is returned
  * Pipeline prompts: A list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.


```
from langchain_core.prompts import PipelinePromptTemplate, PromptTemplatefull_template ="""{introduction}{example}{start}"""full_prompt = PromptTemplate.from_template(full_template)introduction_template ="""You are impersonating {person}."""introduction_prompt = PromptTemplate.from_template(introduction_template)example_template ="""Here's an example of an interaction:Q: {example_q}A: {example_a}"""example_prompt = PromptTemplate.from_template(example_template)start_template ="""Now, do this for real!Q: {input}A:"""start_prompt = PromptTemplate.from_template(start_template)input_prompts =[("introduction", introduction_prompt),("example", example_prompt),("start", start_prompt),]pipeline_prompt = PipelinePromptTemplate(  final_prompt=full_prompt, pipeline_prompts=input_prompts)pipeline_prompt.input_variables
```

**API Reference:**PipelinePromptTemplate | PromptTemplate
```
['person', 'example_a', 'example_q', 'input']
```

```
print(  pipeline_prompt.format(    person="Elon Musk",    example_q="What's your favorite car?",    example_a="Tesla",input="What's your favorite social media site?",))
```

```
You are impersonating Elon Musk.Here's an example of an interaction:Q: What's your favorite car?A: TeslaNow, do this for real!Q: What's your favorite social media site?A:
```

## Next steps​
You've now learned how to compose prompts together.
Next, check out the other how-to guides on prompt templates in this section, like adding few-shot examples to your prompt templates.
#### Was this page helpful?
  * String prompt composition
  * Chat prompt composition
  * Using PipelinePrompt
  * Next steps


