Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.models.groq`
## Setup
For details on how to set up authentication with this model, see model configuration for Groq.
###  LatestGroqModelNames `module-attribute`
```
LatestGroqModelNames = Literal[
  "llama-3.3-70b-versatile",
  "llama-3.3-70b-specdec",
  "llama-3.1-8b-instant",
  "llama-3.2-1b-preview",
  "llama-3.2-3b-preview",
  "llama-3.2-11b-vision-preview",
  "llama-3.2-90b-vision-preview",
  "llama3-70b-8192",
  "llama3-8b-8192",
  "mixtral-8x7b-32768",
  "gemma2-9b-it",
]

```

Latest Groq models.
###  GroqModelName `module-attribute`
```
GroqModelName = Union[str, LatestGroqModelNames]

```

Possible Groq model names.
Since Groq supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See the Groq docs for a full list.
###  GroqModelSettings
Bases: `ModelSettings`
Settings used for a Groq model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
73
74
```
| ```
class GroqModelSettings(ModelSettings):
"""Settings used for a Groq model request."""

```
  
---|---  
###  GroqModel `dataclass`
Bases: `Model`
A model that uses the Groq API.
Internally, this uses the Groq Python client to interact with the API.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
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
133
134
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
154
155
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
167
168
169
170
171
172
173
174
175
176
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
263
264
265
266
267
268
269
270
271
272
273
274
275
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
287
288
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
303
304
305
306
307
308
309
310
311
```
| ```
@dataclass(init=False)
class GroqModel(Model):
"""A model that uses the Groq API.
  Internally, this uses the [Groq Python client](https://github.com/groq/groq-python) to interact with the API.
  Apart from `__init__`, all methods are private or match those of the base class.
  """
  client: AsyncGroq = field(repr=False)
  _model_name: GroqModelName = field(repr=False)
  _system: str | None = field(default='groq', repr=False)
  def __init__(
    self,
    model_name: GroqModelName,
    *,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncHTTPClient | None = None,
  ):
