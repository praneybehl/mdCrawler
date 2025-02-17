Skip to content
# tauri@2.0.0-beta.25
ReturnView on GitHub
### New Features
  * `da25f7353` (#10242 by @amrbashir) Add APIs to enable setting window size constraints separately:
    * Added `WindowBuilder::inner_size_constraints` and `WebviewWindowBuilder::inner_size_constraints` which can be used for setting granular constraints.
    * Added `WindowSizeConstraints` struct
    * Added `Window::set_size_constraints` and `WebviewWindow::set_size_constraints`


### Bug Fixes
  * `e1776946a` (#10362 by @Brendonovich) Use `specta rc.15&#39;s `derive` feature which fixes build issues in docs.rs.
  * `da25f7353` (#10242 by @amrbashir) Apply `minWidth`, `minHieght`, `maxWidth` and `maxHeight` constraints separately, which fixes a long standing bug where these constraints were never applied unless width and height were constrained together.


### What’s Changed
  * `9546548ec` (#10297 by @pewsheen) On macOS, set default titlebar style to `Visible` to prevent webview move out of the view.


### Dependencies
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.21`
  * Upgraded to `tauri-runtime@2.0.0-beta.21`


© 2025 Tauri Contributors. CC-BY / MIT
