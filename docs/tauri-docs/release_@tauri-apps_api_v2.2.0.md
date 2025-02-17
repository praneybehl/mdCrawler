Skip to content
# @tauri-apps/api@2.2.0
ReturnView on GitHub
### New Features
  * `020ea0556` (#11661 by @ahqsoftwares) Add badging APIs:
    * `Window/WebviewWindow::set_badge_count` for Linux, macOS and IOS.
    * `Window/WebviewWindow::set_overlay_icon` for Windows Only.
    * `Window/WebviewWindow::set_badge_label`for macOS Only.
  * `fc30b20be` (#11726 by @amrbashir) Add `TrayIcon.setShowMenuOnLeftClick` method and deprecate `TrayIcon.setMenuOnLeftClick` to match the Rust API.
  * `fc30b20be` (#11726 by @amrbashir) Add `TrayIconOptions.showMenuOnLeftClick` field and deprecate `TrayIconOptions.menuOnLeftClick` to match the Rust API.


### Enhancements
  * `fc30b20be` (#11726 by @amrbashir) Add support for `TrayIconOptions.menuOnLeftClick` option and `TrayIcon.setMenuOnLeftClick` on Windows.


### Bug Fixes
  * `a16796a55` (#12069 by @Legend-Master) Fix `Channel` never calls `onmessage` in some cases
  * `12a48d1e2` (#11741 by @amrbashir) Fix error when calling `PredefinedMenuItem.new` to create an `About` menu item that uses an `Image` instance for the about icon.
  * `12a48d1e2` (#11741 by @amrbashir) Fix error when calling `IconMenuItem.new` using an `Image` instance for the icon.
  * `b63262cd4` (#11724 by @FabianLars) Removed the generic in the type of the callback function argument in `mockIPC` which prevented its proper use in tests using TypeScript.
  * `a6e84f7d2` (#11835 by @ilittlebig) Fix error where using `isAbsolute` would return `Command not found`.


© 2025 Tauri Contributors. CC-BY / MIT
