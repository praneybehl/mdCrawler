Skip to content
# @tauri-apps/api@2.0.0-rc.6
ReturnView on GitHub
### New Features
  * `9014a3f17` (#11066 by @amrbashir) Add `WebviewWindow.clearAllBrowsingData` and `Webview.clearAllBrowsingData` to clear the webview browsing data.
  * `95df53a2e` (#11143 by @Legend-Master) Add the ability to set theme dynamically using `Window.setTheme` or `setTheme` function from the `app` module
  * `d9d2502b4` (#11140 by @amrbashir) Add `Webview.hide` and `Webview.show` methods.
  * `de7414aab` (#11154 by @amrbashir) Add `Window::setEnabled` and `Window::isEnabled` methods


### Bug Fixes
  * `948772a65` (#11114 by @lucasfernog) Change the `button_state` tray event field to camelCase `buttonState`.


### Breaking Changes
  * `0b4495996` (#11121 by @amrbashir) Simplified emitted tray event JS value and updated `TrayIconEvent` type definition to match it.


© 2025 Tauri Contributors. CC-BY / MIT
