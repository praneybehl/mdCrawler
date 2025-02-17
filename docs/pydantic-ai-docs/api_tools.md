Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_ai.tools`
###  AgentDepsT `module-attribute`
```
AgentDepsT = TypeVar(
  "AgentDepsT", default=None, contravariant=True
)

```

Type variable for agent dependencies.
###  RunContext `dataclass`
Bases: `Generic[AgentDepsT]`
Information about the current call.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
@dataclasses.dataclass
class RunContext(Generic[AgentDepsT]):
"""Information about the current call."""
  deps: AgentDepsT
"""Dependencies for the agent."""
  model: models.Model
"""The model used in this run."""
  usage: Usage
"""LLM usage associated with the run."""
  prompt: str
"""The original user prompt passed to the run."""
  messages: list[_messages.ModelMessage] = field(default_factory=list)
"""Messages exchanged in the conversation so far."""
  tool_name: str | None = None
"""Name of the tool being called."""
  retry: int = 0
"""Number of retries so far."""
  run_step: int = 0
"""The current step in the run."""
  def replace_with(
    self, retry: int | None = None, tool_name: str | None | _utils.Unset = _utils.UNSET
  ) -> RunContext[AgentDepsT]:
    # Create a new `RunContext` a new `retry` value and `tool_name`.
    kwargs = {}
    if retry is not None:
      kwargs['retry'] = retry
    if tool_name is not _utils.UNSET:
      kwargs['tool_name'] = tool_name
    return dataclasses.replace(self, **kwargs)

```
  
---|---  
####  deps `instance-attribute`
```
deps: AgentDepsT

```

Dependencies for the agent.
####  model `instance-attribute`
```
model: Model

```

The model used in this run.
####  usage `instance-attribute`
```
usage: Usage

```

LLM usage associated with the run.
####  prompt `instance-attribute`
```
prompt: str

```

The original user prompt passed to the run.
####  messages `class-attribute` `instance-attribute`
```
messages: list[ModelMessage] = field(default_factory=list)

```

Messages exchanged in the conversation so far.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name: str | None = None

```

Name of the tool being called.
####  retry `class-attribute` `instance-attribute`
```
retry: int = 0

```

Number of retries so far.
####  run_step `class-attribute` `instance-attribute`
```
run_step: int = 0

```

The current step in the run.
###  ToolParams `module-attribute`
```
ToolParams = ParamSpec('ToolParams', default=...)

```

Retrieval function param spec.
###  SystemPromptFunc `module-attribute`
```
SystemPromptFunc = Union[
  Callable[[RunContext[AgentDepsT]], str],
  Callable[[RunContext[AgentDepsT]], Awaitable[str]],
  Callable[[], str],
  Callable[[], Awaitable[str]],
]

```

A function that may or maybe not take `RunContext` as an argument, and may or may not be async.
Usage `SystemPromptFunc[AgentDepsT]`.
###  ToolFuncContext `module-attribute`
```
ToolFuncContext = Callable[
  Concatenate[RunContext[AgentDepsT], ToolParams], Any
]

```

A tool function that takes `RunContext` as the first argument.
Usage `ToolContextFunc[AgentDepsT, ToolParams]`.
###  ToolFuncPlain `module-attribute`
```
ToolFuncPlain = Callable[ToolParams, Any]

```

A tool function that does not take `RunContext` as the first argument.
Usage `ToolPlainFunc[ToolParams]`.
###  ToolFuncEither `module-attribute`
```
ToolFuncEither = Union[
  ToolFuncContext[AgentDepsT, ToolParams],
  ToolFuncPlain[ToolParams],
]

```

Either kind of tool function.
This is just a union of `ToolFuncContext` and `ToolFuncPlain`.
Usage `ToolFuncEither[AgentDepsT, ToolParams]`.
###  ToolPrepareFunc `module-attribute`
```
ToolPrepareFunc: TypeAlias = (
  "Callable[[RunContext[AgentDepsT], ToolDefinition], Awaitable[ToolDefinition | None]]"
)

