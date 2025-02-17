Skip to content
# @tauri-apps/api@2.0.0-rc.1
ReturnView on GitHub
### Breaking Changes
  * `b6dca99ff` (#10630 by @lucasfernog) Changed `WebviewWindow.getAll`, `WebviewWindow.getByLabel`, `getAllWebviewWindows`, `Window.getAll`, `Window.getByLabel`, `getAllWindows`, `Webview.getAll`, `Webview.getByLabel`, `getAllWebviews` to be async so their return value are synchronized with the state from the Rust side, meaning new and destroyed windows are reflected.


© 2025 Tauri Contributors. CC-BY / MIT
