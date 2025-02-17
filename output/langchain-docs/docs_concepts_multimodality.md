Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
## Overview​
**Multimodality** refers to the ability to work with data that comes in different forms, such as text, audio, images, and video. Multimodality can appear in various components, allowing models and systems to handle and process a mix of these data types seamlessly.
  * **Chat Models** : These could, in theory, accept and generate multimodal inputs and outputs, handling a variety of data types like text, images, audio, and video.
  * **Embedding Models** : Embedding Models can represent multimodal content, embedding various forms of data—such as text, images, and audio—into vector spaces.
  * **Vector Stores** : Vector stores could search over embeddings that represent multimodal data, enabling retrieval across different types of information.


## Multimodality in chat models​
Pre-requisites
  * Chat models
  * Messages


Multimodal support is still relatively new and less common, model providers have not yet standardized on the "best" way to define the API. As such, LangChain's multimodal abstractions are lightweight and flexible, designed to accommodate different model providers' APIs and interaction patterns, but are **not** standardized across models.
### How to use multimodal models​
  * Use the chat model integration table to identify which models support multimodality.
  * Reference the relevant how-to guides for specific examples of how to use multimodal models.


### What kind of multimodality is supported?​
#### Inputs​
Some models can accept multimodal inputs, such as images, audio, video, or files. The types of multimodal inputs supported depend on the model provider. For instance, Google's Gemini supports documents like PDFs as inputs.
Most chat models that support **multimodal inputs** also accept those values in OpenAI's content blocks format. So far this is restricted to image inputs. For models like Gemini which support video and other bytes input, the APIs also support the native, model-specific representations.
The gist of passing multimodal inputs to a chat model is to use content blocks that specify a type and corresponding data. For example, to pass an image to a chat model:
```
from langchain_core.messages import HumanMessagemessage = HumanMessage(  content=[{"type":"text","text":"describe the weather in this image"},{"type":"image_url","image_url":{"url": image_url}},],)response = model.invoke([message])
```

**API Reference:**HumanMessage
caution
The exact format of the content blocks may vary depending on the model provider. Please refer to the chat model's integration documentation for the correct format. Find the integration in the chat model integration table.
#### Outputs​
Virtually no popular chat models support multimodal outputs at the time of writing (October 2024).
The only exception is OpenAI's chat model (gpt-4o-audio-preview), which can generate audio outputs.
Multimodal outputs will appear as part of the AIMessage response object.
Please see the ChatOpenAI for more information on how to use multimodal outputs.
#### Tools​
Currently, no chat model is designed to work **directly** with multimodal data in a tool call request or ToolMessage result.
However, a chat model can easily interact with multimodal data by invoking tools with references (e.g., a URL) to the multimodal data, rather than the data itself. For example, any model capable of tool calling can be equipped with tools to download and process images, audio, or video.
## Multimodality in embedding models​
Prerequisites
  * Embedding Models


**Embeddings** are vector representations of data used for tasks like similarity search and retrieval.
The current embedding interface used in LangChain is optimized entirely for text-based data, and will **not** work with multimodal data.
As use cases involving multimodal search and retrieval tasks become more common, we expect to expand the embedding interface to accommodate other data types like images, audio, and video.
## Multimodality in vector stores​
Prerequisites
  * Vector stores


Vector stores are databases for storing and retrieving embeddings, which are typically used in search and retrieval tasks. Similar to embeddings, vector stores are currently optimized for text-based data.
As use cases involving multimodal search and retrieval tasks become more common, we expect to expand the vector store interface to accommodate other data types like images, audio, and video.
#### Was this page helpful?
  * Overview
  * Multimodality in chat models
    * How to use multimodal models
    * What kind of multimodality is supported?
  * Multimodality in embedding models
  * Multimodality in vector stores


