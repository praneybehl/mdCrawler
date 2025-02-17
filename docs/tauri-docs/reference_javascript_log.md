Skip to content
# @tauri-apps/plugin-log
## Interfaces
### LogOptions
#### Properties
Property| Type| Defined in  
---|---|---  
`file?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L9  
`keyValues?`| `Record`<`string`, `undefined` | `string`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L11  
`line?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L10  
## Functions
### attachConsole()
```

functionattachConsole():Promise<UnlistenFn>

```

Attaches a listener that writes log entries to the console as they come in.
#### Returns
`Promise`<`UnlistenFn`>
a function to cancel the listener.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L277
### attachLogger()
```

functionattachLogger(fn):Promise<UnlistenFn>

```

Attaches a listener for the log, and calls the passed function for each log entry.
#### Parameters
Parameter| Type| Description  
---|---|---  
`fn`| `LoggerFn`  
#### Returns
`Promise`<`UnlistenFn`>
a function to cancel the listener.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L256
### debug()
```

functiondebug(message, options?):Promise<void>

```

Logs a message at the debug level.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| # Examples `import { debug } from '@tauri-apps/plugin-log'; const pos = { x: 3.234, y: -1.223 }; debug(`New position: x: {pos.x}, y: {pos.y}`);`  
`options`?| `LogOptions`| -  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L214
### error()
```

functionerror(message, options?):Promise<void>

```

Logs a message at the error level.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| # Examples `import { error } from '@tauri-apps/plugin-log'; const err_info = "No connection"; const port = 22; error(`Error: ${err_info} on port ${port}`);`  
`options`?| `LogOptions`| -  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L148
### info()
```

functioninfo(message, options?):Promise<void>

```

Logs a message at the info level.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| # Examples `import { info } from '@tauri-apps/plugin-log'; const conn_info = { port: 40, speed: 3.20 }; info(`Connected to port {conn_info.port} at {conn_info.speed} Mb/s`);`  
`options`?| `LogOptions`| -  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L192
### trace()
```

functiontrace(message, options?):Promise<void>

```

Logs a message at the trace level.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| # Examples `import { trace } from '@tauri-apps/plugin-log'; let pos = { x: 3.234, y: -1.223 }; trace(`Position is: x: {pos.x}, y: {pos.y}`);`  
`options`?| `LogOptions`| -  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L236
### warn()
```

functionwarn(message, options?):Promise<void>

```

Logs a message at the warn level.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| # Examples `import { warn } from '@tauri-apps/plugin-log'; const warn_description = "Invalid Input"; warn(`Warning! {warn_description}!`);`  
`options`?| `LogOptions`| -  
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/log/guest-js/index.ts#L170
© 2025 Tauri Contributors. CC-BY / MIT
