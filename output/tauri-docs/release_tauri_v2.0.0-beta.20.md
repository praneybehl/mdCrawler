Skip to content
# tauri@2.0.0-beta.20
ReturnView on GitHub
### New Features
  * `ae6b13dfc`(#9789) Add `app-region: drag` to HTML elements with `data-tauri-drag-region` on Windows, only WebView2 123+, which should fix dragging using touch.
  * `ec0e092ec`(#9770) Add `App/AppHandle/Window/Webview/WebviewWindow::monitor_from_point(x, y)` getter to get the monitor from a given point.


### Enhancements
  * `5d20530c9`(#9842) Added `AppHandle::set_activation_policy` for macOS.


### Bug Fixes
  * `0b690f242`(#9845) Export `tauri::UriSchemeResponder`.


### Security fixes
  * `d950ac123` Only process IPC commands from the main frame.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.16`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.17`
  * Upgraded to `tauri-runtime@2.0.0-beta.17`
  * Upgraded to `tauri-macros@2.0.0-beta.16`
  * Upgraded to `tauri-build@2.0.0-beta.16`


© 2025 Tauri Contributors. CC-BY / MIT
