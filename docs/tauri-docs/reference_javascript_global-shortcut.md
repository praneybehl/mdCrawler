Skip to content
# @tauri-apps/plugin-global-shortcut
Register global shortcuts.
## Interfaces
### ShortcutEvent
#### Properties
Property| Type| Defined in  
---|---|---  
`id`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L15  
`shortcut`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L14  
`state`| `"Released"` | `"Pressed"`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L16  
## Type Aliases
### ShortcutHandler()
```

type ShortcutHandler: (event) => void;

```

#### Parameters
Parameter| Type  
---|---  
`event`| `ShortcutEvent`  
#### Returns
`void`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L19
## Functions
### isRegistered()
```

functionisRegistered(shortcut):Promise<boolean>

```

Determines whether the given shortcut is registered by this application or not.
If the shortcut is registered by another application, it will still return `false`.
#### Parameters
Parameter| Type| Description  
---|---|---  
`shortcut`| `string`| shortcut definition, modifiers and key separated by ”+” e.g. CmdOrControl+Q  
#### Returns
`Promise`<`boolean`>
#### Example
```

import { isRegistered } from'@tauri-apps/plugin-global-shortcut';
const isRegistered = await isRegistered('CommandOrControl+P');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L117
### register()
```

functionregister(shortcuts, handler):Promise<void>

```

Register a global shortcut or a list of shortcuts.
The handler is called when any of the registered shortcuts are pressed by the user.
If the shortcut is already taken by another application, the handler will not be triggered. Make sure the shortcut is as unique as possible while still taking user experience into consideration.
#### Parameters
Parameter| Type| Description  
---|---|---  
`shortcuts`| `string` | `string`[]| -  
`handler`| `ShortcutHandler`| Shortcut handler callback - takes the triggered shortcut as argument  
#### Returns
`Promise`<`void`>
#### Example
```

import { register } from'@tauri-apps/plugin-global-shortcut';
// register a single hotkey
awaitregister('CommandOrControl+Shift+C', (event)=> {
if (event.state==="Pressed") {
console.log('Shortcut triggered');
}
});
// or register multiple hotkeys at once
awaitregister(['CommandOrControl+Shift+C', 'Alt+A'], (event)=> {
console.log(`Shortcut ${event.shortcut} triggered`);
});

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L51
### unregister()
```

functionunregister(shortcuts):Promise<void>

```

Unregister a global shortcut or a list of shortcuts.
#### Parameters
Parameter| Type  
---|---  
`shortcuts`| `string` | `string`[]  
#### Returns
`Promise`<`void`>
#### Example
```

import { unregister } from'@tauri-apps/plugin-global-shortcut';
// unregister a single hotkey
awaitunregister('CmdOrControl+Space');
// or unregister multiple hotkeys at the same time
awaitunregister(['CmdOrControl+Space', 'Alt+A']);

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L82
### unregisterAll()
```

functionunregisterAll():Promise<void>

```

Unregister all global shortcuts.
#### Returns
`Promise`<`void`>
#### Example
```

import { unregisterAll } from'@tauri-apps/plugin-global-shortcut';
awaitunregisterAll();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/global-shortcut/guest-js/index.ts#L98
© 2025 Tauri Contributors. CC-BY / MIT
