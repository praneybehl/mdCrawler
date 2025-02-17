Skip to content
# tauri@2.0.0-rc.3
ReturnView on GitHub
### Bug Fixes
  * `b1d9ffa1a` (#10582 by @lucasfernog) Fix IPC fallback (postMessage implementation when custom protocol fails) hanging when sending responses.


### What’s Changed
  * `bfc49cc7a` (#10558 by @ahqsoftwares) Remove targetSdk from gradle files
  * `fedf93eb7` (#10585 by @lucasfernog) Change how IPC handles errors to simplify what’s logged in the console.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-rc.3`
  * Upgraded to `tauri-utils@2.0.0-rc.3`
  * Upgraded to `tauri-runtime@2.0.0-rc.3`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.3`
  * Upgraded to `tauri-macros@2.0.0-rc.3`
  * `d39c392b7` (#10655 by @lucasfernog) Update `tao` to 0.29 and `wry` to 0.42.


### Breaking Changes
  * `d0510f52e` (#10641 by @lucasfernog) Added a dedicated type for IPC response body `InvokeResponseBody` for performance reasons. This is only a breaking change if you are directly using types from `tauri::ipc`.


© 2025 Tauri Contributors. CC-BY / MIT
