Skip to content
# tauri@2.0.0-rc.16
ReturnView on GitHub
### New Features
  * `a247170e1` (#11056 by @SpikeHD) Expose the ability to enabled browser extensions in WebView2 on Windows.
  * `9014a3f17` (#11066 by @amrbashir) Add `WebviewWindow::clear_all_browsing_data` and `Webview::clear_all_browsing_data` to clear the webview browsing data.
  * `0ddfc59d6` (#11071 by @amrbashir) Add `Manager::unmanage` to remove previously managed state.
  * `1d8b67b29` (#11162 by @amrbashir) Support async functions for `mobile_entry_point` macro
  * `5621174b0` (#11132 by @chippers) Add `ScopeObjectMatch` for easy scope validation those that can be represented by a boolean return value.
  * `95df53a2e` (#11143 by @Legend-Master) Add the ability to set theme dynamically using `Window::set_theme`, `App::set_theme`
  * `d9d2502b4` (#11140 by @amrbashir) Add `Webview::hide` and `Webview::show` methods.
  * `de7414aab` (#11154 by @amrbashir) Add `Window::set_enabled` and `Window::is_enabled` methods


### Bug Fixes
  * `948772a65` (#11114 by @lucasfernog) Change the `button_state` tray event field to camelCase `buttonState`.
  * `a49fc999f` (#11161 by @amrbashir) Fix internal crash when trying to close the same window multiple times.
  * `62b3a5cd1` (#11043 by @amrbashir) Fix `localStorage` not shared between webviews that use the same data directory.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.14`
  * Upgraded to `tauri-runtime@2.0.0-rc.13`
  * Upgraded to `tauri-utils@2.0.0-rc.13`
  * Upgraded to `tauri-macros@2.0.0-rc.12`
  * Upgraded to `tauri-build@2.0.0-rc.13`


### Breaking Changes
  * `0b4495996` (#11121 by @amrbashir) Simplified emitted tray event JS value and updated `TrayIconEvent` type definition to match it.


© 2025 Tauri Contributors. CC-BY / MIT
