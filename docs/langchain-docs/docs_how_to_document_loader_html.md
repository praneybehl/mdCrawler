Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser.
This covers how to load `HTML` documents into a LangChain Document objects that we can use downstream.
Parsing HTML files often requires specialized tools. Here we demonstrate parsing via Unstructured and BeautifulSoup4, which can be installed via pip. Head over to the integrations page to find integrations with additional services, such as Azure AI Document Intelligence or FireCrawl.
## Loading HTML with Unstructured​
```
%pip install unstructured
```

```
from langchain_community.document_loaders import UnstructuredHTMLLoaderfile_path ="../../docs/integrations/document_loaders/example_data/fake-content.html"loader = UnstructuredHTMLLoader(file_path)data = loader.load()print(data)
```

**API Reference:**UnstructuredHTMLLoader
```
[Document(page_content='My First Heading\n\nMy first paragraph.', metadata={'source': '../../docs/integrations/document_loaders/example_data/fake-content.html'})]
```

## Loading HTML with BeautifulSoup4​
We can also use `BeautifulSoup4` to load HTML documents using the `BSHTMLLoader`. This will extract the text from the HTML into `page_content`, and the page title as `title` into `metadata`.
```
%pip install bs4
```

```
from langchain_community.document_loaders import BSHTMLLoaderloader = BSHTMLLoader(file_path)data = loader.load()print(data)
```

**API Reference:**BSHTMLLoader
```
[Document(page_content='\nTest Title\n\n\nMy First Heading\nMy first paragraph.\n\n\n', metadata={'source': '../../docs/integrations/document_loaders/example_data/fake-content.html', 'title': 'Test Title'})]
```

#### Was this page helpful?
  * Loading HTML with Unstructured
  * Loading HTML with BeautifulSoup4


