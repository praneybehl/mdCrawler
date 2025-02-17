Skip to content
# Opener
GitHub npm  crates.io 
API Reference 
This plugin allows you to open files and URLs in a specified, or the default, application. It also supports “revealing” files in the system’s file explorer.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android |  Only allows to open URLs via `open`  
ios |  Only allows to open URLs via `open`  
## Setup
Install the opener plugin to get started.
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

npmruntauriaddopener

```

```

yarnruntauriaddopener

```

```

pnpmtauriaddopener

```

```

denotasktauriaddopener

```

```

buntauriaddopener

```

```

cargotauriaddopener

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-opener

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_opener::init())
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

npminstall@tauri-apps/plugin-opener

```

```

yarnadd@tauri-apps/plugin-opener

```

```

pnpmadd@tauri-apps/plugin-opener

```

```

denoaddnpm:@tauri-apps/plugin-opener

```

```

bunadd@tauri-apps/plugin-opener

```



## Usage
The shell plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { openPath } from'@tauri-apps/plugin-opener';
// when using `"withGlobalTauri": true`, you may use
// const { openPath } = window.__TAURI__.opener;
// opens a file using the default program:
awaitopenPath('/path/to/file');
// opens a file using `vlc` command on Windows:
awaitopenPath('C:/path/to/file', 'vlc');

```

Note that `app` is an instance of `App` or `AppHandle`.
```

use tauri_plugin_opener::OpenerExt;
// opens a file using the default program:
app.opener().open_path("/path/to/file", None::<&str>);
// opens a file using `vlc` command on Windows:
app.opener().open_path("C:/path/to/file", Some("vlc"));

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
{
"identifier": "opener:allow-open-path",
"allow": [
{
"path": "/path/to/file"
}
]
}
]
}

```

## Default Permission
This permission set allows opening `mailto:`, `tel:`, `https://` and `http://` urls using their default application as well as reveal file in directories using default file explorer
  * `allow-open-url`
  * `allow-reveal-item-in-dir`
  * `allow-default-urls`


## Permission Table
Identifier | Description  
---|---  
`opener:allow-default-urls` |  This enables opening `mailto:`, `tel:`, `https://` and `http://` urls using their default application.  
`opener:allow-open-path` |  Enables the open_path command without any pre-configured scope.  
`opener:deny-open-path` |  Denies the open_path command without any pre-configured scope.  
`opener:allow-open-url` |  Enables the open_url command without any pre-configured scope.  
`opener:deny-open-url` |  Denies the open_url command without any pre-configured scope.  
`opener:allow-reveal-item-in-dir` |  Enables the reveal_item_in_dir command without any pre-configured scope.  
`opener:deny-reveal-item-in-dir` |  Denies the reveal_item_in_dir command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
