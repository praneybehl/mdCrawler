Skip to content
# core
Invoke your custom commands.
This package is also accessible with `window.__TAURI__.core` when `app.withGlobalTauri` in `tauri.conf.json` is set to `true`.
## Classes
### Channel<T>
#### Type Parameters
Type Parameter| Default type  
---|---  
`T`| `unknown`  
#### Constructors
##### new Channel()
```

newChannel<T>(): Channel<T>

```

###### Returns
`Channel`<`T`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L88
#### Properties
Property| Type| Defined in  
---|---|---  
`id`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L78  
#### Accessors
##### onmessage
###### Get Signature
```

get onmessage():(response)=>void

```

###### Returns
`Function`
###### Parameters
Parameter| Type  
---|---  
`response`| `T`  
###### Returns
`void`
###### Set Signature
```

set onmessage(handler): void

```

###### Parameters
Parameter| Type  
---|---  
`handler`| (`response`) => `void`  
###### Returns
`void`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L118
#### Methods
##### __TAURI_TO_IPC_KEY__()
```

__TAURI_TO_IPC_KEY__(): string

```

###### Returns
`string`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L122
##### toJSON()
```

toJSON(): string

```

###### Returns
`string`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L126
### PluginListener
#### Constructors
##### new PluginListener()
```

newPluginListener(
plugin,
event,
channelId): PluginListener

```

###### Parameters
Parameter| Type  
---|---  
`plugin`| `string`  
`event`| `string`  
`channelId`| `number`  
###### Returns
`PluginListener`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L137
#### Properties
Property| Type| Defined in  
---|---|---  
`channelId`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L135  
`event`| `string`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L134  
`plugin`| `string`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L133  
#### Methods
##### unregister()
```

unregister(): Promise<void>

```

###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L143
### Resource
A rust-backed resource stored through `tauri::Manager::resources_table` API.
The resource lives in the main process and does not exist in the Javascript world, and thus will not be cleaned up automatiacally except on application exit. If you want to clean it up early, call `Resource.close`
#### Example
```

import { Resource, invoke } from'@tauri-apps/api/core';
exportclassDatabaseHandleextendsResource {
staticasyncopen(path:string):Promise<DatabaseHandle> {
constrid:number = await invoke('open_db', { path });
returnnewDatabaseHandle(rid);
}
asyncexecute(sql:string):Promise<void> {
awaitinvoke('execute_sql', { rid: this.rid, sql });
}
}

```

#### Extended by
  * `Image`
  * `TrayIcon`


#### Constructors
##### new Resource()
```

newResource(rid): Resource

```

###### Parameters
Parameter| Type  
---|---  
`rid`| `number`  
###### Returns
`Resource`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L290
#### Accessors
##### rid
###### Get Signature
```

get rid(): number

```

###### Returns
`number`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L286
#### Methods
##### close()
```

close(): Promise<void>

```

Destroys and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L298
## Interfaces
### InvokeOptions
#### Since
2.0.0
#### Properties
Property| Type| Defined in  
---|---|---  
`headers`| `Record`<`string`, `string`> | `Headers`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L201  
## Type Aliases
### InvokeArgs
```

type InvokeArgs: Record<string, unknown> | number[] | ArrayBuffer | Uint8Array;

```

Command arguments.
#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L195
### PermissionState
```

type PermissionState: "granted" | "denied" | "prompt" | "prompt-with-rationale";

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L170
## Variables
### SERIALIZE_TO_IPC_FN
```

const SERIALIZE_TO_IPC_FN:"__TAURI_TO_IPC_KEY__" = '__TAURI_TO_IPC_KEY__';

```

A key to be used to implement a special function on your types that define how your type should be serialized when passing across the IPC.
#### Example
Given a type in Rust that looks like this
```

#[derive(serde::Serialize, serde::Deserialize)
enum UserId {
String(String),
Number(u32),
}

```

`UserId::String("id")` would be serialized into `{ String: "id" }` and so we need to pass the same structure back to Rust
```

