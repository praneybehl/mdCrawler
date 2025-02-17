Browser Use home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/browseruse-0aece648/logo/dark.svg)
Search or ask...
Ctrl K
Search...
Navigation
Development
Telemetry
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
Overview
Browser Use collects anonymous usage data to help us understand how the library is being used and to improve the user experience. It also helps us fix bugs faster and prioritize feature development.
## 
​
Data Collection
We use PostHog for telemetry collection. The data is completely anonymized and contains no personally identifiable information.
We never collect personal information, credentials, or specific content from your browser automation tasks.
## 
​
Opting Out
You can disable telemetry by setting an environment variable:
.env
Copy
```
ANONYMIZED_TELEMETRY=false

```

Or in your Python code:
Copy
```
import os
os.environ["ANONYMIZED_TELEMETRY"] = "false"

```

Even when enabled, telemetry has zero impact on the library’s performance or functionality. Code is available in Telemetry Service.
Was this page helpful?
YesNo
Local SetupObservability
On this page
  * Overview
  * Data Collection
  * Opting Out


