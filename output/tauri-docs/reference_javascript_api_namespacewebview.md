Skip to content
# webview
Provides APIs to create webviews, communicate with other webviews and manipulate the current webview.
#### Webview events
Events can be listened to using Webview.listen:
```

import { getCurrentWebview } from"@tauri-apps/api/webview";
getCurrentWebview().listen("my-webview-event", ({ event, payload })=> { });

```

## Classes
### Webview
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
#### Extended by
  * `WebviewWindow`


#### Constructors
##### new Webview()
```

newWebview(
window,
label,
options): Webview

```

Creates a new Webview.
###### Parameters
Parameter| Type| Description  
---|---|---  
`window`| `Window`| the window to add this webview to.  
`label`| `string`| The unique webview label. Must be alphanumeric: `a-zA-Z-/:_`.  
`options`| `WebviewOptions`| -  
###### Returns
`Webview`
The Webview instance to communicate with the webview.
###### Example
```

import { Window } from'@tauri-apps/api/window'
import { Webview } from'@tauri-apps/api/webview'
const appWindow = newWindow('my-label')
const webview = newWebview(appWindow, 'my-label', {
url: 'https://github.com/tauri-apps/tauri'
});
webview.once('tauri://created', function() {
// webview successfully created
});
webview.once('tauri://error', function(e) {
// an error happened creating the webview
});

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L165
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`label`| `string`| The webview label. It is a unique identifier for the webview, can be used to reference it later.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L136  
`listeners`| `Record`<`string`, `EventCallback`<`any`>[]>| Local event listeners.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L141  
`window`| `Window`| The window hosting this webview.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L138  
#### Methods
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L541
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L405
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L475
##### listen()
```

listen<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this webview.
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

