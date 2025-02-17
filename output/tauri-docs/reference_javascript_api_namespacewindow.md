Skip to content
# window
Provides APIs to create windows, communicate with other windows and manipulate the current window.
#### Window events
Events can be listened to using Window.listen:
```

import { getCurrentWindow } from"@tauri-apps/api/window";
getCurrentWindow().listen("my-window-event", ({ event, payload })=> { });

```

## References
### Color
Re-exports Color
### DragDropEvent
Re-exports DragDropEvent
### LogicalPosition
Re-exports LogicalPosition
### LogicalSize
Re-exports LogicalSize
### PhysicalPosition
Re-exports PhysicalPosition
### PhysicalSize
Re-exports PhysicalSize
## Enumerations
### BackgroundThrottlingPolicy
Background throttling policy
#### Since
2.0.0
#### Enumeration Members
##### Disabled
```

Disabled: "disabled";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2030
##### Suspend
```

Suspend: "suspend";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2032
##### Throttle
```

Throttle: "throttle";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2031
### Effect
Platform-specific window effects
#### Since
2.0.0
#### Enumeration Members
##### Acrylic
```

Acrylic: "acrylic";

```

**Windows 10/11**
#### Notes
This effect has bad performance when resizing/dragging the window on Windows 10 v1903+ and Windows 11 build 22000.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2146
##### ~~AppearanceBased~~
```

AppearanceBased: "appearanceBased";

```

A default material appropriate for the view’s effectiveAppearance. **macOS 10.14-**
###### Deprecated
since macOS 10.14. You should instead choose an appropriate semantic material.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2046
##### Blur
```

Blur: "blur";

```

**Windows 7/10/11(22H1) Only**
#### Notes
This effect has bad performance when resizing/dragging the window on Windows 11 build 22621.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2138
##### ContentBackground
```

ContentBackground: "contentBackground";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2118
##### ~~Dark~~
```

Dark: "dark";

```

**macOS 10.14-**
###### Deprecated
since macOS 10.14. Use a semantic material instead.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2058
##### FullScreenUI
```

FullScreenUI: "fullScreenUI";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2110
##### HeaderView
```

HeaderView: "headerView";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2094
##### HudWindow
```

HudWindow: "hudWindow";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2106
##### ~~Light~~
```

Light: "light";

```

**macOS 10.14-**
###### Deprecated
since macOS 10.14. Use a semantic material instead.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2052
##### ~~MediumLight~~
```

MediumLight: "mediumLight";

```

**macOS 10.14-**
###### Deprecated
since macOS 10.14. Use a semantic material instead.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2064
##### Menu
```

Menu: "menu";

```

**macOS 10.11+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2082
##### Mica
```

Mica: "mica";

```

**Windows 11 Only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2130
##### Popover
```

Popover: "popover";

```

**macOS 10.11+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2086
##### Selection
```

Selection: "selection";

```

**macOS 10.10+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2078
##### Sheet
```

Sheet: "sheet";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2098
##### Sidebar
```

Sidebar: "sidebar";

```

**macOS 10.11+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2090
##### Tabbed
```

Tabbed: "tabbed";

```

Tabbed effect that matches the system dark perefence **Windows 11 Only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2150
##### TabbedDark
```

TabbedDark: "tabbedDark";

```

Tabbed effect with dark mode but only if dark mode is enabled on the system **Windows 11 Only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2154
##### TabbedLight
```

TabbedLight: "tabbedLight";

```

Tabbed effect with light mode **Windows 11 Only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2158
##### Titlebar
```

Titlebar: "titlebar";

```

**macOS 10.10+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2074
##### Tooltip
```

Tooltip: "tooltip";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2114
##### ~~UltraDark~~
```

UltraDark: "ultraDark";

```

**macOS 10.14-**
###### Deprecated
since macOS 10.14. Use a semantic material instead.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2070
##### UnderPageBackground
```

UnderPageBackground: "underPageBackground";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2126
##### UnderWindowBackground
```

UnderWindowBackground: "underWindowBackground";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2122
##### WindowBackground
```

WindowBackground: "windowBackground";

```

**macOS 10.14+**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2102
### EffectState
Window effect state **macOS only**
#### See
https://developer.apple.com/documentation/appkit/nsvisualeffectview/state
#### Since
2.0.0
#### Enumeration Members
##### Active
```

Active: "active";

```

Make window effect state always active **macOS only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2176
##### FollowsWindowActiveState
```

FollowsWindowActiveState: "followsWindowActiveState";

```

Make window effect state follow the window’s active state **macOS only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2172
##### Inactive
```

Inactive: "inactive";

```

Make window effect state always inactive **macOS only**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2180
### ProgressBarStatus
#### Enumeration Members
##### Error
```

Error: "error";

```

Error state. **Treated as Normal on linux**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L185
##### Indeterminate
```

Indeterminate: "indeterminate";

```

Indeterminate state. **Treated as Normal on Linux and macOS**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L177
##### None
```

None: "none";

```

Hide progress bar.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L169
##### Normal
```

Normal: "normal";

```

Normal state.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L173
##### Paused
```

Paused: "paused";

```

Paused state. **Treated as Normal on Linux**
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L181
### UserAttentionType
Attention type to request on a window.
#### Since
1.0.0
#### Enumeration Members
##### Critical
```

