Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Toolkits are collections of tools that are designed to be used together for specific tasks. They have convenient loading methods.
All Toolkits expose a `get_tools` method which returns a list of tools. You can therefore do:
```
# Initialize a toolkittoolkit = ExampleTookit(...)# Get list of toolstools = toolkit.get_tools()# Create agentagent = create_agent_method(llm, tools, prompt)
```

#### Was this page helpful?