import { getCurrentWebview } from'@tauri-apps/api/webview';
const unlisten = await getCurrentWebview().listen<string>('state-changed', (event) => {
console.log(`Got error: ${payload}`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L231
##### once()
```

once<T>(event, handler): Promise<UnlistenFn>

```

Listen to an emitted event on this webview only once.
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

import { getCurrentWebview } from'@tauri-apps/api/webview';
const unlisten = await getCurrent().once<null>('initialized', (event) => {
console.log(`Webview initialized!`);
});
// you need to call unlisten if your handler goes out of scope e.g. the component is unmounted
unlisten();

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L266
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
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L593
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L524
##### setBackgroundColor()
```

setBackgroundColor(color): Promise<void>

```

Specify the webview background color.
#### Platfrom-specific:
  * **macOS / iOS** : Not implemented.
  * **Windows** : 
    * On Windows 7, transparency is not supported and the alpha value will be ignored.
    * On Windows higher than 7: translucent colors are not supported so any alpha value other than `0` will be replaced by `255`


###### Parameters
Parameter| Type  
---|---  
`color`| `null` | `Color`  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Since
2.1.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L559
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L459
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L440
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L422
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

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L384
##### getAll()
```

static getAll(): Promise<Webview[]>

```

Gets a list of instances of `Webview` for all available webviews.
###### Returns
`Promise`<`Webview`[]>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L208
##### getByLabel()
```

static getByLabel(label): Promise<null| Webview>

```

Gets the Webview for the webview associated with the given label.
###### Parameters
Parameter| Type| Description  
---|---|---  
`label`| `string`| The webview label.  
###### Returns
`Promise`<`null` | `Webview`>
The Webview instance to communicate with the webview or null if the webview doesn’t exist.
###### Example
```

import { Webview } from'@tauri-apps/api/webview';
const mainWebview = Webview.getByLabel('main');

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L194
##### getCurrent()
```

static getCurrent(): Webview

```

Get an instance of `Webview` for the current webview.
###### Returns
`Webview`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L201
## Interfaces
### WebviewOptions
Configuration for the webview to create.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`acceptFirstMouse?`| `boolean`| Whether clicking an inactive webview also clicks through to the webview on macOS.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L698  
`backgroundColor?`| `Color`| Set the window and webview background color. #### Platform-specific: - **macOS / iOS** : Not implemented. - **Windows** : - On Windows 7, alpha channel is ignored. - On Windows 8 and newer, if alpha channel is not `0`, it will be ignored. **Since** 2.1.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L774  
`backgroundThrottling?`| `BackgroundThrottlingPolicy`| Change the default background throttling behaviour. By default, browsers use a suspend policy that will throttle timers and even unload the whole tab (view) to free resources after roughly 5 minutes when a view became minimized or hidden. This will pause all tasks until the documents visibility state changes back from hidden to visible by bringing the view back to the foreground. ## Platform-specific - **Linux / Windows / Android** : Unsupported. Workarounds like a pending WebLock transaction might suffice. - **iOS** : Supported since version 17.0+. - **macOS** : Supported since version 14.0+. see https://github.com/tauri-apps/tauri/issues/5250#issuecomment-2569380578 **Since** 2.3.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L793  
`devtools?`| `boolean`| Whether web inspector, which is usually called browser devtools, is enabled or not. Enabled by default. This API works in **debug** builds, but requires `devtools` feature flag to enable it in **release** builds. #### Platform-specific - macOS: This will call private functions on **macOS**. - Android: Open `chrome://inspect/#devices` in Chrome to get the devtools window. Wry’s `WebView` devtools API isn’t supported on Android. - iOS: Open Safari > Develop > [Your Device Name] > [Your WebView] to get the devtools window. **Since** 2.1.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L761  
`dragDropEnabled?`| `boolean`| Whether the drag and drop is enabled or not on the webview. By default it is enabled. Disabling it is required to use HTML5 drag and drop on the frontend on Windows.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L694  
`focus?`| `boolean`| Whether the webview should have focus or not **Since** 2.1.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L688  
`height`| `number`| The initial height.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L676  
`incognito?`| `boolean`| Whether or not the webview should be launched in incognito mode. #### Platform-specific - **Android:** Unsupported.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L710  
`proxyUrl?`| `string`| The proxy URL for the WebView for all network requests. Must be either a `http://` or a `socks5://` URL. #### Platform-specific - **macOS** : Requires the `macos-proxy` feature flag and only compiles for macOS 14+.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L720  
`transparent?`| `boolean`| Whether the webview is transparent or not. Note that on `macOS` this requires the `macos-private-api` feature flag, enabled under `tauri.conf.json > app > macOSPrivateApi`. WARNING: Using private APIs on `macOS` prevents your application from being accepted to the `App Store`.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L682  
`url?`| `string`| Remote URL or local file path to open. - URL such as `https://github.com/tauri-apps` is opened directly on a Tauri webview. - data: URL such as `data:text/html,<html>...` is only supported with the `webview-data-url` Cargo feature for the `tauri` dependency. - local file path or route such as `/path/to/page.html` or `/users` is appended to the application URL (the devServer URL on development, or `tauri://localhost/` and `https://tauri.localhost/` on production).| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L668  
`useHttpsScheme?`| `boolean`| Sets whether the custom protocols should use `https://<scheme>.localhost` instead of the default `http://<scheme>.localhost` on Windows and Android. Defaults to `false`. #### Note Using a `https` scheme will NOT allow mixed content when trying to fetch `http` endpoints and therefore will not match the behavior of the `<scheme>://localhost` protocols used on macOS and Linux. #### Warning Changing this value between releases will change the IndexedDB, cookies and localstorage location and your app will not be able to access them. **Since** 2.1.0| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L747  
`userAgent?`| `string`| The user agent for the webview.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L702  
`width`| `number`| The initial width.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L674  
`x`| `number`| The initial vertical position.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L670  
`y`| `number`| The initial horizontal position.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L672  
`zoomHotkeysEnabled?`| `boolean`| Whether page zooming by hotkeys is enabled #### Platform-specific: - **Windows** : Controls WebView2’s `IsZoomControlEnabled` setting. - **MacOS / Linux** : Injects a polyfill that zooms in and out with `ctrl/command` + `-/=`, 20% in each step, ranging from 20% to 1000%. Requires `webview:allow-set-webview-zoom` permission - **Android / iOS** : Unsupported.| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L732  
## Type Aliases
### Color
```

type Color: [number, number, number] | [number, number, number, number] | object | string;

```

An RGBA color. Each value has minimum of 0 and maximum of 255.
It can be either a string `#ffffff`, an array of 3 or 4 elements or an object.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/window.ts#L2018
### DragDropEvent
```

type DragDropEvent: object | object | object | object;

```

The drag and drop event types.
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L42
## Functions
### getAllWebviews()
```

functiongetAllWebviews():Promise<Webview[]>

```

Gets a list of instances of `Webview` for all available webviews.
#### Returns
`Promise`<`Webview`[]>
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L69
### getCurrentWebview()
```

functiongetCurrentWebview():Webview

```

Get an instance of `Webview` for the current webview.
#### Returns
`Webview`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/webview.ts#L53
© 2025 Tauri Contributors. CC-BY / MIT
