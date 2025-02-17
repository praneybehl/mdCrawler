Skip to content
# tauri@2.0.0-beta.15
ReturnView on GitHub
### New Features
  * `58a7a552d`(#9378) Added the `set_zoom` function to the webview API.
  * `58a7a552d`(#9378) Add `zoom_hotkeys_enabled` to enable browser native zoom controls on creating webviews.
  * `4973d73a2`(#9386) Provide a basic zoom hotkey polyfill for non-Windows platforms


### Enhancements
  * `f1674fce6`(#9420) Tauri’s built-in commands for the JS api will now return simplified paths on Windows, removing the `\\?\` prefix.


### Bug Fixes
  * `c8a82ad22`(#9379) Fix deadlock when using the menu/tray/image JS APIs.
  * `6251645ac`(#9360) Fixes an issue causing `getAll()` to list webviews that were already destroyed.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.12`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.12`
  * Upgraded to `tauri-runtime@2.0.0-beta.12`
  * Upgraded to `tauri-macros@2.0.0-beta.12`
  * Upgraded to `tauri-build@2.0.0-beta.12`


### Breaking Changes
  * `c8a82ad22`(#9379) Changed `JsImage::into_img` to take a reference to a `ResourceTable` instead of a `Manager`.


© 2025 Tauri Contributors. CC-BY / MIT
