Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Development
Local Setup
DocumentationCloud API
##### Get Started
  * Introduction
  * Quickstart


##### Customize
  * Supported Models
  * Agent Settings
  * Browser Settings
  * Connect to your Browser
  * Output Format
  * System Prompt
  * Sensitive Data
  * Custom Functions


##### Development
  * Local Setup
  * Telemetry
  * Observability
  * Roadmap


## 
​
Prerequisites
Browser Use requires Python 3.11 or higher. We recommend using uv for Python environment management.
## 
​
Clone the Repository
First, clone the Browser Use repository:
Copy
```
git clone https://github.com/browser-use/browser-use
cd browser-use

```

## 
​
Environment Setup
  1. Create a virtual environment:


Copy
```
uv venv --python 3.11

```

  1. Install dependencies:


Copy
```
# Install the package in editable mode with all development dependencies
uv pip install -e ".[dev]"

```

The `-e` flag installs the package in “editable” mode, which means your local code changes will be reflected immediately without requiring reinstallation. The `[dev]` part installs additional dependencies needed for development.
## 
​
Configuration
Set up your environment variables:
Copy
```
# Copy the example environment file
cp .env.example .env

```

Or manually create a `.env` file with your API keys:
.env
Copy
```
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

```

You can use any LLM model supported by LangChain. See LangChain Models for available options and their specific API key requirements.
## 
​
Development
After setup, you can:
  * Run tests with `pytest`
  * Build the package with `hatch build`
  * Try the examples in the `examples/` directory


## 
​
Getting Help
If you run into any issues:
  1. Check our GitHub Issues
  2. Join our Discord community for support


We welcome contributions! See our Contribution Guide for guidelines on how to help improve Browser Use.
Was this page helpful?
YesNo
Custom FunctionsTelemetry
On this page
  * Prerequisites
  * Clone the Repository
  * Environment Setup
  * Configuration
  * Development
  * Getting Help


