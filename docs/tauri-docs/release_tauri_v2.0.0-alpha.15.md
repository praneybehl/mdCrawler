Skip to content
# tauri@2.0.0-alpha.15
ReturnView on GitHub
### Enhancements
  * `b597aa5f`(#7871) Set `main` as the default `id` for the tray icon registered from the configuration file, so if the `id` is not specified, it can be retrieved using `app.tray_by_id(&quot;main&quot;)`.


### Bug Fixes
  * `a2021c30`(#7866) Changed `IconMenuItem::set_native_icon` signature to take `&amp;self` instead of `&amp;mut self` to fix compilation error on macos.
  * `a68ccaf5`(#7822) Fix `asset` protocol failing to fetch files.
  * `6fbd6dba`(#17) Fix the validation of `std::env::current_exe` warn the user if AppImage is not mounted instead of panicking


### Dependencies
  * Upgraded to `tauri-macros@2.0.0-alpha.8`
  * Upgraded to `tauri-utils@2.0.0-alpha.8`
  * Upgraded to `tauri-build@2.0.0-alpha.9`
  * Upgraded to `tauri-runtime@1.0.0-alpha.2`
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.3`


### Breaking Changes
  * `092a561c`(#7874) Removed `tauri::api` module as most apis have been moved to either a plugin or we recommend using other crates.
  * `deea9436`(#7876) Changed `Env.args` to `Env.args_os` and now uses `OsString` instead of `String`
  * `b7fd88e1`(#7944) `tauri::scope` module is recieving a couple of consistency changes:
    * Added `tauri::scope::fs` module.
    * Removed `scope::IpcScope` re-export, use `scope::ipc::Scope`.
    * Removed `FsScope`, `GlobPattern` and `FsScopeEvent`, use `scope::fs::Scope`, `scope::fs::Pattern` and `scope::fs::Event` respectively.
  * `c0d03af4`(#7943) Changed `TrayIconBuilder/TrayIcon::on_tray_event` to `TrayIconBuilder/TrayIcon::on_tray_icon_event` for consistency of naming.


© 2025 Tauri Contributors. CC-BY / MIT
