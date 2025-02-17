Skip to content
# webviewWindow
## References
### Color
Re-exports Color
### DragDropEvent
Re-exports DragDropEvent
## Classes
### WebviewWindow
Create new webview or get a handle to an existing one.
Webviews are identified by a _label_ a unique identifier that can be used to reference it later. It may only contain alphanumeric characters `a-zA-Z` plus the following special characters `-`, `/`, `:` and `_`.
#### Example
```

import { Window } from"@tauri-apps/api/window"
import { Webview } from"@tauri-apps/api/webview"
const appWindow = newWindow('uniqueLabel');
// loading embedded asset:
const webview = newWebview(appWindow, 'theUniqueLabel', {
url: 'path/to/page.html'
});
// alternatively, load a remote URL:
const webview = newWebview(appWindow, 'theUniqueLabel', {
url: 'https://github.com/tauri-apps/tauri'
});
webview.once('tauri://created', function() {
// webview successfully created
});
webview.once('tauri://error', function(e) {
// an error happened creating the webview
});
// emit an event to the backend
await webview.emit("some-event", "data");
// listen to an event from the backend
const unlisten = await webview.listen("event-name", e => {});
unlisten();

```

#### Since
2.0.0
#### Extends
  * `Webview`.`Window`


#### Constructors
##### new WebviewWindow()
```

newWebviewWindow(label, options): WebviewWindow

```

Creates a new Window hosting a Webview.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`| `string`| The unique webview label. Must be alphanumeric: `a-zA-Z-/:_`.  
`options`| `Omit`<`WebviewOptions`, `"width"` | `"height"` | `"x"` | `"y"`> & `WindowOptions`| -  
###### Returns
`WebviewWindow`
The WebviewWindow instance to communicate with the window and webview.
###### Example
```

import { WebviewWindow } from'@tauri-apps/api/webviewWindow'
const webview = newWebviewWindow('my-label', {
url: 'https://github.com/tauri-apps/tauri'
});
webview.once('tauri://created', function() {
// webview successfully created
});
webview.once('tauri://error', function(e) {
// an error happened creating the webview
});

```

###### Inherited from
`Window`.`constructor`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L75
#### Properties
Property| Type| Description| Inherited from| Defined in  
---|---|---|---|---  
`label`| `string`| The webview label. It is a unique identifier for the webview, can be used to reference it later.| `Window`.`label`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L51  
`listeners`| `Record`<`string`, `EventCallback`<`any`>[]>| Local event listeners.| `Window`.`listeners`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L54  
`window`| `Window`| The window hosting this webview.| `Webview`.`window`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L138  
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

###### Inherited from
`Window`.`center`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L814
##### clearAllBrowsingData()
```

clearAllBrowsingData(): Promise<void>

```

Clears all browsing data for this webview.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().clearAllBrowsingData();

```

###### Inherited from
`Webview`.`clearAllBrowsingData`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L541
##### clearEffects()
```

clearEffects(): Promise<void>

```

Clear any applied effects if possible.
###### Returns
`Promise`<`void`>
###### Inherited from
`Window`.`clearEffects`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1202
##### close()
```

close(): Promise<void>

```

Closes the webview.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().close();

```

###### Inherited from
`Window`.`close`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L405
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

###### Inherited from
`Window`.`destroy`
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

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().emit('webview-loaded', { loggedIn: true, token: 'authToken' });

```

###### Inherited from
`Window`.`emit`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L294
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

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().emitTo('main', 'webview-loaded', { loggedIn: true, token: 'authToken' });

```

###### Inherited from
`Window`.`emitTo`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L322
##### hide()
```

hide(): Promise<void>

```

Hide the webview.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().hide();

```

###### Inherited from
`Window`.`hide`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L475
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

###### Inherited from
`Window`.`innerPosition`
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

###### Inherited from
`Window`.`innerSize`
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

###### Inherited from
`Window`.`isClosable`
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

###### Inherited from
`Window`.`isDecorated`
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
###### Inherited from
`Window`.`isEnabled`
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

###### Inherited from
`Window`.`isFocused`
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

###### Inherited from
`Window`.`isFullscreen`
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

###### Inherited from
`Window`.`isMaximizable`
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

###### Inherited from
`Window`.`isMaximized`
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

###### Inherited from
`Window`.`isMinimizable`
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

###### Inherited from
`Window`.`isMinimized`
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

