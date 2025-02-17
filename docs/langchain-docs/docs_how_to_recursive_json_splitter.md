Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This json splitter splits json data while allowing control over chunk sizes. It traverses json data depth first and builds smaller json chunks. It attempts to keep nested json objects whole but will split them if needed to keep chunks between a min_chunk_size and the max_chunk_size.
If the value is not a nested json, but rather a very large string the string will not be split. If you need a hard cap on the chunk size consider composing this with a Recursive Text splitter on those chunks. There is an optional pre-processing step to split lists, by first converting them to json (dict) and then splitting them as such.
  1. How the text is split: json value.
  2. How the chunk size is measured: by number of characters.


```
%pip install -qU langchain-text-splitters
```

First we load some json data:
```
import jsonimport requests# This is a large nested json object and will be loaded as a python dictjson_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
```

## Basic usage​
Specify `max_chunk_size` to constrain chunk sizes:
```
from langchain_text_splitters import RecursiveJsonSplittersplitter = RecursiveJsonSplitter(max_chunk_size=300)
```

**API Reference:**RecursiveJsonSplitter
To obtain json chunks, use the `.split_json` method:
```
# Recursively split json data - If you need to access/manipulate the smaller json chunksjson_chunks = splitter.split_json(json_data=json_data)for chunk in json_chunks[:3]:print(chunk)
```

```
{'openapi': '3.1.0', 'info': {'title': 'LangSmith', 'version': '0.1.0'}, 'servers': [{'url': 'https://api.smith.langchain.com', 'description': 'LangSmith API endpoint.'}]}{'paths': {'/api/v1/sessions/{session_id}': {'get': {'tags': ['tracer-sessions'], 'summary': 'Read Tracer Session', 'description': 'Get a specific session.', 'operationId': 'read_tracer_session_api_v1_sessions__session_id__get'}}}}{'paths': {'/api/v1/sessions/{session_id}': {'get': {'security': [{'API Key': []}, {'Tenant ID': []}, {'Bearer Auth': []}]}}}}
```

To obtain LangChain Document objects, use the `.create_documents` method:
```
# The splitter can also output documentsdocs = splitter.create_documents(texts=[json_data])for doc in docs[:3]:print(doc)
```

```
page_content='{"openapi": "3.1.0", "info": {"title": "LangSmith", "version": "0.1.0"}, "servers": [{"url": "https://api.smith.langchain.com", "description": "LangSmith API endpoint."}]}'page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}'page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"security": [{"API Key": []}, {"Tenant ID": []}, {"Bearer Auth": []}]}}}}'
```

Or use `.split_text` to obtain string content directly:
```
texts = splitter.split_text(json_data=json_data)print(texts[0])print(texts[1])
```

```
{"openapi": "3.1.0", "info": {"title": "LangSmith", "version": "0.1.0"}, "servers": [{"url": "https://api.smith.langchain.com", "description": "LangSmith API endpoint."}]}{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}
```

## How to manage chunk sizes from list content​
Note that one of the chunks in this example is larger than the specified `max_chunk_size` of 300. Reviewing one of these chunks that was bigger we see there is a list object there:
```
print([len(text)for text in texts][:10])print()print(texts[3])
```

```
[171, 231, 126, 469, 210, 213, 237, 271, 191, 232]{"paths": {"/api/v1/sessions/{session_id}": {"get": {"parameters": [{"name": "session_id", "in": "path", "required": true, "schema": {"type": "string", "format": "uuid", "title": "Session Id"}}, {"name": "include_stats", "in": "query", "required": false, "schema": {"type": "boolean", "default": false, "title": "Include Stats"}}, {"name": "accept", "in": "header", "required": false, "schema": {"anyOf": [{"type": "string"}, {"type": "null"}], "title": "Accept"}}]}}}}
```

The json splitter by default does not split lists.
Specify `convert_lists=True` to preprocess the json, converting list content to dicts with `index:item` as `key:val` pairs:
```
texts = splitter.split_text(json_data=json_data, convert_lists=True)
```

Let's look at the size of the chunks. Now they are all under the max
```
print([len(text)for text in texts][:10])
```

```
[176, 236, 141, 203, 212, 221, 210, 213, 242, 291]
```

The list has been converted to a dict, but retains all the needed contextual information even if split into many chunks:
```
print(texts[1])
```

```
{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": {"0": "tracer-sessions"}, "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}
```

```
# We can also look at the documentsdocs[1]
```

```
Document(page_content='{"paths": {"/api/v1/sessions/{session_id}": {"get": {"tags": ["tracer-sessions"], "summary": "Read Tracer Session", "description": "Get a specific session.", "operationId": "read_tracer_session_api_v1_sessions__session_id__get"}}}}')
```

#### Was this page helpful?
  * Basic usage
  * How to manage chunk sizes from list content


