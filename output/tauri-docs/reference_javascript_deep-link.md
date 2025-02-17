Skip to content
# @tauri-apps/plugin-deep-link
## Functions
### getCurrent()
```

functiongetCurrent():Promise<string[] |null>

```

Get the current URLs that triggered the deep link. Use this on app load to check whether your app was started via a deep link.
#### Returns
`Promise`<`string`[] | `null`>
#### Example
```

import { getCurrent } from'@tauri-apps/plugin-deep-link';
const urls = await getCurrent();

```

#### - **Windows / Linux** : This function reads the command line arguments and checks if there’s only one value, which must be an URL with scheme matching one of the configured values.
Note that you must manually check the arguments when registering deep link schemes dynamically with [`Self::register`]. Additionally, the deep link might have been provided as a CLI argument so you should check if its format matches what you expect..
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/deep-link/guest-js/index.ts#L23
### isRegistered()
```

functionisRegistered(protocol):Promise<boolean>

```

Check whether the app is the default handler for the specified protocol.
#### Parameters
Parameter| Type| Description  
---|---|---  
`protocol`| `string`| The name of the protocol without `://`.  
#### Returns
`Promise`<`boolean`>
#### Example
```

import { isRegistered } from'@tauri-apps/plugin-deep-link';
awaitisRegistered("my-scheme");

```

#### - **macOS / Android / iOS** : Unsupported.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/deep-link/guest-js/index.ts#L80
### onOpenUrl()
```

functiononOpenUrl(handler):Promise<UnlistenFn>

```

Helper function for the `deep-link://new-url` event to run a function each time the protocol is triggered while the app is running. Use `getCurrent` on app load to check whether your app was started via a deep link.
#### Parameters
Parameter| Type  
---|---  
`handler`| (`urls`) => `void`  
#### Returns
`Promise`<`UnlistenFn`>
#### Example
```

import { onOpenUrl } from'@tauri-apps/plugin-deep-link';
awaitonOpenUrl((urls)=> { console.log(urls) });

```

#### - **Windows / Linux** : Unsupported without the single-instance plugin. The OS will spawn a new app instance passing the URL as a CLI argument.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/deep-link/guest-js/index.ts#L99
### register()
```

functionregister(protocol):Promise<null>

```

Register the app as the default handler for the specified protocol.
#### Parameters
Parameter| Type| Description  
---|---|---  
`protocol`| `string`| The name of the protocol without `://`. For example, if you want your app to handle `tauri://` links, call this method with `tauri` as the protocol.  
#### Returns
`Promise`<`null`>
#### Example
```

import { register } from'@tauri-apps/plugin-deep-link';
awaitregister("my-scheme");

```

#### - **macOS / Android / iOS** : Unsupported.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/deep-link/guest-js/index.ts#L42
### unregister()
```

functionunregister(protocol):Promise<null>

```

Unregister the app as the default handler for the specified protocol.
#### Parameters
Parameter| Type| Description  
---|---|---  
`protocol`| `string`| The name of the protocol without `://`.  
#### Returns
`Promise`<`null`>
#### Example
```

import { unregister } from'@tauri-apps/plugin-deep-link';
awaitunregister("my-scheme");

```

#### - **macOS / Linux / Android / iOS** : Unsupported.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/deep-link/guest-js/index.ts#L61
© 2025 Tauri Contributors. CC-BY / MIT