Critical: 1;

```

#### Platform-specific
  * **macOS:** Bounces the dock icon until the application is in focus.
  * **Windows:** Flashes both the window and the taskbar button until the application is in focus.


**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L94
##### Informational
```

Informational: 2;

```

#### Platform-specific
  * **macOS:** Bounces the dock icon once.
  * **Windows:** Flashes the taskbar button until the application is in focus.


**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L100
## Classes
### CloseRequestedEvent
#### Constructors
##### new CloseRequestedEvent()
```

newCloseRequestedEvent(event): CloseRequestedEvent

```

###### Parameters
Parameter| Type  
---|---  
`event`| `Event`<`unknown`>  
###### Returns
`CloseRequestedEvent`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L110
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`event`| `EventName`| Event name| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L105  
`id`| `number`| Event identifier used to unlisten| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L107  
#### Methods
##### isPreventDefault()
```

isPreventDefault(): boolean

```

###### Returns
`boolean`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L119
##### preventDefault()
```

preventDefault(): void

```

###### Returns
`void`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L115
### Window
Create new window or get a handle to an existing one.
Windows are identified by a _label_ a unique identifier that can be used to reference it later. It may only contain alphanumeric characters `a-zA-Z` plus the following special characters `-`, `/`, `:` and `_`.
#### Example
```

import { Window } from"@tauri-apps/api/window"
const appWindow = newWindow('theUniqueLabel');
appWindow.once('tauri://created', function() {
// window successfully created
});
appWindow.once('tauri://error', function(e) {
// an error happened creating the window
});
// emit an event to the backend
await appWindow.emit("some-event", "data");
// listen to an event from the backend
const unlisten = await appWindow.listen("event-name", e => {});
unlisten();

```

#### Since
2.0.0
#### Extended by
  * `WebviewWindow`


#### Constructors
##### new Window()
```

newWindow(label, options): Window

```

Creates a new Window.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`| `string`| The unique window label. Must be alphanumeric: `a-zA-Z-/:_`.  
`options`| `WindowOptions`| -  
###### Returns
`Window`
The Window instance to communicate with the window.
###### Example
```

import { Window } from'@tauri-apps/api/window';
const appWindow = newWindow('my-label');
appWindow.once('tauri://created', function() {
// window successfully created
});
appWindow.once('tauri://error', function(e) {
// an error happened creating the window
});

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L293
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`label`| `string`| The window label. It is a unique identifier for the window, can be used to reference it later.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L271  
`listeners`| `Record`<`string`, `EventCallback`<`any`>[]>| Local event listeners.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L274  
#### Methods
##### center()
```

center(): Promise<void>

```

Centers the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().center();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L814
##### clearEffects()
```

clearEffects(): Promise<void>

```

Clear any applied effects if possible.
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1202
##### close()
```

close(): Promise<void>

```

Closes the window.
Note this emits a closeRequested event so you can intercept it. To force window close, use Window.destroy.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().close();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1123
##### destroy()
```

destroy(): Promise<void>

```

Destroys the window. Behaves like Window.close but forces the window close instead of emitting a closeRequested event.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().destroy();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1139
##### emit()
```

emit(event, payload?):Promise<void>

```

Emits an event to all targets.
###### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `string`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`payload`?| `unknown`| Event payload.  
###### Returns
`Promise`<`void`>
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().emit('window-loaded', { loggedIn: true, token: 'authToken' });

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L444
##### emitTo()
```

emitTo(
target,
event,
payload?):Promise<void>

```

Emits an event to all targets matching the given target.
###### Parameters
Parameter| Type| Description  
---|---|---  
`target`| `string` | `EventTarget`| Label of the target Window/Webview/WebviewWindow or raw EventTarget object.  
`event`| `string`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`payload`?| `unknown`| Event payload.  
###### Returns
`Promise`<`void`>
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().emit('main', 'window-loaded', { loggedIn: true, token: 'authToken' });

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L471
##### hide()
```

hide(): Promise<void>

```

Sets the window visibility to false.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().hide();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1105
##### innerPosition()
```

innerPosition(): Promise<PhysicalPosition>

```

The position of the top-left hand corner of the window’s client area relative to the top-left hand corner of the desktop.
###### Returns
`Promise`<`PhysicalPosition`>
The window’s inner position.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const position = await getCurrentWindow().innerPosition();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L532
##### innerSize()
```

innerSize(): Promise<PhysicalSize>

```

The physical size of the window’s client area. The client area is the content of the window, excluding the title bar and borders.
###### Returns
`Promise`<`PhysicalSize`>
The window’s inner size.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const size = await getCurrentWindow().innerSize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L565
##### isClosable()
```

isClosable(): Promise<boolean>

```

Gets the window’s native close button state.
#### Platform-specific
  * **iOS / Android:** Unsupported.


###### Returns
`Promise`<`boolean`>
Whether the window’s native close button is enabled or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const closable = await getCurrentWindow().isClosable();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L745
##### isDecorated()
```

isDecorated(): Promise<boolean>

```

Gets the window’s current decorated state.
###### Returns
`Promise`<`boolean`>
Whether the window is decorated or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const decorated = await getCurrentWindow().isDecorated();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L666
##### isEnabled()
```

isEnabled(): Promise<boolean>

