Skip to content
# tauri@1.4.0
ReturnView on GitHub
### New Features
  * `7c237209`(#6546) Added `tauri::VERSION` const to get Tauri’s version from Rust.
  * `4c39e46a`(#7026) Added `tauri::webview_version` , to get webview version.
  * `359058ce`(#5939) Add `tauri::api::os::locale` function to get the system locale.
  * `c4d6fb4b`(#2353) Added the `maximizable`, `minimizable` and `closable` options to the window builder.
  * `c4d6fb4b`(#2353) Added the `set_maximizable`, `set_minimizable`, `set_closable`, `is_maximizable`, `is_minimizable` and `is_closable` methods on `Window`.
  * `1d99f8a3`(#4752) Expose the `test` module behind the `test` Cargo feature.
  * `000104bc`(#6472) Add `Window::is_focused` and `Manager::get_focused_window` getters.
  * `441f9646`(#5491) Add `MenuHandle::try_get_item` and `SystemTrayHandle::try_get_item` which returns a `Option` instead of panicking.


### Enhancements
  * `45330e38`(#6375) Enhance the `asset` protocol to support streaming of large files.
  * `df89ccc1`(#6955) Support `passive` mode for NSIS updater.
  * `cd3846c8`(#6955) Restart the app after the NSIS updater is finished.
  * `db7c5fbf`(#7143) Remove `attohttpc` in favor of `reqwest`.
  * `d2710e9d`(#6944) Unpin `time`, `ignore`, and `winnow` crate versions. Developers now have to pin crates if needed themselves. A list of crates that need pinning to adhere to Tauri’s MSRV will be visible in Tauri’s GitHub workflow: https://github.com/tauri-apps/tauri/blob/dev/.github/workflows/test-core.yml#L85.
  * `5d85d099`(#7128) Send updater status events even if default dialog is enabled.


### Bug Fixes
  * `82169e69`(#5208) Fix parsing `allowlist &gt; http &gt; scope` urls that added a trailing slash which broke matching the incoming requests url.
  * `b41b57eb`(#7105) Fix panics when registering an invalid global shortcuts or checking it is registered and return proper errors instead.
  * `aecf1469`(#6889) Fix IPC failing after a failed navigation to an external URL.
  * `076e1a81`(#7119) Fix unlistening to window events failing sometimes.
  * `3f35b452`(#4080) Fix `WindowBuilder::on_navigation` handler not registered properly.
  * `0503eb69`(#7078) On macOS and Linux, fix app crashing when creating a window with `data:` uri.
  * `3700793a`(#6934) Emit `UPTODATE` update status to javascript when the updater server returns status code `204`
  * `ff5e4dbb`(#6794) Fix some configurations not applied when creating the window through Javascript.
  * `65fd674f`(#6652) Play a sound when showing a notification on Windows.
  * `696d77c3`(#4493) Fixes global events not being received on window-specific event listeners.


© 2025 Tauri Contributors. CC-BY / MIT
