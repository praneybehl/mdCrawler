Skip to content
# tauri@1.5.0
ReturnView on GitHub
### New Features
  * `eeb6be54`(#7512) Add `tauri::Manager::emit_filter` and only serialize once when emitting to multiple windows.
  * `6c408b73`(#7269) Add option to specify notification sound.
  * `fdaee9a5`(#7350) Add `tauri::plugin::Builder::register_uri_scheme_protocol`
  * `10e362d0`(#7432) Added `UpdateBuilder::endpoints` to add request endpoints at runtime.
  * `10e362d0`(#7432) Added `UpdateResponse::header` and `UpdateResponse::remove_header` to modify the update download request headers.


### Enhancements
  * `757e959e`(#7344) Open links externally when `&lt;base target=&quot;_blank&quot; /&gt;` exists
  * `c9827338`(#7416) Enhance `readDir` API error with path information.
  * `58d6b899`(#7636) Add `append` option to `FsOptions` in the `fs` JS module, used in `writeTextFile` and `writeBinaryFile`, to be able to append to existing files instead of overwriting it.
  * `9aa34ada`(#7645) Add setting to switch to `http://&lt;scheme&gt;.localhost/` for custom protocols on Windows.


### Bug Fixes
  * `4bf1e85e`(#7722) Properly respect the `focused` option when creating the webview.
  * `0797a002`(#7746) On macOS, fixed tapping on custom title bar doesn’t maximize the window.
  * `1a3dcdb8`(#7185) On Windows, fix NSIS installers requiring administrator rights failing to be launched by updater.
  * `fa7f9b77`(#7341) Fix updater not following endpoint redirects.
  * `6fbd6dba`(#17) Fix the validation of `std::env::current_exe` warn the user if AppImage is not mounted instead of panicking


### Dependencies
  * Upgraded to `tauri-utils@1.5.0`
  * Upgraded to `tauri-runtime-wry@0.14.1`
  * Upgraded to `tauri-runtime@0.14.1`
  * Upgraded to `tauri-macros@1.4.1`


© 2025 Tauri Contributors. CC-BY / MIT
