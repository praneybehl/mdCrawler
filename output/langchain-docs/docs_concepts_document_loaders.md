Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
  * Document loaders API reference


Document loaders are designed to load document objects. LangChain has hundreds of integrations with various data sources to load data from: Slack, Notion, Google Drive, etc.
## Integrations​
You can find available integrations on the Document loaders integrations page.
## Interface​
Documents loaders implement the BaseLoader interface.
Each DocumentLoader has its own specific parameters, but they can all be invoked in the same way with the `.load` method or `.lazy_load`.
Here's a simple example:
```
from langchain_community.document_loaders.csv_loader import CSVLoaderloader = CSVLoader(...# <-- Integration specific parameters here)data = loader.load()
```

**API Reference:**CSVLoader
When working with large datasets, you can use the `.lazy_load` method:
```
for document in loader.lazy_load():print(document)
```

## Related resources​
Please see the following resources for more information:
  * How-to guides for document loaders
  * Document API reference
  * Document loaders integrations


#### Was this page helpful?
  * Integrations
  * Interface
  * Related resources


