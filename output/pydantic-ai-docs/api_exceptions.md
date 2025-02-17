Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.exceptions`
###  ModelRetry
Bases: `Exception`
Exception raised when a tool function should be retried.
The agent will return the message to the model and ask it to try calling the function/tool again.
Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`
```
 8
 9
10
11
12
13
14
15
16
17
18
19
```
| ```
class ModelRetry(Exception):
"""Exception raised when a tool function should be retried.
  The agent will return the message to the model and ask it to try calling the function/tool again.
  """
  message: str
"""The message to return to the model."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)

```
  
---|---  
####  message `instance-attribute`
```
message: str = message

```

The message to return to the model.
###  UserError
Bases: `RuntimeError`
Error caused by a usage mistake by the application developer — You!
Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`
```
22
23
24
25
26
27
28
29
30
```
| ```
class UserError(RuntimeError):
"""Error caused by a usage mistake by the application developer — You!"""
  message: str
"""Description of the mistake."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)

```
  
---|---  
####  message `instance-attribute`
```
message: str = message

```

Description of the mistake.
###  AgentRunError
Bases: `RuntimeError`
Base class for errors occurring during an agent run.
Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`
```
33
34
35
36
37
38
39
40
41
42
43
44
```
| ```
class AgentRunError(RuntimeError):
"""Base class for errors occurring during an agent run."""
  message: str
"""The error message."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)
  def __str__(self) -> str:
    return self.message

```
  
---|---  
####  message `instance-attribute`
```
message: str = message

```

The error message.
###  UsageLimitExceeded
Bases: `AgentRunError`
Error raised when a Model's usage exceeds the specified limits.
Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`
```
47
48
```
| ```
class UsageLimitExceeded(AgentRunError):
"""Error raised when a Model's usage exceeds the specified limits."""

```
  
---|---  
###  UnexpectedModelBehavior
Bases: `AgentRunError`
Error caused by unexpected Model behavior, e.g. an unexpected response code.
Source code in `pydantic_ai_slim/pydantic_ai/exceptions.py`
```
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
```
| ```
class UnexpectedModelBehavior(AgentRunError):
"""Error caused by unexpected Model behavior, e.g. an unexpected response code."""
  message: str
"""Description of the unexpected behavior."""
  body: str | None
"""The body of the response, if available."""
  def __init__(self, message: str, body: str | None = None):
    self.message = message
    if body is None:
      self.body: str | None = None
    else:
      try:
        self.body = json.dumps(json.loads(body), indent=2)
      except ValueError:
        self.body = body
    super().__init__(message)
  def __str__(self) -> str:
    if self.body:
      return f'{self.message}, body:\n{self.body}'
    else:
      return self.message

```
  
---|---  
####  message `instance-attribute`
```
message: str = message

```

Description of the unexpected behavior.
####  body `instance-attribute`
```
body: str | None = dumps(loads(body), indent=2)

```

The body of the response, if available.
