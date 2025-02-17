Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
This text splitter is the recommended one for generic text. It is parameterized by a list of characters. It tries to split on them in order until the chunks are small enough. The default list is `["\n\n", "\n", " ", ""]`. This has the effect of trying to keep all paragraphs (and then sentences, and then words) together as long as possible, as those would generically seem to be the strongest semantically related pieces of text.
  1. How the text is split: by list of characters.
  2. How the chunk size is measured: by number of characters.


Below we show example usage.
To obtain the string content directly, use `.split_text`.
To create LangChain Document objects (e.g., for use in downstream tasks), use `.create_documents`.
```
%pip install -qU langchain-text-splitters
```

```
from langchain_text_splitters import RecursiveCharacterTextSplitter# Load example documentwithopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()text_splitter = RecursiveCharacterTextSplitter(# Set a really small chunk size, just to show.  chunk_size=100,  chunk_overlap=20,  length_function=len,  is_separator_regex=False,)texts = text_splitter.create_documents([state_of_the_union])print(texts[0])print(texts[1])
```

**API Reference:**RecursiveCharacterTextSplitter
```
page_content='Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and'page_content='of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.'
```

```
text_splitter.split_text(state_of_the_union)[:2]
```

```
['Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and', 'of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.']
```

Let's go through the parameters set above for `RecursiveCharacterTextSplitter`:
  * `chunk_size`: The maximum size of a chunk, where size is determined by the `length_function`.
  * `chunk_overlap`: Target overlap between chunks. Overlapping chunks helps to mitigate loss of information when context is divided between chunks.
  * `length_function`: Function determining the chunk size.
  * `is_separator_regex`: Whether the separator list (defaulting to `["\n\n", "\n", " ", ""]`) should be interpreted as regex.


## Splitting text from languages without word boundaries​
Some writing systems do not have word boundaries, for example Chinese, Japanese, and Thai. Splitting text with the default separator list of `["\n\n", "\n", " ", ""]` can cause words to be split between chunks. To keep words together, you can override the list of separators to include additional punctuation:
  * Add ASCII full-stop "`.`", Unicode fullwidth full stop "`．`" (used in Chinese text), and ideographic full stop "`。`" (used in Japanese and Chinese)
  * Add Zero-width space used in Thai, Myanmar, Kmer, and Japanese.
  * Add ASCII comma "`,`", Unicode fullwidth comma "`，`", and Unicode ideographic comma "`、`"


```
text_splitter = RecursiveCharacterTextSplitter(  separators=["\n\n","\n"," ",".",",","\u200b",# Zero-width space"\uff0c",# Fullwidth comma"\u3001",# Ideographic comma"\uff0e",# Fullwidth full stop"\u3002",# Ideographic full stop"",],# Existing args)
```

#### Was this page helpful?
  * Splitting text from languages without word boundaries


