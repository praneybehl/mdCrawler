Skip to content
# tauri@1.0.1
ReturnView on GitHub
  * Added `fn new` constructors for `PhysicalSize`, `LogicalSize`, `PhysicalPosition` and `LogicalPosition` and missing conversion methods. 
    * c7d13a1c feat(core): add missing methods to the dpi module (#4393) on 2022-06-19
  * Set the bundle name and app metadata in the Info.plist file in development mode. 
    * 38f5db6e feat(codegen): fill app metadata in development Info.plist on 2022-06-21
  * Set the application icon in development mode on macOS. 
    * 307c2ebf feat(core): set macOS app icon in development (#4385) on 2022-06-19
  * Fixes the error message when using the `window.unminimize` API without enabling it in the allowlist. 
    * cbceb7d6 fix: some typos (#4403) on 2022-06-19
  * Initialize Tauri script when `devPath` is an external URL with path. 
    * 079b1cc0 fix(core): properly get external URL origin, closes #4414 (#4417) on 2022-06-21
  * Fixes deadlock when a plugin window ready event needs to block the thread waiting on the event loop. 
    * 9d33d093 fix(core): deadlock on plugin webview ready hook (#4462) on 2022-06-24
  * Adjust the updater to fallback to `$HOME/.cache` or the current working directory as temp directory if the system default is in a different mount point. 
    * fd125f76 fix(updater): fallback if tmp is on different mount point, closes #4500 (#4504) on 2022-06-28
  * Properly fill the origin window when using `emit_to` and `emit_all` from `Window`. 
    * 643ae846 fix: fire window-specific event on Window emit_to/emit_all, closes #4493 (#4498) on 2022-06-28
  * Implement `raw_window_handle::HasRawWindowHandle` on Linux. 
    * 3efbc67f feat: implement `raw_window_handle` on Linux (#4469) on 2022-06-26
  * Added `on_drop` hook to the `plugin::Builder`. 
    * be4bb391 feat: add `AppHandle::remove_plugin` and plugin `on_drop`, closes #4361 (#4443) on 2022-06-23
  * Refactored the `tauri-runtime-wry` plugin interface. 
    * e39e2999 refactor(tauri-runtime-wry): enhance plugin interface (#4476) on 2022-06-27
  * Added `AppHandle::remove_plugin`. 
    * be4bb391 feat: add `AppHandle::remove_plugin` and plugin `on_drop`, closes #4361 (#4443) on 2022-06-23
  * The theme API is now implemented on macOS 10.14+. 
    * 6d94ce42 feat(core): theme is now implemented on macOS (#4380) on 2022-06-17
  * Suppress unused variable warning in release builds. 
    * 45981851 chore(lint): unused variable warnings for release builds (#4411) on 2022-06-22
  * Update tao to 0.12 and wry to 0.19. 
    * f6edc6df chore(deps): update tao to 0.12, wry to 0.19, closes #3220 (#4502) on 2022-06-28
  * Added `Notification::notify` API behind the `windows7-compat` Cargo feature, which includes Windows 7 support. 
    * 57039fb2 fix(core): add windows 7 notification support (#4491) on 2022-06-28


© 2025 Tauri Contributors. CC-BY / MIT
