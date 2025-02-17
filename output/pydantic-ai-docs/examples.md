Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# Examples
Examples of how to use PydanticAI and what it can do.
## Usage
These examples are distributed with `pydantic-ai` so you can run them either by cloning the pydantic-ai repo or by simply installing `pydantic-ai` from PyPI with `pip` or `uv`.
### Installing required dependencies
Either way you'll need to install extra dependencies to run some examples, you just need to install the `examples` optional dependency group.
If you've installed `pydantic-ai` via pip/uv, you can install the extra dependencies with:
pipuv
```
pipinstall'pydantic-ai[examples]'

```

```
uvadd'pydantic-ai[examples]'

```

If you clone the repo, you should instead use `uv sync --extra examples` to install extra dependencies.
### Setting model environment variables
These examples will need you to set up authentication with one or more of the LLMs, see the model configuration docs for details on how to do this.
TL;DR: in most cases you'll need to set one of the following environment variables:
OpenAIGoogle Gemini
```
exportOPENAI_API_KEY=your-api-key

```

```
exportGEMINI_API_KEY=your-api-key

```

### Running Examples
To run the examples (this will work whether you installed `pydantic_ai`, or cloned the repo), run:
pipuv
```
python-mpydantic_ai_examples.<example_module_name>

```

```
uvrun-mpydantic_ai_examples.<example_module_name>

```

For examples, to run the very simple `pydantic_model` example:
pipuv
```
python-mpydantic_ai_examples.pydantic_model

```

```
uvrun-mpydantic_ai_examples.pydantic_model

```

If you like one-liners and you're using uv, you can run a pydantic-ai example with zero setup:
```
OPENAI_API_KEY='your-api-key'\
uvrun--with'pydantic-ai[examples]'\
-mpydantic_ai_examples.pydantic_model

```

You'll probably want to edit examples in addition to just running them. You can copy the examples to a new directory with:
pipuv
```
python-mpydantic_ai_examples--copy-toexamples/

```

```
uvrun-mpydantic_ai_examples--copy-toexamples/

```

