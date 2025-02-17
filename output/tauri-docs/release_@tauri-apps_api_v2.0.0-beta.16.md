Skip to content
# @tauri-apps/api@2.0.0-beta.16
ReturnView on GitHub
### New Features
  * `da25f7353` (#10242 by @amrbashir) Add APIs to enable setting window size constraints separately:
    * Added `WindowSizeConstraints` interface in `window` and `webviewWindow` modules.
    * Added `Window.setSizeConstraints` and `WebviewWindow.setSizeConstraints`


### Bug Fixes
  * `3c17fb64f` (#10277 by @Legend-Master) Fix `Webview.reparent` pointing to `set_webview_focus` instead of `reparent` Rust API
  * `da25f7353` (#10242 by @amrbashir) Apply `minWidth`, `minHieght`, `maxWidth` and `maxHeight` constraints separately, which fixes a long standing bug where these constraints were never applied unless width and height were constrained together.


© 2025 Tauri Contributors. CC-BY / MIT
