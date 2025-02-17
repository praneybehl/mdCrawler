Skip to content
# tauri@2.0.0-beta.17
ReturnView on GitHub
### New Features
  * `12b4159bd`(#9392) Add `specta` feature flag which adds `specta` support for `AppHandle`, `State`, `Window`, `Webview` and `WebviewWindow` types.
  * `477bb8cd4`(#9297) Add `App/AppHandle/Window/Webview/WebviewWindow::cursor_position` getter to get the current cursor position.


### Enhancements
  * `eff778b8f`(#9571) Run each plugin initialization script on its own context so they do not interfere with each other or the Tauri init script.


### Bug Fixes
  * `6c047aee1`(#9612) Fix window white flashing on exit on Windows
  * `98101cb17`(#9561) Allow any headers on the IPC custom protocol.


### Dependencies
  * Upgraded to `tauri-runtime@2.0.0-beta.14`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.14`


© 2025 Tauri Contributors. CC-BY / MIT
