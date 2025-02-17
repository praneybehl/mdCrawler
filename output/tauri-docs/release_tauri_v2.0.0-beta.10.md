Skip to content
# tauri@2.0.0-beta.10
ReturnView on GitHub
### New Features
  * `3e472d0af`(#9115) Added `CapabilityBuilder::platform` to link the runtime capability with a specific platform.


### Enhancements
  * `3e472d0af`(#9115) Changed the permission and capability platforms to be optional.
  * `9dc9ca6e3`(#9113) Added `tauri::dev()` to determine whether we are running in development mode or not.


### Bug Fixes
  * `5541aafef`(#9107) Fix `emit` and `emit_to` (when used with `EventTarget::Any`) always skipping the webview listeners.
  * `80c12ead4`(#9121) Fix regression on IPC response when using a channel to return objects.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.8`
  * Upgraded to `tauri-runtime@2.0.0-beta.8`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.8`
  * Upgraded to `tauri-macros@2.0.0-beta.8`
  * Upgraded to `tauri-build@2.0.0-beta.8`


### Breaking Changes
  * `4ef17d083`(#9116) The ACL configuration for remote URLs now uses the URLPattern standard instead of glob patterns.
  * `ed48e2b3c`(#9122) Expose `tauri::image` module to export the `JsImage` type and removed the `Image` root re-export.


© 2025 Tauri Contributors. CC-BY / MIT
