Skip to content
# wry@0.37.0
ReturnView on GitHub
  * `8c86fba` **Breaking change** : Removed `data:` url support, as its native support in Windows and macOS are buggy and unreliable, use `Webview::with_html` instead.
  * `8c86fba` On Linux, decode `FilDropEvent` paths before emitting them to make it consistent across all platforms.
  * `8c86fba` Added `WebViewExtMacOS::reparent`,`WebViewExtWindows::reparent` and `WebViewExtUnix::reparent`.
  * `8c86fba` Revert global keys shortcuts (wry#1156)
  * `8c86fba` **Breaking change** : Removed internal url parsing which had a few side-effects such as encoded url content, now it is up to the user to pass a valid URL as a string. This also came with a few breaking changes:
    * Removed `Url` struct re-export
    * Removed `Error::UrlError` variant.
    * Changed `WebviewAttributes::url` field type to `String`.
    * Changed `WebviewBuilder::with_url` and `WebviewBuilder::with_url_and_headers` return type to `WebviewBuilder` instead of `Result&lt;WebviewBuilder&gt;`.
    * Changed `Webview::url` getter to return a `String` instead of `Url`.


© 2025 Tauri Contributors. CC-BY / MIT