###### Inherited from
`Window`.`isResizable`
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

###### Inherited from
`Window`.`isVisible`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L761
##### listen()
```

listen<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this webivew window.
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

import { WebviewWindow } from'@tauri-apps/api/webviewWindow';
const unlisten = await WebviewWindow.getCurrent().listen<string>('state-changed', (event) => {
console.log(`Got error: ${payload}`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

###### Inherited from
`Window`.`listen`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L155
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

###### Inherited from
`Window`.`maximize`
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

###### Inherited from
`Window`.`minimize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1057
##### once()
```

once<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this webview window only once.
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

import { WebviewWindow } from'@tauri-apps/api/webviewWindow';
const unlisten = await WebviewWindow.getCurrent().once<null>('initialized', (event) => {
console.log(`Webview initialized!`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

###### Inherited from
`Window`.`once`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L190
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

###### Inherited from
`Window`.`onCloseRequested`
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

import { getCurrentWebview } from"@tauri-apps/api/webview";
const unlisten = await getCurrentWebview().onDragDropEvent((event) => {
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

When the debugger panel is open, the drop position of this event may be inaccurate due to a known limitation. To retrieve the correct drop position, please detach the debugger.
###### Inherited from
`Window`.`onDragDropEvent`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L593
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

###### Inherited from
`Window`.`onFocusChanged`
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

###### Inherited from
`Window`.`onMoved`
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

###### Inherited from
`Window`.`onResized`
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

###### Inherited from
`Window`.`onScaleChanged`
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

###### Inherited from
`Window`.`onThemeChanged`
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

###### Inherited from
`Window`.`outerPosition`
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

###### Inherited from
`Window`.`outerSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L585
##### position()
```

position(): Promise<PhysicalPosition>

```

The position of the top-left hand corner of the webview’s client area relative to the top-left hand corner of the desktop.
###### Returns
`Promise`<`PhysicalPosition`>
The webview’s position.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
const position = await getCurrentWebview().position();

```

###### Inherited from
`Webview`.`position`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L367
##### reparent()
```

reparent(window): Promise<void>

```

Moves this webview to the given label.
###### Parameters
Parameter| Type  
---|---  
`window`| `string` | `Window` | `WebviewWindow`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().reparent('other-window');

```

###### Inherited from
`Webview`.`reparent`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L524
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

###### Inherited from
`Window`.`requestUserAttention`
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

###### Inherited from
`Window`.`scaleFactor`
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

###### Inherited from
`Window`.`setAlwaysOnBottom`
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

###### Inherited from
`Window`.`setAlwaysOnTop`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1220
##### setBackgroundColor()
```

setBackgroundColor(color): Promise<void>

```

Set the window and webview background color.
#### Platform-specific:
  * **Android / iOS:** Unsupported for the window layer.
  * **macOS / iOS** : Not implemented for the webview layer.
  * **Windows** : 
    * alpha channel is ignored for the window layer.
    * On Windows 7, alpha channel is ignored for the webview layer.
    * On Windows 8 and newer, if alpha channel is not `0`, it will be ignored.


###### Parameters
Parameter| Type  
---|---  
`color`| `Color`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Since
2.1.0
###### Inherited from
`Window`.`setBackgroundColor`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L222
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

###### Inherited from
`Window`.`setBadgeCount`
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

###### Inherited from
`Window`.`setBadgeLabel`
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

###### Inherited from
`Window`.`setClosable`
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

###### Inherited from
`Window`.`setContentProtected`
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

###### Inherited from
`Window`.`setCursorGrab`
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

###### Inherited from
`Window`.`setCursorIcon`
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

###### Inherited from
`Window`.`setCursorPosition`
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

###### Inherited from
`Window`.`setCursorVisible`
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

###### Inherited from
`Window`.`setDecorations`
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
###### Inherited from
`Window`.`setEffects`
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
###### Inherited from
`Window`.`setEnabled`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L887
##### setFocus()
```

setFocus(): Promise<void>

```

Bring the webview to front and focus.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().setFocus();

```

###### Inherited from
`Window`.`setFocus`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L459
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

###### Inherited from
`Window`.`setFullscreen`
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

###### Inherited from
`Window`.`setIcon`
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

###### Inherited from
`Window`.`setIgnoreCursorEvents`
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

###### Inherited from
`Window`.`setMaximizable`
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

###### Inherited from
`Window`.`setMaxSize`
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

###### Inherited from
`Window`.`setMinimizable`
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

###### Inherited from
`Window`.`setMinSize`
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

###### Inherited from
`Window`.`setOverlayIcon`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1672
##### setPosition()
```

