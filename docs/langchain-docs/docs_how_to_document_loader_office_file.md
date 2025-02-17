Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The Microsoft Office suite of productivity software includes Microsoft Word, Microsoft Excel, Microsoft PowerPoint, Microsoft Outlook, and Microsoft OneNote. It is available for Microsoft Windows and macOS operating systems. It is also available on Android and iOS.
This covers how to load commonly used file formats including `DOCX`, `XLSX` and `PPTX` documents into a LangChain Document object that we can use downstream.
## Loading DOCX, XLSX, PPTX with AzureAIDocumentIntelligenceLoader​
Azure AI Document Intelligence (formerly known as `Azure Form Recognizer`) is machine-learning based service that extracts texts (including handwriting), tables, document structures (e.g., titles, section headings, etc.) and key-value-pairs from digital or scanned PDFs, images, Office and HTML files. Document Intelligence supports `PDF`, `JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF`, `DOCX`, `XLSX`, `PPTX` and `HTML`.
This current implementation of a loader using `Document Intelligence` can incorporate content page-wise and turn it into LangChain documents. The default output format is markdown, which can be easily chained with `MarkdownHeaderTextSplitter` for semantic document chunking. You can also use `mode="single"` or `mode="page"` to return pure texts in a single page or document split by page.
### Prerequisite​
An Azure AI Document Intelligence resource in one of the 3 preview regions: **East US** , **West US2** , **West Europe** - follow this document to create one if you don't have. You will be passing `<endpoint>` and `<key>` as parameters to the loader.
```
%pip install --upgrade --quiet langchain langchain-community azure-ai-documentintelligencefrom langchain_community.document_loaders import AzureAIDocumentIntelligenceLoaderfile_path ="<filepath>"endpoint ="<endpoint>"key ="<key>"loader = AzureAIDocumentIntelligenceLoader(  api_endpoint=endpoint, api_key=key, file_path=file_path, api_model="prebuilt-layout")documents = loader.load()
```

**API Reference:**AzureAIDocumentIntelligenceLoader
#### Was this page helpful?
  * Loading DOCX, XLSX, PPTX with AzureAIDocumentIntelligenceLoader
    * Prerequisite


