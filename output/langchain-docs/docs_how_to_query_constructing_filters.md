Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
We may want to do query analysis to extract filters to pass into retrievers. One way we ask the LLM to represent these filters is as a Pydantic model. There is then the issue of converting that Pydantic model into a filter that can be passed into a retriever.
This can be done manually, but LangChain also provides some "Translators" that are able to translate from a common syntax into filters specific to each retriever. Here, we will cover how to use those translators.
```
from typing import Optionalfrom langchain.chains.query_constructor.ir import(  Comparator,  Comparison,  Operation,  Operator,  StructuredQuery,)from langchain_community.query_constructors.chroma import ChromaTranslatorfrom langchain_community.query_constructors.elasticsearch import ElasticsearchTranslatorfrom pydantic import BaseModel
```

**API Reference:**Comparator | Comparison | Operation | Operator | StructuredQuery | ChromaTranslator | ElasticsearchTranslator
In this example, `year` and `author` are both attributes to filter on.
```
classSearch(BaseModel):  query:str  start_year: Optional[int]  author: Optional[str]
```

```
search_query = Search(query="RAG", start_year=2022, author="LangChain")
```

```
defconstruct_comparisons(query: Search):  comparisons =[]if query.start_year isnotNone:    comparisons.append(      Comparison(        comparator=Comparator.GT,        attribute="start_year",        value=query.start_year,))if query.author isnotNone:    comparisons.append(      Comparison(        comparator=Comparator.EQ,        attribute="author",        value=query.author,))return comparisons
```

```
comparisons = construct_comparisons(search_query)
```

```
_filter = Operation(operator=Operator.AND, arguments=comparisons)
```

```
ElasticsearchTranslator().visit_operation(_filter)
```

```
{'bool': {'must': [{'range': {'metadata.start_year': {'gt': 2022}}},  {'term': {'metadata.author.keyword': 'LangChain'}}]}}
```

```
ChromaTranslator().visit_operation(_filter)
```

```
{'$and': [{'start_year': {'$gt': 2022}}, {'author': {'$eq': 'LangChain'}}]}
```

#### Was this page helpful?
