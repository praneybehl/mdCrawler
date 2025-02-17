Skip to content
# Clipboard
GitHub npm  crates.io 
API Reference 
Read and write to the system clipboard using the clipboard plugin.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android |  Only plain-text content support  
ios |  Only plain-text content support  
## Setup
Install the clipboard plugin to get started.
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

npmruntauriaddclipboard-manager

```

```

yarnruntauriaddclipboard-manager

```

```

pnpmtauriaddclipboard-manager

```

```

denotasktauriaddclipboard-manager

```

```

buntauriaddclipboard-manager

```

```

cargotauriaddclipboard-manager

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-clipboard-manager

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_clipboard_manager::init())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. If you’d like to manage the clipboard in JavaScript then install the npm package as well:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-clipboard-manager

```

```

yarnadd@tauri-apps/plugin-clipboard-manager

```

```

pnpmadd@tauri-apps/plugin-clipboard-manager

```

```

denoaddnpm:@tauri-apps/plugin-clipboard-manager

```

```

bunadd@tauri-apps/plugin-clipboard-manager

```



## Usage
The clipboard plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { writeText, readText } from'@tauri-apps/plugin-clipboard-manager';
// when using `"withGlobalTauri": true`, you may use
// const { writeText, readText } = window.__TAURI__.clipboardManager;
// Write content to clipboard
awaitwriteText('Tauri is awesome!');
// Read content from clipboard
const content = await readText();
console.log(content);
// Prints "Tauri is awesome!" to the console

```

```

use tauri_plugin_clipboard_manager::ClipboardExt;
app.clipboard().write_text("Tauri is awesome!".to_string()).unwrap();
// Read content from clipboard
letcontent=app.clipboard().read_text();
println!("{:?}", content.unwrap());
// Prints "Tauri is awesome!" to the terminal

```

## Default Permission
No features are enabled by default, as we believe the clipboard can be inherently dangerous and it is application specific if read and/or write access is needed.
Clipboard interaction needs to be explicitly enabled.
## Permission Table
Identifier | Description  
---|---  
`clipboard-manager:allow-clear` |  Enables the clear command without any pre-configured scope.  
`clipboard-manager:deny-clear` |  Denies the clear command without any pre-configured scope.  
`clipboard-manager:allow-read-image` |  Enables the read_image command without any pre-configured scope.  
`clipboard-manager:deny-read-image` |  Denies the read_image command without any pre-configured scope.  
`clipboard-manager:allow-read-text` |  Enables the read_text command without any pre-configured scope.  
`clipboard-manager:deny-read-text` |  Denies the read_text command without any pre-configured scope.  
`clipboard-manager:allow-write-html` |  Enables the write_html command without any pre-configured scope.  
`clipboard-manager:deny-write-html` |  Denies the write_html command without any pre-configured scope.  
`clipboard-manager:allow-write-image` |  Enables the write_image command without any pre-configured scope.  
`clipboard-manager:deny-write-image` |  Denies the write_image command without any pre-configured scope.  
`clipboard-manager:allow-write-text` |  Enables the write_text command without any pre-configured scope.  
`clipboard-manager:deny-write-text` |  Denies the write_text command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
