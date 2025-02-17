Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_graph.exceptions`
###  GraphSetupError
Bases: `TypeError`
Error caused by an incorrectly configured graph.
Source code in `pydantic_graph/pydantic_graph/exceptions.py`
```
1
2
3
4
5
6
7
8
9
```
| ```
class GraphSetupError(TypeError):
"""Error caused by an incorrectly configured graph."""
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
###  GraphRuntimeError
Bases: `RuntimeError`
Error caused by an issue during graph execution.
Source code in `pydantic_graph/pydantic_graph/exceptions.py`
```
12
13
14
15
16
17
18
19
20
```
| ```
class GraphRuntimeError(RuntimeError):
"""Error caused by an issue during graph execution."""
  message: str
"""The error message."""
  def __init__(self, message: str):
    self.message = message
    super().__init__(message)

```
  
---|---  
####  message `instance-attribute`
```
message: str = message

```

The error message.
