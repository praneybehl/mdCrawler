Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.usage`
###  Usage `dataclass`
LLM usage associated with a request or run.
Responsibility for calculating usage is on the model; PydanticAI simply sums the usage information across requests.
You'll need to look up the documentation of the model you're using to convert usage to monetary costs.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
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
45
46
47
48
49
50
51
52
53
54
55
56
57
```
| ```
@dataclass
class Usage:
"""LLM usage associated with a request or run.
  Responsibility for calculating usage is on the model; PydanticAI simply sums the usage information across requests.
  You'll need to look up the documentation of the model you're using to convert usage to monetary costs.
  """
  requests: int = 0
"""Number of requests made to the LLM API."""
  request_tokens: int | None = None
"""Tokens used in processing requests."""
  response_tokens: int | None = None
"""Tokens used in generating responses."""
  total_tokens: int | None = None
"""Total tokens used in the whole run, should generally be equal to `request_tokens + response_tokens`."""
  details: dict[str, int] | None = None
"""Any extra details returned by the model."""
  def incr(self, incr_usage: Usage, *, requests: int = 0) -> None:
"""Increment the usage in place.
    Args:
      incr_usage: The usage to increment by.
      requests: The number of requests to increment by in addition to `incr_usage.requests`.
    """
    self.requests += requests
    for f in 'requests', 'request_tokens', 'response_tokens', 'total_tokens':
      self_value = getattr(self, f)
      other_value = getattr(incr_usage, f)
      if self_value is not None or other_value is not None:
        setattr(self, f, (self_value or 0) + (other_value or 0))
    if incr_usage.details:
      self.details = self.details or {}
      for key, value in incr_usage.details.items():
        self.details[key] = self.details.get(key, 0) + value
  def __add__(self, other: Usage) -> Usage:
"""Add two Usages together.
    This is provided so it's trivial to sum usage information from multiple requests and runs.
    """
    new_usage = copy(self)
    new_usage.incr(other)
    return new_usage

```
  
---|---  
####  requests `class-attribute` `instance-attribute`
```
requests: int = 0

```

Number of requests made to the LLM API.
####  request_tokens `class-attribute` `instance-attribute`
```
request_tokens: int | None = None

```

Tokens used in processing requests.
####  response_tokens `class-attribute` `instance-attribute`
```
response_tokens: int | None = None

```

Tokens used in generating responses.
####  total_tokens `class-attribute` `instance-attribute`
```
total_tokens: int | None = None

```

Total tokens used in the whole run, should generally be equal to `request_tokens + response_tokens`.
####  details `class-attribute` `instance-attribute`
```
details: dict[str, int] | None = None

```

Any extra details returned by the model.
####  incr
```
incr(incr_usage: Usage, *, requests: int = 0) -> None

```

Increment the usage in place.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`incr_usage` |  `Usage` |  The usage to increment by. |  _required_  
`requests` |  `int` |  The number of requests to increment by in addition to `incr_usage.requests`. |  `0`  
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
31
32
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
45
46
47
48
```
| ```
def incr(self, incr_usage: Usage, *, requests: int = 0) -> None:
"""Increment the usage in place.
  Args:
    incr_usage: The usage to increment by.
    requests: The number of requests to increment by in addition to `incr_usage.requests`.
  """
  self.requests += requests
  for f in 'requests', 'request_tokens', 'response_tokens', 'total_tokens':
    self_value = getattr(self, f)
    other_value = getattr(incr_usage, f)
    if self_value is not None or other_value is not None:
      setattr(self, f, (self_value or 0) + (other_value or 0))
  if incr_usage.details:
    self.details = self.details or {}
    for key, value in incr_usage.details.items():
      self.details[key] = self.details.get(key, 0) + value

```
  
---|---  
####  __add__
```
__add__(other: Usage) -> Usage

```

Add two Usages together.
This is provided so it's trivial to sum usage information from multiple requests and runs.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
50
51
52
53
54
55
56
57
```
| ```
def __add__(self, other: Usage) -> Usage:
"""Add two Usages together.
  This is provided so it's trivial to sum usage information from multiple requests and runs.
  """
  new_usage = copy(self)
  new_usage.incr(other)
  return new_usage

```
  
---|---  
###  UsageLimits `dataclass`
Limits on model usage.
The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model. Token counts are provided in responses from the model, and the token limits are checked after each response.
Each of the limits can be set to `None` to disable that limit.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
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
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
```
| ```
@dataclass
class UsageLimits:
"""Limits on model usage.
  The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model.
  Token counts are provided in responses from the model, and the token limits are checked after each response.
  Each of the limits can be set to `None` to disable that limit.
  """
  request_limit: int | None = 50
"""The maximum number of requests allowed to the model."""
  request_tokens_limit: int | None = None
"""The maximum number of tokens allowed in requests to the model."""
  response_tokens_limit: int | None = None
