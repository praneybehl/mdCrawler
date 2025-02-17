Skip to content
# tauri@2.0.0-beta.12
ReturnView on GitHub
### New Features
  * `e227fe02f`(#9156) Allow plugins to define (at compile time) JavaScript that are initialized when `withGlobalTauri` is true.


### Enhancements
  * `79b8a3514`(#9151) Improve and optimize event emit calls.


### Bug Fixes
  * `379cc2b35`(#9165) Fix `basename(path, &#39;ext&#39;)` JS API when removing all occurances of `ext` where it should only remove the last one.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-beta.10`
  * Upgraded to `tauri-utils@2.0.0-beta.10`
  * Upgraded to `tauri-runtime@2.0.0-beta.10`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.10`
  * Upgraded to `tauri-macros@2.0.0-beta.10`


### Breaking Changes
  * `acdd76833`(#9155) Removed `App/AppHandle::tray` and `App/AppHandle::remove_tray`, use `App/AppHandle::tray_by_id` and `App/AppHandle::remove_tray_by_id` instead. If these APIs were used to access tray icon configured in `tauri.conf.json`, you can use `App/AppHandle::tray_by_id` with ID `main` or the configured value.
  * `ea0242db4`(#9179) Removed `width` and `height` methods on the JS `Image` class, use `size` instead.


© 2025 Tauri Contributors. CC-BY / MIT
