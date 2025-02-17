Skip to content
# Trunk
Trunk is a WASM web application bundler for Rust. Learn more about Trunk at https://trunkrs.dev. This guide is accurate as of Trunk 0.17.5.
## Checklist
  * Use SSG, Tauri doesn’t officially support server based solutions.
  * Use `serve.ws_protocol = "ws"` so that the hot-reload websocket can connect properly for mobile development.
  * Enable `withGlobalTauri` to ensure that Tauri APIs are available in the `window.__TAURI__` variable and can be imported using `wasm-bindgen`.


## Example Configuration
  1. ##### Update Tauri configuration
tauri.conf.json```

{
"build": {
"beforeDevCommand": "trunk serve",
"beforeBuildCommand": "trunk build",
"devUrl": "http://localhost:8080",
"frontendDist": "../dist"
},
"app": {
"withGlobalTauri": true
}
}

```

  2. ##### Update Trunk configuration
Trunk.toml```

[watch]
ignore = ["./src-tauri"]
[serve]
ws_protocol = "ws"

```



© 2025 Tauri Contributors. CC-BY / MIT
