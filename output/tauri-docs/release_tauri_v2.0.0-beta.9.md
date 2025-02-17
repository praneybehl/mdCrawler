Skip to content
# tauri@2.0.0-beta.9
ReturnView on GitHub
### New Features
  * `46de49aaa`(#9059) Added `set_auto_resize` method for the webview.
  * `d1e77acd8`(#9011) Add a new `Image` type in Rust and JS.


### Enhancements
  * `a77be9747`(#9038) Fallback to the postMessage IPC interface if we cannot reach the IPC custom protocol.
  * `e62ca4ee9`(#9070) Added a mechanism to preserve channel message order.
  * `03098b531`(#9036) `Manager::add_capability` now allows adding a dynamically defined capability instead of only relying on static strings.
  * `b5c743276`(#9086) Use a strict content security policy on the isolation pattern iframe.
  * `46de49aaa`(#9059) When using the `unstable` feature flag, `WebviewWindow` will internally use the child webview interface for flexibility.


### Bug Fixes
  * `86fa339de`(#9071) Fix compile time error in context generation when using `app.windows.windowEffects.color`
  * `947a50b8e`(#9049) Fix `tauri migrate` for http plugin ACL.
  * `fe18012d3`(#9072) Resolve symlinks on the filesystem scope check.
  * `6c0683224`(#9068) Fixes scope resolution grouping scopes for all windows.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-beta.7`
  * Upgraded to `tauri-utils@2.0.0-beta.7`
  * Upgraded to `tauri-runtime@2.0.0-beta.7`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.7`
  * Upgraded to `tauri-macros@2.0.0-beta.7`


### Breaking Changes
  * `d1e77acd8`(#9011) Renamed `icon-ico` and `icon-png` feature flags to `image-ico` and `image-png` respectively
  * `720357fd5`(#9104) Removed `tauri::path::Result` and `tauri::path::Error` which were merely an unintentional re-export of `tauri::Result` and `tauri::Error` so use those instead.
  * `6c0683224`(#9068) The `allows` and `denies` methods from `ipc::ScopeValue`, `ipc::CommandScope` and `ipc::GlobalScope` now returns `&amp;Vec&lt;Arc&lt;T&gt;&gt;` instead of `&amp;Vec&lt;T&gt;`.
  * `d1e77acd8`(#9011) Removed `Context::default_window_icon_mut` and `Context::tray_icon_mut`, use `Context::set_default_window_icon` and `Context::set_tray_icon` instead. Also changed `Context::set_tray_icon` to accept `Option&lt;T&gt;`.
  * `d1e77acd8`(#9011) Removed `Icon` enum, use the new `Image` type instead. All APIs that previously accepted `Icon` have changed to accept `Image` instead.


© 2025 Tauri Contributors. CC-BY / MIT