"""The maximum number of tokens allowed in responses from the model."""
  total_tokens_limit: int | None = None
"""The maximum number of tokens allowed in requests and responses combined."""
  def has_token_limits(self) -> bool:
"""Returns `True` if this instance places any limits on token counts.
    If this returns `False`, the `check_tokens` method will never raise an error.
    This is useful because if we have token limits, we need to check them after receiving each streamed message.
    If there are no limits, we can skip that processing in the streaming response iterator.
    """
    return any(
      limit is not None
      for limit in (self.request_tokens_limit, self.response_tokens_limit, self.total_tokens_limit)
    )
  def check_before_request(self, usage: Usage) -> None:
"""Raises a `UsageLimitExceeded` exception if the next request would exceed the request_limit."""
    request_limit = self.request_limit
    if request_limit is not None and usage.requests >= request_limit:
      raise UsageLimitExceeded(f'The next request would exceed the request_limit of {request_limit}')
  def check_tokens(self, usage: Usage) -> None:
"""Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits."""
    request_tokens = usage.request_tokens or 0
    if self.request_tokens_limit is not None and request_tokens > self.request_tokens_limit:
      raise UsageLimitExceeded(
        f'Exceeded the request_tokens_limit of {self.request_tokens_limit} ({request_tokens=})'
      )
    response_tokens = usage.response_tokens or 0
    if self.response_tokens_limit is not None and response_tokens > self.response_tokens_limit:
      raise UsageLimitExceeded(
        f'Exceeded the response_tokens_limit of {self.response_tokens_limit} ({response_tokens=})'
      )
    total_tokens = usage.total_tokens or 0
    if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
      raise UsageLimitExceeded(f'Exceeded the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})')

```
  
---|---  
####  request_limit `class-attribute` `instance-attribute`
```
request_limit: int | None = 50

```

The maximum number of requests allowed to the model.
####  request_tokens_limit `class-attribute` `instance-attribute`
```
request_tokens_limit: int | None = None

```

The maximum number of tokens allowed in requests to the model.
####  response_tokens_limit `class-attribute` `instance-attribute`
```
response_tokens_limit: int | None = None

```

The maximum number of tokens allowed in responses from the model.
####  total_tokens_limit `class-attribute` `instance-attribute`
```
total_tokens_limit: int | None = None

```

The maximum number of tokens allowed in requests and responses combined.
####  has_token_limits
```
has_token_limits() -> bool

```

Returns `True` if this instance places any limits on token counts.
If this returns `False`, the `check_tokens` method will never raise an error.
This is useful because if we have token limits, we need to check them after receiving each streamed message. If there are no limits, we can skip that processing in the streaming response iterator.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
79
80
81
82
83
84
85
86
87
88
89
90
```
| ```
def has_token_limits(self) -> bool:
"""Returns `True` if this instance places any limits on token counts.
  If this returns `False`, the `check_tokens` method will never raise an error.
  This is useful because if we have token limits, we need to check them after receiving each streamed message.
  If there are no limits, we can skip that processing in the streaming response iterator.
  """
  return any(
    limit is not None
    for limit in (self.request_tokens_limit, self.response_tokens_limit, self.total_tokens_limit)
  )

```
  
---|---  
####  check_before_request
```
check_before_request(usage: Usage) -> None

```

Raises a `UsageLimitExceeded` exception if the next request would exceed the request_limit.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
92
93
94
95
96
```
| ```
def check_before_request(self, usage: Usage) -> None:
"""Raises a `UsageLimitExceeded` exception if the next request would exceed the request_limit."""
  request_limit = self.request_limit
  if request_limit is not None and usage.requests >= request_limit:
    raise UsageLimitExceeded(f'The next request would exceed the request_limit of {request_limit}')

```
  
---|---  
####  check_tokens
```
check_tokens(usage: Usage) -> None

```

Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits.
Source code in `pydantic_ai_slim/pydantic_ai/usage.py`
```
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
```
| ```
def check_tokens(self, usage: Usage) -> None:
"""Raises a `UsageLimitExceeded` exception if the usage exceeds any of the token limits."""
  request_tokens = usage.request_tokens or 0
  if self.request_tokens_limit is not None and request_tokens > self.request_tokens_limit:
    raise UsageLimitExceeded(
      f'Exceeded the request_tokens_limit of {self.request_tokens_limit} ({request_tokens=})'
    )
  response_tokens = usage.response_tokens or 0
  if self.response_tokens_limit is not None and response_tokens > self.response_tokens_limit:
    raise UsageLimitExceeded(
      f'Exceeded the response_tokens_limit of {self.response_tokens_limit} ({response_tokens=})'
    )
  total_tokens = usage.total_tokens or 0
  if self.total_tokens_limit is not None and total_tokens > self.total_tokens_limit:
    raise UsageLimitExceeded(f'Exceeded the total_tokens_limit of {self.total_tokens_limit} ({total_tokens=})')

```
  
---|---
