Skip to content
# wry@0.32.0
ReturnView on GitHub
  * `4bdf1c3`(#1017) Added `WebViewBuilder::with_asynchronous_custom_protocol` to allow implementing a protocol handler that resolves asynchronously.
  * `70d8ae0`(#1009) Fixes Android freezing when handling request due to endless iteration when reading request headers.
  * `b5e1875`(#994) **Breaking change** Wry now defaults to `http://&lt;scheme&gt;.localhost/` for custom protocols on Windows.
  * `b5e1875`(#994) Add `WebViewBuilderExtWindows::with_https_scheme` to be able to choose between `http` and `https` for custom protocols on Windows.
  * `fa15076`(#163) Add `winit` and `tao` feature flag with `tao` as default.
  * `4bdf1c3`(#1017) **Breaking change:** `WebViewBuidler::with_custom_protocol` closure now returns `http::Response` instead of `Result&lt;http::Response&gt;`.
  * `ebc4a20`(#1015) Add `WebViewAtrributes.focused` and `WebViewBuilder::with_focused` to control whether to focus the webview upon creation or not. Supported on Windows and Linux only.


© 2025 Tauri Contributors. CC-BY / MIT
