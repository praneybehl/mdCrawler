Skip to content
# @tauri-apps/plugin-updater
## Classes
### Update
#### Extends
  * `Resource`


#### Constructors
##### new Update()
```

newUpdate(metadata): Update

```

###### Parameters
Parameter| Type  
---|---  
`metadata`| `UpdateMetadata`  
###### Returns
`Update`
###### Overrides
`Resource.constructor`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L64
#### Properties
Property| Type| Defined in  
---|---|---  
`available`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L56  
`body?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L60  
`currentVersion`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L57  
`date?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L59  
`rawJson`| `Record`<`string`, `unknown`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L61  
`version`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L58  
#### Accessors
##### rid
###### Get Signature
```

get rid(): number

```

###### Returns
`number`
###### Inherited from
`Resource.rid`
**Source** : undefined
#### Methods
##### close()
```

close(): Promise<void>

```

Destroys and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
###### Overrides
`Resource.close`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L122
##### download()
```

download(onEvent?, options?):Promise<void>

```

Download the updater package
###### Parameters
Parameter| Type  
---|---  
`onEvent`?| (`progress`) => `void`  
`options`?| `DownloadOptions`  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L75
##### downloadAndInstall()
```

downloadAndInstall(onEvent?, options?):Promise<void>

```

Downloads the updater package and installs it
###### Parameters
Parameter| Type  
---|---  
`onEvent`?| (`progress`) => `void`  
`options`?| `DownloadOptions`  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L107
##### install()
```

install(): Promise<void>

```

Install downloaded updater package
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L92
## Interfaces
### CheckOptions
Options used when checking for updates
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`headers?`| `HeadersInit`| Request headers| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L12  
`proxy?`| `string`| A proxy url to be used when checking and downloading updates.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L20  
`target?`| `string`| Target identifier for the running application. This is sent to the backend.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L24  
`timeout?`| `number`| Timeout in milliseconds| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L16  
### DownloadOptions
Options used when downloading an update
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`headers?`| `HeadersInit`| Request headers| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L32  
`timeout?`| `number`| Timeout in milliseconds| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L36  
## Type Aliases
### DownloadEvent
```

type DownloadEvent: object | object | object;

```

Updater download event
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L50
## Functions
### check()
```

functioncheck(options?):Promise<Update|null>

```

Check for updates, resolves to `null` if no updates are available
#### Parameters
Parameter| Type  
---|---  
`options`?| `CheckOptions`  
#### Returns
`Promise`<`Update` | `null`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/updater/guest-js/index.ts#L129
© 2025 Tauri Contributors. CC-BY / MIT
