Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
## Overview​
Applications based on LLMs frequently entail extracting data from databases or files, like PDFs, and converting it into a format that LLMs can utilize. In LangChain, this usually involves creating Document objects, which encapsulate the extracted text (`page_content`) along with metadata—a dictionary containing details about the document, such as the author's name or the date of publication.
`Document` objects are often formatted into prompts that are fed into an LLM, allowing the LLM to use the information in the `Document` to generate a desired response (e.g., summarizing the document). `Documents` can be either used immediately or indexed into a vectorstore for future retrieval and use.
The main abstractions for Document Loading are:
Component| Description  
---|---  
Document| Contains `text` and `metadata`  
BaseLoader| Use to convert raw data into `Documents`  
Blob| A representation of binary data that's located either in a file or in memory  
BaseBlobParser| Logic to parse a `Blob` to yield `Document` objects  
This guide will demonstrate how to write custom document loading and file parsing logic; specifically, we'll see how to:
  1. Create a standard document Loader by sub-classing from `BaseLoader`.
  2. Create a parser using `BaseBlobParser` and use it in conjunction with `Blob` and `BlobLoaders`. This is useful primarily when working with files.


## Standard Document Loader​
A document loader can be implemented by sub-classing from a `BaseLoader` which provides a standard interface for loading documents.
### Interface​
Method Name| Explanation  
---|---  
lazy_load| Used to load documents one by one **lazily**. Use for production code.  
alazy_load| Async variant of `lazy_load`  
load| Used to load all the documents into memory **eagerly**. Use for prototyping or interactive work.  
aload| Used to load all the documents into memory **eagerly**. Use for prototyping or interactive work. **Added in 2024-04 to LangChain.**  
  * The `load` methods is a convenience method meant solely for prototyping work -- it just invokes `list(self.lazy_load())`.
  * The `alazy_load` has a default implementation that will delegate to `lazy_load`. If you're using async, we recommend overriding the default implementation and providing a native async implementation.


important
When implementing a document loader do **NOT** provide parameters via the `lazy_load` or `alazy_load` methods.
All configuration is expected to be passed through the initializer (**init**). This was a design choice made by LangChain to make sure that once a document loader has been instantiated it has all the information needed to load documents.
### Implementation​
Let's create an example of a standard document loader that loads a file and creates a document from each line in the file.
```
from typing import AsyncIterator, Iteratorfrom langchain_core.document_loaders import BaseLoaderfrom langchain_core.documents import DocumentclassCustomDocumentLoader(BaseLoader):"""An example document loader that reads a file line by line."""def__init__(self, file_path:str)->None:"""Initialize the loader with a file path.    Args:      file_path: The path to the file to load.    """    self.file_path = file_pathdeflazy_load(self)-> Iterator[Document]:# <-- Does not take any arguments"""A lazy loader that reads a file line by line.    When you're implementing lazy load methods, you should use a generator    to yield documents one by one.    """withopen(self.file_path, encoding="utf-8")as f:      line_number =0for line in f:yield Document(          page_content=line,          metadata={"line_number": line_number,"source": self.file_path},)        line_number +=1# alazy_load is OPTIONAL.# If you leave out the implementation, a default implementation which delegates to lazy_load will be used!asyncdefalazy_load(    self,)-> AsyncIterator[Document]:# <-- Does not take any arguments"""An async lazy loader that reads a file line by line."""# Requires aiofiles (install with pip)# https://github.com/Tinche/aiofilesimport aiofilesasyncwith aiofiles.open(self.file_path, encoding="utf-8")as f:      line_number =0asyncfor line in f:yield Document(          page_content=line,          metadata={"line_number": line_number,"source": self.file_path},)        line_number +=1
```

**API Reference:**BaseLoader | Document
### Test 🧪​
To test out the document loader, we need a file with some quality content.
```
withopen("./meow.txt","w", encoding="utf-8")as f:  quality_content ="meow meow🐱 \n meow meow🐱 \n meow😻😻"  f.write(quality_content)loader = CustomDocumentLoader("./meow.txt")
```

```
## Test out the lazy load interfacefor doc in loader.lazy_load():print()print(type(doc))print(doc)
```

```
<class 'langchain_core.documents.base.Document'>page_content='meow meow🐱 \n' metadata={'line_number': 0, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow meow🐱 \n' metadata={'line_number': 1, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
```

