Skip to content
# dpi
## Classes
### LogicalPosition
A position represented in logical pixels.
#### Since
2.0.0
#### Constructors
##### new LogicalPosition()
```

newLogicalPosition(x, y): LogicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`x`| `number`  
`y`| `number`  
###### Returns
`LogicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L208
##### new LogicalPosition()
```

newLogicalPosition(object): LogicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.Logical`| `object`  
`object.Logical.x`| `number`  
`object.Logical.y`| `number`  
###### Returns
`LogicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L209
##### new LogicalPosition()
```

newLogicalPosition(object): LogicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.x`| `number`  
`object.y`| `number`  
###### Returns
`LogicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L210
#### Properties
Property| Modifier| Type| Default value| Defined in  
---|---|---|---|---  
`type`| `readonly`| `"Logical"`| `'Logical'`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L204  
`x`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L205  
`y`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L206  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`x`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L252  
`y`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L253  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L250
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`x`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L252  
`y`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L253  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L257
##### toPhysical()
```

toPhysical(scaleFactor): PhysicalPosition

```

Converts the logical position to a physical one.
###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`PhysicalPosition`
###### Example
```

import { LogicalPosition } from'@tauri-apps/api/dpi';
import { getCurrentWindow } from'@tauri-apps/api/window';
const appWindow = getCurrentWindow();
const factor = await appWindow.scaleFactor();
const position = newLogicalPosition(400, 500);
const physical = position.toPhysical(factor);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L246
### LogicalSize
A size represented in logical pixels.
#### Since
2.0.0
#### Constructors
##### new LogicalSize()
```

newLogicalSize(width, height): LogicalSize

```

###### Parameters
Parameter| Type  
---|---  
`width`| `number`  
`height`| `number`  
###### Returns
`LogicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L17
##### new LogicalSize()
```

newLogicalSize(object): LogicalSize

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.Logical`| `object`  
`object.Logical.height`| `number`  
`object.Logical.width`| `number`  
###### Returns
`LogicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L18
##### new LogicalSize()
```

newLogicalSize(object): LogicalSize

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.height`| `number`  
`object.width`| `number`  
###### Returns
`LogicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L19
#### Properties
Property| Modifier| Type| Default value| Defined in  
---|---|---|---|---  
`height`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L15  
`type`| `readonly`| `"Logical"`| `'Logical'`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L13  
`width`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L14  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`height`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L62  
`width`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L61  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L59
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`height`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L62  
`width`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L61  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L66
##### toPhysical()
```

toPhysical(scaleFactor): PhysicalSize

```

Converts the logical size to a physical one.
###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`PhysicalSize`
###### Example
```

import { LogicalSize } from'@tauri-apps/api/dpi';
import { getCurrentWindow } from'@tauri-apps/api/window';
const appWindow = getCurrentWindow();
const factor = await appWindow.scaleFactor();
const size = newLogicalSize(400, 500);
const physical = size.toPhysical(factor);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L55
### PhysicalPosition
A position represented in physical pixels.
#### Since
2.0.0
#### Constructors
##### new PhysicalPosition()
```

newPhysicalPosition(x, y): PhysicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`x`| `number`  
`y`| `number`  
###### Returns
`PhysicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L273
##### new PhysicalPosition()
```

newPhysicalPosition(object): PhysicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.Physical`| `object`  
`object.Physical.x`| `number`  
`object.Physical.y`| `number`  
###### Returns
`PhysicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L274
##### new PhysicalPosition()
```

newPhysicalPosition(object): PhysicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.x`| `number`  
`object.y`| `number`  
###### Returns
`PhysicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L275
#### Properties
Property| Modifier| Type| Default value| Defined in  
---|---|---|---|---  
`type`| `readonly`| `"Physical"`| `'Physical'`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L269  
`x`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L270  
`y`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L271  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`x`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L317  
`y`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L318  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L315
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`x`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L317  
`y`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L318  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L322
##### toLogical()
```

toLogical(scaleFactor): LogicalPosition

```

Converts the physical position to a logical one.
###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`LogicalPosition`
###### Example
```

import { PhysicalPosition } from'@tauri-apps/api/dpi';
import { getCurrentWindow } from'@tauri-apps/api/window';
const appWindow = getCurrentWindow();
const factor = await appWindow.scaleFactor();
const position = newPhysicalPosition(400, 500);
const physical = position.toLogical(factor);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L311
### PhysicalSize
A size represented in physical pixels.
#### Since
2.0.0
#### Constructors
##### new PhysicalSize()
```

newPhysicalSize(width, height): PhysicalSize

```

###### Parameters
Parameter| Type  
---|---  
`width`| `number`  
`height`| `number`  
###### Returns
`PhysicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L82
##### new PhysicalSize()
```

