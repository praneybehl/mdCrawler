Skip to content
# @tauri-apps/api@2.1.0
ReturnView on GitHub
### New Features
  * `5c4b83084` (#11191 by @amrbashir) Improved support for `dpi` module types to allow these types to be used without manual conversions with `invoke`:
    * Added `SERIALIZE_TO_IPC_FN` const in `core` module which can be used to implement custom IPC serialization for types passed to `invoke`.
    * Added `Size` and `Position` classes in `dpi` module.
    * Implementd `SERIALIZE_TO_IPC_FN` method on `PhysicalSize`, `PhysicalPosition`, `LogicalSize` and `LogicalPosition` to convert it into a valid IPC-compatible value that can be deserialized correctly on the Rust side into its equivalent struct.
  * `4d545ab3c` (#11486 by @amrbashir) Added `Webview::setBackgroundColor`, `WebviewWindow::setBackgroundColor` APIs to set the window background color dynamically and a `backgroundColor` window option to set the background color on window creation.
  * `cbc095ec5` (#11451 by @amrbashir) Add `app &gt; windows &gt; devtools` config option and when creating the webview from JS, to enable or disable devtools for a specific webview.
  * `2a75c64b5` (#11469 by @amrbashir) Added `windowClassname` option, when constructing a `Webview` or `WebviewWindow`, to specify the name of the window class on Windows.


### Bug Fixes
  * `54cbf59b5` (#11441 by @amrbashir) Fix submenu created as a menu item instead of a submenu when created by using an object in the `items` field in the options object passed to `Menu.new` or `Submenu.new`.


© 2025 Tauri Contributors. CC-BY / MIT
