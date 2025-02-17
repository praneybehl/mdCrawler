Skip to content
# tauri@2.1.0
ReturnView on GitHub
### New Features
  * `fabc2f283` (#11485 by @39zde) Adds a new configuration option `app &gt; security &gt; headers` to define headers that will be added to every http response from tauri to the web view. This doesn’t include IPC messages and error responses.
  * `8036c78e0` (#11455 by @amrbashir) Add `PathResolver::home_dir()` method on Android.
  * `5c4b83084` (#11191 by @amrbashir) Improved support for `dpi` module types to allow these types to be used without manual conversions with `invoke`:
    * Added `SERIALIZE_TO_IPC_FN` const in `core` module which can be used to implement custom IPC serialization for types passed to `invoke`.
    * Added `Size` and `Position` classes in `dpi` module.
    * Implementd `SERIALIZE_TO_IPC_FN` method on `PhysicalSize`, `PhysicalPosition`, `LogicalSize` and `LogicalPosition` to convert it into a valid IPC-compatible value that can be deserialized correctly on the Rust side into its equivalent struct.
  * `4d545ab3c` (#11486 by @amrbashir) Added `Window::set_background_color` and `WindowBuilder::background_color`.
  * `cbc095ec5` (#11451 by @amrbashir) Add `app &gt; windows &gt; devtools` config option and when creating the webview from JS, to enable or disable devtools for a specific webview.
  * `f0da0bde8` (#11439 by @lucasfernog) Added `WebviewWindow::resolve_command_scope` to check a command scope at runtime.
  * “ Detect if `SERIALIZE_TO_IPC_FN`, const from the JS `core` module, is implemented on objects when serializing over IPC and use it.
  * `f37e97d41` (#11477 by @amrbashir) Add `app &gt; windows &gt; useHttpsScheme` config option to choose whether the custom protocols should use `https://&lt;scheme&gt;.localhost` instead of the default `http://&lt;scheme&gt;.localhost` on Windows and Android
  * `f37e97d41` (#11477 by @amrbashir) Add `WebviewWindowBuilder/WebviewBuilder::use_https_scheme` to choose whether the custom protocols should use `https://&lt;scheme&gt;.localhost` instead of the default `http://&lt;scheme&gt;.localhost` on Windows and Android
  * `cbc095ec5` (#11451 by @amrbashir) Add `WebviewWindowBuilder::devtools` and `WebviewBuilder::devtools` to enable or disable devtools for a specific webview.
  * `129414faa` (#11569 by @amrbashir) Add `WebviewBuilder::focused` method to choose whether to focus webview or not on creation.
  * `2a75c64b5` (#11469 by @amrbashir) Added `app &gt; windows &gt; windowClassname` config option to specify the name of the window class on Windows.
  * `2a75c64b5` (#11469 by @amrbashir) Added `WindowBuilder/WebviewWindowBuilder::window_classname` method to specify the name of the window class on Windows.


### Enhancements
  * `17c6952ae` (#11522 by @amrbashir) Enhance the error message when using `async` commands with a reference.
  * `c33bbf457` (#11575 by @kornelski) Include the path in ACL I/O errors.


### Bug Fixes
  * `229d7f8e2` (#11616 by @amrbashir) Fix regression in creating child webviews on macOS and Windows, covering the whole window.
  * `8c6d1e8e6` (#11401 by @amrbashir) Fix `App/AppHandle/Window/Webview/WebviewWindow::cursor_position` getter method failing on Linux with `GDK may only be used from the main thread`.
  * `f8994b214` (#11581 by @Mikkel-T) Fix listeners created with `EventTarget::AnyLabel` never receiving events.
  * `4191a7a53` (#11583 by @amrbashir) Fix tray events not fired for tray icons created inside an async command.
  * `129414faa` (#11569 by @amrbashir) Fix webview not focused by default.


### Dependencies
  * Upgraded to `tauri-utils@2.1.0`
  * Upgraded to `tauri-runtime@2.2.0`
  * Upgraded to `tauri-runtime-wry@2.2.0`
  * Upgraded to `tauri-macros@2.0.3`
  * Upgraded to `tauri-build@2.0.3`


© 2025 Tauri Contributors. CC-BY / MIT
