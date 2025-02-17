Skip to content
# tauri@2.0.0-rc.12
ReturnView on GitHub
### New Features
  * `35bd9dd3d` (#10977 by @amrbashir) Add `mainBinaryName` config option to set the file name for the main binary.


### Enhancements
  * `5eb036f33` (#11002 by @lucasfernog) Handle macOS binary name change on the `process::restart` function.


### Bug Fixes
  * `63649d82d` (#10971 by @amrbashir) Fix schema generation for `core:default` set.
  * `be18ed50d` (#10982 by @lucasfernog) Add a Proguard rule to prevent custom JSON deserializer and serializer classes from being optimized away.
  * `00182ebf8` (#10988 by @lucasfernog) Fix `requestPermissions` not resolving on Android.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-rc.11`
  * Upgraded to `tauri-utils@2.0.0-rc.11`
  * Upgraded to `tauri-runtime@2.0.0-rc.11`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.11`
  * Upgraded to `tauri-macros@2.0.0-rc.10`


### Breaking Changes
  * `fe5ff1228` (#10978 by @lucasfernog) Rename `PermissionState::Unknown` to `PermissionState::Prompt`.


© 2025 Tauri Contributors. CC-BY / MIT
