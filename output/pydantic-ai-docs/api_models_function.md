Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.models.function`
A model controlled by a local function.
`FunctionModel` is similar to `TestModel`, but allows greater control over the model's behavior.
Its primary use case is for more advanced unit testing than is possible with `TestModel`.
Here's a minimal example:
function_model_usage.py```
from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel, AgentInfo
my_agent = Agent('openai:gpt-4o')

async def model_function(
  messages: list[ModelMessage], info: AgentInfo
) -> ModelResponse:
  print(messages)
"""
  [
    ModelRequest(
      parts=[
        UserPromptPart(
          content='Testing my agent...',
          timestamp=datetime.datetime(...),
          part_kind='user-prompt',
        )
      ],
      kind='request',
    )
  ]
  """
  print(info)
"""
  AgentInfo(
    function_tools=[], allow_text_result=True, result_tools=[], model_settings=None
  )
  """
  return ModelResponse(parts=[TextPart('hello world')])

async def test_my_agent():
"""Unit test for my_agent, to be run by pytest."""
  with my_agent.override(model=FunctionModel(model_function)):
    result = await my_agent.run('Testing my agent...')
    assert result.data == 'hello world'

```

See Unit testing with `FunctionModel` for detailed documentation.
###  FunctionModel `dataclass`
Bases: `Model`
A model controlled by a local function.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
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
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
```
| ```
@dataclass(init=False)
class FunctionModel(Model):
"""A model controlled by a local function.
  Apart from `__init__`, all methods are private or match those of the base class.
  """
  function: FunctionDef | None = None
  stream_function: StreamFunctionDef | None = None
  _model_name: str = field(repr=False)
  _system: str | None = field(default=None, repr=False)
  @overload
  def __init__(self, function: FunctionDef) -> None: ...
  @overload
  def __init__(self, *, stream_function: StreamFunctionDef) -> None: ...
  @overload
  def __init__(self, function: FunctionDef, *, stream_function: StreamFunctionDef) -> None: ...
  def __init__(self, function: FunctionDef | None = None, *, stream_function: StreamFunctionDef | None = None):
"""Initialize a `FunctionModel`.
    Either `function` or `stream_function` must be provided, providing both is allowed.
    Args:
      function: The function to call for non-streamed requests.
      stream_function: The function to call for streamed requests.
    """
    if function is None and stream_function is None:
      raise TypeError('Either `function` or `stream_function` must be provided')
    self.function = function
    self.stream_function = stream_function
    function_name = self.function.__name__ if self.function is not None else ''
    stream_function_name = self.stream_function.__name__ if self.stream_function is not None else ''
    self._model_name = f'function:{function_name}:{stream_function_name}'
  async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, usage.Usage]:
    agent_info = AgentInfo(
      model_request_parameters.function_tools,
      model_request_parameters.allow_text_result,
      model_request_parameters.result_tools,
      model_settings,
    )
    assert self.function is not None, 'FunctionModel must receive a `function` to support non-streamed requests'
    if inspect.iscoroutinefunction(self.function):
      response = await self.function(messages, agent_info)
    else:
      response_ = await _utils.run_in_executor(self.function, messages, agent_info)
      assert isinstance(response_, ModelResponse), response_
      response = response_
    response.model_name = f'function:{self.function.__name__}'
    # TODO is `messages` right here? Should it just be new messages?
    return response, _estimate_usage(chain(messages, [response]))
  @asynccontextmanager
  async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncIterator[StreamedResponse]:
    agent_info = AgentInfo(
      model_request_parameters.function_tools,
      model_request_parameters.allow_text_result,
      model_request_parameters.result_tools,
      model_settings,
    )
    assert (
      self.stream_function is not None
    ), 'FunctionModel must receive a `stream_function` to support streamed requests'
    response_stream = PeekableAsyncStream(self.stream_function(messages, agent_info))
    first = await response_stream.peek()
    if isinstance(first, _utils.Unset):
      raise ValueError('Stream function must return at least one item')
    yield FunctionStreamedResponse(_model_name=f'function:{self.stream_function.__name__}', _iter=response_stream)
  @property
  def model_name(self) -> str:
"""The model name."""
    return self._model_name
  @property
  def system(self) -> str | None:
"""The system / model provider."""
    return self._system

```
  
---|---  
####  __init__
```
__init__(function: FunctionDef) -> None

```

```
__init__(*, stream_function: StreamFunctionDef) -> None

```

```
__init__(
  function: FunctionDef,
  *,
  stream_function: StreamFunctionDef
) -> None

```

```
__init__(
  function: FunctionDef | None = None,
  *,
  stream_function: StreamFunctionDef | None = None
)

```

Initialize a `FunctionModel`.
Either `function` or `stream_function` must be provided, providing both is allowed.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `FunctionDef | None` |  The function to call for non-streamed requests. |  `None`  
`stream_function` |  `StreamFunctionDef | None` |  The function to call for streamed requests. |  `None`  
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
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
```
| ```
def __init__(self, function: FunctionDef | None = None, *, stream_function: StreamFunctionDef | None = None):
"""Initialize a `FunctionModel`.
  Either `function` or `stream_function` must be provided, providing both is allowed.
  Args:
    function: The function to call for non-streamed requests.
    stream_function: The function to call for streamed requests.
  """
  if function is None and stream_function is None:
    raise TypeError('Either `function` or `stream_function` must be provided')
  self.function = function
  self.stream_function = stream_function
  function_name = self.function.__name__ if self.function is not None else ''
  stream_function_name = self.stream_function.__name__ if self.stream_function is not None else ''
  self._model_name = f'function:{function_name}:{stream_function_name}'

