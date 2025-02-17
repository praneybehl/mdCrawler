Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.models`
Logic related to making requests to an LLM.
The aim here is to make a common interface for different LLMs, so that the rest of the code can be agnostic to the specific LLM being used.
###  KnownModelName `module-attribute`
```
KnownModelName = Literal[
  "anthropic:claude-3-5-haiku-latest",
  "anthropic:claude-3-5-sonnet-latest",
  "anthropic:claude-3-opus-latest",
  "claude-3-5-haiku-latest",
  "claude-3-5-sonnet-latest",
  "claude-3-opus-latest",
  "cohere:c4ai-aya-expanse-32b",
  "cohere:c4ai-aya-expanse-8b",
  "cohere:command",
  "cohere:command-light",
  "cohere:command-light-nightly",
  "cohere:command-nightly",
  "cohere:command-r",
  "cohere:command-r-03-2024",
  "cohere:command-r-08-2024",
  "cohere:command-r-plus",
  "cohere:command-r-plus-04-2024",
  "cohere:command-r-plus-08-2024",
  "cohere:command-r7b-12-2024",
  "google-gla:gemini-1.0-pro",
  "google-gla:gemini-1.5-flash",
  "google-gla:gemini-1.5-flash-8b",
  "google-gla:gemini-1.5-pro",
  "google-gla:gemini-2.0-flash-exp",
  "google-gla:gemini-2.0-flash-thinking-exp-01-21",
  "google-gla:gemini-exp-1206",
  "google-gla:gemini-2.0-flash",
  "google-gla:gemini-2.0-flash-lite-preview-02-05",
  "google-vertex:gemini-1.0-pro",
  "google-vertex:gemini-1.5-flash",
  "google-vertex:gemini-1.5-flash-8b",
  "google-vertex:gemini-1.5-pro",
  "google-vertex:gemini-2.0-flash-exp",
  "google-vertex:gemini-2.0-flash-thinking-exp-01-21",
  "google-vertex:gemini-exp-1206",
  "google-vertex:gemini-2.0-flash",
  "google-vertex:gemini-2.0-flash-lite-preview-02-05",
  "gpt-3.5-turbo",
  "gpt-3.5-turbo-0125",
  "gpt-3.5-turbo-0301",
  "gpt-3.5-turbo-0613",
  "gpt-3.5-turbo-1106",
  "gpt-3.5-turbo-16k",
  "gpt-3.5-turbo-16k-0613",
  "gpt-4",
  "gpt-4-0125-preview",
  "gpt-4-0314",
  "gpt-4-0613",
  "gpt-4-1106-preview",
  "gpt-4-32k",
  "gpt-4-32k-0314",
  "gpt-4-32k-0613",
  "gpt-4-turbo",
  "gpt-4-turbo-2024-04-09",
  "gpt-4-turbo-preview",
  "gpt-4-vision-preview",
  "gpt-4o",
  "gpt-4o-2024-05-13",
  "gpt-4o-2024-08-06",
  "gpt-4o-2024-11-20",
  "gpt-4o-audio-preview",
  "gpt-4o-audio-preview-2024-10-01",
  "gpt-4o-audio-preview-2024-12-17",
  "gpt-4o-mini",
  "gpt-4o-mini-2024-07-18",
  "gpt-4o-mini-audio-preview",
  "gpt-4o-mini-audio-preview-2024-12-17",
  "groq:gemma2-9b-it",
  "groq:llama-3.1-8b-instant",
  "groq:llama-3.2-11b-vision-preview",
  "groq:llama-3.2-1b-preview",
  "groq:llama-3.2-3b-preview",
  "groq:llama-3.2-90b-vision-preview",
  "groq:llama-3.3-70b-specdec",
  "groq:llama-3.3-70b-versatile",
  "groq:llama3-70b-8192",
  "groq:llama3-8b-8192",
  "groq:mixtral-8x7b-32768",
  "mistral:codestral-latest",
  "mistral:mistral-large-latest",
  "mistral:mistral-moderation-latest",
  "mistral:mistral-small-latest",
  "o1",
  "o1-2024-12-17",
  "o1-mini",
  "o1-mini-2024-09-12",
  "o1-preview",
  "o1-preview-2024-09-12",
  "o3-mini",
  "o3-mini-2025-01-31",
  "openai:chatgpt-4o-latest",
  "openai:gpt-3.5-turbo",
  "openai:gpt-3.5-turbo-0125",
  "openai:gpt-3.5-turbo-0301",
  "openai:gpt-3.5-turbo-0613",
  "openai:gpt-3.5-turbo-1106",
  "openai:gpt-3.5-turbo-16k",
  "openai:gpt-3.5-turbo-16k-0613",
  "openai:gpt-4",
  "openai:gpt-4-0125-preview",
  "openai:gpt-4-0314",
  "openai:gpt-4-0613",
  "openai:gpt-4-1106-preview",
  "openai:gpt-4-32k",
  "openai:gpt-4-32k-0314",
  "openai:gpt-4-32k-0613",
  "openai:gpt-4-turbo",
  "openai:gpt-4-turbo-2024-04-09",
  "openai:gpt-4-turbo-preview",
  "openai:gpt-4-vision-preview",
  "openai:gpt-4o",
  "openai:gpt-4o-2024-05-13",
  "openai:gpt-4o-2024-08-06",
  "openai:gpt-4o-2024-11-20",
  "openai:gpt-4o-audio-preview",
  "openai:gpt-4o-audio-preview-2024-10-01",
  "openai:gpt-4o-audio-preview-2024-12-17",
  "openai:gpt-4o-mini",
  "openai:gpt-4o-mini-2024-07-18",
  "openai:gpt-4o-mini-audio-preview",
  "openai:gpt-4o-mini-audio-preview-2024-12-17",
  "openai:o1",
  "openai:o1-2024-12-17",
  "openai:o1-mini",
  "openai:o1-mini-2024-09-12",
  "openai:o1-preview",
  "openai:o1-preview-2024-09-12",
  "openai:o3-mini",
  "openai:o3-mini-2025-01-31",
  "test",
]

