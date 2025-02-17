Skip to content
# tauri@2.0.0-beta.14
ReturnView on GitHub
### New Features
  * `06833f4fa`(#9100) Added `Rect` struct.
  * `06833f4fa`(#9100) Add `Webview::bounds` and `Webview::set_bounds` APIs.


### Enhancements
  * `06833f4fa`(#9100) Enhance the IPC URL check by using the Origin header on the custom protocol IPC and the new request URI field on the postMessage IPC instead of using `Webview::url()` which only returns the URL of the main frame and is not suitable for iframes (iframe URL fetch is still not supported on Android and on Linux when using the postMessage IPC).


### Bug Fixes
  * `c33f6e6cf`(#9211) Fixed an issue preventing webview/window creation events to not be emitted. This also fixed the `getByLabel` and `getAll` JavaScript functions.


### What’s Changed
  * `06833f4fa`(#9100) Updated `http` crate to `1.1`


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.11`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.11`
  * Upgraded to `tauri-runtime@2.0.0-beta.11`
  * Upgraded to `tauri-macros@2.0.0-beta.11`
  * Upgraded to `tauri-build@2.0.0-beta.11`


### Breaking Changes
  * `06833f4fa`(#9100) Rename `FileDrop` to `DragDrop` on structs, enums and enum variants. Also renamed `file_drop` to `drag_drop` on fields and function names.
  * `284eca9ef`(#9272) `Manager::resources_table` is now scoped so each `App/AppHandle/Window/Webview/WebviewWindow` has its own resource collection.
  * `06833f4fa`(#9100) Refactored the tray icon event struct:
    * Changed `TrayIconEvent.icon_rect` type to use the new `tauri::Rect` type.
    * Removed `TrayIconEvent.x` and `TrayIconEvent.y` fields and combined them into `TrayIconEvent.position` field.
    * Removed `tauri::tray::Rectangle` struct.


© 2025 Tauri Contributors. CC-BY / MIT
