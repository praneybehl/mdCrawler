Skip to content
# tauri@1.0.0-rc.5
ReturnView on GitHub
  * Added `updater_target` method to the `Builder` struct.
    * 579312f8 feat(updater): separate intel and apple silicon targets, closes #3359 (#3739) on 2022-03-23
  * Added an option to disable the CSP injection of distributable assets nonces and hashes.
    * f6e32ee1 feat(core): add dangerous option to disable compile time CSP injection (#3775) on 2022-03-28
  * Toggle devtools when `Ctrl + Shift + I` or `Command + Option + I` is pressed.
    * e05d718a feat(core): add hotkey to toggle devtools, closes #3776 (#3791) on 2022-03-28
  * Use asynchronous file dialog on macOS and Windows to properly set the parent window.
    * bf89a05f fix(core): dialog parent window on macOS, closes #3312 (#3753) on 2022-03-23
  * The `Error` enum is now `Send + Sync`.
    * da1e8793 feat(core): improve and cleanup the `Error` enum (#3748) on 2022-03-22
  * Do not allow path traversal on the asset protocol.
    * 34a402f9 fix(core): do not allow path traversal on the asset protocol (#3774) on 2022-03-27
  * Properly apply the CSP when loading a route that fallbacks to index.html.
    * bcd43168 fix(core): properly add CSP header to fallback routes (#3641) on 2022-03-08
  * Fix CSP usage on Linux when changing it via the `on_web_resource_request` handler.
    * f5efc248 fix(core): runtime CSP changes on Linux on 2022-03-07
  * Improved the updater response validation and error messages.
    * dbc2873e feat(updater): improve validation and error messages, closes #3761 (#3780) on 2022-03-27
  * **Breaking change:** The `MenuItem::About` variant is now associated with a tuple value `(String, AboutMetadata)`.
    * 5fb74332 chore(deps): update wry to 0.14, tao to 0.7 (#3790) on 2022-03-28
  * Replace multiple dependencies who’s C code compiled concurrently and caused the other ones to bloat compile time significantly.
  * `zstd` -> `brotli`
  * `blake3` -> a vendored version of the blake3 reference
  * `ring` -> `getrandom`


See https://github.com/tauri-apps/tauri/pull/3773 for more information about these specific choices.
  * 8661e3e2 replace dependencies with long build times when used together (closes #3571) (#3773) on 2022-03-27
  * **Breaking change:** The `Window::hwnd` method now returns _HWND_ from `windows-rs` crate instead of _c_void_ on Windows. 
    * 4e807a53 Support window parenting on macOS, closes #3751 (#3754) on 2022-03-23
  * Support window parenting on macOS 
    * 4e807a53 Support window parenting on macOS, closes #3751 (#3754) on 2022-03-23
  * **Breaking change:** The updater default targets have been renamed to include better support for different architectures. 
    * 579312f8 feat(updater): separate intel and apple silicon targets, closes #3359 (#3739) on 2022-03-23
  * **Breaking change:** Removed `RunEvent::CloseRequested` and `RunEvent::WindowClosed` and added `RunEvent::WindowEvent`. 
    * edad9f4f refactor(core): add `RunEvent::WindowEvent` (#3793) on 2022-03-28
  * **Breaking change:** Removed `window_label` from `RunEvent::ExitRequested`. 
    * 9ddf8d84 fix(core): properly fire `WindowEvent::Destroyed`, closes #3688 (#3778) on 2022-03-28
  * **Breaking change:** The `tauri://` events are no longer emitted to listeners using `Window::listen`. Use the `App::run` closure, `Window::on_window_event` and `Window::on_menu_event` instead. 
    * 5d538ec2 refactor(core): use the event loop proxy to send updater events (#3687) on 2022-03-15
  * The `App::setup` closure can now return a boxed error directly. 
    * da1e8793 feat(core): improve and cleanup the `Error` enum (#3748) on 2022-03-22
  * Implement `Debug` for `tauri::State`. 
    * 0b49dd56 impl Debug for State closes #3676 (#3677) on 2022-03-12
  * **Breaking change:** The `Manager::manage` function now returns a bool indicating whether the type is already managed or not. 
    * 263b45e1 refactor(core): return boolean on `Manager::manage` (#3682) on 2022-03-13
  * Set the `Access-Control-Allow-Origin` header on the `tauri` protocol response with the initial webview URL as value. 
    * 1730b1a5 feat(core): enable CORS on the tauri protocol (#3750) on 2022-03-22
  * **Breaking change:** The `tauri_runtime` crate is no longer exported since its API is not stable. 
    * 1099a969 refactor(core): do not export `tauri_runtime` on `tauri` (#3749) on 2022-03-22
  * Added `Temp` to the `BaseDirectory` enum. 
    * 266156a0 feat(core): add `BaseDirectory::Temp` and `$TEMP` variable (#3763) on 2022-03-24
  * Added `$TEMP` to the allowed variables to the filesystem and asset protocol scopes. 
    * 266156a0 feat(core): add `BaseDirectory::Temp` and `$TEMP` variable (#3763) on 2022-03-24
  * Update `wry` to `0.14` and `tao` to `0.7`. 
    * f2d24ef2 chore(deps): update wry (#1482) on 2021-04-14
    * e267ebf1 Apply Version Updates From Current Changes (#1486) on 2021-04-14
    * 5fb74332 chore(deps): update wry to 0.14, tao to 0.7 (#3790) on 2022-03-28
  * Added `updater` method to `App` and `AppHandle`, a builder to check for app updates. 
    * 4094494a feat(core): add API to manually trigger updater check (#3712) on 2022-03-17
    * c64268f9 feat(updater): expose builder, allow setting a custom version checker (#3792) on 2022-03-28
  * Allow using a custom updater version checker via `App::updater().should_install()`. 
    * c64268f9 feat(updater): expose builder, allow setting a custom version checker (#3792) on 2022-03-28
  * Added download progress events to the updater. 
    * f0db3f9b feat(updater): add download progress events (#3734) on 2022-03-18
  * Send updater events to the `App::run` closure. 
    * 5d538ec2 refactor(core): use the event loop proxy to send updater events (#3687) on 2022-03-15
  * Run the updater on startup even if no window was created. 
    * c4ca80f9 feat(core): use AppHandle instead of Window on the updater logic (#3702) on 2022-03-15
  * Properly fire the window destroyed event. 
    * 9ddf8d84 fix(core): properly fire `WindowEvent::Destroyed`, closes #3688 (#3778) on 2022-03-28
  * Added `close_devtools` and `is_devtools_open` APIs to the `Window` struct. 
    * e05d718a feat(core): add hotkey to toggle devtools, closes #3776 (#3791) on 2022-03-28
  * Added the `WindowEvent::FileDrop` variant. 
    * 07d1584c feat(core): add `WindowEvent::FileDrop`, closes #3664 (#3686) on 2022-03-13
  * Added a configuration flag for disallowing install downgrades on Windows. **Breaking change:** The default behavior on Windows is now to allow downgrades. 
    * 8b807e09 refactor(bundler): allow downgrades, add option to disallow on Windows (#3777) on 2022-03-27


© 2025 Tauri Contributors. CC-BY / MIT
