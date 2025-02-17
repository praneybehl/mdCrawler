Skip to content
# tauri@2.0.0-beta.11
ReturnView on GitHub
### New Features
  * `490a6b424`(#9147) The `Assets` trait now include a `setup` method that lets you run initialization code for your custom asset provider.


### Bug Fixes
  * `85de230f3`(#9144) Fix old JS listeners being dropped on page load after it was possible to create new listeners.
  * `e673854c8`(#9133) Fixes capability remote domain not allowing subpaths, query parameters and hash when those values are empty.


### Dependencies
  * Upgraded to `tauri-macros@2.0.0-beta.9`
  * Upgraded to `tauri-utils@2.0.0-beta.9`
  * Upgraded to `tauri-build@2.0.0-beta.9`
  * Upgraded to `tauri-runtime@2.0.0-beta.9`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.9`


### Breaking Changes
  * `490a6b424`(#9147) The `Context` struct and the `Assets` trait now takes a `R: Runtime` generic.
  * `ba0206d8a`(#9141) `Context::assets` now returns `&amp;dyn Assets` instead of `&amp;A` generic.
  * `ba0206d8a`(#9141) The `Context` type no longer uses the `&lt;A: Assets&gt;` generic so the assets implementation can be swapped with `Context::assets_mut`.
  * `490a6b424`(#9147) Removed `Context::assets_mut` and added `Context::set_assets`.
  * `db0a24a97`(#9132) Use the image crate for `tauri::image::Image` and remove the `from_png_bytes` and `from_ico_bytes` APIs.


© 2025 Tauri Contributors. CC-BY / MIT
