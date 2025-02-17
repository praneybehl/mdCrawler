Skip to content
# tauri@2.0.0-beta.3
ReturnView on GitHub
### New Features
  * `16e550ec`(#8844) Add webview-specific events for multi-webview windows:
    * Add `WebviewEvent` enum
    * Add `RunEvent::WebviewEvent` variant.
    * Add `Builder::on_webview_event` and `Webview::on_webview_event` methods.


### Enhancements
  * `11a5816b`(#8864) A file-drop now allows sub-directories recursively when the path is a directory.
  * `0cb0a15c`(#8789) Add `webviews` array on the capability for usage on multiwebview contexts.
  * `258494bd`(#8806) Added `Manager::add_capability` to add a capability file at runtime.
  * `5618f6d2`(#8856) Relax requirements on plugin’s identifiers to be alphanumeric and `-` instead of only lower alpha and `-`.


### Bug Fixes
  * `16e550ec`(#8844) Fix JS event listeners registered using JS `listen` api with `EventTarget::Any` never fired.
  * `8751c329`(#8793) Fix invoking toggle devtools by hotkey.
  * `bd73ab0a`(#8766) When using the multiwebview mode, properly remove the webview from memory on `Webview::close`.
  * `46b6598a`(#8826) Fix JS `onCloseRequested` catching close event from other windows.
  * `2e6db908`(#8777) Fix regression in `tauri::Error` not being `Sync`.


### What’s Changed
  * `76ce9f61`(#3002) Enhance centering a newly created window, it will no longer jump to center after being visible.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.2`
  * Upgraded to `tauri-build@2.0.0-beta.2`
  * Upgraded to `tauri-macros@2.0.0-beta.2`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.2`
  * Upgraded to `tauri-runtime@2.0.0-beta.2`


### Breaking Changes
  * `258494bd`(#8806) Removed the lifetime parameter from `ipc::GlobalScope` and `ipc::CommandScope`.
  * `f284f9c5`(#8898) Changed the capability `remote` configuration to take a list of `urls` instead of `domains` for more flexibility.
  * `2f55bfec`(#8795) Update raw-window-handle to 0.6.
  * `2e6db908`(#8777) Require `ScopeObject::Error` to be `Sync` as well.


© 2025 Tauri Contributors. CC-BY / MIT
