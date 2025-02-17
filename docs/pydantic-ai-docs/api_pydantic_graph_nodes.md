Skip to content 
Version Notice
This documentation is ahead of the last release by 8 commits. You may see documentation for features not yet supported in the latest release v0.0.24 2025-02-12. 
# `pydantic_graph.nodes`
###  GraphRunContext `dataclass`
Bases: `Generic[StateT, DepsT]`
Context for a graph.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
27
28
29
30
31
32
33
34
```
| ```
@dataclass
class GraphRunContext(Generic[StateT, DepsT]):
"""Context for a graph."""
  state: StateT
"""The state of the graph."""
  deps: DepsT
"""Dependencies for the graph."""

```
  
---|---  
####  state `instance-attribute`
```
state: StateT

```

The state of the graph.
####  deps `instance-attribute`
```
deps: DepsT

```

Dependencies for the graph.
###  BaseNode
Bases: `ABC`, `Generic[StateT, DepsT, NodeRunEndT]`
Base class for a node.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
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
```
| ```
class BaseNode(ABC, Generic[StateT, DepsT, NodeRunEndT]):
"""Base class for a node."""
  docstring_notes: ClassVar[bool] = False
"""Set to `True` to generate mermaid diagram notes from the class's docstring.
  While this can add valuable information to the diagram, it can make diagrams harder to view, hence
  it is disabled by default. You can also customise notes overriding the
  [`get_note`][pydantic_graph.nodes.BaseNode.get_note] method.
  """
  @abstractmethod
  async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.
    This is an abstract method that must be implemented by subclasses.
    !!! note "Return types used at runtime"
      The return type of this method are read by `pydantic_graph` at runtime and used to define which
      nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
      and enforced when running the graph.
    Args:
      ctx: The graph context.
    Returns:
      The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
    """
    ...
  @classmethod
  @cache
  def get_id(cls) -> str:
"""Get the ID of the node."""
    return cls.__name__
  @classmethod
  def get_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.
    By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
    is `True`. You can override this method to customise the node notes.
    """
    if not cls.docstring_notes:
      return None
    docstring = cls.__doc__
    # dataclasses get an automatic docstring which is just their signature, we don't want that
    if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
      docstring = None
    if docstring:
      # remove indentation from docstring
      import inspect
      docstring = inspect.cleandoc(docstring)
    return docstring
  @classmethod
  def get_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
    type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
    try:
      return_hint = type_hints['return']
    except KeyError as e:
      raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') from e
    next_node_edges: dict[str, Edge] = {}
    end_edge: Edge | None = None
    returns_base_node: bool = False
    for return_type in _utils.get_union_args(return_hint):
      return_type, annotations = _utils.unpack_annotated(return_type)
      edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
      return_type_origin = get_origin(return_type) or return_type
      if return_type_origin is End:
        end_edge = edge
      elif return_type_origin is BaseNode:
        # TODO: Should we disallow this?
        returns_base_node = True
      elif issubclass(return_type_origin, BaseNode):
        next_node_edges[return_type.get_id()] = edge
      else:
        raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')
    return NodeDef(
      cls,
      cls.get_id(),
      cls.get_note(),
      next_node_edges,
      end_edge,
      returns_base_node,
    )

```
  
---|---  
####  docstring_notes `class-attribute`
```
docstring_notes: bool = False

```

Set to `True` to generate mermaid diagram notes from the class's docstring.
While this can add valuable information to the diagram, it can make diagrams harder to view, hence it is disabled by default. You can also customise notes overriding the `get_note` method.
####  run `abstractmethod` `async`
```
run(
  ctx: GraphRunContext[StateT, DepsT]
) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]

```

Run the node.
This is an abstract method that must be implemented by subclasses.
Return types used at runtime
The return type of this method are read by `pydantic_graph` at runtime and used to define which nodes can be called next in the graph. This is displayed in mermaid diagrams and enforced when running the graph.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`ctx` |  `GraphRunContext[StateT, DepsT]` |  The graph context. |  _required_  
Returns:
Type | Description  
---|---  
`BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]` |  The next node to run or `End` to signal the end of the graph.  
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
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
```
| ```
@abstractmethod
async def run(self, ctx: GraphRunContext[StateT, DepsT]) -> BaseNode[StateT, DepsT, Any] | End[NodeRunEndT]:
"""Run the node.
  This is an abstract method that must be implemented by subclasses.
  !!! note "Return types used at runtime"
    The return type of this method are read by `pydantic_graph` at runtime and used to define which
    nodes can be called next in the graph. This is displayed in [mermaid diagrams](mermaid.md)
    and enforced when running the graph.
  Args:
    ctx: The graph context.
  Returns:
    The next node to run or [`End`][pydantic_graph.nodes.End] to signal the end of the graph.
  """
  ...

