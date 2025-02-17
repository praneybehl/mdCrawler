Skip to content
# tauri@1.0.0-rc.12
ReturnView on GitHub
  * Expose option to set the dialog type. 
    * f46175d5 feat(core): expose option to set dialog type, closes #4183 (#4187) on 2022-05-21
  * Expose `title` option in the message dialog API. 
    * ae99f991 feat(core): expose message dialog’s title option, ref #4183 (#4186) on 2022-05-21
  * Immediately create windows when using `tauri::App` as manager. 
    * 52d17754 fix(core): immediately create window when using tauri::App, closes #4170 (#4172) on 2022-05-21
  * Account the monitor position when centering a window. 
    * a7a9fde1 fix(core): account for monitor position when centering window (#4166) on 2022-05-21
  * Allow the canonical, absolute form of a path for the filesystem scope on Windows if `std::fs::canonicalize` returns a path, fallback to `\\?\$PATH`. 
    * 78f2565e fix: allow return value of fs::canonicalize on fs scope, closes #4130 (#4188) on 2022-05-21
  * Fixes updater documentation not showing on docs.rs. 
    * 55892c35 fix(core): updater documentation not showing on docs.rs (#4190) on 2022-05-22
  * Fixes HTTP timeout not working on Windows when using the `attohttpc` client. 
    * d99c5d58 fix(core): HTTP timeout not working on Windows, closes #4050 (#4185) on 2022-05-21
  * Update `windows-rs` to `0.37.0`, which requires Rust 1.61.0+. 
    * 2326be39 feat(core): update windows-rs to 0.37.0 (#4199) on 2022-05-24
  * **Breaking change:** The `WindowBuilder` struct now has a lifetime annotation `WindowBuilder&lt;R: Runtime, &#39;a&gt;`. 
    * 52d17754 fix(core): immediately create window when using tauri::App, closes #4170 (#4172) on 2022-05-21


© 2025 Tauri Contributors. CC-BY / MIT
