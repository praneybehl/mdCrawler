Skip to content
# tauri@2.0.4
ReturnView on GitHub
### New Features
  * `bcf279278` (#11354) On Windows, Add `ContextMenu::hpopupmenu` method to get the `HMENU` used for popups and tray icon menu.


### Enhancements
  * `e3b09be7f` (#11362) Added `Builder::channel_interceptor` to intercept messages to be sent to the frontend, complemeting the `Builder::invoke_system` interface.
  * `3cb73d08c` (#11355) Mark the event commands as async so they do not block the main thread.


### Bug Fixes
  * `f3f521f03` (#11348) Fix `TAURI_ANDROID_PACKAGE_UNESCAPED not set` panic during compilation for Android when using an older tauri cli.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.1.1`


© 2025 Tauri Contributors. CC-BY / MIT
