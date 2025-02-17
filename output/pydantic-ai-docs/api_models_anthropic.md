Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.models.anthropic`
## Setup
For details on how to set up authentication with this model, see model configuration for Anthropic.
###  LatestAnthropicModelNames `module-attribute`
```
LatestAnthropicModelNames = Literal[
  "claude-3-5-haiku-latest",
  "claude-3-5-sonnet-latest",
  "claude-3-opus-latest",
]

```

Latest Anthropic models.
###  AnthropicModelName `module-attribute`
```
AnthropicModelName = Union[str, LatestAnthropicModelNames]

```

Possible Anthropic model names.
Since Anthropic supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See the Anthropic docs for a full list.
###  AnthropicModelSettings
Bases: `ModelSettings`
Settings used for an Anthropic model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
82
83
84
85
86
87
88
```
| ```
class AnthropicModelSettings(ModelSettings):
"""Settings used for an Anthropic model request."""
  anthropic_metadata: MetadataParam
"""An object describing metadata about the request.
  Contains `user_id`, an external identifier for the user who is associated with the request."""

```
  
---|---  
####  anthropic_metadata `instance-attribute`
```
anthropic_metadata: MetadataParam

```

An object describing metadata about the request.
Contains `user_id`, an external identifier for the user who is associated with the request.
###  AnthropicModel `dataclass`
Bases: `Model`
A model that uses the Anthropic API.
Internally, this uses the Anthropic Python client to interact with the API.
Apart from `__init__`, all methods are private or match those of the base class.
Note
The `AnthropicModel` class does not yet support streaming responses. We anticipate adding support for streaming responses in a near-term future release.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
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
312
313
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
```
| ```
@dataclass(init=False)
class AnthropicModel(Model):
"""A model that uses the Anthropic API.
  Internally, this uses the [Anthropic Python client](https://github.com/anthropics/anthropic-sdk-python) to interact with the API.
  Apart from `__init__`, all methods are private or match those of the base class.
  !!! note
    The `AnthropicModel` class does not yet support streaming responses.
    We anticipate adding support for streaming responses in a near-term future release.
  """
  client: AsyncAnthropic = field(repr=False)
  _model_name: AnthropicModelName = field(repr=False)
  _system: str | None = field(default='anthropic', repr=False)
  def __init__(
    self,
    model_name: AnthropicModelName,
    *,
    api_key: str | None = None,
    anthropic_client: AsyncAnthropic | None = None,
    http_client: AsyncHTTPClient | None = None,
  ):
