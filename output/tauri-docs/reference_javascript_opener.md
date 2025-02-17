Skip to content
# @tauri-apps/plugin-opener
Open files and URLs using their default application.
## Security
This API has a scope configuration that forces you to restrict the files and urls to be opened.
### Restricting access to the open | `open` API
On the configuration object, `open: true` means that the open API can be used with any URL, as the argument is validated with the `^((mailto:\w+)|(tel:\w+)|(https?://\w+)).+` regex. You can change that regex by changing the boolean value to a string, e.g. `open: ^https://github.com/`.
## Functions
### openPath()
```

functionopenPath(path, openWith?):Promise<void>

```

Opens a path with the system’s default app, or the one specified with openWith.
#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| The path to open.  
`openWith`?| `string`| The app to open the path with. If not specified, defaults to the system default application for the specified path type.  
#### Returns
`Promise`<`void`>
#### Example
```

import { openPath } from'@tauri-apps/plugin-opener';
// opens a file using the default program:
awaitopenPath('/path/to/file');
// opens a file using `vlc` command on Windows.
awaitopenPath('C:/path/to/file', 'vlc');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/opener/guest-js/index.ts#L66
### openUrl()
```

functionopenUrl(url, openWith?):Promise<void>

```

Opens a url with the system’s default app, or the one specified with openWith.
#### Parameters
Parameter| Type| Description  
---|---|---  
`url`| `string`| The URL to open.  
`openWith`?| `string`| The app to open the URL with. If not specified, defaults to the system default application for the specified url type.  
#### Returns
`Promise`<`void`>
#### Example
```

import { openUrl } from'@tauri-apps/plugin-opener';
// opens the given URL on the default browser:
awaitopenUrl('https://github.com/tauri-apps/tauri');
// opens the given URL using `firefox`:
awaitopenUrl('https://github.com/tauri-apps/tauri', 'firefox');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/opener/guest-js/index.ts#L41
### revealItemInDir()
```

functionrevealItemInDir(path):Promise<unknown>

```

Reveal a path with the system’s default explorer.
#### Platform-specific:
  * **Android / iOS:** Unsupported.


#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| The path to reveal.  
#### Returns
`Promise`<`unknown`>
#### Example
```

import { revealItemInDir } from'@tauri-apps/plugin-opener';
awaitrevealItemInDir('/path/to/file');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/opener/guest-js/index.ts#L90
© 2025 Tauri Contributors. CC-BY / MIT
