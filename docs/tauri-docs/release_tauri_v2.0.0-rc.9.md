Skip to content
# tauri@2.0.0-rc.9
ReturnView on GitHub
### New Features
  * `0899e5083` (#10884 by @amrbashir) Derive serde `Serialize` for `SafePathBuf`
  * `431ca2c77` (#10870 by @Legend-Master) Add `FromStr` impl for `SafePathBuf`


### Bug Fixes
  * `79de4332b` (#10841 by @lucasfernog) Fixes IPC postMessage raw body processing when using the isolation pattern.
  * `6696e4880` (#10842 by @lucasfernog) Fixes a warning when using a null value on the `invoke.resolve()` iOS plugin API.


### What’s Changed
  * `27d018343` (#10844 by @lucasfernog) Changes how the Info.plist is embedded on macOS development to avoid a clippy warning.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.8`
  * Upgraded to `tauri-utils@2.0.0-rc.8`
  * Upgraded to `tauri-runtime@2.0.0-rc.8`
  * Upgraded to `tauri-macros@2.0.0-rc.7`
  * Upgraded to `tauri-build@2.0.0-rc.8`


### Breaking Changes
  * `5048a7293` (#10840 by @lucasfernog) The `linux-ipc-protocol` feature is now always enabled, so the Cargo feature flag was removed. This increases the minimum webkit2gtk version to a release that does not affect the minimum target Linux distros for Tauri apps.


© 2025 Tauri Contributors. CC-BY / MIT
