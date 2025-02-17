Skip to content
# Upload
GitHub npm  crates.io 
API Reference 
Upload files from disk to a remote server over HTTP. Download files from a remote HTTP server to disk.
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

npmruntauriaddupload

```

```

yarnruntauriaddupload

```

```

pnpmtauriaddupload

```

```

denotasktauriaddupload

```

```

buntauriaddupload

```

```

cargotauriaddupload

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-upload

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_upload::init())
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

npminstall@tauri-apps/plugin-upload

```

```

yarnadd@tauri-apps/plugin-upload

```

```

pnpmadd@tauri-apps/plugin-upload

```

```

denoaddnpm:@tauri-apps/plugin-upload

```

```

bunadd@tauri-apps/plugin-upload

```



## Usage
Once you’ve completed the registration and setup process for the plugin, you can access all of its APIs through the JavaScript guest bindings.
Here’s an example of how you can use the plugin to upload and download files:
```

import { upload } from'@tauri-apps/plugin-upload';
// when using `"withGlobalTauri": true`, you may use
// const { upload } = window.__TAURI__.upload;
upload(
'https://example.com/file-upload',
'./path/to/my/file.txt',
({ progress, total })=>
console.log(`Uploaded ${progress} of ${total} bytes`), // a callback that will be called with the upload progress
{ 'Content-Type': 'text/plain' } // optional headers to send with the request
);

```

```

import { download } from'@tauri-apps/plugin-upload';
// when using `"withGlobalTauri": true`, you may use
// const { download } = window.__TAURI__.upload;
download(
'https://example.com/file-download-link',
'./path/to/save/my/file.txt',
({ progress, total })=>
console.log(`Downloaded ${progress} of ${total} bytes`), // a callback that will be called with the download progress
{ 'Content-Type': 'text/plain' } // optional headers to send with the request
);

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"upload:default",
]
}

```

## Default Permission
This permission set configures what kind of operations are available from the upload plugin.
#### Granted Permissions
All operations are enabled by default.
  * `allow-upload`
  * `allow-download`


## Permission Table
Identifier | Description  
---|---  
`upload:allow-download` |  Enables the download command without any pre-configured scope.  
`upload:deny-download` |  Denies the download command without any pre-configured scope.  
`upload:allow-upload` |  Enables the upload command without any pre-configured scope.  
`upload:deny-upload` |  Denies the upload command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
