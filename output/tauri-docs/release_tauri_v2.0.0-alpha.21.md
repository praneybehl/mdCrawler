Skip to content
# tauri@2.0.0-alpha.21
ReturnView on GitHub
### New Features
  * `29ced5ce`(#8159) Added `WindowBuilder::on_download` to handle download request events.


### Enhancements
  * `d621d343`(#8607) Added tracing for window startup, plugins, `Window::eval`, events, IPC, updater and custom protocol request handlers behind the `tracing` feature flag.


### What’s Changed
  * `cb640c8e`(#8393) Fix `RunEvent::WindowEvent(event: WindowEvent::FileDrop(FileDropEvent))` never triggered and always prevent default OS behavior when `disable_file_drop_handler` is not used.


### Dependencies
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.9`
  * Upgraded to `tauri-utils@2.0.0-alpha.13`
  * Upgraded to `tauri-runtime@1.0.0-alpha.8`
  * Upgraded to `tauri-macros@2.0.0-alpha.13`
  * Upgraded to `tauri-build@2.0.0-alpha.14`


### Breaking Changes
  * `2032228c`(#8430) Removed `GlobalWindowEvent` struct, and unpacked its field to be passed directly to `tauri::Builder::on_window_event`.


© 2025 Tauri Contributors. CC-BY / MIT
