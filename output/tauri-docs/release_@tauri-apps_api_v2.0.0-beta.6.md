Skip to content
# @tauri-apps/api@2.0.0-beta.6
ReturnView on GitHub
### New Features
  * `acdd76833`(#9155) Add `TrayIcon.getById` and `TrayIcon.removeById` static methods.


### Enhancements
  * `ea0242db4`(#9179) The `Image` constructor is now public (for internal use only).


### Bug Fixes
  * `379cc2b35`(#9165) Fix `basename(path, &#39;ext&#39;)` JS API when removing all occurances of `ext` where it should only remove the last one.


### Breaking Changes
  * `ea0242db4`(#9179) `Image::rgba()` now returns `Promise&lt;Uint8Array&gt;`.
  * `ea0242db4`(#9179) Removed `width` and `height` methods on the JS `Image` class, use `size` instead.


© 2025 Tauri Contributors. CC-BY / MIT