```
## Test out the async implementationasyncfor doc in loader.alazy_load():print()print(type(doc))print(doc)
```

```
<class 'langchain_core.documents.base.Document'>page_content='meow meow🐱 \n' metadata={'line_number': 0, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow meow🐱 \n' metadata={'line_number': 1, 'source': './meow.txt'}<class 'langchain_core.documents.base.Document'>page_content=' meow😻😻' metadata={'line_number': 2, 'source': './meow.txt'}
```

tip
`load()` can be helpful in an interactive environment such as a jupyter notebook.
Avoid using it for production code since eager loading assumes that all the content can fit into memory, which is not always the case, especially for enterprise data.
```
loader.load()
```

```
[Document(page_content='meow meow🐱 \n', metadata={'line_number': 0, 'source': './meow.txt'}), Document(page_content=' meow meow🐱 \n', metadata={'line_number': 1, 'source': './meow.txt'}), Document(page_content=' meow😻😻', metadata={'line_number': 2, 'source': './meow.txt'})]
```

## Working with Files​
Many document loaders involve parsing files. The difference between such loaders usually stems from how the file is parsed, rather than how the file is loaded. For example, you can use `open` to read the binary content of either a PDF or a markdown file, but you need different parsing logic to convert that binary data into text.
As a result, it can be helpful to decouple the parsing logic from the loading logic, which makes it easier to re-use a given parser regardless of how the data was loaded.
### BaseBlobParser​
A `BaseBlobParser` is an interface that accepts a `blob` and outputs a list of `Document` objects. A `blob` is a representation of data that lives either in memory or in a file. LangChain python has a `Blob` primitive which is inspired by the Blob WebAPI spec.
```
from langchain_core.document_loaders import BaseBlobParser, BlobclassMyParser(BaseBlobParser):"""A simple parser that creates a document from each line."""deflazy_parse(self, blob: Blob)-> Iterator[Document]:"""Parse a blob into a document line by line."""    line_number =0with blob.as_bytes_io()as f:for line in f:        line_number +=1yield Document(          page_content=line,          metadata={"line_number": line_number,"source": blob.source},)
```

**API Reference:**BaseBlobParser | Blob
```
blob = Blob.from_path("./meow.txt")parser = MyParser()
```

```
list(parser.lazy_parse(blob))
```

```
[Document(page_content='meow meow🐱 \n', metadata={'line_number': 1, 'source': './meow.txt'}), Document(page_content=' meow meow🐱 \n', metadata={'line_number': 2, 'source': './meow.txt'}), Document(page_content=' meow😻😻', metadata={'line_number': 3, 'source': './meow.txt'})]
```

Using the **blob** API also allows one to load content directly from memory without having to read it from a file!
```
blob = Blob(data=b"some data from memory\nmeow")list(parser.lazy_parse(blob))
```

```
[Document(page_content='some data from memory\n', metadata={'line_number': 1, 'source': None}), Document(page_content='meow', metadata={'line_number': 2, 'source': None})]
```

### Blob​
Let's take a quick look through some of the Blob API.
```
blob = Blob.from_path("./meow.txt", metadata={"foo":"bar"})
```

```
blob.encoding
```

```
'utf-8'
```

```
blob.as_bytes()
```

```
b'meow meow\xf0\x9f\x90\xb1 \n meow meow\xf0\x9f\x90\xb1 \n meow\xf0\x9f\x98\xbb\xf0\x9f\x98\xbb'
```

```
blob.as_string()
```

```
'meow meow🐱 \n meow meow🐱 \n meow😻😻'
```

```
blob.as_bytes_io()
```

```
<contextlib._GeneratorContextManager at 0x743f34324450>
```

```
blob.metadata
```

```
{'foo': 'bar'}
```

```
blob.source
```

```
'./meow.txt'
```

### Blob Loaders​
While a parser encapsulates the logic needed to parse binary data into documents, _blob loaders_ encapsulate the logic that's necessary to load blobs from a given storage location.
A the moment, `LangChain` only supports `FileSystemBlobLoader`.
You can use the `FileSystemBlobLoader` to load blobs and then use the parser to parse them.
```
from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoaderblob_loader = FileSystemBlobLoader(path=".", glob="*.mdx", show_progress=True)
```

