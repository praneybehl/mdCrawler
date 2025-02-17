Skip to content
# Websocket
GitHub npm  crates.io 
API Reference 
Open a WebSocket connection using a Rust client in JavaScript.
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
Install the websocket plugin to get started.
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

npmruntauriaddwebsocket

```

```

yarnruntauriaddwebsocket

```

```

pnpmtauriaddwebsocket

```

```

denotasktauriaddwebsocket

```

```

buntauriaddwebsocket

```

```

cargotauriaddwebsocket

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-websocket

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_websocket::init())
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

npminstall@tauri-apps/plugin-websocket

```

```

yarnadd@tauri-apps/plugin-websocket

```

```

pnpmadd@tauri-apps/plugin-websocket

```

```

denoaddnpm:@tauri-apps/plugin-websocket

```

```

bunadd@tauri-apps/plugin-websocket

```



## Usage
The websocket plugin is available in JavaScript.
```

import WebSocket from'@tauri-apps/plugin-websocket';
// when using `"withGlobalTauri": true`, you may use
// const WebSocket = window.__TAURI__.websocket;
const ws = await WebSocket.connect('ws://127.0.0.1:8080');
ws.addListener((msg)=> {
console.log('Received Message:', msg);
});
awaitws.send('Hello World!');
awaitws.disconnect();

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
"permissions": ["websocket:default"]
}

```

## Default Permission
Allows connecting and sending data to a WebSocket server
  * `allow-connect`
  * `allow-send`


## Permission Table
Identifier | Description  
---|---  
`websocket:allow-connect` |  Enables the connect command without any pre-configured scope.  
`websocket:deny-connect` |  Denies the connect command without any pre-configured scope.  
`websocket:allow-send` |  Enables the send command without any pre-configured scope.  
`websocket:deny-send` |  Denies the send command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