"""Initialize an Anthropic model.
    Args:
      model_name: The name of the Anthropic model to use. List of model names available
        [here](https://docs.anthropic.com/en/docs/about-claude/models).
      api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
        will be used if available.
      anthropic_client: An existing
        [`AsyncAnthropic`](https://github.com/anthropics/anthropic-sdk-python?tab=readme-ov-file#async-usage)
        client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    self._model_name = model_name
    if anthropic_client is not None:
      assert http_client is None, 'Cannot provide both `anthropic_client` and `http_client`'
      assert api_key is None, 'Cannot provide both `anthropic_client` and `api_key`'
      self.client = anthropic_client
    elif http_client is not None:
      self.client = AsyncAnthropic(api_key=api_key, http_client=http_client)
    else:
      self.client = AsyncAnthropic(api_key=api_key, http_client=cached_async_http_client())
  async def request(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, usage.Usage]:
    check_allow_model_requests()
    response = await self._messages_create(
      messages, False, cast(AnthropicModelSettings, model_settings or {}), model_request_parameters
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
    response = await self._messages_create(
      messages, True, cast(AnthropicModelSettings, model_settings or {}), model_request_parameters
    )
    async with response:
      yield await self._process_streamed_response(response)
  @property
  def model_name(self) -> AnthropicModelName:
"""The model name."""
    return self._model_name
  @property
  def system(self) -> str | None:
"""The system / model provider."""
    return self._system
  @overload
  async def _messages_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[True],
    model_settings: AnthropicModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncStream[RawMessageStreamEvent]:
    pass
  @overload
  async def _messages_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[False],
    model_settings: AnthropicModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> AnthropicMessage:
    pass
  async def _messages_create(
    self,
    messages: list[ModelMessage],
    stream: bool,
    model_settings: AnthropicModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> AnthropicMessage | AsyncStream[RawMessageStreamEvent]:
    # standalone function to make it easier to override
    tools = self._get_tools(model_request_parameters)
    tool_choice: ToolChoiceParam | None
    if not tools:
      tool_choice = None
    else:
      if not model_request_parameters.allow_text_result:
        tool_choice = {'type': 'any'}
      else:
        tool_choice = {'type': 'auto'}
      if (allow_parallel_tool_calls := model_settings.get('parallel_tool_calls')) is not None:
        tool_choice['disable_parallel_tool_use'] = not allow_parallel_tool_calls
    system_prompt, anthropic_messages = self._map_message(messages)
    return await self.client.messages.create(
      max_tokens=model_settings.get('max_tokens', 1024),
      system=system_prompt or NOT_GIVEN,
      messages=anthropic_messages,
      model=self._model_name,
      tools=tools or NOT_GIVEN,
      tool_choice=tool_choice or NOT_GIVEN,
      stream=stream,
      temperature=model_settings.get('temperature', NOT_GIVEN),
      top_p=model_settings.get('top_p', NOT_GIVEN),
      timeout=model_settings.get('timeout', NOT_GIVEN),
      metadata=model_settings.get('anthropic_metadata', NOT_GIVEN),
    )
  def _process_response(self, response: AnthropicMessage) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
    items: list[ModelResponsePart] = []
    for item in response.content:
      if isinstance(item, TextBlock):
        items.append(TextPart(content=item.text))
      else:
        assert isinstance(item, ToolUseBlock), 'unexpected item type'
        items.append(
          ToolCallPart(
            tool_name=item.name,
            args=cast(dict[str, Any], item.input),
            tool_call_id=item.id,
          )
        )
    return ModelResponse(items, model_name=response.model)
  async def _process_streamed_response(self, response: AsyncStream[RawMessageStreamEvent]) -> StreamedResponse:
    peekable_response = _utils.PeekableAsyncStream(response)
    first_chunk = await peekable_response.peek()
    if isinstance(first_chunk, _utils.Unset):
      raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')
    # Since Anthropic doesn't provide a timestamp in the message, we'll use the current time
    timestamp = datetime.now(tz=timezone.utc)
    return AnthropicStreamedResponse(
      _model_name=self._model_name, _response=peekable_response, _timestamp=timestamp
    )
  def _get_tools(self, model_request_parameters: ModelRequestParameters) -> list[ToolParam]:
    tools = [self._map_tool_definition(r) for r in model_request_parameters.function_tools]
    if model_request_parameters.result_tools:
      tools += [self._map_tool_definition(r) for r in model_request_parameters.result_tools]
    return tools
  def _map_message(self, messages: list[ModelMessage]) -> tuple[str, list[MessageParam]]:
"""Just maps a `pydantic_ai.Message` to a `anthropic.types.MessageParam`."""
    system_prompt: str = ''
    anthropic_messages: list[MessageParam] = []
    for m in messages:
      if isinstance(m, ModelRequest):
        for part in m.parts:
          if isinstance(part, SystemPromptPart):
            system_prompt += part.content
          elif isinstance(part, UserPromptPart):
            anthropic_messages.append(MessageParam(role='user', content=part.content))
          elif isinstance(part, ToolReturnPart):
            anthropic_messages.append(
              MessageParam(
                role='user',
                content=[
                  ToolResultBlockParam(
                    tool_use_id=_guard_tool_call_id(t=part, model_source='Anthropic'),
                    type='tool_result',
                    content=part.model_response_str(),
                    is_error=False,
                  )
                ],
              )
            )
          elif isinstance(part, RetryPromptPart):
            if part.tool_name is None:
              anthropic_messages.append(MessageParam(role='user', content=part.model_response()))
            else:
              anthropic_messages.append(
                MessageParam(
                  role='user',
                  content=[
                    ToolResultBlockParam(
                      tool_use_id=_guard_tool_call_id(t=part, model_source='Anthropic'),
                      type='tool_result',
                      content=part.model_response(),
                      is_error=True,
                    ),
                  ],
                )
              )
      elif isinstance(m, ModelResponse):
        content: list[TextBlockParam | ToolUseBlockParam] = []
        for item in m.parts:
          if isinstance(item, TextPart):
            content.append(TextBlockParam(text=item.content, type='text'))
          else:
            assert isinstance(item, ToolCallPart)
            content.append(self._map_tool_call(item))
        anthropic_messages.append(MessageParam(role='assistant', content=content))
      else:
        assert_never(m)
    return system_prompt, anthropic_messages
  @staticmethod
  def _map_tool_call(t: ToolCallPart) -> ToolUseBlockParam:
    return ToolUseBlockParam(
      id=_guard_tool_call_id(t=t, model_source='Anthropic'),
      type='tool_use',
      name=t.tool_name,
      input=t.args_as_dict(),
    )
  @staticmethod
  def _map_tool_definition(f: ToolDefinition) -> ToolParam:
    return {
      'name': f.name,
      'description': f.description,
      'input_schema': f.parameters_json_schema,
    }

```
  
---|---  
####  __init__
```
__init__(
  model_name: AnthropicModelName,
  *,
  api_key: str | None = None,
  anthropic_client: AsyncAnthropic | None = None,
  http_client: AsyncClient | None = None
)

```

Initialize an Anthropic model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model_name` |  `AnthropicModelName` |  The name of the Anthropic model to use. List of model names available here. |  _required_  
`api_key` |  `str | None` |  The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable will be used if available. |  `None`  
`anthropic_client` |  `AsyncAnthropic | None` |  An existing `AsyncAnthropic` client to use, if provided, `api_key` and `http_client` must be `None`. |  `None`  
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`  
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
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
```
| ```
def __init__(
  self,
  model_name: AnthropicModelName,
  *,
  api_key: str | None = None,
  anthropic_client: AsyncAnthropic | None = None,
  http_client: AsyncHTTPClient | None = None,
):
"""Initialize an Anthropic model.
  Args:
    model_name: The name of the Anthropic model to use. List of model names available
      [here](https://docs.anthropic.com/en/docs/about-claude/models).
    api_key: The API key to use for authentication, if not provided, the `ANTHROPIC_API_KEY` environment variable
      will be used if available.
    anthropic_client: An existing
      [`AsyncAnthropic`](https://github.com/anthropics/anthropic-sdk-python?tab=readme-ov-file#async-usage)
      client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
  """
  self._model_name = model_name
  if anthropic_client is not None:
    assert http_client is None, 'Cannot provide both `anthropic_client` and `http_client`'
    assert api_key is None, 'Cannot provide both `anthropic_client` and `api_key`'
    self.client = anthropic_client
  elif http_client is not None:
    self.client = AsyncAnthropic(api_key=api_key, http_client=http_client)
  else:
    self.client = AsyncAnthropic(api_key=api_key, http_client=cached_async_http_client())

```
  
---|---  
####  model_name `property`
```
model_name: AnthropicModelName

```

The model name.
####  system `property`
```
system: str | None

```

The system / model provider.
###  AnthropicStreamedResponse `dataclass`
Bases: `StreamedResponse`
Implementation of `StreamedResponse` for Anthropic models.
Source code in `pydantic_ai_slim/pydantic_ai/models/anthropic.py`
```
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
```
| ```
@dataclass
class AnthropicStreamedResponse(StreamedResponse):
"""Implementation of `StreamedResponse` for Anthropic models."""
  _model_name: AnthropicModelName
  _response: AsyncIterable[RawMessageStreamEvent]
  _timestamp: datetime
  async def _get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
    current_block: TextBlock | ToolUseBlock | None = None
    current_json: str = ''
    async for event in self._response:
      self._usage += _map_usage(event)
      if isinstance(event, RawContentBlockStartEvent):
        current_block = event.content_block
        if isinstance(current_block, TextBlock) and current_block.text:
          yield self._parts_manager.handle_text_delta(vendor_part_id='content', content=current_block.text)
        elif isinstance(current_block, ToolUseBlock):
          maybe_event = self._parts_manager.handle_tool_call_delta(
            vendor_part_id=current_block.id,
            tool_name=current_block.name,
            args=cast(dict[str, Any], current_block.input),
            tool_call_id=current_block.id,
          )
          if maybe_event is not None:
            yield maybe_event
      elif isinstance(event, RawContentBlockDeltaEvent):
        if isinstance(event.delta, TextDelta):
          yield self._parts_manager.handle_text_delta(vendor_part_id='content', content=event.delta.text)
        elif (
          current_block and event.delta.type == 'input_json_delta' and isinstance(current_block, ToolUseBlock)
        ):
          # Try to parse the JSON immediately, otherwise cache the value for later. This handles
          # cases where the JSON is not currently valid but will be valid once we stream more tokens.
          try:
            parsed_args = json_loads(current_json + event.delta.partial_json)
            current_json = ''
          except JSONDecodeError:
            current_json += event.delta.partial_json
            continue
          # For tool calls, we need to handle partial JSON updates
          maybe_event = self._parts_manager.handle_tool_call_delta(
            vendor_part_id=current_block.id,
            tool_name='',
            args=parsed_args,
            tool_call_id=current_block.id,
          )
          if maybe_event is not None:
            yield maybe_event
      elif isinstance(event, (RawContentBlockStopEvent, RawMessageStopEvent)):
        current_block = None
  @property
  def model_name(self) -> AnthropicModelName:
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
model_name: AnthropicModelName

```

Get the model name of the response.
####  timestamp `property`
```
timestamp: datetime

```

Get the timestamp of the response.
