Skip to content
# tauri@2.0.0-rc.0
ReturnView on GitHub
### Bug Fixes
  * `6755af230`(#10435) Fix Specta remote implementation target for `Channel`.
  * `24445d71d`(#10432) Fixes asset resolving when not using the `compression` feature.


### Enhancements
  * `1e0793b68` (#10357) Enhance `AssetResolver::get` in development mode by reading distDir directly as a fallback to the embedded assets.
  * `7aeac39e7` (#10397) Make the set of gtk application id optional, to allow more then one instance of the app running at the same time.
  * `cf994a6bb` (#10405) Add `tauri::plugin::Builder::try_build` to allow plugins to check if their `TauriPlugin` initialization is valid.


### Security fixes
  * `426d14bb4` (#10423) Explicitly check that the main frame’s origin is the sender of Isolation Payloads
  * `289ae5555` (#10386) Re-enable TLS checks that were previously disabled to support an insecure HTTPS custom protocol on Android which is no longer used.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.0`
  * Upgraded to `tauri-macros@2.0.0-rc.0`
  * Upgraded to `tauri-build@2.0.0-rc.0`
  * Upgraded to `tauri-runtime@2.0.0-rc.0`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.0`


### Breaking Changes
  * `758d28c8a` (#10390) Core plugin permissions are now prefixed with `core:`, the `core:default` permission set can now be used and the `core` plugin name is reserved. The `tauri migrate` tool will automate the migration process, which involves prefixing all `app`, `event`, `image`, `menu`, `path`, `resources`, `tray`, `webview` and `window` permissions with `core:`.


© 2025 Tauri Contributors. CC-BY / MIT
