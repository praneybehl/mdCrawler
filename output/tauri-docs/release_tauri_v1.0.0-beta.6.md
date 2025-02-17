Skip to content
# tauri@1.0.0-beta.6
ReturnView on GitHub
  * **Breaking change:** The `tauri::async_runtime::spawn` function now returns `tauri::async_runtime::JoinHandle&lt;T&gt;`.
    * 9aeb04fa feat(core): `async_runtime` `handle` API, `spawn` returns `JoinHandle` (#2399) on 2021-08-11
  * **Breaking change:** Added `window_parent: Option&lt;&amp;Window&gt;` as first argument to the `ask` and `message` APIs on the `tauri::api::dialog` module.
    * c76f4b7d feat(core): set parent window on ask and message dialog APIs (#2454) on 2021-08-16
  * Allow the `tauri::api::dialog` APIs to be executed on any secondary thread. **Breaking change:** All dialog APIs now takes a closure instead of returning the response on the function call.
    * 2088cd0f refactor(core): handle dialog threading internally, closes #2223 (#2429) on 2021-08-14
    * 60b1e260 chore: adjust change file on 2021-08-16
  * **Breaking change:** The `Plugin` trait `initialize` method now takes an `AppHandle` reference instead of `App`.
    * c17532f7 refactor(core): change Plugin `initialize` signature, move register t… (#2347) on 2021-08-03
  * **Breaking change:** Remove menu feature flag since there’s no package dependency need to be installed on any platform anymore.
    * f81ebddf feat: remove menu feature flag (#2415) on 2021-08-13
  * Adds `set_activation_policy` API to the `tauri::App` struct (macOS only).
    * 4a031add feat(core): expose `set_activation_policy`, closes #2258 (#2420) on 2021-08-13
  * Add `handle` API to `tauri::async_runtime`.
    * 9aeb04fa feat(core): `async_runtime` `handle` API, `spawn` returns `JoinHandle` (#2399) on 2021-08-11
  * Assets will now fallback to `&lt;uri&gt;/index.html` before `/index.html`, allowing anchor links to work as expected.
    * d22da650 fix(core): fallback to `{asset}/index.html` before `index.html`, closes #2328 (#2329) on 2021-08-02
  * Fix `data-tauri-drag-region` double-click, will now respect `resizable: false` and won’t maximize.
    * 1a510066 fix(core): `data-tauri-drag-region` didn’t respect resizable, closes #2314 (#2316) on 2021-08-02
  * Fix `Notification.requestPermission()` throwing `Unhandled Promise Rejection: TypeError: undefined is not a function (near &#39;...window.__TAURI__.invoke...&#39;)`
    * cf9f6aa1 fix(core): fix typo in notifications, closes #2330 (#2331) on 2021-08-02
  * Fix blur/focus events being incorrect on Windows.
    * d832d575 fix(windows): use webview events on windows (#2277) on 2021-07-23
  * Move items which `tauri::api` re-exports from `tauri-utils` to individual module `utils`. Because these items has their own Error/Result types which are not related to api module at all.
    * 12642a1a doc: update doc in tauri-utils and tauri (#2435) on 2021-08-15
    * cd55d671 doc: update tauri documentations (#2446) on 2021-08-16
  * Allow registering a plugin through an `AppHandle` instance using the `plugin` method.
    * 5b7be813 feat(core): add plugin register API on the `Manager` trait (#2340) on 2021-08-02
    * c17532f7 refactor(core): change Plugin `initialize` signature, move register t… (#2347) on 2021-08-03
  * Embed Info.plist file contents on binary on dev.
    * 537ab1b6 feat(core): inject src-tauri/Info.plist file on dev and merge on bundle, closes #1570 #2338 (#2444) on 2021-08-15
  * Add `ExitRequested` event that allows preventing the app from exiting when all windows are closed, and an `AppHandle.exit()` function to exit the app manually.
    * 892c63a0 feat(#2287): Add `ExitRequested` event to let users prevent app from exiting (#2293) on 2021-08-09
  * Change `App.create_window()` and `AppHandle.create_window()` to accept an `Into&lt;String&gt;` type instead of `String`.
    * 8216cba1 `App.create_window()` to accept any `Into&lt;String&gt;` type (fix #2290) (#2291) on 2021-07-26
  * Fixes `defaultPath` option on dialog API not setting the file name if it doesn’t exist on Linux.
    * 8b2cc261 fix(core): dialog’s `defaultPath` behavior on Linux, closes #2232 (#2382) on 2021-08-10
  * Fix ES Module detection for default imports with relative paths or scoped packages and exporting of async functions.
    * b2b36cfe fix(core): fixes ES Module detection for default imports with relative paths or scoped packages (#2380) on 2021-08-10
    * fbf8caf5 fix(core): ESM detection when using `export async function` (#2425) on 2021-08-14
  * Fix `listen` calls receiving past events.
    * 1ecb8651 fix(core): `listen` receiving past events, closes #2323 (#2371) on 2021-08-09
  * Fixes file drop events being swapped (`file-drop-hover` on drop and `file-drop` on hover).
    * c2b0fe1c fix(core): fix wrong file drop events (#2300) on 2021-07-31
  * Fixes `app.listen_global` not receiving events emitted in javascript.
    * a8c1de55 fix listen_global not listening to events with a window label (#2272) on 2021-07-23
  * Fixes minimum window height being used as maximum height.
    * e3f99165 fix(core) minHeight being used as maxHeight (#2247) on 2021-07-19
  * Fixes `unlisten` calls from JavaScript removing every registered event listener.
    * aa498e72 fix: unlisten removes all listeners, closes #2264 (#2302) on 2021-07-29
  * Use `Url.join()` when building webview URLs in `WindowManager`, to handle edge cases and leading/trailing slashes in paths and urls.
    * 31685c9f fix(#2281): Prevent double slashes when joining URLs (#2282) on 2021-07-23
  * Fixes `fs-all` feature not requiring the `base64` crate.
    * 9b32b939 fix(core): `fs-all` feature not including `base64` crate, closes #2336 (#2368) on 2021-08-08
  * Update gtk and its related libraries to v0.14. This also remove requirements of `clang` as build dependency.
    * 63ad3039 chore(linux): bump gtk to v0.14 (#2361) on 2021-08-07
  * Use `HeaderValue::from_bytes` instead of `HeaderValue::from_str` and `HeaderValue#to_bytes` instead of `HeaderValue#to_str` to improve compatibility.
    * 1635798a feat(core): improve HeaderValue compatibility, closes #2162 (#2438) on 2021-08-15
  * Implement `Debug` on public API structs and enums.
    * fa9341ba feat(core): implement `Debug` on public API structs/enums, closes #2292 (#2387) on 2021-08-11
  * Adds `Resumed` and `MainEventsCleared` variants to the `Event` enum.
    * 6be3f433 feat(core): add `Resumed` and `MainEventsCleared` events, closes #2127 (#2439) on 2021-08-15
  * Panic when a dispatcher getter method (`Window`, `GlobalShortcutHandle`, `ClipboardManager` and `MenuHandle` APIs) is called on the main thread.
    * 50ffdc06 feat(core): panic when a dispatcher getter is used on the main thread (#2455) on 2021-08-16
  * Use `percent_encoding::percent_decode` on the `asset` custom protocol URL before reading the file.
    * 9acd8301 fix(core): percent decode asset protocol URL (#2427) on 2021-08-14
  * Keep original value on `config &gt; package &gt; productName` on Linux (previously converted to kebab-case).
    * 3f039cb8 fix: keep original `productName` for .desktop `Name` field, closes #2295 (#2384) on 2021-08-10
  * Inject the invoke key on regular `&lt;script&gt;&lt;/script&gt;` tags.
    * d0142e87 fix(core): invoke key injection on regular JS scripts, closes #2342 (#2344) on 2021-08-03
  * Remove salt-related APIs (no longer needed after the `__TAURI_INVOKE_KEY__` implementation).
    * e2a0704c refactor(core): remove salt APIs (#2426) on 2021-08-14
  * Update minimum Rust version to 1.54.0.
    * a5394716 chore: update rust to 1.54.0 (#2434) on 2021-08-15
  * Run the setup callback after preparing the system tray.
    * 1792c455 fix(core): run setup after preparing system tray (#2312) on 2021-07-28
  * Fixes a consistency issue on the order of `tauri::process::Command` emitted events.
    * 737da872 fix(core): random shell command output order, closes #2184 (#2376) on 2021-08-09
  * Force data directory even on non-local window.
    * 70a19414 fix(core): Force data_directory on Windows (#2288) on 2021-07-23
  * Allow creation of empty Window with `create_tao_window()` and management with `send_tao_window_event()` on the AppHandler.
    * 88080855 feat(window): Allow creation of Window without `wry` (#2321) on 2021-07-29
    * 15566cfd feat(core): add API to send wry window message to the event loop (#2339) on 2021-08-02
  * Make `ClipboardManager` and `GlobalShortcutManager` public as they are exposed in the `AppHandle`.
    * 6e0dbf63 fix(core): Expose `ClipboardManager` and `GlobalShortcutManager` (#2263) on 2021-08-03
  *     * Support macOS tray icon template to adjust automatically based on taskbar color.
  * Images you mark as template images should consist of only black and clear colors. You can use the alpha channel in the image to adjust the opacity of black content, however.
  * 426a6b49 feat(macOS): Implement tray icon template (#2322) on 2021-07-29
  * Add `Event::Ready` on the `run()` callback. Triggered once when the event loop is ready.
    * 28c6b7ad feat: add `Event::Ready` (#2433) on 2021-08-15
  *     * Do not run the updater with UAC task if server don’t tell us. (Allow toggling server-side)
  * The updater expect a field named `with_elevated_task` with a `boolean` and will not run if the task is not installed first. (windows only)
  * c5761190 fix(updater): Run elevated task only if server tell us (#2357) on 2021-08-08
  * Add `try_state` API to the `Manager` trait.
    * 84a0e04c feat(core): `try_state` API on the `Manager` trait (#2341) on 2021-08-02


© 2025 Tauri Contributors. CC-BY / MIT
