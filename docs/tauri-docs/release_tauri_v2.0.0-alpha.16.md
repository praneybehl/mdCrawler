Skip to content
# tauri@2.0.0-alpha.16
ReturnView on GitHub
### New Features
  * `c085adda`(#8009) Added `set_progress_bar` to `Window`.
  * `c1ec0f15`(#7933) Added `Window::set_always_on_bottom` and the `always_on_bottom` option when creating a window.
  * `880266a7`(#8031) Bump the MSRV to 1.70.
  * `ed32257d`(#7794) On Windows, add `Effect::Tabbed`,`Effect::TabbedDark` and `Effect::TabbedLight` effects.


### Enhancements
  * `46dcb941`(#8006) Include mobile on docs.rs targets.


### What’s Changed
  * `fb10b879`(#8039) Added the `app` plugin back into core.
  * `c9a9246c`(#8007) Added the `window` plugin back into core.


### Dependencies
  * Upgraded to `tauri-runtime@1.0.0-alpha.3`
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.4`
  * Upgraded to `tauri-utils@2.0.0-alpha.9`
  * Upgraded to `tauri-build@2.0.0-alpha.10`
  * Upgraded to `tauri-macros@2.0.0-alpha.9`


### Breaking Changes
  * `a63e71f9`(#7942) The initialization script for `Builder::invoke_system` now must initialize the `window.__TAURI_INTERNALS__.postMessage` function instead of `window.__TAURI_POST_MESSAGE__`.
  * `12b8d18b`(#7875) - Removed `tauri::path::Error` and added its variants to `tauri::Error`
    * Removed `tauri::path::Result` and `tauri::plugin::Result` aliases, you should use `tauri::Result` or your own `Result` type.
  * `8b166e9b`(#7949) Changed `TAURI_AUTOMATION` to `TAURI_WEBVIEW_AUTOMATION`
  * `2558fab8`(#7939) This release contains a number of breaking changes to improve the consistency of tauri internals and the public facing APIs and simplifying the types where applicable:
    * Removed `EventHandler` type.
    * Added `EventId` type
    * Changed `Manager::listen_global` and `Window::listen` to return the new `EventId` type instead of `EventHandler`.
    * Removed the return type of `Manager::once_global` and `Window::once`
    * Changed `Manager::unlisten` and `Window::unlisten` to take he new `EventId` type.
    * Added `tauri::scope::ScopeEventId`
    * Changed `FsScope::listen` to return the new `ScopeEventId` instead of `Uuid`.
    * Added `FsScope::unlisten`


© 2025 Tauri Contributors. CC-BY / MIT
