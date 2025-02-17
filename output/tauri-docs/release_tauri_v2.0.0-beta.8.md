Skip to content
# tauri@2.0.0-beta.8
ReturnView on GitHub
### New Features
  * `d7f56fef`(#9014) Allow defining a permission that only applies to a set of target platforms via the `platforms` configuration option.


### Bug Fixes
  * `e1d5b790`(#8995) Fixes capability webview label check.
  * `222a96b7`(#8999) Fixes `Window::add_child` deadlock.
  * `e4463f08`(#8930) Clear JS event listeneres on page load, which fixes zombie listeners when the page reloads.
  * `222a96b7`(#8999) Fixes `Webview::reparent` not updating the webview parent window reference.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-beta.6`
  * Upgraded to `tauri-utils@2.0.0-beta.6`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.6`
  * Upgraded to `tauri-runtime@2.0.0-beta.6`
  * Upgraded to `tauri-macros@2.0.0-beta.6`


### Breaking Changes
  * `3657ad82`(#9008) Allow defining permissions for the application commands via `tauri_build::Attributes::app_manifest`.


### Breaking Changes
  * `b9e6a018`(#8937) The `custom-protocol` Cargo feature is no longer required on your application and is now ignored. To check if running on production, use `#[cfg(not(dev))]` instead of `#[cfg(feature = &quot;custom-protocol&quot;)]`.


© 2025 Tauri Contributors. CC-BY / MIT
