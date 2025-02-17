Skip to content
# wry@0.23.0
ReturnView on GitHub
  * Properly parse the content type header for the `android.webkit.WebResourceResponse` mime type. 
    * 1db5ea6 fix(android): properly parse content-type for response mime type (#772) on 2022-11-27
  * Change typo in `WebViewBuilderExtWindows::with_additionl_browser_args`. to `WebViewBuilderExtWindows::with_additional_browser_args`. 
    * db1c290 fix(windows): Fix typo in method name of `WebViewBuilderExtWindows` (#781) on 2022-12-02
  * Add `Webiew::load_url`. 
    * a2b9531 feat: add `Webiew::navigate_to_url`, closes #776 (#777) on 2022-11-30
  * Change the type of `WebViewBuilderExtWindows::with_additional_browser_args` argument from `AsRef&lt;str&gt;` to `Into&lt;String&gt;` to reduce extra allocation. 
    * b0ff06a perf: reduce extra allocation at `WebViewBuilderExtWindows::with_additional_browser_args` argument (#783) on 2022-12-03
  * Validate custom protocol response status code on Android. 
    * 7f585c7 feat(android): validate custom protocol response status code (#779) on 2022-11-30
  * [https://github.com/tauri-apps/wry/commit/04422bc1b579d9388ce03c2388b8f415dbc0747b] On macOS, revert content view to native NSView ([#782])(https://github.com/tauri-apps/wry/pull/782)


© 2025 Tauri Contributors. CC-BY / MIT
