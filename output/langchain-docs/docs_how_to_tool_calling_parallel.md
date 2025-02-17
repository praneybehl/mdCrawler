Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
OpenAI-specific
This API is currently only supported by OpenAI.
OpenAI tool calling performs tool calling in parallel by default. That means that if we ask a question like "What is the weather in Tokyo, New York, and Chicago?" and we have a tool for getting the weather, it will call the tool 3 times in parallel. We can force it to call only a single tool once by using the `parallel_tool_call` parameter.
First let's set up our tools and model:
```
from langchain_core.tools import tool@tooldefadd(a:int, b:int)->int:"""Adds a and b."""return a + b@tooldefmultiply(a:int, b:int)->int:"""Multiplies a and b."""return a * btools =[add, multiply]
```

**API Reference:**tool
```
import osfrom getpass import getpassfrom langchain_openai import ChatOpenAIif"OPENAI_API_KEY"notin os.environ:  os.environ["OPENAI_API_KEY"]= getpass()llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

**API Reference:**ChatOpenAI
Now let's show a quick example of how disabling parallel tool calls work:
```
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)llm_with_tools.invoke("Please call the first tool two times").tool_calls
```

```
[{'name': 'add', 'args': {'a': 2, 'b': 2}, 'id': 'call_Hh4JOTCDM85Sm9Pr84VKrWu5'}]
```

As we can see, even though we explicitly told the model to call a tool twice, by disabling parallel tool calls the model was constrained to only calling one.
#### Was this page helpful?
