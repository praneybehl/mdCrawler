Skip to content
# tauri@2.0.0-beta.23
ReturnView on GitHub
### New Features
  * `148f04887` (#9979) Add `defaultWindowIcon` to the JS `app` module to retrieve the default window icon in JS.
  * `5b769948a` (#9959) Add `include_image` macro to help embedding instances of `Image` struct at compile-time in rust to be used with window, menu or tray icons.
  * `ddaabda36` (#9922) Add `WebviewWindowBuilder::on_download`.


### Enhancements
  * `cee0bfcd6` (#10092) Make `tray:default` and `menu:default` include all tray and menu permissions


### Bug Fixes
  * `e93ca1df3` (#10138) Fix `InvokeBody::deserialize` method deserialization for `InvokeBody::Raw` variant
  * `e6e17ad1c` (#9954) Add `std` feature to `raw-window-handle` crate so that using `default-features = false` on `tauri` crate can work
  * `f29b78811` (#9862) On Windows, handle resizing undecorated windows natively which improves performance and fixes a couple of annoyances with previous JS implementation:
    * No more cursor flickering when moving the cursor across an edge.
    * Can resize from top even when `data-tauri-drag-region` element exists there.
    * Upon starting rezing, clicks don’t go through elements behind it so no longer accidental clicks.


### What’s Changed
  * `669b9c6b5` (#9621) Set the gtk application to the identifier defined in `tauri.conf.json` to ensure the app uniqueness.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.18`
  * Upgraded to `tauri-build@2.0.0-beta.18`
  * Upgraded to `tauri-macros@2.0.0-beta.18`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.19`
  * Upgraded to `tauri-runtime@2.0.0-beta.19`
  * `f955f7b49` (#9929) Switch from `dirs_next` to `dirs` as `dirs_next` is now unmaintained while `dirs` is
  * `d4c908cfb` (#10048) Update `windows` crate to version `0.57` and `webview2-com` crate to version `0.31`


### Breaking Changes
  * `3afe82894` (#10134) Changed `WebviewWindow::navigate` and `Webview::navigate` method signature to return a `Result`


© 2025 Tauri Contributors. CC-BY / MIT
