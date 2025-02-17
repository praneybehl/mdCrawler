Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Follow this guide if you're trying to migrate off one of the old memory classes listed below:
Memory Type| Description  
---|---  
`ConversationSummaryMemory`| Continually summarizes the conversation history. The summary is updated after each conversation turn. The abstraction returns the summary of the conversation history.  
`ConversationSummaryBufferMemory`| Provides a running summary of the conversation together with the most recent messages in the conversation under the constraint that the total number of tokens in the conversation does not exceed a certain limit.  
Please follow the following how-to guide on summarization in LangGraph.
This guide shows how to maintain a running summary of the conversation while discarding older messages, ensuring they aren't re-processed during later turns.
#### Was this page helpful?
