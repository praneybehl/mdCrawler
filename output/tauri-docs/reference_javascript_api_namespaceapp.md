Skip to content
# app
## Functions
### defaultWindowIcon()
```

functiondefaultWindowIcon():Promise<Image|null>

```

Get the default window icon.
#### Returns
`Promise`<`Image` | `null`>
#### Example
```

import { defaultWindowIcon } from'@tauri-apps/api/app';
awaitdefaultWindowIcon();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L99
### getName()
```

functiongetName():Promise<string>

```

Gets the application name.
#### Returns
`Promise`<`string`>
#### Example
```

import { getName } from'@tauri-apps/api/app';
const appName = await getName();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L39
### getTauriVersion()
```

functiongetTauriVersion():Promise<string>

```

Gets the Tauri version.
#### Returns
`Promise`<`string`>
#### Example
```

import { getTauriVersion } from'@tauri-apps/api/app';
const tauriVersion = await getTauriVersion();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L54
### getVersion()
```

functiongetVersion():Promise<string>

```

Gets the application version.
#### Returns
`Promise`<`string`>
#### Example
```

import { getVersion } from'@tauri-apps/api/app';
const appVersion = await getVersion();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L25
### hide()
```

functionhide():Promise<void>

```

Hides the application on macOS.
#### Returns
`Promise`<`void`>
#### Example
```

import { hide } from'@tauri-apps/api/app';
awaithide();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L84
### setTheme()
```

functionsetTheme(theme?):Promise<void>

```

Set app’s theme, pass in `null` or `undefined` to follow system theme
#### Parameters
Parameter| Type  
---|---  
`theme`?| `null` | `Theme`  
#### Returns
`Promise`<`void`>
#### Example
```

import { setTheme } from'@tauri-apps/api/app';
awaitsetTheme('dark');

```

#### Platform-specific
  * **iOS / Android:** Unsupported.


#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L120
### show()
```

functionshow():Promise<void>

```

Shows the application on macOS. This function does not automatically focus any specific app window.
#### Returns
`Promise`<`void`>
#### Example
```

import { show } from'@tauri-apps/api/app';
awaitshow();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/app.ts#L69
© 2025 Tauri Contributors. CC-BY / MIT
