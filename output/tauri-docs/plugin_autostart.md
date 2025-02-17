Skip to content
# Autostart
GitHub npm  crates.io 
API Reference 
Automatically launch your application at system startup.
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
Install the autostart plugin to get started.
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

npmruntauriaddautostart

```

```

yarnruntauriaddautostart

```

```

pnpmtauriaddautostart

```

```

denotasktauriaddautostart

```

```

buntauriaddautostart

```

```

cargotauriaddautostart

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-autostart--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_autostart::init(tauri_plugin_autostart::MacosLauncher::LaunchAgent, Some(vec!["--flag1", "--flag2"]) /* arbitrary number of args to pass to your app */));
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. You can install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-autostart

```

```

yarnadd@tauri-apps/plugin-autostart

```

```

pnpmadd@tauri-apps/plugin-autostart

```

```

denoaddnpm:@tauri-apps/plugin-autostart

```

```

bunadd@tauri-apps/plugin-autostart

```



## Usage
The autostart plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { enable, isEnabled, disable } from'@tauri-apps/plugin-autostart';
// when using `"withGlobalTauri": true`, you may use
// const { enable, isEnabled, disable } = window.__TAURI__.autostart;
// Enable autostart
awaitenable();
// Check enable state
console.log(`registered for autostart? ${awaitisEnabled()}`);
// Disable autostart
disable();

```

```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
{
use tauri_plugin_autostart::MacosLauncher;
use tauri_plugin_autostart::ManagerExt;
app.handle().plugin(tauri_plugin_autostart::init(
MacosLauncher::LaunchAgent,
Some(vec!["--flag1", "--flag2"]),
));
// Get the autostart manager
letautostart_manager=app.autolaunch();
// Enable autostart
let_=autostart_manager.enable();
// Check enable state
println!("registered for autostart? {}", autostart_manager.is_enabled().unwrap());
// Disable autostart
let_=autostart_manager.disable();
}
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"autostart:allow-enable",
"autostart:allow-disable",
"autostart:allow-is-enabled"
]
}

```

## Default Permission
This permission set configures if your application can enable or disable auto starting the application on boot.
#### Granted Permissions
It allows all to check, enable and disable the automatic start on boot.
  * `allow-enable`
  * `allow-disable`
  * `allow-is-enabled`


## Permission Table
Identifier | Description  
---|---  
`autostart:allow-disable` |  Enables the disable command without any pre-configured scope.  
`autostart:deny-disable` |  Denies the disable command without any pre-configured scope.  
`autostart:allow-enable` |  Enables the enable command without any pre-configured scope.  
`autostart:deny-enable` |  Denies the enable command without any pre-configured scope.  
`autostart:allow-is-enabled` |  Enables the is_enabled command without any pre-configured scope.  
`autostart:deny-is-enabled` |  Denies the is_enabled command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
