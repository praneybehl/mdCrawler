Skip to content
# tauri@1.0.0-rc.7
ReturnView on GitHub
  * **Breaking change:** Removed `tauri::api::file::ArchiveFormat::Plain`. 
    * f7d3d93b refactor(core): improve performance of the `extract` API (#3963) on 2022-04-25
  * Fallback to `{path}.html` when `{path}` is not found in the Tauri custom protocol handler. 
    * 7864d41d feat(core): fallback to `{path}.html` in Tauri protocol loader ref #3887 (#3939) on 2022-04-21
  * **Breaking change:** Use ayatana-appindicator for Linux system tray by default. Use the `gtk-tray` Cargo feature to use `libappindicator` instead. 
    * f2a30d8b refactor(core): use ayatana appindicator by default, keep option to use gtk (#3916) on 2022-04-19
  * Reduce the amount of generated code for the API endpoints. 
    * c23f139b perf(core): improve binary size with api enum serde refactor (#3952) on 2022-04-24
  * *_Breaking change::_ Added the `clipboard` Cargo feature. 
    * 24e4ff20 refactor(core): add clipboard Cargo feature, enhancing binary size (#3957) on 2022-04-24
  * **Breaking change:** The process Command API stdio lines now includes the trailing `\r`. 
    * b5622882 fix(cli): exit on non-compilation Cargo errors, closes #3930 (#3942) on 2022-04-22
  * Expose Window cursor APIs `set_cursor_grab`, `set_cursor_visible`, `set_cursor_icon` and `set_cursor_position`. 
    * c54ddfe9 feat: expose window cursor APIs, closes #3888 #3890 (#3935) on 2022-04-21
  * **Breaking change:** The `tauri::api::file::Extract#extract_file` function has been moved to `tauri::api::file::Entry#extract`. 
    * f7d3d93b refactor(core): improve performance of the `extract` API (#3963) on 2022-04-25
  * **Breaking change:** The `tauri::api::file::Extract#files` function has been renamed to `with_files` for performance reasons. 
    * f7d3d93b refactor(core): improve performance of the `extract` API (#3963) on 2022-04-25
  * Improved the performance of the `tauri::api::fs::Extract` API. 
    * f7d3d93b refactor(core): improve performance of the `extract` API (#3963) on 2022-04-25
  * Fixes a panic when using the `create_tao_window` API. 
    * 320329a9 fix(core): insert to webview_id_map on tao window creation, closes #3883 (#3932) on 2022-04-21
  * Fixes the HTTP API form text fields. 
    * cc356084 fix(core): do not serialize strings in http api form, closes #3910 (#3928) on 2022-04-20
  * Set the application bundle identifier for the notifications on macOS. 
    * f67ae6bd fix(core): set bundle id for notifications on macOS (#3839) on 2022-04-01
  * Fixes a panic when a menu event is triggered when all windows are minimized on macOS. 
    * 70ff55c1 fix(core): panic on menu event with minimized windows, closes #3902 (#3918) on 2022-04-20
  * Fixes a rendering issue when resizing the window with the devtools open. 
    * 80b714af fix: rendering issue when resizing with devtools open closes #3914 #3814 (#3915) on 2022-04-19
  * Fixes the `WindowBuilder` export. 
    * 985d2508 fix(tauri): export `WindowBuilder` struct instead of trait, closes #3827 (#3833) on 2022-03-31
  * The HTTP API now supports `multipart/form-data` requests. You need to set the `Content-Type` header and enable the `http-multipart` Cargo feature. 
    * 1397d912 feat(core): add support to multipart/form-data requests, closes #2118 (#3929) on 2022-04-22
  * *_Breaking change::_ Added the `global-shortcut` Cargo feature. 
    * e11878bc refactor(core): add global-shortcut Cargo feature, enhancing binary size (#3956) on 2022-04-24
  * Added `tauri::api::http::HttpRequestBuilder#header` method. 
    * 81705bb3 feat(updater): add method to set request headers closes #3896 (#3931) on 2022-04-22
  * **Breaking change:** The `tauri::api::http::HttpRequestBuilder#headers` method now takes `header::HeaderMap` instead of a `HashMap`. 
    * 81705bb3 feat(updater): add method to set request headers closes #3896 (#3931) on 2022-04-22
  * **Breaking change:** The `tauri::api::http::Response#headers` method now returns `&amp;header::HeaderMap` instead of `&amp;HashMap`. 
    * 81705bb3 feat(updater): add method to set request headers closes #3896 (#3931) on 2022-04-22
  * **Breaking change:** The `api::http` timeouts are now represented as `std::time::Duration` instead of a `u64`. 
    * 0ecfad59 refactor(updater): unset request timeout, add builder setter (#3847) on 2022-04-02
  * **Breaking change:** The `tauri::api::http::FormPart::Bytes` enum variant has been renamed to `File` with a value object `{ file, mime, file_name }`. 
    * 1397d912 feat(core): add support to multipart/form-data requests, closes #2118 (#3929) on 2022-04-22
  * **Breaking change:** Removed `App::create_window`, `AppHandle::create_window`, `Builder::create_window` and `Window::create_window`. 
    * 7c7d854a refactor(core): remove deprecated APIs (#3834) on 2022-04-01
  * **Breaking change:** Removed `tauri::api::http::FormPart::File`. 
    * cc356084 fix(core): do not serialize strings in http api form, closes #3910 (#3928) on 2022-04-20
  * Added `WindowEvent::ThemeChanged(theme)`. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21
  * Added `theme` getter on `Window`. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21
  * Added `UpdateResponse::body` and `UpdateResponse::date`. 
    * c7696f34 feat(updater): add `body` and `date` getters (#3802) on 2022-03-29
  * **Breaking change** : Removed the `tauri::updater::Error::UnsupportedPlatform` variant and added `UnsupportedLinuxPackage`, `UnsupportedOs` and `UnsupportedArch` for better error information. 
    * ed716793 refactor(updater): improve unsupported error variants, closes #3817 (#3849) on 2022-04-05
  * Add updater `Downloaded` status event. 
    * 9712ed1a feat(updater): add `Downloaded` status event (#3804) on 2022-04-01
  * Allow setting app updater request headers via `AppHandle::updater().header()`. 
    * 81705bb3 feat(updater): add method to set request headers closes #3896 (#3931) on 2022-04-22
  * The updater default timeout is now unset, and the `UpdateBuilder` has a `timeout` setter. 
    * 0ecfad59 refactor(updater): unset request timeout, add builder setter (#3847) on 2022-04-02
  * Added `theme` setter to the WindowBuilder. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21


© 2025 Tauri Contributors. CC-BY / MIT