```

Whether the window is enabled or disabled.
###### Returns
`Promise`<`boolean`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setEnabled(false);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L906
##### isFocused()
```

isFocused(): Promise<boolean>

```

Gets the window’s current focus state.
###### Returns
`Promise`<`boolean`>
Whether the window is focused or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const focused = await getCurrentWindow().isFocused();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L650
##### isFullscreen()
```

isFullscreen(): Promise<boolean>

```

Gets the window’s current fullscreen state.
###### Returns
`Promise`<`boolean`>
Whether the window is in fullscreen mode or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const fullscreen = await getCurrentWindow().isFullscreen();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L604
##### isMaximizable()
```

isMaximizable(): Promise<boolean>

```

Gets the window’s native maximize button state.
#### Platform-specific
  * **Linux / iOS / Android:** Unsupported.


###### Returns
`Promise`<`boolean`>
Whether the window’s native maximize button is enabled or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const maximizable = await getCurrentWindow().isMaximizable();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L703
##### isMaximized()
```

isMaximized(): Promise<boolean>

```

Gets the window’s current maximized state.
###### Returns
`Promise`<`boolean`>
Whether the window is maximized or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const maximized = await getCurrentWindow().isMaximized();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L634
##### isMinimizable()
```

isMinimizable(): Promise<boolean>

```

Gets the window’s native minimize button state.
#### Platform-specific
  * **Linux / iOS / Android:** Unsupported.


###### Returns
`Promise`<`boolean`>
Whether the window’s native minimize button is enabled or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const minimizable = await getCurrentWindow().isMinimizable();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L724
##### isMinimized()
```

isMinimized(): Promise<boolean>

```

Gets the window’s current minimized state.
###### Returns
`Promise`<`boolean`>
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const minimized = await getCurrentWindow().isMinimized();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L618
##### isResizable()
```

isResizable(): Promise<boolean>

```

Gets the window’s current resizable state.
###### Returns
`Promise`<`boolean`>
Whether the window is resizable or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const resizable = await getCurrentWindow().isResizable();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L682
##### isVisible()
```

isVisible(): Promise<boolean>

```

Gets the window’s current visible state.
###### Returns
`Promise`<`boolean`>
Whether the window is visible or not.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const visible = await getCurrentWindow().isVisible();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L761
##### listen()
```

