Skip to content
# tauri@2.0.0-rc.13
ReturnView on GitHub
### Enhancements
  * `bc4804d48` (#10924 by @madsmtm) Use `objc2` internally and in examples, leading to better memory safety.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.12`


### Breaking Changes
  * `bc4804d48` (#10924 by @madsmtm) Change the pointer type of `PlatformWebview`’s `inner`, `controller`, `ns_window` and `view_controller` to `c_void`, to avoid publically depending on `objc`.


© 2025 Tauri Contributors. CC-BY / MIT