```

Known model names that can be used with the `model` parameter of `Agent`.
`KnownModelName` is provided as a concise way to specify a model.
###  ModelRequestParameters `dataclass`
Configuration for an agent's request to a model, specifically related to tools and result handling.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
168
169
170
171
172
173
174
```
| ```
@dataclass
class ModelRequestParameters:
"""Configuration for an agent's request to a model, specifically related to tools and result handling."""
  function_tools: list[ToolDefinition]
  allow_text_result: bool
  result_tools: list[ToolDefinition]

```
  
---|---  
###  Model
Bases: `ABC`
Abstract class for a model.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
177
178
179
180
181
182
183
184
185
186
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
```
| ```
class Model(ABC):
"""Abstract class for a model."""
  @abstractmethod
  async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, Usage]:
"""Make a request to the model."""
    raise NotImplementedError()
  @asynccontextmanager
  async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncIterator[StreamedResponse]:
"""Make a request to the model and return a streaming response."""
    # This method is not required, but you need to implement it if you want to support streamed responses
    raise NotImplementedError(f'Streamed requests not supported by this {self.__class__.__name__}')
    # yield is required to make this a generator for type checking
    # noinspection PyUnreachableCode
    yield # pragma: no cover
  @property
  @abstractmethod
  def model_name(self) -> str:
"""The model name."""
    raise NotImplementedError()
  @property
  @abstractmethod
  def system(self) -> str | None:
"""The system / model provider, ex: openai."""
    raise NotImplementedError()

```
  
---|---  
####  request `abstractmethod` `async`
```
request(
  messages: list[ModelMessage],
  model_settings: ModelSettings | None,
  model_request_parameters: ModelRequestParameters,
) -> tuple[ModelResponse, Usage]

```

Make a request to the model.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
180
181
182
183
184
185
186
187
188
```
| ```
@abstractmethod
async def request(
  self,
  messages: list[ModelMessage],
  model_settings: ModelSettings | None,
  model_request_parameters: ModelRequestParameters,
) -> tuple[ModelResponse, Usage]:
"""Make a request to the model."""
  raise NotImplementedError()

```
  
---|---  
####  request_stream `async`
```
request_stream(
  messages: list[ModelMessage],
  model_settings: ModelSettings | None,
  model_request_parameters: ModelRequestParameters,
) -> AsyncIterator[StreamedResponse]

```

Make a request to the model and return a streaming response.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
```
| ```
@asynccontextmanager
async def request_stream(
  self,
  messages: list[ModelMessage],
  model_settings: ModelSettings | None,
  model_request_parameters: ModelRequestParameters,
) -> AsyncIterator[StreamedResponse]:
"""Make a request to the model and return a streaming response."""
  # This method is not required, but you need to implement it if you want to support streamed responses
  raise NotImplementedError(f'Streamed requests not supported by this {self.__class__.__name__}')
  # yield is required to make this a generator for type checking
  # noinspection PyUnreachableCode
  yield # pragma: no cover

```
  
---|---  
####  model_name `abstractmethod` `property`
```
model_name: str

```

The model name.
####  system `abstractmethod` `property`
```
system: str | None