setPosition(position): Promise<void>

```

Sets the webview position.
###### Parameters
Parameter| Type| Description  
---|---|---  
`position`| `LogicalPosition` | `PhysicalPosition` | `Position`| The new position, in logical or physical pixels.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrent, LogicalPosition } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().setPosition(newLogicalPosition(600, 500));

```

###### Inherited from
`Window`.`setPosition`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L440
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

###### Inherited from
`Window`.`setProgressBar`
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

###### Inherited from
`Window`.`setResizable`
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

###### Inherited from
`Window`.`setShadow`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1182
##### setSize()
```

setSize(size): Promise<void>

```

Resizes the webview.
###### Parameters
Parameter| Type| Description  
---|---|---  
`size`| `LogicalSize` | `PhysicalSize` | `Size`| The logical or physical size.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrent, LogicalSize } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().setSize(newLogicalSize(600, 500));

```

###### Inherited from
`Window`.`setSize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L422
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

###### Inherited from
`Window`.`setSizeConstraints`
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

###### Inherited from
`Window`.`setSkipTaskbar`
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
###### Inherited from
`Window`.`setTheme`
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

###### Inherited from
`Window`.`setTitle`
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
###### Inherited from
`Window`.`setTitleBarStyle`
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
###### Inherited from
`Window`.`setVisibleOnAllWorkspaces`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1716
##### setZoom()
```

setZoom(scaleFactor): Promise<void>

```

Set webview zoom level.
###### Parameters
Parameter| Type  
---|---  
`scaleFactor`| `number`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().setZoom(1.5);

```

###### Inherited from
`Webview`.`setZoom`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L507
##### show()
```

show(): Promise<void>

```

Show the webview.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
awaitgetCurrentWebview().show();

```

###### Inherited from
`Window`.`show`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L491
##### size()
```

size(): Promise<PhysicalSize>

```

The physical size of the webview’s client area. The client area is the content of the webview, excluding the title bar and borders.
###### Returns
`Promise`<`PhysicalSize`>
The webview’s size.
###### Example
```

import { getCurrentWebview } from'@tauri-apps/api/webview';
const size = await getCurrentWebview().size();

```

###### Inherited from
`Webview`.`size`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L384
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

###### Inherited from
`Window`.`startDragging`
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

###### Inherited from
`Window`.`startResizeDragging`
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

###### Inherited from
`Window`.`theme`
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

###### Inherited from
`Window`.`title`
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

###### Inherited from
`Window`.`toggleMaximize`
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

###### Inherited from
`Window`.`unmaximize`
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

###### Inherited from
`Window`.`unminimize`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L1073
##### getAll()
```

static getAll(): Promise<WebviewWindow[]>

```

Gets a list of instances of `Webview` for all available webviews.
###### Returns
`Promise`<`WebviewWindow`[]>
###### Inherited from
`Window`.`getAll`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L132
##### getByLabel()
```

static getByLabel(label): Promise<null| WebviewWindow>

```

Gets the Webview for the webview associated with the given label.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`| `string`| The webview label.  
###### Returns
`Promise`<`null` | `WebviewWindow`>
The Webview instance to communicate with the webview or null if the webview doesn’t exist.
###### Example
```

import { Webview } from'@tauri-apps/api/webviewWindow';
const mainWebview = Webview.getByLabel('main');

```

###### Inherited from
`Window`.`getByLabel`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L112
##### getCurrent()
```

static getCurrent(): WebviewWindow

```

Get an instance of `Webview` for the current webview.
###### Returns
`WebviewWindow`
###### Inherited from
`Window`.`getCurrent`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L125
## Functions
### getAllWebviewWindows()
```

functiongetAllWebviewWindows():Promise<WebviewWindow[]>

```

Gets a list of instances of `Webview` for all available webview windows.
#### Returns
`Promise`<`WebviewWindow`[]>
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L34
### getCurrentWebviewWindow()
```

functiongetCurrentWebviewWindow():WebviewWindow

```

Get an instance of `Webview` for the current webview window.
#### Returns
`WebviewWindow`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webviewWindow.ts#L23
© 2025 Tauri Contributors. CC-BY / MIT
