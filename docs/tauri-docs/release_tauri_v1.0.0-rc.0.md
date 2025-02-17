Skip to content
# tauri@1.0.0-rc.0
ReturnView on GitHub
  * The dialog allowlist now includes flags for the `message`, `ask` and `confirm` APIs. 
    * d660cab3 feat: enhance allowlist configuration [TRI-027] (#11) on 2022-01-09
  *     * **Breaking change:** Renamed `tauri::Event` to `tauri::RunEvent`
  * Exported `tauri::Event` and `tauri::EventHandler` so you can define a function and pass it to `Window::listen`
  * 15358b18 Expose event interface. fixes #2733 (#3321) on 2022-02-04
  * The `tauri::api` modules `http`, `notification`, `dialog`, and `process::Command` APIs are now hidden behind a feature flag, `http-api`, `notification`, `dialog` and `command`, respectively. 
    * 6feb5a0c refactor(core): api feature flags, documentation (#26) on 2022-01-09
  * Add `title` option to file open/save dialogs. 
    * e1d6a6e6 Create api-file-dialog-title.md (#3235) on 2022-01-16
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Added `any_thread()` to the `tauri::Builder` to run applications on any thread (only exposed on Linux and Windows). 
    * af44bf81 feat(core): allow app run on any thread on Linux & Windows, closes #3172 (#3353) on 2022-02-07
  * Enable CORS on the `asset` protocol. 
    * d28ac8aa fix(core): enable CORS on the `asset` protocol, closes #2965 (#2974) on 2021-12-09
  * The `asset://` custom protocol is only defined when either the `api-all`, `protocol-all` or `protocol-asset` feature flags are enabled. These feature flags are accessible with the `tauri.conf.json` allowlist. 
    * 7920ff14 feat: scope the `fs` API and the `asset` protocol [TRI-026] [TRI-010] [TRI-011] (#10) on 2022-01-09
  * Expose the `asset_resolver` API on the `App` and `AppHandle` structs. 
    * 7c6c7adc feat(core): add `asset_resolver` API (#2879) on 2021-11-12
  * **Breaking change:** Refactored the types returned from the `async_runtime` module. 
    * a3537078 feat(core): allow running along another tokio runtime, closes #2838 (#2973) on 2021-12-08
  * Added `tauri::async_runtime::set` method, allowing to share your tokio runtime with Tauri. 
    * a3537078 feat(core): allow running along another tokio runtime, closes #2838 (#2973) on 2021-12-08
  * Added `tauri::async_runtime::spawn_blocking` API. 
    * a3537078 feat(core): allow running along another tokio runtime, closes #2838 (#2973) on 2021-12-08
  * The `callback` and `error` invoke fields, along with other `transformCallback` usages, are now validated to be numeric. 
    * a48b8b18 feat(core): validate callbacks and event names [TRI-038] [TRI-020] (#21) on 2022-01-09
  * Change `Error::ParseCliArguments(clap::Error)` to `Error::ParseCliArguments(String)` because `clap::Error` is not `Send`. 
    * 1f988535 chore(deps) Update Tauri Core (#2480) on 2021-08-24
  * The `api::process::Command` APIs are now hidden behind the `command` feature flag. 
    * eed01728 feat(core): add `shell &gt; sidecar` allowlist and `process` feature flag [TRI-037] (#18) on 2021-10-24
  * Add `tauri::api::path::log_dir` function to access the suggested log directory path. 
    * acbb3ae7 feat: add Log directory (#2736) on 2021-10-16
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * The `process`, `path` and `updater` APIs now takes a `tauri::Env` argument, used to force environment variables load on startup to prevent env var update attacks. 
    * 7209fdf7 refactor(core): load APPIMAGE and APPDIR env vars on startup [TRI-007] [TRI-041] on 2022-01-09
  * Now `resolve()`, `join()` and `normalize()` from the `path` module, won’t throw errors if the path doesn’t exist, which matches NodeJS behavior. 
    * fe381a0b fix: `join` no longer cares if path doesn’t exist, closes #2499 (#2548) on 2021-09-21
  * **Breaking change:** Return `Window` on `App` and `AppHandle`’s `create_window` function. 
    * e15a8af8 refactor(core): return `Window` on `create_window` API (#3211) on 2022-01-13
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Apply `nonce` to `script` and `style` tags and set them on the `CSP` (`script-src` and `style-src` fetch directives). 
    * cf54dcf9 feat: improve `CSP` security with nonces and hashes, add `devCsp` [TRI-004] (#8) on 2022-01-09
  * The path returned from `tauri::api::process::current_binary` is now cached when loading the binary. 
    * 7c3db7a3 cache current binary path much sooner (#45) on 2022-02-01
  * Added an API to use a custom invoke system to receive and respond to commands (`Builder#invoke_system`). 
    * 15164d93 feat(core): allow defining a custom invoke system (#2899) on 2021-11-16
  * Inject configured `CSP` on `data:` URLs. 
    * 8259cd64 feat(core): inject `CSP` on data URLs [TRI-049] (#16) on 2022-01-09
  * Emit `tauri://*` events to Rust listeners. 
    * 4c4ab1eb fix(core): trigger `tauri://*` events to Rust listeners, closes #2901 (#2902) on 2021-11-16
  * Emit `tauri://window-created` event for windows created on the backend. 
    * 1dbd887a fix(core): emit tauri://window-created event for windows created on Rust (#3299) on 2022-02-04
  * Enable non-session cookie persistence on Linux. 
    * d7c02a30 feat(core): persist non-session cookies on Linux (#3052) on 2021-12-09
  * Expose `tauri::api::ipc::{serialize_js_with, serialize_js}` functions. 
    * 5a94200f feat(core): expose functions to serialize `serde::Serialize` values to JS (#3354) on 2022-02-07
  * Resolve `asset` protocol HTTP request instead of panicking if the file does not exist or cannot be read. 
    * 03fc92c8 fix(core): resolve request instead of panicking on asset protocol (#3347) on 2022-02-06
  * Avoid `async_runtime::block_on` panics when used along another tokio runtime. 
    * a3537078 feat(core): allow running along another tokio runtime, closes #2838 (#2973) on 2021-12-08
  * Prevent window closing if `tauri://close-requested` is listened on the JS layer. Users must call `appWindow.close()` manually when listening to that event. 
    * 74dff536 fix(core): emit `tauri://close-requested` to JS, closes #2996 (#3041) on 2021-12-09
  * Fixes a deadlock when creating a window from a menu event handler. 
    * 9c82006b fix(core): deadlock when creating window from menu handler, closes #3110 (#3126) on 2021-12-28
  * Fixes the dialog `defaultPath` usage on Linux. 
    * 2212bd5d fix: dialog default path on Linux, closes #3091 (#3123) on 2021-12-27
  * Fixes `WindowEvent::Focus` and `WindowEvent::Blur` events not firing. 
    * 3b33d67a fix: re-adding focus/blur events for linux and macos (fix #2485) (#2489) on 2021-08-24
  * Fixes `tauri://focus` and `tauri://blur` events not firing. 
    * 3b33d67a fix: re-adding focus/blur events for linux and macos (fix #2485) (#2489) on 2021-08-24
  * Use webview’s inner_size instead of window’s value to get the correct size on macOS. 
    * 4c0c780e fix(core): window’s inner_size usage, closes #2187 (#2690) on 2021-09-29
  * Fixes resource directory resolution on Linux. 
    * 1a28904b fix(core): resource path resolution on Linux, closes #2493 on 2021-08-22
  * Fixes the menu id mapping not reflecting the current window. 
    * ac37b56e fix(core): menu id map not reflecting the current window menu (#2726) on 2021-10-08
  * `Manager::once_global` and `Window::once` allow `FnOnce` callbacks. 
    * d5400a3d `once_global` and `once` accept FnOnce callbacks (#3383) on 2022-02-10
  * Properly check if document is loaded before invoking commands. 
    * 000d126e fix(core): properly check if document is loaded, closes #2716 (#2900) on 2021-11-16
  * Initialize system tray before windows so `tray_handle` can be accessed on command handlers. 
    * dbe0d21b fix(core): initialize system tray before app windows on 2021-08-31
  * Reimplement `remove_system_tray` on Windows to drop the `SystemTray` to run its cleanup code. 
    * a03b8554 fix(core): tray not closing on Windows (#3351) on 2022-02-07
  * Immediately listen to `tauri://window-created` event to catch it before the application triggers it. 
    * 878b8b9a fix(core): immediately listen to window-created, closes #3297 (#3298) on 2022-02-04
  * The `tauri::Window#emit` function now correctly sends the event to all windows that has a registered listener. **Breaking change:** `Window#emit_and_trigger` and `Window#emit` now requires the payload to be cloneable. 
    * 9b340552 fix(core): window-specific event delivery, closes #3302 (#3344) on 2022-02-06
  * Allow using a fixed version for the Webview2 runtime via the `tauri &gt; bundle &gt; windows &gt; webviewFixedRuntimePath` config option. 
    * 85df94f2 feat(core): config for fixed webview2 runtime version path (#27) on 2021-11-02
  * The updater `pubkey` is now a required field for security reasons. Sign your updates with the `tauri signer` command. 
    * d95cc831 feat: enforce updater public key [TRI-015] (#42) on 2022-01-09
  * `tauri::api::HttpRequestBuilder::new` now returns a `Result` to validate the url. 
    * 0ad1c651 feat(core): add `http` allowlist scope [TRI-008] (#24) on 2021-10-29
  * Added the `isolation` pattern. 
    * d5d6d2ab Isolation Pattern (#43) Co-authored-by: Ngo Iok Ui (Wu Yu Wei) <wusyong9104@gmail.com> Co-authored-by: Lucas Fernandes Nogueira <lucas@tauri.app> on 2022-01-17
  * Added `abort` method to `tauri::async_runtime::JoinHandle`. 
    * ad169759 feat: Add JoinHandle::abort() (#2877) on 2021-11-13
  * Adds support for using JSON5 format for the `tauri.conf.json` file, along with also supporting the `.json5` extension.


Here is the logic flow that determines if JSON or JSON5 will be used to parse the config:
  1. Check if `tauri.conf.json` exists a. Parse it with `serde_json` b. Parse it with `json5` if `serde_json` fails c. Return original `serde_json` error if all above steps failed
  2. Check if `tauri.conf.json5` exists a. Parse it with `json5` b. Return error if all above steps failed
  3. Return error if all above steps failed


  * 995de57a Add seamless support for using JSON5 in the config file (#47) on 2022-02-03
  * Allow preventing opening the default browser on a click on an `&lt;a target=&quot;_blank&quot;&gt;` element via `stopImmediatePropagation()`. 
    * 10e3190f fix(core): do not use capture on _blank link event handler, closes #2791 (#3349) on 2022-02-07
  * The `run_return` API is now available on Linux. 
    * 8483fde9 feat(core): expose `run_return` on Linux (#3352) on 2022-02-07
  * Allow window, global shortcut and clipboard APIs to be called on the main thread. 
    * 2812c446 feat(core): window, shortcut and clipboard API calls on main thread (#2659) on 2021-09-26
    * d24fd8d1 feat(tauri-runtime-wry): allow window creation and closing on the main thread (#2668) on 2021-09-27
  * Add `Menu::with_items` constructor, taking an iterator of `MenuEntry`. 
    * 7cc95e10 feat(core): add `Menu::with_items`, closes #2807 (#2966) on 2021-12-27
  * The updater now expects signatures created with the latest CLI release. 
    * c2a6e8d7 chore(deps) Update Tauri Core (#2746) on 2021-10-13
  * Change event loop callbacks definition to allow callers to move in mutable values. 
    * bdbf905e Transformed event-loop callback to FnMut to allow mutable values (#2667) on 2021-09-27
  * Fixes `Notification.requestPermission()` deadlock. 
    * 48f3768c fix(core): `Notification.requestPermission()` deadlock regression on 2021-08-24
  * Added `Window#open_devtools` API. 
    * 55aa22de feat(core): add `Window#open_devtools` API, closes #1213 (#3350) on 2022-02-07
  * Add a `plugin::Builder` struct to make plugin creation more convenient. 
    * 9aed2996 feat: `plugin::Builder` closes #2959 (#3005) on 2022-02-07
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Added `on_event` on the `Plugin` trait, which allows a plugin to react to the event loop. 
    * cc2f39a2 feat(core): add `on_event` hook on the `Plugin` trait (#2656) on 2021-09-26
  * Prevent path traversal on the file system APIs. 
    * 4d89f60d refactor(core): prevent path traversal [TRI-012] (#35) on 2021-12-06
  * **Breaking change:** Add `macos-private-api` feature flag, enabled via `tauri.conf.json &gt; tauri &gt; macOSPrivateApi`. 
    * 6ac21b3c feat: add private api feature flag (#7) on 2022-01-09
  * Add `raw_headers` to `tauri::api::http::ResponseData`. 
    * b7a2345b feat(core): add raw headers to HTTP API, closes #2695 (#3053) on 2022-01-07
  * Implement `raw_window_handle::RawWindowHandle` for `tauri::Window` on `Windows` and `macOS`. The `tauri::api::dialog::window_parent` function was removed since now you can use the window directly. 
    * e98c1af4 feat(core): expose message dialog APIs, fix window.confirm, implement HasRawWindowHandle for Window, closes #2535 (#2700) on 2021-10-02
  * Refactor `create_tao_window` API to return `Weak&lt;Window&gt;` instead of `Arc&lt;Window&gt;`. 
    * c1494b35 refactor: return Weak<Window> on create_tao_window on 2021-08-31
  * Added the `tauri::api::dialog::blocking` module. 
    * 4818531a refactor(core): add blocking dialog APIs, improve docs, closes #3255 (#3270) on 2022-02-05
  * The notification endpoint now checks for the permission flag and requests if the value is not set. 
    * 239bba56 refactor(core): check notification permission on the Rust endpoint [TRI-017] (#23) on 2022-01-09
  * **Breaking change:** The `WindowEvent::CloseRequested` variant now includes `label` and `signal_tx` fields to allow preventing closing the window. 
    * 74dff536 fix(core): emit `tauri://close-requested` to JS, closes #2996 (#3041) on 2021-12-09
  * **Breaking change:** Move `__currentWindow` and `__windows` values from `window.__TAURI__` to `window.__TAURI_METADATA__`. 
    * f5109e0c fix(api): window label null instead of actual value, closes #3295 (#3332) on 2022-02-04
  * Remove the `BaseDirectory::Current` enum variant for security reasons. 
    * 696dca58 refactor(core): remove `BaseDirectory::Current` variant on 2022-01-26
  * **Breaking change:** Remove default webview window when `tauri.conf.json &gt; tauri &gt; windows` is not set. 
    * c119060e refactor(core): empty default value for config > tauri > windows (#3380) on 2022-02-10
  * **Breaking change:** Renamed the `rpc` module to `ipc`. 
    * 3420aa50 refactor: IPC handler [TRI-019] (#9) on 2022-01-09
  * Expose `run_on_main_thread` APIs on `Window` and `AppHandle`. 
    * 53fdfe52 feat(core): expose `run_on_main_thread` API (#2711) on 2021-10-04
  * The minimum Rust version is now `1.56`. 
    * a9dfc015 feat: update to edition 2021 and set minimum rust to 1.56 (#2789) on 2021-10-22
  * The minimum Rust version is now 1.57. 
    * d5d6d2ab Isolation Pattern (#43) Co-authored-by: Ngo Iok Ui (Wu Yu Wei) <wusyong9104@gmail.com> Co-authored-by: Lucas Fernandes Nogueira <lucas@tauri.app> on 2022-01-17
  * Scopes the `filesystem` APIs from the webview access using `tauri.conf.json &gt; tauri &gt; allowlist &gt; fs &gt; scope`. Scopes the `asset` protocol access using `tauri.conf.json &gt; tauri &gt; allowlist &gt; protocol &gt; assetScope`. Scopes the `http` APIs from the webview access using `tauri.conf.json &gt; tauri &gt; allowlist &gt; http &gt; scope`. Scopes the `shell` execute API from the webview access using `tauri.conf.json &gt; tauri &gt; allowlist &gt; shell &gt; scope`. Additionally, check the `tauri.conf.json &gt; tauri &gt; bundle &gt; externalBin` to prevent access to unknown sidecars. 
    * 7920ff14 feat: scope the `fs` API and the `asset` protocol [TRI-026] [TRI-010] [TRI-011] (#10) on 2022-01-09
    * 0ad1c651 feat(core): add `http` allowlist scope [TRI-008] (#24) on 2021-10-29
    * d4db95e7 feat(core): shell execute API scope [TRI-002] (#36) on 2021-12-01
  * `Builder#setup` closure type changed from `Fn` to `FnOnce`. 
    * 3f3599b9 refactor(core): change `setup` closure type to `FnOnce`, closes #3061 (#3065) on 2021-12-27
  * The `tauri::api::shell::open`’s `with` argument is now an enum value instead of any string. 
    * 63921fad refactor: change `tauri::api::open` `with` argument to an enum [TRI-022] (#19) on 2022-01-09
  * The `shell` allowlist now includes a `sidecar` flag, which enables the use of the `shell` API to execute sidecars. 
    * eed01728 feat(core): add `shell &gt; sidecar` allowlist and `process` feature flag [TRI-037] (#18) on 2021-10-24
  * **Breaking change:** The sidecar’s target triple suffix is now removed at build time. 
    * 3035e458 Remove target triple from sidecar bin paths, closes #3355 (#3356) on 2022-02-07
  * Fix streaming of small files using the `asset` protocol. 
    * 151e629e fix(core): streaming of small files using `asset://`, closes #2854 (#3039) on 2021-12-09
  * Add `set_menu` API on `tauri::SystemTrayHandle`. 
    * 0e4d12b5 fix: #2502 Expose `set_menu` from tao through the TrayHandle struct (#2532) on 2021-10-02
  * Adds `unlisten` function to the `Window` struct. 
    * 3a59f5f7 Unlisten to an event on this window (#2664) on 2021-09-28
  * Force updater endpoint URL to use `https` on release builds. 
    * c077f449 feat: force endpoint URL to use https on release [TRI-015] (#41) on 2022-01-09
  * Validate the `std::env::current_exe` return value if `APPDIR` or `APPIMAGE` environment variables are set. 
    * 6fbd6dba feat(core): validate `AppImage` execution when env vars are set [TRI-041] (#17) on 2021-10-24
  * The event name is now validated. On a IPC message, it returns an error if it fails validation; on the Rust side, it panics. It must include only alphanumeric characters, `-`, `/`, `:` and `_`. 
    * a48b8b18 feat(core): validate callbacks and event names [TRI-038] [TRI-020] (#21) on 2022-01-09
  * The window label is now validated and must be alphanumeric, resulting in a panic if it isn’t. 
    * 680554de feat: validate window label [TRI-021] (#13) on 2021-10-23
  * Allow `tauri.conf.json &gt; package &gt; version` to specify a path to a `package.json` file and pull the version from it. 
    * 46f2eae8 feat: allow config’s version to be a path to package.json, closes #2967 (#2971) on 2022-01-07
  * Added `clipboard` field on the `WebviewAttributes` struct, which must be set to `true` to enable clipboard access on the webview. 
    * d42ccfb3 feat: add `clipboard` flag to `WebviewAttributes` [TRI-032] (#12) on 2021-10-23
  * Replace all of the `winapi` crate references with the `windows` crate, and replace `webview2` and `webview2-sys` with `webview2-com` and `webview2-com-sys` built with the `windows` crate. This goes along with updates to the TAO and WRY `next` branches. 
    * bb00d5bd Replace winapi with windows crate and use webview2-com instead of webview2 (#2615) on 2021-09-24
  * Show `Ok/Cancel` buttons instead of `Yes/No` when executing `window.confirm`. 
    * e98c1af4 feat(core): expose message dialog APIs, fix window.confirm, implement HasRawWindowHandle for Window, closes #2535 (#2700) on 2021-10-02
  * Update the `windows` crate to 0.25.0, which comes with pre-built libraries. WRY and Tao can both reference the same types directly from the `windows` crate instead of sharing bindings in `webview2-com-sys`. 
    * 34be6cf3 Update webview2-com and windows crates (#2875) on 2021-11-11


© 2025 Tauri Contributors. CC-BY / MIT
