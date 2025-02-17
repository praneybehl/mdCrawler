Skip to content
# tauri@1.0.0-beta.2
ReturnView on GitHub
  * Remove anonymous lifetimes on examples.
    * c1f8e113 chore: remove unnecessary anonymous lifetimes (#1829) on 2021-05-14
  * Moves `shell`, `dialog::FileDialogBuilder` and `process::Command` APIs behind their allowlist feature flags.
    * aab3e1f1 refactor(core): move api modules behind allowlist feature flags (#1864) on 2021-05-19
  * Adds `create_window` API to the `AppHandle` struct.
    * 95d518af feat(core): expose `AppHandle`, add `create_window` API (#1855) on 2021-05-18
  * Adds a `handle` function to the `App` struct, which returns a `Send` handle to the app instance.
    * 95d518af feat(core): expose `AppHandle`, add `create_window` API (#1855) on 2021-05-18
  * Use `attohttpc` on the HTTP API by default for bundle size optimization. `reqwest` is implemented behind the `reqwest-client` feature flag.
    * 17c7c439 refactor(core): use `attohttpc` by default (#1861) on 2021-05-19
  * Kill child processes spawned with `tauri::api::process::Command` on `tauri::App` drop. Can be skipped with `tauri::Builder#skip_cleanup_on_drop`.
    * 4bdc4066 feat(core): kill sidecar child processes on App drop, closes #1896 (#1932) on 2021-06-01
  * Adds `clipboard` APIs (write and read text).
    * 285bf64b feat(core): add clipboard writeText and readText APIs (#2035) on 2021-06-21
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Allow accessing an `AppHandle` instance on a command through dependency injection.
    * 59784c7e feat(core): implement `CommandArg` for `AppHandle` (#2037) on 2021-06-21
  * Fixes child processes messages not arriving until the subprocess is terminated.
    * df21ffc6 fix(core): command mpsc usage, closes #1935 (#1936) on 2021-06-01
  * Adds `config` and `package_info` getters to the `App` and `AppHandle` structs.
    * 70fc87a7 feat(core): add `config` and `package_info` getters on App and AppHandle (#2016) on 2021-06-20
  * Expose mutable getters for the rest of the public `Context` getters.
  * `pub fn assets_mut(&amp;mut self) -&gt; &amp;mut Arc&lt;A&gt;`
  * `pub fn default_window_icon_mut(&amp;mut self) -&gt; &amp;mut Option&lt;Vec&lt;u8&gt;&gt;`
  * `pub fn system_tray_icon_mut(&amp;mut self) -&gt; &amp;mut Option&lt;Icon&gt;`
  * `pub fn package_info_mut(&amp;mut self) -&gt; &amp;mut tauri::api::PackageInfo`
  * 754c2e76 feat(core): finish mutable getters for `Context` (#1814) on 2021-05-13
  * Adds `request_user_attention` API to the `Window` struct.
    * 7dcca6e9 feat(core): add `request_user_attention` API, closes #2023 (#2026) on 2021-06-20
  * Adds `show`, `hide`, `is_visible` and `toggle` APIs to the `MenuHandle`.
    * 954460c5 feat(core): MenuHandle `show`, `hide`, `is_visible` and `toggle` APIs (#1958) on 2021-06-15
  * Allow `dev_path` and `dist_dir` to be an array of root files and directories to embed.
    * 6ec54c53 feat(core): allow `dev_path`, `dist_dir` as array of paths, fixes #1897 (#1926) on 2021-05-31
  * Validate `tauri.conf.json &gt; build &gt; devPath` and `tauri.conf.json &gt; build &gt; distDir` values.
    * e97846aa feat(core): validate `devPath` and `distDir` values (#1848) on 2021-05-17
  * Set the Tauri window as parent for dialogs.
    * abf78c58 fix(core): set parent window handle on dialogs, closes #1876 (#1889) on 2021-05-21
  * Fallback to `index.html` on asset loading so router with history mode works.
    * 8a7921e5 fix(core): fallback to index.html on asset loading, closes #2020 #2021 (#2022) on 2021-06-20
  * Fixes custom protocol asset loader not decoding the percent-encoded path.
    * c021968e fix(core): asset loading not decoding percent-encoded path, closes #1879 (#1938) on 2021-06-01
  * As some frameworks automatically add “true” as the value of the attribute, we need to check if it exists instead.
    * 23707764 Drag region attribute check (#1907) on 2021-05-30
  * Fixes build without the dialog Cargo features.
    * 49fb3b72 fix(core): build without dialog Cargo features (#1973) on 2021-06-09
  * Allow disabling the webview file drop handler (required to use drag and drop on the frontend on Windows) using the `tauri.conf.json &gt; tauri &gt; windows &gt; fileDropEnabled` flag or the `WebviewAttributes#disable_file_drop_handler` method.
    * 9cd10df4 feat(core): allow disabling file drop handler, closes #2014 (#2030) on 2021-06-21
  * Fixes the HTTP API binary response serialization.
    * 47f75584 fix(core): resolve HTTP API on non-ok status code, fix binary response, closes #2046 (#2053) on 2021-06-23
  * The `http` APIs now resolve the returned promise when the API call finishes with an error status code.
    * 47f75584 fix(core): resolve HTTP API on non-ok status code, fix binary response, closes #2046 (#2053) on 2021-06-23
  * Run the `notification.show()` method on a dedicated async task to prevent a panic on Windows.
    * 86d0aaa0 fix(core): notification panic on Windows, closes #917 (#2011) on 2021-06-19
  * Fixes HTTP API headers being overwritten when using the `reqwest` client.
    * 1006c1cf fix(core): HTTP headers being overwritten by reqwest, closes #2032 (#2036) on 2021-06-21
  * Remove closed window from the `window.__TAURI__.__windows` array, used by the `window.getAll` API from `@tauri-apps/api`.
    * ebaa33cb fix(core): remove closed window from `window.__TAURI__.__windows` (#2057) on 2021-06-23
  * Panic on window getters usage on the main thread when the event loop is not running and document it.
    * ab3eb44b fix(core): deadlock on window getters, fixes #1893 (#1998) on 2021-06-16
  * Adds `focus` API to the WindowBuilder.
    * 5f351622 feat(core): add focus API to the WindowBuilder and WindowOptions, #1737 on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * **Breaking change:** The global shortcut API is now managed by `tao` so it cannot be accessed globally, the manager is now exposed on the `App` and `AppHandle` structs.
    * 3280c4aa refactor(core): global shortcut is now provided by `tao` (#2031) on 2021-06-21
  * Hide `phf` crate export (not public API).
    * cd1a299a chore(core): hide phf, closes #1961 (#1964) on 2021-06-09
  * (internal): allow `wry` dependency to be optional again while keeping default args. code that wishes to expose a struct with a default arg should use the `crate::manager::default_args!` macro to declare the struct, so that it can automatically feature-gate `DefaultArgs` behind using `wry`.
    * 3d8dcbbf fix(core): allow wry to be an optional dep again (fix #1841) (#1854) on 2021-05-17
  * Adds `is_decorated` getter on Window.
    * f58a2114 feat(core): add `is_decorated` Window getter on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Adds `is_resizable` getter on Window.
    * 1e8af280 feat(core): add `is_resizable` Window getter on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Adds `is_visible` getter on Window.
    * 36506c96 feat(core): add `is_visible` API on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Read `tauri.conf.json &gt; tauri &gt; bundle &gt; icons` and use the first `.png` icon as window icon on Linux. Defaults to `icon/icon.png` if a PNG icon is not configured.
    * 40b717ed feat(core): set window icon on Linux, closes #1922 (#1937) on 2021-06-01
  * Adds `accelerator` method to the `CustomMenuItem` struct to define a keyboard shortcut for the menu item.
    * 034c2601 feat(core): add `accelerator` method to `CustomMenuItem` (#2043) on 2021-06-22
  * **Breaking change:** The `menu` API was not designed to have all the new features: submenus, item updates, disabled state… so we broke it before going to stable.
    * f7e9fe8f refactor(core): new system tray and window menu APIs, closes #1898 (#1944) on 2021-06-04
  * Adds a `PathResolver` struct to simplify the usage of the `tauri::api::path::{app_dir, resource_dir}` APIs, accessible through the `App` and `AppHandle` `path_resolver` methods.
    * 5ca462f6 feat(core): add path resolver API to the App and AppHandle structs (#2015) on 2021-06-19
  * Removes `image` dependency. For now only `.ico` icons on Windows are supported, and we’ll implement other types on demand to optimize bundle size.
    * 1be37a3f refactor(core): remove `image` dependency (#1859) on 2021-05-18
  * Remove window object from the `Manager` internal `HashMap` on close. This fixes the behavior of using `[App|AppHandle|Window]#get_window` after the window is closed (now correctly returns `None`).
    * 08c161c5 fix(core): remove window from HashMap on close (#2024) on 2021-06-20
  * Improve RPC security by requiring a numeric code to invoke commands. The codes are generated by the Rust side and injected into the app’s code using a closure, so external scripts can’t access the backend. This change doesn’t protect `withGlobalTauri` (`window.__TAURI__`) usage.
    * 160fb052 feat(core): improve RPC security, closes #814 (#2047) on 2021-06-22
  * Adds `run_iteration` API to the `App` and return the app instance on the `build` method of the `Builder`. The `run_iteration` method runs the window event loop step by step, allowing Tauri to be run along other applications.
    * 8c0d0739 feat(core): add `run_iteration`, `parent_window` and `owner_window` APIs, closes #1872 (#1874) on 2021-05-21
  * The `run_on_main_thread` API now uses WRY’s UserEvent, so it wakes the event loop.
    * 9bf82f0d fix(core): `run_on_main_thread` now wakes the event loop (#1949) on 2021-06-04
  * Adds `set_focus` API on Window.
    * bb6992f8 feat(core): add `set_focus` window API, fixes #1737 on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Adds `set_skip_taskbar` API on Window.
    * e06aa277 feat(core): add `set_skip_taskbar` API on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * Adds `skip_taskbar` API to the WindowBuilder.
    * 5525b03a feat(core): add `skip_taskbar` API to the WindowBuilder/WindowOptions on 2021-05-30
    * dee71ad5 fix(workflows): update docs workflow syntax (#2054) on 2021-06-23
  * **Breaking change:** The `system_tray` and `on_system_tray_event` APIs were not designed to have all the new features: submenus, item updates, click events, positioning… so we broke it before going to stable.
    * f7e9fe8f refactor(core): new system tray and window menu APIs, closes #1898 (#1944) on 2021-06-04
  * Fix loading url containing URI fragment
    * 07fd9a92 fix(core): add hash symbol in uri parse, closes #1943 (#1947) on 2021-06-05
  * Adds `Window#center` and `WindowBuilder#center` APIs.
    * 5cba6eb4 feat(core): add window `center` API, closes #1822 (#1954) on 2021-06-05
  * Adds window native handle getter (HWND on Windows).
    * abf78c58 fix(core): set parent window handle on dialogs, closes #1876 (#1889) on 2021-05-21


© 2025 Tauri Contributors. CC-BY / MIT
