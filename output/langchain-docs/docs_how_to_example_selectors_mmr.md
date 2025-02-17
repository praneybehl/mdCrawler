Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
The `MaxMarginalRelevanceExampleSelector` selects examples based on a combination of which examples are most similar to the inputs, while also optimizing for diversity. It does this by finding the examples with the embeddings that have the greatest cosine similarity with the inputs, and then iteratively adding them while penalizing them for closeness to already selected examples.
```
from langchain_community.vectorstores import FAISSfrom langchain_core.example_selectors import(  MaxMarginalRelevanceExampleSelector,  SemanticSimilarityExampleSelector,)from langchain_core.prompts import FewShotPromptTemplate, PromptTemplatefrom langchain_openai import OpenAIEmbeddingsexample_prompt = PromptTemplate(  input_variables=["input","output"],  template="Input: {input}\nOutput: {output}",)# Examples of a pretend task of creating antonyms.examples =[{"input":"happy","output":"sad"},{"input":"tall","output":"short"},{"input":"energetic","output":"lethargic"},{"input":"sunny","output":"gloomy"},{"input":"windy","output":"calm"},]
```

**API Reference:**FAISS | MaxMarginalRelevanceExampleSelector | SemanticSimilarityExampleSelector | FewShotPromptTemplate | PromptTemplate | OpenAIEmbeddings
```
example_selector = MaxMarginalRelevanceExampleSelector.from_examples(# The list of examples available to select from.  examples,# The embedding class used to produce embeddings which are used to measure semantic similarity.  OpenAIEmbeddings(),# The VectorStore class that is used to store the embeddings and do a similarity search over.  FAISS,# The number of examples to produce.  k=2,)mmr_prompt = FewShotPromptTemplate(# We provide an ExampleSelector instead of examples.  example_selector=example_selector,  example_prompt=example_prompt,  prefix="Give the antonym of every input",  suffix="Input: {adjective}\nOutput:",  input_variables=["adjective"],)
```

```
# Input is a feeling, so should select the happy/sad example as the first oneprint(mmr_prompt.format(adjective="worried"))
```

```
Give the antonym of every inputInput: happyOutput: sadInput: windyOutput: calmInput: worriedOutput:
```

```
# Let's compare this to what we would just get if we went solely off of similarity,# by using SemanticSimilarityExampleSelector instead of MaxMarginalRelevanceExampleSelector.example_selector = SemanticSimilarityExampleSelector.from_examples(# The list of examples available to select from.  examples,# The embedding class used to produce embeddings which are used to measure semantic similarity.  OpenAIEmbeddings(),# The VectorStore class that is used to store the embeddings and do a similarity search over.  FAISS,# The number of examples to produce.  k=2,)similar_prompt = FewShotPromptTemplate(# We provide an ExampleSelector instead of examples.  example_selector=example_selector,  example_prompt=example_prompt,  prefix="Give the antonym of every input",  suffix="Input: {adjective}\nOutput:",  input_variables=["adjective"],)print(similar_prompt.format(adjective="worried"))
```

```
Give the antonym of every inputInput: happyOutput: sadInput: sunnyOutput: gloomyInput: worriedOutput:
```

#### Was this page helpful?
