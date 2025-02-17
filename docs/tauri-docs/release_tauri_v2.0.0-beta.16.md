Skip to content
# tauri@2.0.0-beta.16
ReturnView on GitHub
### New Features
  * `70c51371e`(#9539) Add `window.isTauri` to check whether running inside tauri or not.


### Bug Fixes
  * `daf018e4f`(#9505) Fix resource tables not cleaned up on exit which causes tray icon inside resource tables not cleaned up on exit
  * `a07b51320`(#9490) Add missing permission for `window.start_resize_dragging`
  * `35b25f7e5`(#9530) Do not use JS optional chaining to prevent script errors on older webviews such as macOS 10.14.


### What’s Changed
  * `005fe8ce1`(#9410) Fix `closable`, `maximizable` and `minimizable` options not taking effect when used in tauri.conf.json or from JS APIs.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.13`
  * Upgraded to `tauri-build@2.0.0-beta.13`
  * Upgraded to `tauri-utils@2.0.0-beta.13`
  * Upgraded to `tauri-runtime@2.0.0-beta.13`
  * Upgraded to `tauri-macros@2.0.0-beta.13`


© 2025 Tauri Contributors. CC-BY / MIT