import { SERIALIZE_TO_IPC_FN } from"@tauri-apps/api/core"
classUserIdString {
id
constructor(id) {
this.id= id
}
[SERIALIZE_TO_IPC_FN]() {
return { String: this.id }
}
}
classUserIdNumber {
id
constructor(id) {
this.id= id
}
[SERIALIZE_TO_IPC_FN]() {
return { Number: this.id }
}
}
type UserId =UserIdString|UserIdNumber

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L60
## Functions
### addPluginListener()
```

functionaddPluginListener<T>(
plugin,
event,
cb):Promise<PluginListener>

```

Adds a listener to a plugin event.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type  
---|---  
`plugin`| `string`  
`event`| `string`  
`cb`| (`payload`) => `void`  
#### Returns
`Promise`<`PluginListener`>
The listener object to stop listening to the events.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L158
### checkPermissions()
```

functioncheckPermissions<T>(plugin):Promise<T>

```

Get permission state for a plugin.
This should be used by plugin authors to wrap their actual implementation.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type  
---|---  
`plugin`| `string`  
#### Returns
`Promise`<`T`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L177
### convertFileSrc()
```

functionconvertFileSrc(filePath, protocol):string

```

Convert a device file path to an URL that can be loaded by the webview. Note that `asset:` and `http://asset.localhost` must be added to `app.security.csp` in `tauri.conf.json`. Example CSP value: `"csp": "default-src 'self' ipc: http://ipc.localhost; img-src 'self' asset: http://asset.localhost"` to use the asset protocol on image sources.
Additionally, `"enable" : "true"` must be added to `app.security.assetProtocol` in `tauri.conf.json` and its access scope must be defined on the `scope` array on the same `assetProtocol` object.
#### Parameters
Parameter| Type| Default value| Description  
---|---|---|---  
`filePath`| `string`| `undefined`| The file path.  
`protocol`| `string`| `'asset'`| The protocol to use. Defaults to `asset`. You only need to set this when using a custom protocol.  
#### Returns
`string`
the URL that can be used as source on the webview.
#### Example
```

import { appDataDir, join } from'@tauri-apps/api/path';
import { convertFileSrc } from'@tauri-apps/api/core';
const appDataDirPath = await appDataDir();
const filePath = await join(appDataDirPath, 'assets/video.mp4');
const assetUrl = convertFileSrc(filePath);
const video = document.getElementById('my-video');
const source = document.createElement('source');
source.type='video/mp4';
source.src= assetUrl;
video.appendChild(source);
video.load();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L257
### invoke()
```

functioninvoke<T>(
cmd,
args,
options?):Promise<T>

```

Sends a message to the backend.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type| Description  
---|---|---  
`cmd`| `string`| The command name.  
`args`| `InvokeArgs`| The optional arguments to pass to the command.  
`options`?| `InvokeOptions`| The request options.  
#### Returns
`Promise`<`T`>
A promise resolving or rejecting to the backend response.
#### Example
```

import { invoke } from'@tauri-apps/api/core';
awaitinvoke('login', { user: 'tauri', password: 'poiwe3h4r5ip3yrhtew9ty' });

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L219
### isTauri()
```

functionisTauri():boolean

```

#### Returns
`boolean`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L305
### requestPermissions()
```

functionrequestPermissions<T>(plugin):Promise<T>

```

Request permissions.
This should be used by plugin authors to wrap their actual implementation.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type  
---|---  
`plugin`| `string`  
#### Returns
`Promise`<`T`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L186
### transformCallback()
```

functiontransformCallback<T>(callback?, once?):number

```

Transforms a callback function to a string identifier that can be passed to the backend. The backend uses the identifier to `eval()` the callback.
#### Type Parameters
Type Parameter| Default type  
---|---  
`T`| `unknown`  
#### Parameters
Parameter| Type| Default value  
---|---|---  
`callback`?| (`response`) => `void`| `undefined`  
`once`?| `boolean`| `false`  
#### Returns
`number`
A unique identifier associated with the callback function.
#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L70
© 2025 Tauri Contributors. CC-BY / MIT