newPhysicalSize(object): PhysicalSize

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.Physical`| `object`  
`object.Physical.height`| `number`  
`object.Physical.width`| `number`  
###### Returns
`PhysicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L83
##### new PhysicalSize()
```

newPhysicalSize(object): PhysicalSize

```

###### Parameters
Parameter| Type  
---|---  
`object`| `object`  
`object.height`| `number`  
`object.width`| `number`  
###### Returns
`PhysicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L84
#### Properties
Property| Modifier| Type| Default value| Defined in  
---|---|---|---|---  
`height`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L80  
`type`| `readonly`| `"Physical"`| `'Physical'`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L78  
`width`| `public`| `number`| `undefined`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L79  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`height`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L123  
`width`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L122  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L120
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
Name| Type| Defined in  
---|---|---  
`height`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L123  
`width`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L122  
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L127
##### toLogical()
```

toLogical(scaleFactor): LogicalSize

```

Converts the physical size to a logical one.
###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`LogicalSize`
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const appWindow = getCurrentWindow();
const factor = await appWindow.scaleFactor();
const size = await appWindow.innerSize(); // PhysicalSize
const logical = size.toLogical(factor);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L116
### Position
A position represented either in physical or in logical pixels.
This type is basically a union type of `LogicalSize` and `PhysicalSize` but comes in handy when using `tauri::Position` in Rust as an argument to a command, as this class automatically serializes into a valid format so it can be deserialized correctly into `tauri::Position`
So instead of
```

import { invoke } from'@tauri-apps/api/core';
import { LogicalPosition, PhysicalPosition } from'@tauri-apps/api/dpi';
const position:LogicalPosition|PhysicalPosition = someFunction(); // where someFunction returns either LogicalPosition or PhysicalPosition
const validPosition = position instanceof LogicalPosition
? { Logical: { x: position.x, y: position.y } }
: { Physical: { x: position.x, y: position.y } }
awaitinvoke("do_something_with_position", { position: validPosition });

```

You can just use `Position`
```

import { invoke } from'@tauri-apps/api/core';
import { LogicalPosition, PhysicalPosition, Position } from'@tauri-apps/api/dpi';
const position:LogicalPosition|PhysicalPosition = someFunction(); // where someFunction returns either LogicalPosition or PhysicalPosition
const validPosition = newPosition(position);
awaitinvoke("do_something_with_position", { position: validPosition });

```

#### Since
2.1.0
#### Constructors
##### new Position()
```

newPosition(position): Position

```

###### Parameters
Parameter| Type  
---|---  
`position`| `LogicalPosition` | `PhysicalPosition`  
###### Returns
`Position`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L362
#### Properties
Property| Type| Defined in  
---|---|---  
`position`| `LogicalPosition` | `PhysicalPosition`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L360  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L378
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L387
##### toLogical()
```

toLogical(scaleFactor): LogicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`LogicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L366
##### toPhysical()
```

toPhysical(scaleFactor): PhysicalPosition

```

###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`PhysicalPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L372
### Size
A size represented either in physical or in logical pixels.
This type is basically a union type of `LogicalSize` and `PhysicalSize` but comes in handy when using `tauri::Size` in Rust as an argument to a command, as this class automatically serializes into a valid format so it can be deserialized correctly into `tauri::Size`
So instead of
```

import { invoke } from'@tauri-apps/api/core';
import { LogicalSize, PhysicalSize } from'@tauri-apps/api/dpi';
const size:LogicalSize|PhysicalSize = someFunction(); // where someFunction returns either LogicalSize or PhysicalSize
const validSize = size instanceof LogicalSize
? { Logical: { width: size.width, height: size.height } }
: { Physical: { width: size.width, height: size.height } }
awaitinvoke("do_something_with_size", { size: validSize });

```

You can just use `Size`
```

import { invoke } from'@tauri-apps/api/core';
import { LogicalSize, PhysicalSize, Size } from'@tauri-apps/api/dpi';
const size:LogicalSize|PhysicalSize = someFunction(); // where someFunction returns either LogicalSize or PhysicalSize
const validSize = newSize(size);
awaitinvoke("do_something_with_size", { size: validSize });

```

#### Since
2.1.0
#### Constructors
##### new Size()
```

newSize(size): Size

```

###### Parameters
Parameter| Type  
---|---  
`size`| `LogicalSize` | `PhysicalSize`  
###### Returns
`Size`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L167
#### Properties
Property| Type| Defined in  
---|---|---  
`size`| `LogicalSize` | `PhysicalSize`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L165  
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): object

```

###### Returns
`object`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L183
##### toJSON()
```

toJSON(): object

```

###### Returns
`object`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L192
##### toLogical()
```

toLogical(scaleFactor): LogicalSize

```

###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`LogicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L171
##### toPhysical()
```

toPhysical(scaleFactor): PhysicalSize

```

###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`PhysicalSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/dpi.ts#L177
© 2025 Tauri Contributors. CC-BY / MIT
