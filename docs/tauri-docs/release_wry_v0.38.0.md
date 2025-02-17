Skip to content
# wry@0.38.0
ReturnView on GitHub
  * `e6f0fbd`(#1180) Fixes a null pointer exception when running `window.ipc.postMessage(null)` on Android.
  * `5789bf7`(#1187) **Breaking change** : Refactored the file-drop handling on the webview for better representation of the actual drag and drop operation:
    * Renamed `file-drop` cargo feature flag to `drag-drop`.
    * Removed `FileDropEvent` enum and replaced with a new `DragDropEvent` enum.
    * Renamed `WebViewAttributes::file_drop_handler` field to `WebViewAttributes::drag_drop_handler`.
    * Renamed `WebViewAttributes::with_file_drop_handler` method to `WebViewAttributes::with_drag_drop_handler`.
  * `b8fea39`(#1183) Changed `WebViewBuilder::with_ipc_handler` closure to take `http::Request` instead of `String` so the request URL is available.
  * `3a2026b`(#1182) **Breaking changes** : Changed a few methods on `WebView` type to return a `Result`:
    * `Webview::url`
    * `Webview::zoom`
    * `Webview::load_url`
    * `Webview::load_url_with_headers`
    * `Webview::bounds`
    * `Webview::set_bounds`
    * `Webview::set_visible`
    * `WebviewExtWindows::set_theme`
    * `WebviewExtWindows::set_memory_usage_level`
    * `WebviewExtWindows::reparent`
    * `WebviewExtUnix::reparent`
    * `WebviewExtMacOS::reparent`
  * `e1e2e07`(#1190) Update `webview2-com` crate to `0.29`
  * `e1e2e07`(#1190) Update `windows` crate to `0.54`
  * `00bc96d`(#1179) Added `WryActivity::onWebViewCreate(android.webkit.WebView)` on Android.


© 2025 Tauri Contributors. CC-BY / MIT
