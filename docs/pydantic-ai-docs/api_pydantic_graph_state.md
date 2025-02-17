Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_graph.state`
###  StateT `module-attribute`
```
StateT = TypeVar('StateT', default=None)

```

Type variable for the state in a graph.
###  deep_copy_state
```
deep_copy_state(state: StateT) -> StateT

```

Default method for snapshotting the state in a graph run, uses `copy.deepcopy`.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
24
25
26
27
28
29
```
| ```
def deep_copy_state(state: StateT) -> StateT:
"""Default method for snapshotting the state in a graph run, uses [`copy.deepcopy`][copy.deepcopy]."""
  if state is None:
    return state
  else:
    return copy.deepcopy(state)

```
  
---|---  
###  NodeStep `dataclass`
Bases: `Generic[StateT, RunEndT]`
History step describing the execution of a node in a graph.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
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
58
59
60
61
```
| ```
@dataclass
class NodeStep(Generic[StateT, RunEndT]):
"""History step describing the execution of a node in a graph."""
  state: StateT
"""The state of the graph after the node has been run."""
  node: Annotated[BaseNode[StateT, Any, RunEndT], CustomNodeSchema()]
"""The node that was run."""
  start_ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the node started running."""
  duration: float | None = None
"""The duration of the node run in seconds."""
  kind: Literal['node'] = 'node'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  # TODO waiting for https://github.com/pydantic/pydantic/issues/11264, should be an InitVar
  snapshot_state: Annotated[Callable[[StateT], StateT], pydantic.Field(exclude=True, repr=False)] = field(
    default=deep_copy_state, repr=False
  )
"""Function to snapshot the state of the graph."""
  def __post_init__(self):
    # Copy the state to prevent it from being modified by other code
    self.state = self.snapshot_state(self.state)
  def data_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.node)

```
  
---|---  
####  state `instance-attribute`
```
state: StateT

```

The state of the graph after the node has been run.
####  node `instance-attribute`
```
node: Annotated[
  BaseNode[StateT, Any, RunEndT], CustomNodeSchema()
]

```

The node that was run.
####  start_ts `class-attribute` `instance-attribute`
```
start_ts: datetime = field(default_factory=now_utc)

```

The timestamp when the node started running.
####  duration `class-attribute` `instance-attribute`
```
duration: float | None = None

```

The duration of the node run in seconds.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal['node'] = 'node'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  snapshot_state `class-attribute` `instance-attribute`
```
snapshot_state: Annotated[
  Callable[[StateT], StateT],
  Field(exclude=True, repr=False),
] = field(default=deep_copy_state, repr=False)

```

Function to snapshot the state of the graph.
####  data_snapshot
```
data_snapshot() -> BaseNode[StateT, Any, RunEndT]

```

Returns a deep copy of `self.node`.
Useful for summarizing history.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
56
57
58
59
60
61
```
| ```
def data_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.node)

```
  
---|---  
###  EndStep `dataclass`
Bases: `Generic[RunEndT]`
History step describing the end of a graph run.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
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
```
| ```
@dataclass
class EndStep(Generic[RunEndT]):
"""History step describing the end of a graph run."""
  result: End[RunEndT]
"""The result of the graph run."""
  ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the graph run ended."""
  kind: Literal['end'] = 'end'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  def data_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.result)

```
  
---|---  
####  result `instance-attribute`
```
result: End[RunEndT]

```

The result of the graph run.
####  ts `class-attribute` `instance-attribute`
```
ts: datetime = field(default_factory=now_utc)

```

The timestamp when the graph run ended.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal['end'] = 'end'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  data_snapshot
```
data_snapshot() -> End[RunEndT]

```

Returns a deep copy of `self.result`.
Useful for summarizing history.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
75
76
77
78
79
80
```
| ```
def data_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.result)

```
  
---|---  
###  HistoryStep `module-attribute`
```
HistoryStep = Union[
  NodeStep[StateT, RunEndT], EndStep[RunEndT]
]

```

A step in the history of a graph run.
`Graph.run` returns a list of these steps describing the execution of the graph, together with the run return value.