```

Definition of a function that can prepare a tool definition at call time.
See tool docs for more information.
Example — here `only_if_42` is valid as a `ToolPrepareFunc`:
```
from typing import Union
from pydantic_ai import RunContext, Tool
from pydantic_ai.tools import ToolDefinition
async def only_if_42(
  ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
  if ctx.deps == 42:
    return tool_def
def hitchhiker(ctx: RunContext[int], answer: str) -> str:
  return f'{ctx.deps}{answer}'
hitchhiker = Tool(hitchhiker, prepare=only_if_42)

```

Usage `ToolPrepareFunc[AgentDepsT]`.
###  DocstringFormat `module-attribute`
```
DocstringFormat = Literal[
  "google", "numpy", "sphinx", "auto"
]

```

Supported docstring formats.
  * `'google'` — Google-style docstrings.
  * `'numpy'` — Numpy-style docstrings.
  * `'sphinx'` — Sphinx-style docstrings.
  * `'auto'` — Automatically infer the format based on the structure of the docstring.


###  Tool `dataclass`
Bases: `Generic[AgentDepsT]`
A tool function for an agent.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
@dataclass(init=False)
class Tool(Generic[AgentDepsT]):
"""A tool function for an agent."""
  function: ToolFuncEither[AgentDepsT]
  takes_ctx: bool
  max_retries: int | None
  name: str
  description: str
  prepare: ToolPrepareFunc[AgentDepsT] | None
  docstring_format: DocstringFormat
  require_parameter_descriptions: bool
  _is_async: bool = field(init=False)
  _single_arg_name: str | None = field(init=False)
  _positional_fields: list[str] = field(init=False)
  _var_positional_field: str | None = field(init=False)
  _validator: SchemaValidator = field(init=False, repr=False)
  _parameters_json_schema: ObjectJsonSchema = field(init=False)
  # TODO: Move this state off the Tool class, which is otherwise stateless.
  #  This should be tracked inside a specific agent run, not the tool.
  current_retry: int = field(default=0, init=False)
  def __init__(
    self,
    function: ToolFuncEither[AgentDepsT],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ):
"""Create a new tool instance.
    Example usage:
```python {noqa="I001"}
    from pydantic_ai import Agent, RunContext, Tool
    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
      return f'{ctx.deps} {x} {y}'
    agent = Agent('test', tools=[Tool(my_tool)])
```
    or with a custom prepare method:
```python {noqa="I001"}
    from typing import Union
    from pydantic_ai import Agent, RunContext, Tool
    from pydantic_ai.tools import ToolDefinition
    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
      return f'{ctx.deps} {x} {y}'
    async def prep_my_tool(
      ctx: RunContext[int], tool_def: ToolDefinition
    ) -> Union[ToolDefinition, None]:
      # only register the tool if `deps == 42`
      if ctx.deps == 42:
        return tool_def
    agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
```

    Args:
      function: The Python function to call as the tool.
      takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
        this is inferred if unset.
      max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
      name: Name of the tool, inferred from the function if `None`.
      description: Description of the tool, inferred from the function if `None`.
      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
    """
    if takes_ctx is None:
      takes_ctx = _pydantic.takes_ctx(function)
    f = _pydantic.function_schema(function, takes_ctx, docstring_format, require_parameter_descriptions)
    self.function = function
    self.takes_ctx = takes_ctx
    self.max_retries = max_retries
    self.name = name or function.__name__
    self.description = description or f['description']
    self.prepare = prepare
    self.docstring_format = docstring_format
    self.require_parameter_descriptions = require_parameter_descriptions
    self._is_async = inspect.iscoroutinefunction(self.function)
    self._single_arg_name = f['single_arg_name']
    self._positional_fields = f['positional_fields']
    self._var_positional_field = f['var_positional_field']
    self._validator = f['validator']
    self._parameters_json_schema = f['json_schema']
  async def prepare_tool_def(self, ctx: RunContext[AgentDepsT]) -> ToolDefinition | None:
"""Get the tool definition.
    By default, this method creates a tool definition, then either returns it, or calls `self.prepare`
    if it's set.
    Returns:
      return a `ToolDefinition` or `None` if the tools should not be registered for this run.
    """
    tool_def = ToolDefinition(
      name=self.name,
      description=self.description,
      parameters_json_schema=self._parameters_json_schema,
    )
    if self.prepare is not None:
      return await self.prepare(ctx, tool_def)
    else:
      return tool_def
  async def run(
    self, message: _messages.ToolCallPart, run_context: RunContext[AgentDepsT]
  ) -> _messages.ToolReturnPart | _messages.RetryPromptPart:
"""Run the tool function asynchronously."""
    try:
      if isinstance(message.args, str):
        args_dict = self._validator.validate_json(message.args)
      else:
        args_dict = self._validator.validate_python(message.args)
    except ValidationError as e:
      return self._on_error(e, message)
    args, kwargs = self._call_args(args_dict, message, run_context)
    try:
      if self._is_async:
        function = cast(Callable[[Any], Awaitable[str]], self.function)
        response_content = await function(*args, **kwargs)
      else:
        function = cast(Callable[[Any], str], self.function)
        response_content = await _utils.run_in_executor(function, *args, **kwargs)
    except ModelRetry as e:
      return self._on_error(e, message)
    self.current_retry = 0
    return _messages.ToolReturnPart(
      tool_name=message.tool_name,
      content=response_content,
      tool_call_id=message.tool_call_id,
    )
  def _call_args(
    self,
    args_dict: dict[str, Any],
    message: _messages.ToolCallPart,
    run_context: RunContext[AgentDepsT],
  ) -> tuple[list[Any], dict[str, Any]]:
    if self._single_arg_name:
      args_dict = {self._single_arg_name: args_dict}
    ctx = dataclasses.replace(run_context, retry=self.current_retry, tool_name=message.tool_name)
    args = [ctx] if self.takes_ctx else []
    for positional_field in self._positional_fields:
      args.append(args_dict.pop(positional_field))
    if self._var_positional_field:
      args.extend(args_dict.pop(self._var_positional_field))
    return args, args_dict
  def _on_error(
    self, exc: ValidationError | ModelRetry, call_message: _messages.ToolCallPart
  ) -> _messages.RetryPromptPart:
    self.current_retry += 1
    if self.max_retries is None or self.current_retry > self.max_retries:
      raise UnexpectedModelBehavior(f'Tool exceeded max retries count of {self.max_retries}') from exc
    else:
      if isinstance(exc, ValidationError):
        content = exc.errors(include_url=False)
      else:
        content = exc.message
      return _messages.RetryPromptPart(
        tool_name=call_message.tool_name,
        content=content,
        tool_call_id=call_message.tool_call_id,
      )

```
  
---|---  
####  __init__
```
__init__(
  function: ToolFuncEither[AgentDepsT],
  *,
  takes_ctx: bool | None = None,
  max_retries: int | None = None,
  name: str | None = None,
  description: str | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = "auto",
  require_parameter_descriptions: bool = False
)

```

Create a new tool instance.
Example usage:
```
from pydantic_ai import Agent, RunContext, Tool
async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
  return f'{ctx.deps}{x}{y}'
agent = Agent('test', tools=[Tool(my_tool)])

```

or with a custom prepare method:
```
from typing import Union
from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.tools import ToolDefinition
async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
  return f'{ctx.deps}{x}{y}'
async def prep_my_tool(
  ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
  # only register the tool if `deps == 42`
  if ctx.deps == 42:
    return tool_def
agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `ToolFuncEither[AgentDepsT]` |  The Python function to call as the tool. |  _required_  
`takes_ctx` |  `bool | None` |  Whether the function takes a `RunContext` first argument, this is inferred if unset. |  `None`  
`max_retries` |  `int | None` |  Maximum number of retries allowed for this tool, set to the agent default if `None`. |  `None`  
`name` |  `str | None` |  Name of the tool, inferred from the function if `None`. |  `None`  
`description` |  `str | None` |  Description of the tool, inferred from the function if `None`. |  `None`  
`prepare` |  `ToolPrepareFunc[AgentDepsT] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See `ToolPrepareFunc`. |  `None`  
`docstring_format` |  `DocstringFormat` |  The format of the docstring, see `DocstringFormat`. Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. |  `'auto'`  
`require_parameter_descriptions` |  `bool` |  If True, raise an error if a parameter description is missing. Defaults to False. |  `False`  
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
def __init__(
  self,
  function: ToolFuncEither[AgentDepsT],
  *,
  takes_ctx: bool | None = None,
  max_retries: int | None = None,
  name: str | None = None,
  description: str | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = 'auto',
  require_parameter_descriptions: bool = False,
):
"""Create a new tool instance.
  Example usage:
  ```python {noqa="I001"}
  from pydantic_ai import Agent, RunContext, Tool
  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'
  agent = Agent('test', tools=[Tool(my_tool)])
  ```
  or with a custom prepare method:
  ```python {noqa="I001"}
  from typing import Union
  from pydantic_ai import Agent, RunContext, Tool
  from pydantic_ai.tools import ToolDefinition
  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'
  async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
  ) -> Union[ToolDefinition, None]:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
      return tool_def
  agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
  ```

  Args:
    function: The Python function to call as the tool.
    takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
      this is inferred if unset.
    max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
    name: Name of the tool, inferred from the function if `None`.
    description: Description of the tool, inferred from the function if `None`.
    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
  """
  if takes_ctx is None:
    takes_ctx = _pydantic.takes_ctx(function)
  f = _pydantic.function_schema(function, takes_ctx, docstring_format, require_parameter_descriptions)
  self.function = function
  self.takes_ctx = takes_ctx
  self.max_retries = max_retries
  self.name = name or function.__name__
  self.description = description or f['description']
  self.prepare = prepare
  self.docstring_format = docstring_format
  self.require_parameter_descriptions = require_parameter_descriptions
  self._is_async = inspect.iscoroutinefunction(self.function)
  self._single_arg_name = f['single_arg_name']
  self._positional_fields = f['positional_fields']
  self._var_positional_field = f['var_positional_field']
  self._validator = f['validator']
  self._parameters_json_schema = f['json_schema']

```
  
---|---  
####  prepare_tool_def `async`
```
prepare_tool_def(
  ctx: RunContext[AgentDepsT],
) -> ToolDefinition | None

```

Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls `self.prepare` if it's set.
Returns:
Type | Description  
---|---  
`ToolDefinition | None` |  return a `ToolDefinition` or `None` if the tools should not be registered for this run.  
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
async def prepare_tool_def(self, ctx: RunContext[AgentDepsT]) -> ToolDefinition | None:
"""Get the tool definition.
  By default, this method creates a tool definition, then either returns it, or calls `self.prepare`
  if it's set.
  Returns:
    return a `ToolDefinition` or `None` if the tools should not be registered for this run.
  """
  tool_def = ToolDefinition(
    name=self.name,
    description=self.description,
    parameters_json_schema=self._parameters_json_schema,
  )
  if self.prepare is not None:
    return await self.prepare(ctx, tool_def)
  else:
    return tool_def

```
  
---|---  
####  run `async`
```
run(
  message: ToolCallPart,
  run_context: RunContext[AgentDepsT],
) -> ToolReturnPart | RetryPromptPart

```

Run the tool function asynchronously.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
```
| ```
async def run(
  self, message: _messages.ToolCallPart, run_context: RunContext[AgentDepsT]
) -> _messages.ToolReturnPart | _messages.RetryPromptPart:
"""Run the tool function asynchronously."""
  try:
    if isinstance(message.args, str):
      args_dict = self._validator.validate_json(message.args)
    else:
      args_dict = self._validator.validate_python(message.args)
  except ValidationError as e:
    return self._on_error(e, message)
  args, kwargs = self._call_args(args_dict, message, run_context)
  try:
    if self._is_async:
      function = cast(Callable[[Any], Awaitable[str]], self.function)
      response_content = await function(*args, **kwargs)
    else:
      function = cast(Callable[[Any], str], self.function)
      response_content = await _utils.run_in_executor(function, *args, **kwargs)
  except ModelRetry as e:
    return self._on_error(e, message)
  self.current_retry = 0
  return _messages.ToolReturnPart(
    tool_name=message.tool_name,
    content=response_content,
    tool_call_id=message.tool_call_id,
  )

```
  
---|---  
###  ObjectJsonSchema `module-attribute`
```
ObjectJsonSchema: TypeAlias = dict[str, Any]

```

Type representing JSON schema of an object, e.g. where `"type": "object"`.
This type is used to define tools parameters (aka arguments) in ToolDefinition.
With PEP-728 this should be a TypedDict with `type: Literal['object']`, and `extra_parts=Any`
###  ToolDefinition `dataclass`
Definition of a tool passed to a model.
This is used for both function tools result tools.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
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
356
357
358
359
360
```
| ```
@dataclass
class ToolDefinition:
"""Definition of a tool passed to a model.
  This is used for both function tools result tools.
  """
  name: str
"""The name of the tool."""
  description: str
"""The description of the tool."""
  parameters_json_schema: ObjectJsonSchema
"""The JSON schema for the tool's parameters."""
  outer_typed_dict_key: str | None = None
"""The key in the outer [TypedDict] that wraps a result tool.
  This will only be set for result tools which don't have an `object` JSON schema.
  """

```
  
---|---  
####  name `instance-attribute`
```
name: str

```

The name of the tool.
####  description `instance-attribute`
```
description: str

```

The description of the tool.
####  parameters_json_schema `instance-attribute`
```
parameters_json_schema: ObjectJsonSchema

```

The JSON schema for the tool's parameters.
####  outer_typed_dict_key `class-attribute` `instance-attribute`
```
outer_typed_dict_key: str | None = None

```

The key in the outer [TypedDict] that wraps a result tool.
This will only be set for result tools which don't have an `object` JSON schema.
