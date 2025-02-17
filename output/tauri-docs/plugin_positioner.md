Skip to content
# Positioner
GitHub npm  crates.io 
API Reference 
Position your windows at well-known locations.
This plugin is a port of electron-positioner for Tauri.
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
Install the positioner plugin to get started.
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

npmruntauriaddpositioner

```

```

yarnruntauriaddpositioner

```

```

pnpmtauriaddpositioner

```

```

denotasktauriaddpositioner

```

```

buntauriaddpositioner

```

```

cargotauriaddpositioner

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-positioner--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_positioner::init());
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

npminstall@tauri-apps/plugin-positioner

```

```

yarnadd@tauri-apps/plugin-positioner

```

```

pnpmadd@tauri-apps/plugin-positioner

```

```

denoaddnpm:@tauri-apps/plugin-positioner

```

```

bunadd@tauri-apps/plugin-positioner

```



Additional setup is required to get tray-relative positions to work.
  1. Add `tray-icon` feature to your `Cargo.toml` file:
src-tauri/Cargo.toml```

[dependencies]
tauri-plugin-positioner = { version = "2.0.0", features = ["tray-icon"] }

```

  2. Setup `on_tray_event` for positioner plugin:
src-tauri/src/lib.rs```

pubfnrun() {
tauri::Builder::default()
// This is required to get tray-relative positions to work
.setup(|app| {
#[cfg(desktop)]
{
app.handle().plugin(tauri_plugin_positioner::init());
tauri::tray::TrayIconBuilder::new()
.on_tray_icon_event(|tray_handle, event| {
tauri_plugin_positioner::on_tray_event(tray_handle.app_handle(), &event);
})
.build(app)?;
}
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```



## Usage
The plugin’s APIs are available through the JavaScript guest bindings:
```

import { moveWindow, Position } from'@tauri-apps/plugin-positioner';
// when using `"withGlobalTauri": true`, you may use
// const { moveWindow, Position } = window.__TAURI__.positioner;
moveWindow(Position.TopRight);

```

You can import and use the Window trait extension directly through Rust:
```

use tauri_plugin_positioner::{WindowExt, Position};
letmutwin=app.get_webview_window("main").unwrap();
let_=win.as_ref().window().move_window(Position::TopRight);

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"positioner:default",
]
}

```

## Default Permission
Allows the moveWindow and handleIconState APIs
  * `allow-move-window`
  * `allow-move-window-constrained`
  * `allow-set-tray-icon-state`


## Permission Table
Identifier | Description  
---|---  
`positioner:allow-move-window` |  Enables the move_window command without any pre-configured scope.  
`positioner:deny-move-window` |  Denies the move_window command without any pre-configured scope.  
`positioner:allow-move-window-constrained` |  Enables the move_window_constrained command without any pre-configured scope.  
`positioner:deny-move-window-constrained` |  Denies the move_window_constrained command without any pre-configured scope.  
`positioner:allow-set-tray-icon-state` |  Enables the set_tray_icon_state command without any pre-configured scope.  
`positioner:deny-set-tray-icon-state` |  Denies the set_tray_icon_state command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
