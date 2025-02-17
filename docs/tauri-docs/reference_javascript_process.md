Skip to content
# @tauri-apps/plugin-process
Perform operations on the current process.
## Functions
### exit()
```

functionexit(code):Promise<void>

```

Exits immediately with the given `exitCode`.
#### Parameters
Parameter| Type| Default value| Description  
---|---|---|---  
`code`| `number`| `0`| The exit code to use.  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { exit } from'@tauri-apps/plugin-process';
awaitexit(1);

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/process/guest-js/index.ts#L25
### relaunch()
```

functionrelaunch():Promise<void>

```

Exits the current instance of the app then relaunches it.
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { relaunch } from'@tauri-apps/plugin-process';
awaitrelaunch();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/process/guest-js/index.ts#L41
© 2025 Tauri Contributors. CC-BY / MIT
