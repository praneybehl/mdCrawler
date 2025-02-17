Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
Here we cover how to load `Markdown` documents into LangChain Document objects that we can use downstream.
We will cover:
  * Basic usage;
  * Parsing of Markdown into elements such as titles, list items, and text.


LangChain implements an UnstructuredMarkdownLoader object which requires the Unstructured package. First we install it:
```
%pip install "unstructured[md]" nltk
```

Basic usage will ingest a Markdown file to a single document. Here we demonstrate on LangChain's readme:
```
from langchain_community.document_loaders import UnstructuredMarkdownLoaderfrom langchain_core.documents import Documentmarkdown_path ="../../../README.md"loader = UnstructuredMarkdownLoader(markdown_path)data = loader.load()assertlen(data)==1assertisinstance(data[0], Document)readme_content = data[0].page_contentprint(readme_content[:250])
```

**API Reference:**UnstructuredMarkdownLoader | Document
```
🦜️🔗 LangChain⚡ Build context-aware reasoning applications ⚡Looking for the JS/TS library? Check out LangChain.js.To help you ship LangChain apps to production faster, check out LangSmith. LangSmith is a unified developer platform for building,
```

## Retain Elements​
Under the hood, Unstructured creates different "elements" for different chunks of text. By default we combine those together, but you can easily keep that separation by specifying `mode="elements"`.
```
loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")data = loader.load()print(f"Number of documents: {len(data)}\n")for document in data[:2]:print(f"{document}\n")
```

```
Number of documents: 66page_content='🦜️🔗 LangChain' metadata={'source': '../../../README.md', 'category_depth': 0, 'last_modified': '2024-06-28T15:20:01', 'languages': ['eng'], 'filetype': 'text/markdown', 'file_directory': '../../..', 'filename': 'README.md', 'category': 'Title'}page_content='⚡ Build context-aware reasoning applications ⚡' metadata={'source': '../../../README.md', 'last_modified': '2024-06-28T15:20:01', 'languages': ['eng'], 'parent_id': '200b8a7d0dd03f66e4f13456566d2b3a', 'filetype': 'text/markdown', 'file_directory': '../../..', 'filename': 'README.md', 'category': 'NarrativeText'}
```

Note that in this case we recover three distinct element types:
```
print(set(document.metadata["category"]for document in data))
```

```
{'ListItem', 'NarrativeText', 'Title'}
```

#### Was this page helpful?
  * Retain Elements


