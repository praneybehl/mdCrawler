Skip to content
# Window State
GitHub npm  crates.io 
API Reference 
Save window positions and sizes and restore them when the app is reopened.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the window-state plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriaddwindow-state

```

```

yarnruntauriaddwindow-state

```

```

pnpmtauriaddwindow-state

```

```

denotasktauriaddwindow-state

```

```

buntauriaddwindow-state

```

```

cargotauriaddwindow-state

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-window-state--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_window_state::Builder::default().build());
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-window-state

```

```

yarnadd@tauri-apps/plugin-window-state

```

```

pnpmadd@tauri-apps/plugin-window-state

```

```

denoaddnpm:@tauri-apps/plugin-window-state

```

```

bunadd@tauri-apps/plugin-window-state

```



## Usage
After adding the window-state plugin, all windows will remember their state when the app is being closed and will restore to their previous state on the next launch.
You can also access the window-state plugin in both JavaScript and Rust.
### JavaScript
You can use `saveWindowState` to manually save the window state:
```

import { saveWindowState, StateFlags } from'@tauri-apps/plugin-window-state';
// when using `"withGlobalTauri": true`, you may use
// const { saveWindowState, StateFlags } = window.__TAURI__.windowState;
saveWindowState(StateFlags.ALL);

```

Similarly you can manually restore a window’s state from disk:
```

import {
restoreStateCurrent,
StateFlags,
} from'@tauri-apps/plugin-window-state';
// when using `"withGlobalTauri": true`, you may use
// const { restoreStateCurrent, StateFlags } = window.__TAURI__.windowState;
restoreStateCurrent(StateFlags.ALL);

```

### Rust
You can use the `save_window_state()` method exposed by the `AppHandleExt` trait:
```

use tauri_plugin_window_state::{AppHandleExt, StateFlags};
// `tauri::AppHandle` now has the following additional method
app.save_window_state(StateFlags::all()); // will save the state of all open windows to disk

```

Similarly you can manually restore a window’s state from disk using the `restore_state()` method exposed by the `WindowExt` trait:
```

use tauri_plugin_window_state::{WindowExt, StateFlags};
// all `Window` types now have the following additional method
window.restore_state(StateFlags::all()); // will restore the window's state from disk

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"window-state:default",
]
}

```

## Default Permission
This permission set configures what kind of operations are available from the window state plugin.
#### Granted Permissions
All operations are enabled by default.
  * `allow-filename`
  * `allow-restore-state`
  * `allow-save-window-state`


## Permission Table
Identifier | Description  
---|---  
`window-state:allow-filename` |  Enables the filename command without any pre-configured scope.  
`window-state:deny-filename` |  Denies the filename command without any pre-configured scope.  
`window-state:allow-restore-state` |  Enables the restore_state command without any pre-configured scope.  
`window-state:deny-restore-state` |  Denies the restore_state command without any pre-configured scope.  
`window-state:allow-save-window-state` |  Enables the save_window_state command without any pre-configured scope.  
`window-state:deny-save-window-state` |  Denies the save_window_state command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
