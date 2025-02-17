Skip to content
# tauri@2.0.3
ReturnView on GitHub
### New Features
  * `1d3f51e10` (#11228 by @amrbashir) Add `tauri::Builder::on_menu_event`.


### Bug Fixes
  * `d609bef9f` (#11314 by @amrbashir) Fix android invalid proguard file when using an `identifier` that contains a component that is a reserved kotlin keyword, like `in`, `class`, etc
  * `04fd3a7db` (#11264 by @chrox) Respond with empty body for `HEAD` requests to `asset` protocol
  * `4731f0cf3` (#11290 by @lucasfernog) Export the `ipc::Invoke` struct.
  * `2d087ee4b` (#11268 by @amrbashir) On Linux, fix commands, that use `Webview` or `WebviewWindow` as an argument, receiving an incorrect webview when using multi webviews.
  * `2d087ee4b` (#11268 by @amrbashir) On Linux, fix events only emitted to first webview only when using multi webviews.
  * `2d087ee4b` (#11268 by @amrbashir) On Linux, fix custom protocols receiving an incorrect webview label when using multi webviews


### Dependencies
  * Upgraded to `tauri-runtime@2.1.0`
  * Upgraded to `tauri-runtime-wry@2.1.0`


© 2025 Tauri Contributors. CC-BY / MIT
