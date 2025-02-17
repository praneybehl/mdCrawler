Skip to content
# wry@0.35.2
ReturnView on GitHub
  * `0ef041f`(#1133) On Linux, apply passed webview bounds when using `WebView::new_gtk` or `WebViewBuilder::new_gtk` with `gtk::Fixed` widget. This allows to create multiple webviews inside `gtk::Fixed` in the same window.
  * `0ef041f`(#1133) Added tracing spans for `evaluate_script`, `ipc_handler` and `custom_protocols` behind the `tracing` feature flag.


© 2025 Tauri Contributors. CC-BY / MIT