"""Initialize a Groq model.
    Args:
      model_name: The name of the Groq model to use. List of model names available
        [here](https://console.groq.com/docs/models).
      api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
        will be used if available.
      groq_client: An existing
        [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
        client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    self._model_name = model_name
    if groq_client is not None:
      assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
      assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
      self.client = groq_client
    elif http_client is not None:
      self.client = AsyncGroq(api_key=api_key, http_client=http_client)
    else:
      self.client = AsyncGroq(api_key=api_key, http_client=cached_async_http_client())
  async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, usage.Usage]:
    check_allow_model_requests()
    response = await self._completions_create(
      messages, False, cast(GroqModelSettings, model_settings or {}), model_request_parameters
    )
    return self._process_response(response), _map_usage(response)
  @asynccontextmanager
  async def request_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncIterator[StreamedResponse]:
    check_allow_model_requests()
    response = await self._completions_create(
      messages, True, cast(GroqModelSettings, model_settings or {}), model_request_parameters
    )
    async with response:
      yield await self._process_streamed_response(response)
  @property
  def model_name(self) -> GroqModelName:
"""The model name."""
    return self._model_name
  @property
  def system(self) -> str | None:
"""The system / model provider."""
    return self._system
  @overload
  async def _completions_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[True],
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncStream[ChatCompletionChunk]:
    pass
  @overload
  async def _completions_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[False],
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> chat.ChatCompletion:
    pass
  async def _completions_create(
    self,
    messages: list[ModelMessage],
    stream: bool,
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> chat.ChatCompletion | AsyncStream[ChatCompletionChunk]:
    tools = self._get_tools(model_request_parameters)
    # standalone function to make it easier to override
    if not tools:
      tool_choice: Literal['none', 'required', 'auto'] | None = None
    elif not model_request_parameters.allow_text_result:
      tool_choice = 'required'
    else:
      tool_choice = 'auto'
    groq_messages = list(chain(*(self._map_message(m) for m in messages)))
    return await self.client.chat.completions.create(
      model=str(self._model_name),
      messages=groq_messages,
      n=1,
      parallel_tool_calls=model_settings.get('parallel_tool_calls', NOT_GIVEN),
      tools=tools or NOT_GIVEN,
      tool_choice=tool_choice or NOT_GIVEN,
      stream=stream,
      max_tokens=model_settings.get('max_tokens', NOT_GIVEN),
      temperature=model_settings.get('temperature', NOT_GIVEN),
      top_p=model_settings.get('top_p', NOT_GIVEN),
      timeout=model_settings.get('timeout', NOT_GIVEN),
      seed=model_settings.get('seed', NOT_GIVEN),
      presence_penalty=model_settings.get('presence_penalty', NOT_GIVEN),
      frequency_penalty=model_settings.get('frequency_penalty', NOT_GIVEN),
      logit_bias=model_settings.get('logit_bias', NOT_GIVEN),
    )
  def _process_response(self, response: chat.ChatCompletion) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
    timestamp = datetime.fromtimestamp(response.created, tz=timezone.utc)
    choice = response.choices[0]
    items: list[ModelResponsePart] = []
    if choice.message.content is not None:
      items.append(TextPart(content=choice.message.content))
    if choice.message.tool_calls is not None:
      for c in choice.message.tool_calls:
        items.append(ToolCallPart(tool_name=c.function.name, args=c.function.arguments, tool_call_id=c.id))
    return ModelResponse(items, model_name=response.model, timestamp=timestamp)
  async def _process_streamed_response(self, response: AsyncStream[ChatCompletionChunk]) -> GroqStreamedResponse:
"""Process a streamed response, and prepare a streaming response to return."""
    peekable_response = _utils.PeekableAsyncStream(response)
    first_chunk = await peekable_response.peek()
    if isinstance(first_chunk, _utils.Unset):
      raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')
    return GroqStreamedResponse(
      _response=peekable_response,
      _model_name=self._model_name,
      _timestamp=datetime.fromtimestamp(first_chunk.created, tz=timezone.utc),
    )
  def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[chat.ChatCompletionToolParam]:
    tools = [self._map_tool_definition(r) for r in model_request_parameters.function_tools]
    if model_request_parameters.result_tools:
      tools += [self._map_tool_definition(r) for r in model_request_parameters.result_tools]
    return tools
  def _map_message(self, message: ModelMessage) -> Iterable[chat.ChatCompletionMessageParam]:
"""Just maps a `pydantic_ai.Message` to a `groq.types.ChatCompletionMessageParam`."""
    if isinstance(message, ModelRequest):
      yield from self._map_user_message(message)
    elif isinstance(message, ModelResponse):
      texts: list[str] = []
      tool_calls: list[chat.ChatCompletionMessageToolCallParam] = []
      for item in message.parts:
        if isinstance(item, TextPart):
          texts.append(item.content)
        elif isinstance(item, ToolCallPart):
          tool_calls.append(self._map_tool_call(item))
        else:
          assert_never(item)
      message_param = chat.ChatCompletionAssistantMessageParam(role='assistant')
      if texts:
        # Note: model responses from this model should only have one text item, so the following
        # shouldn't merge multiple texts into one unless you switch models between runs:
        message_param['content'] = '\n\n'.join(texts)
      if tool_calls:
        message_param['tool_calls'] = tool_calls
      yield message_param
    else:
      assert_never(message)
  @staticmethod
  def _map_tool_call(t: ToolCallPart) -> chat.ChatCompletionMessageToolCallParam:
    return chat.ChatCompletionMessageToolCallParam(
      id=_guard_tool_call_id(t=t, model_source='Groq'),
      type='function',
      function={'name': t.tool_name, 'arguments': t.args_as_json_str()},
    )
  @staticmethod
  def _map_tool_definition(f: ToolDefinition) -> chat.ChatCompletionToolParam:
    return {
      'type': 'function',
      'function': {
        'name': f.name,
        'description': f.description,
        'parameters': f.parameters_json_schema,
      },
    }
  @classmethod
  def _map_user_message(cls, message: ModelRequest) -> Iterable[chat.ChatCompletionMessageParam]:
    for part in message.parts:
      if isinstance(part, SystemPromptPart):
        yield chat.ChatCompletionSystemMessageParam(role='system', content=part.content)
      elif isinstance(part, UserPromptPart):
        yield chat.ChatCompletionUserMessageParam(role='user', content=part.content)
      elif isinstance(part, ToolReturnPart):
        yield chat.ChatCompletionToolMessageParam(
          role='tool',
          tool_call_id=_guard_tool_call_id(t=part, model_source='Groq'),
          content=part.model_response_str(),
        )
      elif isinstance(part, RetryPromptPart):
        if part.tool_name is None:
          yield chat.ChatCompletionUserMessageParam(role='user', content=part.model_response())
        else:
          yield chat.ChatCompletionToolMessageParam(
            role='tool',
            tool_call_id=_guard_tool_call_id(t=part, model_source='Groq'),
            content=part.model_response(),
          )

```
  
---|---  
####  __init__
```
__init__(
  model_name: GroqModelName,
  *,
  api_key: str | None = None,
  groq_client: AsyncGroq | None = None,
  http_client: AsyncClient | None = None
)

```

Initialize a Groq model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model_name` |  `GroqModelName` |  The name of the Groq model to use. List of model names available here. |  _required_  
`api_key` |  `str | None` |  The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable will be used if available. |  `None`  
`groq_client` |  `AsyncGroq | None` |  An existing `AsyncGroq` client to use, if provided, `api_key` and `http_client` must be `None`. |  `None`  
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`  
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
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
```
| ```
def __init__(
  self,
  model_name: GroqModelName,
  *,
  api_key: str | None = None,
  groq_client: AsyncGroq | None = None,
  http_client: AsyncHTTPClient | None = None,
):
"""Initialize a Groq model.
  Args:
    model_name: The name of the Groq model to use. List of model names available
      [here](https://console.groq.com/docs/models).
    api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
      will be used if available.
    groq_client: An existing
      [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
      client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
  """
  self._model_name = model_name
  if groq_client is not None:
    assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
    assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
    self.client = groq_client
  elif http_client is not None:
    self.client = AsyncGroq(api_key=api_key, http_client=http_client)
  else:
    self.client = AsyncGroq(api_key=api_key, http_client=cached_async_http_client())

```
  
---|---  
####  model_name `property`
```
model_name: GroqModelName

```

The model name.
####  system `property`
```
system: str | None

```

The system / model provider.
###  GroqStreamedResponse `dataclass`
Bases: `StreamedResponse`
Implementation of `StreamedResponse` for Groq models.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
```
| ```
@dataclass
class GroqStreamedResponse(StreamedResponse):
"""Implementation of `StreamedResponse` for Groq models."""
  _model_name: GroqModelName
  _response: AsyncIterable[ChatCompletionChunk]
  _timestamp: datetime
  async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
    async for chunk in self._response:
      self._usage += _map_usage(chunk)
      try:
        choice = chunk.choices[0]
      except IndexError:
        continue
      # Handle the text part of the response
      content = choice.delta.content
      if content is not None:
        yield self._parts_manager.handle_text_delta(vendor_part_id='content', content=content)
      # Handle the tool calls
      for dtc in choice.delta.tool_calls or []:
        maybe_event = self._parts_manager.handle_tool_call_delta(
          vendor_part_id=dtc.index,
          tool_name=dtc.function and dtc.function.name,
          args=dtc.function and dtc.function.arguments,
          tool_call_id=dtc.id,
        )
        if maybe_event is not None:
          yield maybe_event
  @property
  def model_name(self) -> GroqModelName:
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
model_name: GroqModelName

```

Get the model name of the response.
####  timestamp `property`
```
timestamp: datetime

```

Get the timestamp of the response.
