Skip to content
# Process
GitHub npm  crates.io 
API Reference 
This plugin provides APIs to access the current process. To spawn child processes, see the shell plugin.
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
Install the plugin-process to get started.
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

npmruntauriaddprocess

```

```

yarnruntauriaddprocess

```

```

pnpmtauriaddprocess

```

```

denotasktauriaddprocess

```

```

buntauriaddprocess

```

```

cargotauriaddprocess

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-process

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_process::init())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. If you’d like to utilize the plugin in JavaScript then install the npm package as well:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-process

```

```

yarnadd@tauri-apps/plugin-process

```

```

pnpmadd@tauri-apps/plugin-process

```

```

denoaddnpm:@tauri-apps/plugin-process

```

```

bunadd@tauri-apps/plugin-process

```



## Usage
The process plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { exit, relaunch } from'@tauri-apps/plugin-process';
// when using `"withGlobalTauri": true`, you may use
// const { exit, relaunch } = window.__TAURI__.process;
// exits the app with the given status code
awaitexit(0);
// restarts the app
awaitrelaunch();

```

Note that `app` is an instance of `AppHandle`.
```

// exits the app with the given status code
app.exit(0);
// restarts the app
app.restart();

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"process:default",
]
}

```

## Default Permission
This permission set configures which process features are by default exposed.
#### Granted Permissions
This enables to quit via `allow-exit` and restart via `allow-restart` the application.
  * `allow-exit`
  * `allow-restart`


## Permission Table
Identifier | Description  
---|---  
`process:allow-exit` |  Enables the exit command without any pre-configured scope.  
`process:deny-exit` |  Denies the exit command without any pre-configured scope.  
`process:allow-restart` |  Enables the restart command without any pre-configured scope.  
`process:deny-restart` |  Denies the restart command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
