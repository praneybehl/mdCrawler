Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# Installation
PydanticAI is available on PyPI as `pydantic-ai` so installation is as simple as:
pipuv
```
pipinstallpydantic-ai

```

```
uvaddpydantic-ai

```

(Requires Python 3.9+)
This installs the `pydantic_ai` package, core dependencies, and libraries required to use all the models included in PydanticAI. If you want to use a specific model, you can install the "slim" version of PydanticAI.
## Use with Pydantic Logfire
PydanticAI has an excellent (but completely optional) integration with Pydantic Logfire to help you view and understand agent runs.
To use Logfire with PydanticAI, install `pydantic-ai` or `pydantic-ai-slim` with the `logfire` optional group:
pipuv
```
pipinstall'pydantic-ai[logfire]'

```

```
uvadd'pydantic-ai[logfire]'

```

From there, follow the Logfire setup docs to configure Logfire.
## Running Examples
We distribute the `pydantic_ai_examples` directory as a separate PyPI package (`pydantic-ai-examples`) to make examples extremely easy to customize and run.
To install examples, use the `examples` optional group:
pipuv
```
pipinstall'pydantic-ai[examples]'

```

```
uvadd'pydantic-ai[examples]'

```

To run the examples, follow instructions in the examples docs.
## Slim Install
If you know which model you're going to use and want to avoid installing superfluous packages, you can use the `pydantic-ai-slim` package. For example, if you're using just `OpenAIModel`, you would run:
pipuv
```
pipinstall'pydantic-ai-slim[openai]'

```

```
uvadd'pydantic-ai-slim[openai]'

```

`pydantic-ai-slim` has the following optional groups:
  * `logfire` — installs `logfire` PyPI ↗
  * `openai` — installs `openai` PyPI ↗
  * `vertexai` — installs `google-auth` PyPI ↗ and `requests` PyPI ↗
  * `anthropic` — installs `anthropic` PyPI ↗
  * `groq` — installs `groq` PyPI ↗
  * `mistral` — installs `mistralai` PyPI ↗
  * `cohere` - installs `cohere` PyPI ↗


See the models documentation for information on which optional dependencies are required for each model.
You can also install dependencies for multiple models and use cases, for example:
pipuv
```
pipinstall'pydantic-ai-slim[openai,vertexai,logfire]'

```

```
uvadd'pydantic-ai-slim[openai,vertexai,logfire]'

```