```
  
---|---  
####  get_id `cached` `classmethod`
```
get_id() -> str

```

Get the ID of the node.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
67
68
69
70
71
```
| ```
@classmethod
@cache
def get_id(cls) -> str:
"""Get the ID of the node."""
  return cls.__name__

```
  
---|---  
####  get_note `classmethod`
```
get_note() -> str | None

```

Get a note about the node to render on mermaid charts.
By default, this returns a note only if `docstring_notes` is `True`. You can override this method to customise the node notes.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
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
```
| ```
@classmethod
def get_note(cls) -> str | None:
"""Get a note about the node to render on mermaid charts.
  By default, this returns a note only if [`docstring_notes`][pydantic_graph.nodes.BaseNode.docstring_notes]
  is `True`. You can override this method to customise the node notes.
  """
  if not cls.docstring_notes:
    return None
  docstring = cls.__doc__
  # dataclasses get an automatic docstring which is just their signature, we don't want that
  if docstring and is_dataclass(cls) and docstring.startswith(f'{cls.__name__}('):
    docstring = None
  if docstring:
    # remove indentation from docstring
    import inspect
    docstring = inspect.cleandoc(docstring)
  return docstring

```
  
---|---  
####  get_node_def `classmethod`
```
get_node_def(
  local_ns: dict[str, Any] | None
) -> NodeDef[StateT, DepsT, NodeRunEndT]

```

Get the node definition.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
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
122
123
124
125
126
```
| ```
@classmethod
def get_node_def(cls, local_ns: dict[str, Any] | None) -> NodeDef[StateT, DepsT, NodeRunEndT]:
"""Get the node definition."""
  type_hints = get_type_hints(cls.run, localns=local_ns, include_extras=True)
  try:
    return_hint = type_hints['return']
  except KeyError as e:
    raise exceptions.GraphSetupError(f'Node {cls} is missing a return type hint on its `run` method') from e
  next_node_edges: dict[str, Edge] = {}
  end_edge: Edge | None = None
  returns_base_node: bool = False
  for return_type in _utils.get_union_args(return_hint):
    return_type, annotations = _utils.unpack_annotated(return_type)
    edge = next((a for a in annotations if isinstance(a, Edge)), Edge(None))
    return_type_origin = get_origin(return_type) or return_type
    if return_type_origin is End:
      end_edge = edge
    elif return_type_origin is BaseNode:
      # TODO: Should we disallow this?
      returns_base_node = True
    elif issubclass(return_type_origin, BaseNode):
      next_node_edges[return_type.get_id()] = edge
    else:
      raise exceptions.GraphSetupError(f'Invalid return type: {return_type}')
  return NodeDef(
    cls,
    cls.get_id(),
    cls.get_note(),
    next_node_edges,
    end_edge,
    returns_base_node,
  )

```
  
---|---  
###  End `dataclass`
Bases: `Generic[RunEndT]`
Type to return from a node to signal the end of the graph.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
129
130
131
132
133
134
```
| ```
@dataclass
class End(Generic[RunEndT]):
"""Type to return from a node to signal the end of the graph."""
  data: RunEndT
"""Data to return from the graph."""

```
  
---|---  
####  data `instance-attribute`
```
data: RunEndT

```

Data to return from the graph.
###  Edge `dataclass`
Annotation to apply a label to an edge in a graph.
Source code in `pydantic_graph/pydantic_graph/nodes.py`
```
137
138
139
140
141
142
```
| ```
@dataclass
class Edge:
"""Annotation to apply a label to an edge in a graph."""
  label: str | None
"""Label for the edge."""

```
  
---|---  
####  label `instance-attribute`
```
label: str | None

```

Label for the edge.
###  DepsT `module-attribute`
```
DepsT = TypeVar('DepsT', default=None, contravariant=True)

```

Type variable for the dependencies of a graph and node.
###  RunEndT `module-attribute`
```
RunEndT = TypeVar('RunEndT', covariant=True, default=None)

```

Covariant type variable for the return type of a graph `run`.
###  NodeRunEndT `module-attribute`
```
NodeRunEndT = TypeVar(
  "NodeRunEndT", covariant=True, default=Never
)

```

Covariant type variable for the return type of a node `run`.