listen<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this window.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `EventName`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`handler`| `EventCallback`<`T`>| Event handler.  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const unlisten = await getCurrentWindow().listen<string>('state-changed', (event) => {
console.log(`Got error: ${payload}`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L382
##### maximize()
```

maximize(): Promise<void>

```

Maximizes the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().maximize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1009
##### minimize()
```

minimize(): Promise<void>

```

Minimizes the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().minimize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1057
##### once()
```

once<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this window only once.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`event`| `EventName`| Event name. Must include only alphanumeric characters, `-`, `/`, `:` and `_`.  
`handler`| `EventCallback`<`T`>| Event handler.  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const unlisten = await getCurrentWindow().once<null>('initialized', (event) => {
console.log(`Window initialized!`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L417
##### onCloseRequested()
```

onCloseRequested(handler): Promise<UnlistenFn>

```

Listen to window close requested. Emitted when the user requests to closes the window.
###### Parameters
Parameter| Type  
---|---  
`handler`| (`event`) => `void` | `Promise`<`void`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
import { confirm } from'@tauri-apps/api/dialog';
const unlisten = await getCurrentWindow().onCloseRequested(async (event) => {
const confirmed = await confirm('Are you sure?');
if (!confirmed) {
// user did not confirm closing the window; let's prevent it
event.preventDefault();
}
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1824
##### onDragDropEvent()
```

onDragDropEvent(handler): Promise<UnlistenFn>

```

Listen to a file drop event. The listener is triggered when the user hovers the selected files on the webview, drops the files or cancels the operation.
###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`DragDropEvent`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/webview";
const unlisten = await getCurrentWindow().onDragDropEvent((event) => {
if (event.payload.type === 'over') {
console.log('User hovering', event.payload.position);
} else if (event.payload.type === 'drop') {
console.log('User dropped', event.payload.paths);
} else {
console.log('File drop cancelled');
}
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1862
##### onFocusChanged()
```

onFocusChanged(handler): Promise<UnlistenFn>

```

Listen to window focus change.
###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`boolean`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
const unlisten = await getCurrentWindow().onFocusChanged(({ payload: focused }) => {
console.log('Focus changed, window is focused? ' + focused);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1940
##### onMoved()
```

onMoved(handler): Promise<UnlistenFn>

```

Listen to window move.
###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`PhysicalPosition`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
const unlisten = await getCurrentWindow().onMoved(({ payload: position }) => {
console.log('Window moved', position);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1795
##### onResized()
```

onResized(handler): Promise<UnlistenFn>

```

Listen to window resize.
###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`PhysicalSize`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
const unlisten = await getCurrentWindow().onResized(({ payload: size }) => {
console.log('Window resized', size);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1771
##### onScaleChanged()
```

onScaleChanged(handler): Promise<UnlistenFn>

```

Listen to window scale change. Emitted when the window’s scale factor has changed. The following user actions can cause DPI changes:
  * Changing the display’s resolution.
  * Changing the display’s scale factor (e.g. in Control Panel on Windows).
  * Moving the window to a display with a different scale factor.


###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`ScaleFactorChanged`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
const unlisten = await getCurrentWindow().onScaleChanged(({ payload }) => {
console.log('Scale changed', payload.scaleFactor, payload.size);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1980
##### onThemeChanged()
```

onThemeChanged(handler): Promise<UnlistenFn>

```

Listen to the system theme change.
###### Parameters
Parameter| Type  
---|---  
`handler`| `EventCallback`<`Theme`>  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event. Note that removing the listener is required if your listener goes out of scope e.g. the component is unmounted.
###### Example
```

import { getCurrentWindow } from"@tauri-apps/api/window";
const unlisten = await getCurrentWindow().onThemeChanged(({ payload: theme }) => {
console.log('New theme: ' + theme);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2006
##### outerPosition()
```

outerPosition(): Promise<PhysicalPosition>

```

The position of the top-left hand corner of the window relative to the top-left hand corner of the desktop.
###### Returns
`Promise`<`PhysicalPosition`>
The window’s outer position.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const position = await getCurrentWindow().outerPosition();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L548
##### outerSize()
```

outerSize(): Promise<PhysicalSize>

```

The physical size of the entire window. These dimensions include the title bar and borders. If you don’t want that (and you usually don’t), use inner_size instead.
###### Returns
`Promise`<`PhysicalSize`>
The window’s outer size.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const size = await getCurrentWindow().outerSize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L585
##### requestUserAttention()
```

requestUserAttention(requestType): Promise<void>

```

Requests user attention to the window, this has no effect if the application is already focused. How requesting for user attention manifests is platform dependent, see `UserAttentionType` for details.
Providing `null` will unset the request for user attention. Unsetting the request for user attention might not be done automatically by the WM when the window receives input.
#### Platform-specific
  * **macOS:** `null` has no effect.
  * **Linux:** Urgency levels have the same effect.


###### Parameters
Parameter| Type  
---|---  
`requestType`| `null` | `UserAttentionType`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().requestUserAttention();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L840
##### scaleFactor()
```

scaleFactor(): Promise<number>

```

The scale factor that can be used to map physical pixels to logical pixels.
###### Returns
`Promise`<`number`>
The window’s monitor scale factor.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const factor = await getCurrentWindow().scaleFactor();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L516
##### setAlwaysOnBottom()
```

setAlwaysOnBottom(alwaysOnBottom): Promise<void>

```

Whether the window should always be below other windows.
###### Parameters
Parameter| Type| Description  
---|---|---  
`alwaysOnBottom`| `boolean`| Whether the window should always be below other windows or not.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setAlwaysOnBottom(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1238
##### setAlwaysOnTop()
```

setAlwaysOnTop(alwaysOnTop): Promise<void>

```

Whether the window should always be on top of other windows.
###### Parameters
Parameter| Type| Description  
---|---|---  
`alwaysOnTop`| `boolean`| Whether the window should always be on top of other windows or not.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setAlwaysOnTop(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1220
##### setBackgroundColor()
```

setBackgroundColor(color): Promise<void>

```

Sets the window background color.
#### Platform-specific:
  * **Windows:** alpha channel is ignored.
  * **iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`color`| `Color`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Since
2.1.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1532
##### setBadgeCount()
```

setBadgeCount(count?):Promise<void>

```

Sets the badge count. It is app wide and not specific to this window.
#### Platform-specific
  * **Windows** : Unsupported. Use @{linkcode Window.setOverlayIcon} instead.


###### Parameters
Parameter| Type| Description  
---|---|---  
`count`?| `number`| The badge count. Use `undefined` to remove the badge.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setBadgeCount(5);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1624
##### setBadgeLabel()
```

setBadgeLabel(label?):Promise<void>

```

Sets the badge cont **macOS only**.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`?| `string`| The badge label. Use `undefined` to remove the badge.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setBadgeLabel("Hello");

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1643
##### setClosable()
```

setClosable(closable): Promise<void>

```

Sets whether the window’s native close button is enabled or not.
#### Platform-specific
  * **Linux:** GTK+ will do its best to convince the window manager not to show a close button. Depending on the system, this function may not have any effect when called on a window that is already visible
  * **iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`closable`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setClosable(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L974
##### setContentProtected()
```

setContentProtected(protected_): Promise<void>

```

Prevents the window contents from being captured by other apps.
###### Parameters
Parameter| Type  
---|---  
`protected_`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setContentProtected(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1255
##### setCursorGrab()
```

setCursorGrab(grab): Promise<void>

```

Grabs the cursor, preventing it from leaving the window.
There’s no guarantee that the cursor will be hidden. You should hide it by yourself if you want so.
#### Platform-specific
  * **Linux:** Unsupported.
  * **macOS:** This locks the cursor in a fixed location, which looks visually awkward.


###### Parameters
Parameter| Type| Description  
---|---|---  
`grab`| `boolean`| `true` to grab the cursor icon, `false` to release it.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setCursorGrab(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1471
##### setCursorIcon()
```

setCursorIcon(icon): Promise<void>

```

Modifies the cursor icon of the window.
###### Parameters
Parameter| Type| Description  
---|---|---  
`icon`| `CursorIcon`| The new cursor icon.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setCursorIcon('help');

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1513
##### setCursorPosition()
```

setCursorPosition(position): Promise<void>

```

Changes the position of the cursor in window coordinates.
###### Parameters
Parameter| Type| Description  
---|---|---  
`position`| `LogicalPosition` | `PhysicalPosition` | `Position`| The new cursor position.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, LogicalPosition } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setCursorPosition(newLogicalPosition(600, 300));

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1547
##### setCursorVisible()
```

setCursorVisible(visible): Promise<void>

```

Modifies the cursor’s visibility.
#### Platform-specific
  * **Windows:** The cursor is only hidden within the confines of the window.
  * **macOS:** The cursor is hidden as long as the window has input focus, even if the cursor is outside of the window.


###### Parameters
Parameter| Type| Description  
---|---|---  
`visible`| `boolean`| If `false`, this will hide the cursor. If `true`, this will show the cursor.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setCursorVisible(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1495
##### setDecorations()
```

setDecorations(decorations): Promise<void>

```

Whether the window should have borders and bars.
###### Parameters
Parameter| Type| Description  
---|---|---  
`decorations`| `boolean`| Whether the window should have borders and bars.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setDecorations(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1156
##### setEffects()
```

setEffects(effects): Promise<void>

```

Set window effects.
###### Parameters
Parameter| Type  
---|---  
`effects`| `Effects`  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1192
##### setEnabled()
```

setEnabled(enabled): Promise<void>

```

Enable or disable the window.
###### Parameters
Parameter| Type  
---|---  
`enabled`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setEnabled(false);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L887
##### setFocus()
```

setFocus(): Promise<void>

```

Bring the window to front and focus.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setFocus();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1397
##### setFullscreen()
```

setFullscreen(fullscreen): Promise<void>

```

Sets the window fullscreen state.
###### Parameters
Parameter| Type| Description  
---|---|---  
`fullscreen`| `boolean`| Whether the window should go to fullscreen or not.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setFullscreen(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1380
##### setIcon()
```

setIcon(icon): Promise<void>

```

Sets the window icon.
###### Parameters
Parameter| Type| Description  
---|---|---  
`icon`| | `string` | `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`> | `Image`| Icon bytes or path to the icon file.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setIcon('/tauri/awesome.png');

```

Note that you may need the `image-ico` or `image-png` Cargo features to use this API. To enable it, change your Cargo.toml file:
```

[dependencies]
tauri = { version = "...", features = ["...", "image-png"] }

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1421
##### setIgnoreCursorEvents()
```

setIgnoreCursorEvents(ignore): Promise<void>

```

Changes the cursor events behavior.
###### Parameters
Parameter| Type| Description  
---|---|---  
`ignore`| `boolean`| `true` to ignore the cursor events; `false` to process them as usual.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setIgnoreCursorEvents(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1568
##### setMaximizable()
```

setMaximizable(maximizable): Promise<void>

```

Sets whether the window’s native maximize button is enabled or not. If resizable is set to false, this setting is ignored.
#### Platform-specific
  * **macOS:** Disables the “zoom” button in the window titlebar, which is also used to enter fullscreen mode.
  * **Linux / iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`maximizable`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setMaximizable(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L929
##### setMaxSize()
```

setMaxSize(size): Promise<void>

```

Sets the window maximum inner size. If the `size` argument is undefined, the constraint is unset.
###### Parameters
Parameter| Type| Description  
---|---|---  
`size`| | `undefined` | `null` | `LogicalSize` | `PhysicalSize` | `Size`| The logical or physical inner size, or `null` to unset the constraint.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, LogicalSize } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setMaxSize(newLogicalSize(600, 500));

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1311
##### setMinimizable()
```

setMinimizable(minimizable): Promise<void>

```

Sets whether the window’s native minimize button is enabled or not.
#### Platform-specific
  * **Linux / iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`minimizable`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setMinimizable(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L951
##### setMinSize()
```

setMinSize(size): Promise<void>

```

Sets the window minimum inner size. If the `size` argument is not provided, the constraint is unset.
###### Parameters
Parameter| Type| Description  
---|---|---  
`size`| | `undefined` | `null` | `LogicalSize` | `PhysicalSize` | `Size`| The logical or physical inner size, or `null` to unset the constraint.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, PhysicalSize } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setMinSize(newPhysicalSize(600, 500));

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1291
##### setOverlayIcon()
```

setOverlayIcon(icon?):Promise<void>

```

Sets the overlay icon. **Windows only** The overlay icon can be set for every window.
Note that you may need the `image-ico` or `image-png` Cargo features to use this API. To enable it, change your Cargo.toml file:
```

[dependencies]
tauri = { version = "...", features = ["...", "image-png"] }

```

###### Parameters
Parameter| Type| Description  
---|---|---  
`icon`?| | `string` | `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`> | `Image`| Icon bytes or path to the icon file. Use `undefined` to remove the overlay icon.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setOverlayIcon("/tauri/awesome.png");

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1672
##### setPosition()
```

setPosition(position): Promise<void>

```

Sets the window outer position.
###### Parameters
Parameter| Type| Description  
---|---|---  
`position`| `LogicalPosition` | `PhysicalPosition` | `Position`| The new position, in logical or physical pixels.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, LogicalPosition } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setPosition(newLogicalPosition(600, 500));

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1360
##### setProgressBar()
```

setProgressBar(state): Promise<void>

```

Sets the taskbar progress state.
#### Platform-specific
  * **Linux / macOS** : Progress bar is app-wide and not specific to this window.
  * **Linux** : Only supported desktop environments with `libunity` (e.g. GNOME).


###### Parameters
Parameter| Type  
---|---  
`state`| `ProgressBarState`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, ProgressBarStatus } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setProgressBar({
status: ProgressBarStatus.Normal,
progress: 50,
});

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1700
##### setResizable()
```

setResizable(resizable): Promise<void>

```

Updates the window resizable flag.
###### Parameters
Parameter| Type  
---|---  
`resizable`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setResizable(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L868
##### setShadow()
```

setShadow(enable): Promise<void>

```

Whether or not the window should have shadow.
#### Platform-specific
  * **Windows:**
    * `false` has no effect on decorated window, shadows are always ON.
    * `true` will make undecorated window have a 1px white border, and on Windows 11, it will have a rounded corners.
  * **Linux:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`enable`| `boolean`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setShadow(false);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1182
##### setSize()
```

setSize(size): Promise<void>

```

Resizes the window with a new inner size.
###### Parameters
Parameter| Type| Description  
---|---|---  
`size`| `LogicalSize` | `PhysicalSize` | `Size`| The logical or physical inner size.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow, LogicalSize } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setSize(newLogicalSize(600, 500));

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1273
##### setSizeConstraints()
```

setSizeConstraints(constraints): Promise<void>

```

Sets the window inner size constraints.
###### Parameters
Parameter| Type| Description  
---|---|---  
`constraints`| `undefined` | `null` | `WindowSizeConstraints`| The logical or physical inner size, or `null` to unset the constraint.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setSizeConstraints({ minWidth: 300 });

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1331
##### setSkipTaskbar()
```

setSkipTaskbar(skip): Promise<void>

```

Whether the window icon should be hidden from the taskbar or not.
#### Platform-specific
  * **macOS:** Unsupported.


###### Parameters
Parameter| Type| Description  
---|---|---  
`skip`| `boolean`| true to hide window icon, false to show it.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setSkipTaskbar(true);

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1445
##### setTheme()
```

setTheme(theme?):Promise<void>

```

Set window theme, pass in `null` or `undefined` to follow system theme
#### Platform-specific
  * **Linux / macOS** : Theme is app-wide and not specific to this window.
  * **iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`theme`?| `null` | `Theme`  
###### Returns
`Promise`<`void`>
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1745
##### setTitle()
```

setTitle(title): Promise<void>

```

Sets the window title.
###### Parameters
Parameter| Type| Description  
---|---|---  
`title`| `string`| The new title  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().setTitle('Tauri');

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L992
##### setTitleBarStyle()
```

setTitleBarStyle(style): Promise<void>

```

Sets the title bar style. **macOS only**.
###### Parameters
Parameter| Type  
---|---  
`style`| `TitleBarStyle`  
###### Returns
`Promise`<`void`>
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1728
##### setVisibleOnAllWorkspaces()
```

setVisibleOnAllWorkspaces(visible): Promise<void>

```

Sets whether the window should be visible on all workspaces or virtual desktops.
#### Platform-specific
  * **Windows / iOS / Android:** Unsupported.


###### Parameters
Parameter| Type  
---|---  
`visible`| `boolean`  
###### Returns
`Promise`<`void`>
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1716
##### show()
```

show(): Promise<void>

```

Sets the window visibility to true.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().show();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1089
##### startDragging()
```

startDragging(): Promise<void>

```

Starts dragging the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().startDragging();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1585
##### startResizeDragging()
```

startResizeDragging(direction): Promise<void>

```

Starts resize-dragging the window.
###### Parameters
Parameter| Type  
---|---  
`direction`| `ResizeDirection`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().startResizeDragging();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1601
##### theme()
```

theme(): Promise<null| Theme>

```

Gets the window’s current theme.
#### Platform-specific
  * **macOS:** Theme was introduced on macOS 10.14. Returns `light` on macOS 10.13 and below.


###### Returns
`Promise`<`null` | `Theme`>
The window theme.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const theme = await getCurrentWindow().theme();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L796
##### title()
```

title(): Promise<string>

```

Gets the window’s current title.
###### Returns
`Promise`<`string`>
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
const title = await getCurrentWindow().title();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L775
##### toggleMaximize()
```

toggleMaximize(): Promise<void>

```

Toggles the window maximized state.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().toggleMaximize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1041
##### unmaximize()
```

unmaximize(): Promise<void>

```

Unmaximizes the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().unmaximize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1025
##### unminimize()
```

unminimize(): Promise<void>

```

Unminimizes the window.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWindow } from'@tauri-apps/api/window';
awaitgetCurrentWindow().unminimize();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1073
##### getAll()
```

static getAll(): Promise<Window[]>

```

Gets a list of instances of `Window` for all available windows.
###### Returns
`Promise`<`Window`[]>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L340
##### getByLabel()
```

static getByLabel(label): Promise<null| Window>

```

Gets the Window associated with the given label.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`| `string`| The window label.  
###### Returns
`Promise`<`null` | `Window`>
The Window instance to communicate with the window or null if the window doesn’t exist.
###### Example
```

import { Window } from'@tauri-apps/api/window';
const mainWindow = Window.getByLabel('main');

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L326
##### getCurrent()
```

static getCurrent(): Window

```

Get an instance of `Window` for the current window.
###### Returns
`Window`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L333
##### getFocusedWindow()
```

static getFocusedWindow(): Promise<null| Window>

```

Gets the focused window.
###### Returns
`Promise`<`null` | `Window`>
The Window instance or `undefined` if there is not any focused window.
###### Example
```

import { Window } from'@tauri-apps/api/window';
const focusedWindow = Window.getFocusedWindow();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L354
## Interfaces
### Effects
The window effects configuration object
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`color?`| `Color`| Window effect color. Affects Effect.Blur and Effect.Acrylic only on Windows 10 v1903+. Doesn’t have any effect on Windows 7 or Windows 11.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2205  
`effects`| `Effect`[]| List of Window effects to apply to the Window. Conflicting effects will apply the first one and ignore the rest.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2192  
`radius?`| `number`| Window effect corner radius **macOS Only**| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2200  
`state?`| `EffectState`| Window effect state **macOS Only**| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2196  
### Monitor
Allows you to retrieve information about a given monitor.
#### Since
1.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`name`| `null` | `string`| Human-readable name of the monitor| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L49  
`position`| `PhysicalPosition`| the Top-left corner position of the monitor relative to the larger full screen area.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L53  
`scaleFactor`| `number`| The scale factor that can be used to map physical pixels to logical pixels.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L55  
`size`| `PhysicalSize`| The monitor’s resolution.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L51  
### ProgressBarState
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`progress?`| `number`| The progress bar progress. This can be a value ranging from `0` to `100`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L203  
`status?`| `ProgressBarStatus`| The progress bar status.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L199  
### ScaleFactorChanged
The payload for the `scaleChange` event.
#### Since
1.0.2
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`scaleFactor`| `number`| The new window scale factor.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L78  
`size`| `PhysicalSize`| The new window size| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L80  
### WindowOptions
Configuration for the window to create.
#### Since
1.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`alwaysOnBottom?`| `boolean`| Whether the window should always be below other windows.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2255  
`alwaysOnTop?`| `boolean`| Whether the window should always be on top of other windows or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2253  
`backgroundColor?`| `Color`| Set the window background color. #### Platform-specific: - **Android / iOS:** Unsupported. - **Windows** : alpha channel is ignored. **Since** 2.1.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2351  
`backgroundThrottling?`| `BackgroundThrottlingPolicy`| Change the default background throttling behaviour. ## Platform-specific - **Linux / Windows / Android** : Unsupported. Workarounds like a pending WebLock transaction might suffice. - **iOS** : Supported since version 17.0+. - **macOS** : Supported since version 14.0+. see https://github.com/tauri-apps/tauri/issues/5250#issuecomment-2569380578 **Since** 2.3.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2365  
`center?`| `boolean`| Show window in the center of the screen..| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2215  
`closable?`| `boolean`| Whether the window’s native close button is enabled or not. Defaults to `true`.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2306  
`contentProtected?`| `boolean`| Prevents the window contents from being captured by other apps.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2257  
`decorations?`| `boolean`| Whether the window should have borders and bars or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2251  
`focus?`| `boolean`| Whether the window will be initially focused or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2239  
`fullscreen?`| `boolean`| Whether the window is in fullscreen mode or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2237  
`height?`| `number`| The initial height.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2223  
`hiddenTitle?`| `boolean`| If `true`, sets the window title to be hidden on macOS.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2287  
`maxHeight?`| `number`| The maximum height. Only applies if `maxWidth` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2231  
`maximizable?`| `boolean`| Whether the window’s native maximize button is enabled or not. Defaults to `true`.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2298  
`maximized?`| `boolean`| Whether the window should be maximized upon creation or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2247  
`maxWidth?`| `number`| The maximum width. Only applies if `maxHeight` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2229  
`minHeight?`| `number`| The minimum height. Only applies if `minWidth` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2227  
`minimizable?`| `boolean`| Whether the window’s native minimize button is enabled or not. Defaults to `true`.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2302  
`minWidth?`| `number`| The minimum width. Only applies if `minHeight` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2225  
`parent?`| `string` | `Window` | `WebviewWindow`| Sets a parent to the window to be created. Can be either a `Window` or a label of the window. #### Platform-specific - **Windows** : This sets the passed parent as an owner window to the window to be created. From MSDN owned windows docs: - An owned window is always above its owner in the z-order. - The system automatically destroys an owned window when its owner is destroyed. - An owned window is hidden when its owner is minimized. - **Linux** : This makes the new window transient for parent, see https://docs.gtk.org/gtk3/method.Window.set_transient_for.html - **macOS** : This adds the window as a child of parent, see https://developer.apple.com/documentation/appkit/nswindow/1419152-addchildwindow?language=objc| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2320  
`resizable?`| `boolean`| Whether the window is resizable or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2233  
`shadow?`| `boolean`| Whether or not the window has shadow. #### Platform-specific - **Windows:** - `false` has no effect on decorated window, shadows are always ON. - `true` will make undecorated window have a 1px white border, and on Windows 11, it will have a rounded corners. - **Linux:** Unsupported. **Since** 2.0.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2273  
`skipTaskbar?`| `boolean`| Whether or not the window icon should be added to the taskbar.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2259  
`tabbingIdentifier?`| `string`| Defines the window tabbing identifier on macOS. Windows with the same tabbing identifier will be grouped together. If the tabbing identifier is not set, automatic tabbing will be disabled.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2294  
`theme?`| `Theme`| The initial window theme. Defaults to the system theme. Only implemented on Windows and macOS 10.14+.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2279  
`title?`| `string`| Window title.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2235  
`titleBarStyle?`| `TitleBarStyle`| The style of the macOS title bar.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2283  
`transparent?`| `boolean`| Whether the window is transparent or not. Note that on `macOS` this requires the `macos-private-api` feature flag, enabled under `tauri.conf.json > app > macOSPrivateApi`. WARNING: Using private APIs on `macOS` prevents your application from being accepted to the `App Store`.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2245  
`visible?`| `boolean`| Whether the window should be immediately visible upon creation or not.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2249  
`visibleOnAllWorkspaces?`| `boolean`| Whether the window should be visible on all workspaces or virtual desktops. #### Platform-specific - **Windows / iOS / Android:** Unsupported. **Since** 2.0.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2329  
`width?`| `number`| The initial width.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2221  
`windowEffects?`| `Effects`| Window effects. Requires the window to be transparent. #### Platform-specific: - **Windows** : If using decorations or shadows, you may want to try this workaround https://github.com/tauri-apps/tao/issues/72#issuecomment-975607891 - **Linux** : Unsupported| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2340  
`x?`| `number`| The initial vertical position. Only applies if `y` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2217  
`y?`| `number`| The initial horizontal position. Only applies if `x` is also set.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2219  
### WindowSizeConstraints
#### Properties
Property| Type| Defined in  
---|---|---  
`maxHeight?`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L192  
`maxWidth?`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L191  
`minHeight?`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L190  
`minWidth?`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L189  
## Type Aliases
### CursorIcon
```

type CursorIcon:
| "default"
| "crosshair"
| "hand"
| "arrow"
| "move"
| "text"
| "wait"
| "help"
| "progress"
| "notAllowed"
| "contextMenu"
| "cell"
| "verticalText"
| "alias"
| "copy"
| "noDrop"
| "grab"
| "grabbing"
| "allScroll"
| "zoomIn"
| "zoomOut"
| "eResize"
| "nResize"
| "neResize"
| "nwResize"
| "sResize"
| "seResize"
| "swResize"
| "wResize"
| "ewResize"
| "nsResize"
| "neswResize"
| "nwseResize"
| "colResize"
| "rowResize";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L124
### Theme
```

type Theme: "light" | "dark";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L58
### TitleBarStyle
```

type TitleBarStyle: "visible" | "transparent" | "overlay";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L59
## Functions
### availableMonitors()
```

functionavailableMonitors():Promise<Monitor[]>

```

Returns the list of all the monitors available on the system.
#### Returns
`Promise`<`Monitor`[]>
#### Example
```

import { availableMonitors } from'@tauri-apps/api/window';
const monitors = availableMonitors();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2440
### currentMonitor()
```

functioncurrentMonitor():Promise<Monitor|null>

```

Returns the monitor on which the window currently resides. Returns `null` if current monitor can’t be detected.
#### Returns
`Promise`<`Monitor` | `null`>
#### Example
```

import { currentMonitor } from'@tauri-apps/api/window';
const monitor = currentMonitor();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2390
### cursorPosition()
```

functioncursorPosition():Promise<PhysicalPosition>

```

Get the cursor position relative to the top-left hand corner of the desktop.
Note that the top-left hand corner of the desktop is not necessarily the same as the screen. If the user uses a desktop with multiple monitors, the top-left hand corner of the desktop is the top-left hand corner of the main monitor on Windows and macOS or the top-left of the leftmost monitor on X11.
The coordinates can be negative if the top-left hand corner of the window is outside of the visible screen region.
#### Returns
`Promise`<`PhysicalPosition`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2456
### getAllWindows()
```

functiongetAllWindows():Promise<Window[]>

```

Gets a list of instances of `Window` for all available windows.
#### Returns
`Promise`<`Window`[]>
#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L223
### getCurrentWindow()
```

functiongetCurrentWindow():Window

```

Get an instance of `Window` for the current window.
#### Returns
`Window`
#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L211
### monitorFromPoint()
```

functionmonitorFromPoint(x, y):Promise<Monitor|null>

```

Returns the monitor that contains the given point. Returns `null` if can’t find any.
#### Parameters
Parameter| Type  
---|---  
`x`| `number`  
`y`| `number`  
#### Returns
`Promise`<`Monitor` | `null`>
#### Example
```

import { monitorFromPoint } from'@tauri-apps/api/window';
const monitor = monitorFromPoint();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2423
### primaryMonitor()
```

functionprimaryMonitor():Promise<Monitor|null>

```

Returns the primary monitor of the system. Returns `null` if it can’t identify any monitor as a primary one.
#### Returns
`Promise`<`Monitor` | `null`>
#### Example
```

import { primaryMonitor } from'@tauri-apps/api/window';
const monitor = primaryMonitor();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2407
© 2025 Tauri Contributors. CC-BY / MIT
