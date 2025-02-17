Skip to content
# tauri@1.3.0
ReturnView on GitHub
  * Added the `additional_browser_args` option when creating a window. 
    * 3dc38b15 feat(core): expose additional_browser_args to window config (fix: #5757) (#5799) on 2022-12-14
  * Fix passing `--profile` to cargo in `tauri build` causing conflict with `--release` passed by the CLI. 
    * bfa69691 fix(cli): detect `--profile`. closes #6255 (#6268) on 2023-02-18
  * Added the `content_protected` option when creating a window and `Window::set_content_protected` to change it at runtime. 
    * 4ab5545b feat: add content protection api, closes #5132 (#5513) on 2022-12-13
  * Fix serialization of js `Map` when used in `invoke`. 
    * d4d6a98d fix(core): convert js `Map` to object before serialization, closes #6078 (#6099) on 2023-01-19
  * Added `Window::on_navigation`. 
    * 3f35b452 Expose wry navigation_handler via WindowBuilder closes #4080 (#5686) on 2022-12-27
  * Sync `__TAURI_METADATA__.__windows` across all windows. 
    * 146a794c fix(core): sync windows metadata across all windows, closes #5571 (#5615) on 2022-12-27
  * Fix `UpdaterBuilder::check` returning a parsing error when `204` is sent from server where it should instead return a `UpToDate` error. 
    * eb1ec041 fix(core/updater): read and parse response after checking status code, closes #6192 (#6575) on 2023-03-31
  * Added `OkWithLabel` and `OkCancelWithLabels` variants to the `api::dialog::MessageDialogButtons` enum to set the text of the dialog buttons. 
    * 00e1efaa feat: customize button texts of message dialog (#4383) on 2022-12-28
  * Added `Builder::device_event_filter` and `App::set_device_event_filter` methods. 
    * 73fd60ee expose set_device_event_filter in tauri (#5562) on 2022-12-13
  * Fix resize glitch when double clicking a custom titlebar in the top resize area. 
    * 4892637f fix: Resizing glitch on custom titlebar click (closes #2549) (#5966) on 2023-01-04
  * Fixes tray events not being delivered. 
    * 138cb8d7 fix(tauri-runtime-wry): tray event listener not registered (#6270) on 2023-02-14
  * Fix the filesystem scope allowing sub-directories of the directory picked by the dialog when `recursive` option was `false`. 
    * 72389b00 Merge pull request from GHSA-6mv3-wm7j-h4w5 on 2022-12-22
  * Add `is_minimized()` window method. 
    * 62144ef3 feat: add is_minimized (fix #3878) (#5618) on 2022-12-13
  * Bump minimum supported Rust version to 1.60. 
    * 5fdc616d feat: Use the zbus-backed of notify-rust (#6332) on 2023-03-31
  * Update the `open` crate to v3.2 to fix an URL encoding bug on Windows. 
    * 708efbd9 fix(core/tauri): upgrade `open` to 3.2 to fix a bug on Windows (#6441) on 2023-04-06
  * Added support to `mailto:` and `tel:` links on the shell API. 
    * d0d873e3 feat(core): add support to mailto: and tel: links, closes #5521 (#5544) on 2022-12-12
  * Pin `os_info` to `=3.5`. 
    * a8d640b3 fix(core): pin unarray and os_info (#6212) on 2023-02-07
  * Pin raw-window-handle to 0.5.0 to keep MSRV. 
    * c46c09f3 fix(deps): pin raw-window-handle to 0.5.0 (#6480) on 2023-03-17
  * Pin `time` to `0.3.15`. 
    * 3d16461b fix(core): pin time to 0.3.15 (#6312) on 2023-02-19
  * Added configuration to specify remote URLs allowed to access the IPC. 
    * ee71c31f feat(core): allow configuring remote domains with IPC access, closes #5088 (#5918) on 2023-04-11
  * Add `title` getter on window. 
    * 233e43b0 feat: add `title` getter on window, closes #5023 (#5515) on 2022-12-13
  * Implement `SystemTray::with_tooltip` and `SystemTrayHandle::set_tooltip` for Windows and macOS. 
    * 2265e097 feat(windows): implement `with_tooltip` (#5938) on 2023-01-01
  * Added window’s `url()` getter. 
    * d17027e1 feat: expose url method (#5914) on 2022-12-26
  * On Windows, change webview theme based on Window theme for more accurate `prefers-color-scheme` support. 
    * 7a8d570d fix: sync webview theme with window theme on Windows, closes #5802 (#5874) on 2022-12-27
  * Add a method to the `WindowBuilder` struct to recreate windows from tauri.conf.json configurations. 
    * 49dff27e feat(core): create WindowBuilder from WindowConfig (#6073) on 2023-01-17
  * On Windows, Fix missing `WindowEvent::Focused` in `App::run` callback. 
    * ff4ea1ea fix: dispatch focus event to app.run on Windows, closes #6460 (#6504) on 2023-03-31
  * Pin `winnow` crate to 0.4.1 to keep the 1.60 MSRV.


© 2025 Tauri Contributors. CC-BY / MIT
