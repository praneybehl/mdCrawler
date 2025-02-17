Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Prerequisites
This guide assumes familiarity with the following concepts:
  * Chat models
  * LLMs


You may find yourself in a situation where you are getting rate limited by the model provider API because you're making too many requests.
For example, this might happen if you are running many parallel queries to benchmark the chat model on a test dataset.
If you are facing such a situation, you can use a rate limiter to help match the rate at which you're making request to the rate allowed by the API.
Requires `langchain-core >= 0.2.24`
This functionality was added in `langchain-core == 0.2.24`. Please make sure your package is up to date.
## Initialize a rate limiter​
Langchain comes with a built-in in memory rate limiter. This rate limiter is thread safe and can be shared by multiple threads in the same process.
The provided rate limiter can only limit the number of requests per unit time. It will not help if you need to also limit based on the size of the requests.
```
from langchain_core.rate_limiters import InMemoryRateLimiterrate_limiter = InMemoryRateLimiter(  requests_per_second=0.1,# <-- Super slow! We can only make a request once every 10 seconds!!  check_every_n_seconds=0.1,# Wake up every 100 ms to check whether allowed to make a request,  max_bucket_size=10,# Controls the maximum burst size.)
```

**API Reference:**InMemoryRateLimiter
## Choose a model​
Choose any model and pass to it the rate_limiter via the `rate_limiter` attribute.
```
import osimport timefrom getpass import getpassif"ANTHROPIC_API_KEY"notin os.environ:  os.environ["ANTHROPIC_API_KEY"]= getpass()from langchain_anthropic import ChatAnthropicmodel = ChatAnthropic(model_name="claude-3-opus-20240229", rate_limiter=rate_limiter)
```

**API Reference:**ChatAnthropic
Let's confirm that the rate limiter works. We should only be able to invoke the model once per 10 seconds.
```
for _ inrange(5):  tic = time.time()  model.invoke("hello")  toc = time.time()print(toc - tic)
```

```
11.59907364845275910.750212192535410.2442579269409188.8308875560760511.645203590393066
```

#### Was this page helpful?
  * Initialize a rate limiter
  * Choose a model


