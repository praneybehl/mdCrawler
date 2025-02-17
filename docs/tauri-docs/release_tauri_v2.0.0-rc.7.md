Skip to content
# tauri@2.0.0-rc.7
ReturnView on GitHub
### New Features
  * `1e441811e` (#10786 by @amrbashir) On Windows, Add and emit `DoubleClick` variant for `TrayIconEvent`.


### Enhancements
  * `f86a8146a` (#10761 by @rdlabo) Added `getArgs` and `getRawArgs` methods to the plugin `Invoke` class (Kotlin and Swift), which lets you parse the arguments manually instead of through the `parseArgs` method.


### Bug Fixes
  * `03f2a5098` (#10718 by @rdlabo) Update swift-rs fixing a plugin build when native dependencies are used.
  * `22d2afa89` (#10800 by @lucasfernog) Change the Android Proguard rules to keep custom JSON deserializers.
  * `fbe76a955` (#10797 by @lucasfernog) Uint8Arrays and ArrayBuffers are now properly serialized as an array of numbers.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.7`
  * Upgraded to `tauri-build@2.0.0-rc.7`
  * Upgraded to `tauri-runtime@2.0.0-rc.7`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.7`
  * Upgraded to `tauri-macros@2.0.0-rc.6`


© 2025 Tauri Contributors. CC-BY / MIT
