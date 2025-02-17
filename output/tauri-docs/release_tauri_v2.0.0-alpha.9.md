Skip to content
# tauri@2.0.0-alpha.9
ReturnView on GitHub
  * `256c30c7`(#6863) Enhance parsing of annotated Android plugin methods to support private functions.
  * `73c803a5`(#6837) Added static function `loadConfig` on the Android `PluginManager` class.
  * `edb16d13`(#6831) Adjust Android plugin exception error.
  * `0ab5f40d`(#6813) Add channel API for sending data across the IPC.
  * `31444ac1`(#6725) On Android, update proguard rules.
  * `8ce32e74`(#6986) Add `default_window_icon` getter on `App` and `AppHandle`.
  * `2a5175a8`(#6779) Enhance Android’s `JSObject` return types.
  * `bb2a8ccf`(#6830) Use actual iOS plugin instance to run command with `throws`.
  * `94224906`(#6783) Generate `TauriActivity` Kotlin class on the build script.
  * `7a4b1fb9`(#6839) Added support to attibutes for each command path in the `generate_handler` macro.
  * `9a79dc08`(#6947) Remove `enable_tauri_api` from the IPC scope.
  * `dfa407ff`(#6763) Expose plugin configuration on the Android and iOS plugin classes.
  * `3245d14b`(#6895) Moved the `app` feature to its own plugin in the plugins-workspace repository.
  * `09376af5`(#6704) Moved the `cli` feature to its own plugin in the plugins-workspace repository.
  * `2d5378bf`(#6717) Moved the dialog APIs to its own plugin in the plugins-workspace repository.
  * `39f1b04f`(#6943) Moved the `event` JS APIs to a plugin.
  * `fc4d687e`(#6716) Moved the file system APIs to its own plugin in the plugins-workspace repository.
  * `f78a3783`(#6742) Moved the `http` feature to its own plugin in the plugins-workspace repository.
  * `29ce9ce2`(#6902) Moved the `os` feature to its own plugin in the plugins-workspace repository.
  * `60cf9ed2`(#6905) Moved the `process` feature to its own plugin in the plugins-workspace repository.
  * `e1e85dc2`(#6925) Moved the `protocol` scope configuration to the `asset_protocol` field in `SecurityConfig`.
  * `96639ca2`(#6749) Moved the `shell` functionality to its own plugin in the plugins-workspace repository.
  * `e1e85dc2`(#6925) Moved the updater configuration to the `BundleConfig`.
  * `b072daa3`(#6919) Moved the `updater` feature to its own plugin in the plugins-workspace repository.
  * `3188f376`(#6883) Bump the MSRV to 1.65.
  * `d693e526`(#6780) Added the `onNewIntent` Plugin hook on Android.
  * `34b8f339`(#6705) Add `app` method for the `PluginApi` struct.
  * `96639ca2`(#6749) Moved the `tauri::api::process` module to `tauri::process`.
  * `cdad6e08`(#6774) Changed how the `tauri-android` dependency is injected. This requires the `gen/android` project to be recreated.
  * `e1e85dc2`(#6925) Removed the allowlist configuration.
  * `cebd7526`(#6728) Moved the `clipboard` feature to its own plugin in the plugins-workspace repository.
  * `e1e85dc2`(#6925) Removed extract and move APIs from `tauri::api::file`.
  * `3f17ee82`(#6737) Moved the `global-shortcut` feature to its own plugin in the plugins-workspace repository.
  * `ae102980`(#6719) Refactor the `Context` conditional fields and only parse the tray icon on desktop.
  * `2d5378bf`(#6717) Remove the updater’s dialog option.
  * `e1e85dc2`(#6925) Removed `UpdaterEvent`. See `tauri-plugin-updater` for new usage.
  * `9a79dc08`(#6947) Moved the `window` JS APIs to its own plugin in the plugins-workspace repository.
  * `22a76338`(#6713) Expose `SafePathBuf` type in `tauri::path`.
  * `c4171152`(#6909) Enable shadows by default.
  * `dfa407ff`(#6763) Change iOS plugin init function signature to `func init_plugin() -&gt; Plugin`.


© 2025 Tauri Contributors. CC-BY / MIT