```

The system / model provider, ex: openai.
###  StreamedResponse `dataclass`
Bases: `ABC`
Streamed response from an LLM when calling a tool.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
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
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
```
| ```
@dataclass
class StreamedResponse(ABC):
"""Streamed response from an LLM when calling a tool."""
  _parts_manager: ModelResponsePartsManager = field(default_factory=ModelResponsePartsManager, init=False)
  _event_iterator: AsyncIterator[ModelResponseStreamEvent] | None = field(default=None, init=False)
  _usage: Usage = field(default_factory=Usage, init=False)
  def __aiter__(self) -> AsyncIterator[ModelResponseStreamEvent]:
"""Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""
    if self._event_iterator is None:
      self._event_iterator = self._get_event_iterator()
    return self._event_iterator
  @abstractmethod
  async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
"""Return an async iterator of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.
    This method should be implemented by subclasses to translate the vendor-specific stream of events into
    pydantic_ai-format events.
    """
    raise NotImplementedError()
    # noinspection PyUnreachableCode
    yield
  def get(self) -> ModelResponse:
"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""
    return ModelResponse(
      parts=self._parts_manager.get_parts(), model_name=self.model_name, timestamp=self.timestamp
    )
  def usage(self) -> Usage:
"""Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""
    return self._usage
  @property
  @abstractmethod
  def model_name(self) -> str:
"""Get the model name of the response."""
    raise NotImplementedError()
  @property
  @abstractmethod
  def timestamp(self) -> datetime:
"""Get the timestamp of the response."""
    raise NotImplementedError()

```
  
---|---  
####  __aiter__
```
__aiter__() -> AsyncIterator[ModelResponseStreamEvent]

```

Stream the response as an async iterable of `ModelResponseStreamEvent`s.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
225
226
227
228
229
```
| ```
def __aiter__(self) -> AsyncIterator[ModelResponseStreamEvent]:
"""Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""
  if self._event_iterator is None:
    self._event_iterator = self._get_event_iterator()
  return self._event_iterator

```
  
---|---  
####  get
```
get() -> ModelResponse

```

Build a `ModelResponse` from the data received from the stream so far.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
242
243
244
245
246
```
| ```
def get(self) -> ModelResponse:
"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""
  return ModelResponse(
    parts=self._parts_manager.get_parts(), model_name=self.model_name, timestamp=self.timestamp
  )

```
  
---|---  
####  usage
```
usage() -> Usage

```

Get the usage of the response so far. This will not be the final usage until the stream is exhausted.
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
248
249
250
```
| ```
def usage(self) -> Usage:
"""Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""
  return self._usage

```
  
---|---  
####  model_name `abstractmethod` `property`
```
model_name: str

```

Get the model name of the response.
####  timestamp `abstractmethod` `property`
```
timestamp: datetime

```

Get the timestamp of the response.
###  ALLOW_MODEL_REQUESTS `module-attribute`
```
ALLOW_MODEL_REQUESTS = True

```

Whether to allow requests to models.
This global setting allows you to disable request to most models, e.g. to make sure you don't accidentally make costly requests to a model during tests.
The testing models `TestModel` and `FunctionModel` are no affected by this setting.
###  check_allow_model_requests
```
check_allow_model_requests() -> None

```

Check if model requests are allowed.
If you're defining your own models that have costs or latency associated with their use, you should call this in `Model.request` and `Model.request_stream`.
Raises:
Type | Description  
---|---  
`RuntimeError` |  If model requests are not allowed.  
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
276
277
278
279
280
281
282
283
284
285
286
```
| ```
def check_allow_model_requests() -> None:
"""Check if model requests are allowed.
  If you're defining your own models that have costs or latency associated with their use, you should call this in
  [`Model.request`][pydantic_ai.models.Model.request] and [`Model.request_stream`][pydantic_ai.models.Model.request_stream].
  Raises:
    RuntimeError: If model requests are not allowed.
  """
  if not ALLOW_MODEL_REQUESTS:
    raise RuntimeError('Model requests are not allowed, since ALLOW_MODEL_REQUESTS is False')

```
  
---|---  
###  override_allow_model_requests
```
override_allow_model_requests(
  allow_model_requests: bool,
) -> Iterator[None]

```

Context manager to temporarily override `ALLOW_MODEL_REQUESTS`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`allow_model_requests` |  `bool` |  Whether to allow model requests within the context. |  _required_  
Source code in `pydantic_ai_slim/pydantic_ai/models/__init__.py`
```
289
290
291
292
293
294
295
296
297
298
299
300
301
302
```
| ```
@contextmanager
def override_allow_model_requests(allow_model_requests: bool) -> Iterator[None]:
"""Context manager to temporarily override [`ALLOW_MODEL_REQUESTS`][pydantic_ai.models.ALLOW_MODEL_REQUESTS].
  Args:
    allow_model_requests: Whether to allow model requests within the context.
  """
  global ALLOW_MODEL_REQUESTS
  old_value = ALLOW_MODEL_REQUESTS
  ALLOW_MODEL_REQUESTS = allow_model_requests # pyright: ignore[reportConstantRedefinition]
  try:
    yield
  finally:
    ALLOW_MODEL_REQUESTS = old_value # pyright: ignore[reportConstantRedefinition]

```
  
---|---
