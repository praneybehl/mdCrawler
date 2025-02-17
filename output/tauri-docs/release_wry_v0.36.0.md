Skip to content
# wry@0.36.0
ReturnView on GitHub
  * `8646120`(#1159) On android, fix `no non-static method &quot;.evalScript(ILjava/lang/String;)&quot;` when calling `Window::eval`.
  * `8646120`(#1159) On macOS, fix a release build crashes with SEGV when calling `WebView::evaluate_script`. This crash bug was introduced at v0.35.2.
  * `8646120`(#1159) **Breaking change** Update raw-window-handle crate to v0.6.
    * `HasWindowHandle` trait is required for window types instead of `HasRawWindowHandle`.
    * `wry::raw_window_handle` now re-exports v0.6.
  * `8646120`(#1159) On `macOS`, fix menu keyboard shortcuts. This issue bug was introduced in `v2` when added `webview` as `child`.


© 2025 Tauri Contributors. CC-BY / MIT
