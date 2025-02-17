Skip to content
# Global Shortcut
GitHub npm  crates.io 
API Reference 
Register global shortcuts.
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
Install the global-shortcut plugin to get started.
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

npmruntauriaddglobal-shortcut

```

```

yarnruntauriaddglobal-shortcut

```

```

pnpmtauriaddglobal-shortcut

```

```

denotasktauriaddglobal-shortcut

```

```

buntauriaddglobal-shortcut

```

```

cargotauriaddglobal-shortcut

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-global-shortcut--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_global_shortcut::Builder::new().build());
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

npminstall@tauri-apps/plugin-global-shortcut

```

```

yarnadd@tauri-apps/plugin-global-shortcut

```

```

pnpmadd@tauri-apps/plugin-global-shortcut

```

```

denoaddnpm:@tauri-apps/plugin-global-shortcut

```

```

bunadd@tauri-apps/plugin-global-shortcut

```



## Usage
The global-shortcut plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { register } from'@tauri-apps/plugin-global-shortcut';
// when using `"withGlobalTauri": true`, you may use
// const { register } = window.__TAURI__.globalShortcut;
awaitregister('CommandOrControl+Shift+C', ()=> {
console.log('Shortcut triggered');
});

```

src-tauri/src/lib.rs```

pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
{
use tauri_plugin_global_shortcut::{Code, GlobalShortcutExt, Modifiers, Shortcut, ShortcutState};
letctrl_n_shortcut= Shortcut::new(Some(Modifiers::CONTROL), Code::KeyN);
app.handle().plugin(
tauri_plugin_global_shortcut::Builder::new().with_handler(move|_app, shortcut, event| {
println!("{:?}", shortcut);
ifshortcut==&ctrl_n_shortcut {
matchevent.state() {
ShortcutState::Pressed => {
println!("Ctrl-N Pressed!");
}
ShortcutState::Released => {
println!("Ctrl-N Released!");
}
}
}
})
.build(),
)?;
app.global_shortcut().register(ctrl_n_shortcut)?;
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
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": [
"global-shortcut:allow-is-registered",
"global-shortcut:allow-register",
"global-shortcut:allow-unregister"
]
}

```

## Default Permission
No features are enabled by default, as we believe the shortcuts can be inherently dangerous and it is application specific if specific shortcuts should be registered or unregistered.
## Permission Table
Identifier | Description  
---|---  
`global-shortcut:allow-is-registered` |  Enables the is_registered command without any pre-configured scope.  
`global-shortcut:deny-is-registered` |  Denies the is_registered command without any pre-configured scope.  
`global-shortcut:allow-register` |  Enables the register command without any pre-configured scope.  
`global-shortcut:deny-register` |  Denies the register command without any pre-configured scope.  
`global-shortcut:allow-register-all` |  Enables the register_all command without any pre-configured scope.  
`global-shortcut:deny-register-all` |  Denies the register_all command without any pre-configured scope.  
`global-shortcut:allow-unregister` |  Enables the unregister command without any pre-configured scope.  
`global-shortcut:deny-unregister` |  Denies the unregister command without any pre-configured scope.  
`global-shortcut:allow-unregister-all` |  Enables the unregister_all command without any pre-configured scope.  
`global-shortcut:deny-unregister-all` |  Denies the unregister_all command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