```
  
---|---  
####  model_name `property`
```
model_name: str

```

The model name.
####  system `property`
```
system: str | None

```

The system / model provider.
###  AgentInfo `dataclass`
Information about an agent.
This is passed as the second to functions used within `FunctionModel`.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
```
| ```
@dataclass(frozen=True)
class AgentInfo:
"""Information about an agent.
  This is passed as the second to functions used within [`FunctionModel`][pydantic_ai.models.function.FunctionModel].
  """
  function_tools: list[ToolDefinition]
"""The function tools available on this agent.
  These are the tools registered via the [`tool`][pydantic_ai.Agent.tool] and
  [`tool_plain`][pydantic_ai.Agent.tool_plain] decorators.
  """
  allow_text_result: bool
"""Whether a plain text result is allowed."""
  result_tools: list[ToolDefinition]
"""The tools that can called as the final result of the run."""
  model_settings: ModelSettings | None
"""The model settings passed to the run call."""

```
  
---|---  
####  function_tools `instance-attribute`
```
function_tools: list[ToolDefinition]

```

The function tools available on this agent.
These are the tools registered via the `tool` and `tool_plain` decorators.
####  allow_text_result `instance-attribute`
```
allow_text_result: bool

```

Whether a plain text result is allowed.
####  result_tools `instance-attribute`
```
result_tools: list[ToolDefinition]

```

The tools that can called as the final result of the run.
####  model_settings `instance-attribute`
```
model_settings: ModelSettings | None

```

The model settings passed to the run call.
###  DeltaToolCall `dataclass`
Incremental change to a tool call.
Used to describe a chunk when streaming structured responses.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
156
157
158
159
160
161
162
163
164
165
166
```
| ```
@dataclass
class DeltaToolCall:
"""Incremental change to a tool call.
  Used to describe a chunk when streaming structured responses.
  """
  name: str | None = None
"""Incremental change to the name of the tool."""
  json_args: str | None = None
"""Incremental change to the arguments as JSON"""

```
  
---|---  
####  name `class-attribute` `instance-attribute`
```
name: str | None = None

```

Incremental change to the name of the tool.
####  json_args `class-attribute` `instance-attribute`
```
json_args: str | None = None

```

Incremental change to the arguments as JSON
###  DeltaToolCalls `module-attribute`
```
DeltaToolCalls: TypeAlias = dict[int, DeltaToolCall]

```

A mapping of tool call IDs to incremental changes.
###  FunctionDef `module-attribute`
```
FunctionDef: TypeAlias = Callable[
  [list[ModelMessage], AgentInfo],
  Union[ModelResponse, Awaitable[ModelResponse]],
]

```

A function used to generate a non-streamed response.
###  StreamFunctionDef `module-attribute`
```
StreamFunctionDef: TypeAlias = Callable[
  [list[ModelMessage], AgentInfo],
  AsyncIterator[Union[str, DeltaToolCalls]],
]

```

A function used to generate a streamed response.
While this is defined as having return type of `AsyncIterator[Union[str, DeltaToolCalls]]`, it should really be considered as `Union[AsyncIterator[str], AsyncIterator[DeltaToolCalls]`,
E.g. you need to yield all text or all `DeltaToolCalls`, not mix them.
###  FunctionStreamedResponse `dataclass`
Bases: `StreamedResponse`
Implementation of `StreamedResponse` for FunctionModel.
Source code in `pydantic_ai_slim/pydantic_ai/models/function.py`
```
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
```
| ```
@dataclass
class FunctionStreamedResponse(StreamedResponse):
"""Implementation of `StreamedResponse` for [FunctionModel][pydantic_ai.models.function.FunctionModel]."""
  _model_name: str
  _iter: AsyncIterator[str | DeltaToolCalls]
  _timestamp: datetime = field(default_factory=_utils.now_utc)
  def __post_init__(self):
    self._usage += _estimate_usage([])
  async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
    async for item in self._iter:
      if isinstance(item, str):
        response_tokens = _estimate_string_tokens(item)
        self._usage += usage.Usage(response_tokens=response_tokens, total_tokens=response_tokens)
        yield self._parts_manager.handle_text_delta(vendor_part_id='content', content=item)
      else:
        delta_tool_calls = item
        for dtc_index, delta_tool_call in delta_tool_calls.items():
          if delta_tool_call.json_args:
            response_tokens = _estimate_string_tokens(delta_tool_call.json_args)
            self._usage += usage.Usage(response_tokens=response_tokens, total_tokens=response_tokens)
          maybe_event = self._parts_manager.handle_tool_call_delta(
            vendor_part_id=dtc_index,
            tool_name=delta_tool_call.name,
            args=delta_tool_call.json_args,
            tool_call_id=None,
          )
          if maybe_event is not None:
            yield maybe_event
  @property
  def model_name(self) -> str:
"""Get the model name of the response."""
    return self._model_name
  @property
  def timestamp(self) -> datetime:
"""Get the timestamp of the response."""
    return self._timestamp

```
  
---|---  
####  model_name `property`
```
model_name: str

```

Get the model name of the response.
####  timestamp `property`
```
timestamp: datetime

```

Get the timestamp of the response.
