Skip to content
# @tauri-apps/api@2.0.0-beta.1
ReturnView on GitHub
### New Features
  * `16e550ec`(#8844) Add a new `webviewWindow` module that exports `WebviewWindow` class and related methods such as `getCurrent` and `getAll`.
  * `16e550ec`(#8844) Add `Window.onFileDropEvent` method.


### Breaking Changes
  * `16e550ec`(#8844) Renamed the following enum variants of `TauriEvent` enum:
    * `TauriEvent.WEBVIEW_FILE_DROP` -> `TauriEvent.FILE_DROP`
    * `TauriEvent.WEBVIEW_FILE_DROP_HOVER` -> `TauriEvent.FILE_DROP_HOVER`
    * `TauriEvent.WEBVIEW_FILE_DROP_CANCELLED` -> `TauriEvent.FILE_DROP_CANCELLED`
  * `16e550ec`(#8844) Move `WebviewWindow` class from `webview` module to a new `webviewWindow` module.


© 2025 Tauri Contributors. CC-BY / MIT