**API Reference:**FileSystemBlobLoader
```
parser = MyParser()for blob in blob_loader.yield_blobs():for doc in parser.lazy_parse(blob):print(doc)break
```

```
 0%|     | 0/8 [00:00<?, ?it/s]
```

```
page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}page_content='# Markdown\n' metadata={'line_number': 1, 'source': 'markdown.mdx'}page_content='# JSON\n' metadata={'line_number': 1, 'source': 'json.mdx'}page_content='---\n' metadata={'line_number': 1, 'source': 'pdf.mdx'}page_content='---\n' metadata={'line_number': 1, 'source': 'index.mdx'}page_content='# File Directory\n' metadata={'line_number': 1, 'source': 'file_directory.mdx'}page_content='# CSV\n' metadata={'line_number': 1, 'source': 'csv.mdx'}page_content='# HTML\n' metadata={'line_number': 1, 'source': 'html.mdx'}
```

### Generic Loader​
LangChain has a `GenericLoader` abstraction which composes a `BlobLoader` with a `BaseBlobParser`.
`GenericLoader` is meant to provide standardized classmethods that make it easy to use existing `BlobLoader` implementations. At the moment, only the `FileSystemBlobLoader` is supported.
```
from langchain_community.document_loaders.generic import GenericLoaderloader = GenericLoader.from_filesystem(  path=".", glob="*.mdx", show_progress=True, parser=MyParser())for idx, doc inenumerate(loader.lazy_load()):if idx <5:print(doc)print("... output truncated for demo purposes")
```

**API Reference:**GenericLoader
```
 0%|     | 0/8 [00:00<?, ?it/s]
```

```
page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}page_content='\n' metadata={'line_number': 2, 'source': 'office_file.mdx'}page_content='>[The Microsoft Office](https://www.office.com/) suite of productivity software includes Microsoft Word, Microsoft Excel, Microsoft PowerPoint, Microsoft Outlook, and Microsoft OneNote. It is available for Microsoft Windows and macOS operating systems. It is also available on Android and iOS.\n' metadata={'line_number': 3, 'source': 'office_file.mdx'}page_content='\n' metadata={'line_number': 4, 'source': 'office_file.mdx'}page_content='This covers how to load commonly used file formats including `DOCX`, `XLSX` and `PPTX` documents into a document format that we can use downstream.\n' metadata={'line_number': 5, 'source': 'office_file.mdx'}... output truncated for demo purposes
```

#### Custom Generic Loader​
If you really like creating classes, you can sub-class and create a class to encapsulate the logic together.
You can sub-class from this class to load content using an existing loader.
```
from typing import AnyclassMyCustomLoader(GenericLoader):@staticmethoddefget_parser(**kwargs: Any)-> BaseBlobParser:"""Override this method to associate a default parser with the class."""return MyParser()
```

```
loader = MyCustomLoader.from_filesystem(path=".", glob="*.mdx", show_progress=True)for idx, doc inenumerate(loader.lazy_load()):if idx <5:print(doc)print("... output truncated for demo purposes")
```

```
 0%|     | 0/8 [00:00<?, ?it/s]
```

```
page_content='# Microsoft Office\n' metadata={'line_number': 1, 'source': 'office_file.mdx'}page_content='\n' metadata={'line_number': 2, 'source': 'office_file.mdx'}page_content='>[The Microsoft Office](https://www.office.com/) suite of productivity software includes Microsoft Word, Microsoft Excel, Microsoft PowerPoint, Microsoft Outlook, and Microsoft OneNote. It is available for Microsoft Windows and macOS operating systems. It is also available on Android and iOS.\n' metadata={'line_number': 3, 'source': 'office_file.mdx'}page_content='\n' metadata={'line_number': 4, 'source': 'office_file.mdx'}page_content='This covers how to load commonly used file formats including `DOCX`, `XLSX` and `PPTX` documents into a document format that we can use downstream.\n' metadata={'line_number': 5, 'source': 'office_file.mdx'}... output truncated for demo purposes
```

#### Was this page helpful?
  * Overview
  * Standard Document Loader
    * Interface
    * Implementation
    * Test 🧪
  * Working with Files
    * BaseBlobParser
    * Blob
    * Blob Loaders
    * Generic Loader


