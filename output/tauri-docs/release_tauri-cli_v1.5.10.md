Skip to content
# tauri-cli@1.5.10
ReturnView on GitHub
### New Features
  * `89911296`(#8259) On macOS, support for signing nested .dylib, .app, .xpc and .framework under predefined directories inside the bundled frameworks (“MacOS”, “Frameworks”, “Plugins”, “Helpers”, “XPCServices” and “Libraries”).


### Bug Fixes
  * `b0f27814`(#8776) Fix `fail to rename app` when using `--profile dev`.
  * `0bff8c32`(#8697) Fix the built-in dev server failing to serve files when URL had queries `?` and other url components.
  * `67d7877f`(#8520) The cli now also watches cargo workspace members if the tauri folder is the workspace root.


### Dependencies
  * Upgraded to `tauri-bundler@1.5.0`


© 2025 Tauri Contributors. CC-BY / MIT
