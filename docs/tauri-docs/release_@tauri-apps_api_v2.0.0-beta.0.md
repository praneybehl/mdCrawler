Skip to content
# @tauri-apps/api@2.0.0-beta.0
ReturnView on GitHub
### New Features
  * `74a2a603`(#8661) Implement access control list for IPC usage.
  * `a093682d`(#8621) Added `emitTo` api to `event` module which is equivalent to the rust `emit_to` method. Also added `emitTo` method on `Window`, `Webivew` and `WebviewWindow` classes.
  * `a2fc3a63`(#8657) Add `visibleOnAllWorkspaces` option when creating the window in JS and `Window.setVisibleOnAllWorkspaces` method.
  * `7f033f6d`(#8537) Add `Window.startResizeDragging`.
  * `9eaeb5a8`(#8622) Add `parent` option when creating a window.
  * `af610232`(#8710) Added `Window::destroy` to force close a window.
  * `c77b4032`(#8280) Added support to multiwebview via the new `window` and `webview` modules.


### Breaking Changes
  * `c77b4032`(#8280) Removed event callback’s `windowLabel`.
  * `c77b4032`(#8280) The event target is now an object so you can target either a window or a webview.
  * `c77b4032`(#8280) Moved webview-specific APIs from the `Window` class to the `Webview` class.
  * `c77b4032`(#8280) Renamed `TauriEvent.WINDOW_FILE_DROP` to `TauriEvent.WEBVIEW_FILE_DROP`, `TauriEvent.WINDOW_FILE_DROP_HOVER` to `TauriEvent.WEBVIEW_FILE_DROP_HOVER` and `TauriEvent.WINDOW_FILE_DROP_CANCELLED` to `TauriEvent.WEBVIEW_FILE_DROP_CANCELLED`.
  * `c77b4032`(#8280) Added back the `WebviewWindow` API that exposes functionality of a window that hosts a single webview. The dedicated `Window` and `Webview` types are exposed for multiwebview features.
  * `af610232`(#8710) `Window::close` now triggers a close requested event instead of forcing the window to be closed.


© 2025 Tauri Contributors. CC-BY / MIT
