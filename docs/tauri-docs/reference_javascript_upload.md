Skip to content
# @tauri-apps/plugin-upload
## Functions
### download()
```

functiondownload(
url,
filePath,
progressHandler?,
headers?,
body?):Promise<void>

```

#### Parameters
Parameter| Type  
---|---  
`url`| `string`  
`filePath`| `string`  
`progressHandler`?| `ProgressHandler`  
`headers`?| `Map`<`string`, `string`>  
`body`?| `string`  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/upload/guest-js/index.ts#L44
### upload()
```

functionupload(
url,
filePath,
progressHandler?,
headers?):Promise<string>

```

#### Parameters
Parameter| Type  
---|---  
`url`| `string`  
`filePath`| `string`  
`progressHandler`?| `ProgressHandler`  
`headers`?| `Map`<`string`, `string`>  
#### Returns
`Promise`<`string`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/upload/guest-js/index.ts#L16
© 2025 Tauri Contributors. CC-BY / MIT
