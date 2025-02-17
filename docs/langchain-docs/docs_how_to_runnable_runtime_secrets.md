Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Requires `langchain-core >= 0.2.22`
We can pass in secrets to our runnables at runtime using the `RunnableConfig`. Specifically we can pass in secrets with a `__` prefix to the `configurable` field. This will ensure that these secrets aren't traced as part of the invocation:
```
from langchain_core.runnables import RunnableConfigfrom langchain_core.tools import tool@tooldeffoo(x:int, config: RunnableConfig)->int:"""Sum x and a secret int"""return x + config["configurable"]["__top_secret_int"]foo.invoke({"x":5},{"configurable":{"__top_secret_int":2,"traced_key":"bar"}})
```

**API Reference:**RunnableConfig | tool
```
7
```

Looking at the LangSmith trace for this run, we can see that "traced_key" was recorded (as part of Metadata) while our secret int was not: https://smith.langchain.com/public/aa7e3289-49ca-422d-a408-f6b927210170/r
#### Was this page helpful?
