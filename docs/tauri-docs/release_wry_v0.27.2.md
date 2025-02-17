Skip to content
# wry@0.27.2
ReturnView on GitHub
  * On Android, Add support for native back button navigation. 
    * fc232a3 feat(android): add support for native back navigation (#918) on 2023-04-03
  * Fix `WebView::url` getter on Android. 
    * 427cf92 Unify custom porotocol across Android/iOS (#546) on 2022-04-11
    * b89398a Publish New Versions (#547) on 2022-04-26
    * c22744a fix(android): use correct method signature (#917) on 2023-03-31
  * Add Webview attribute to enable/disable autoplay. Enabled by default. 
    * 6a523cc feat: Add setting to enable autoplay (#913) on 2023-04-04
  * Fix the `WebViewBuilder::with_url` when the projet use `mimalloc`
    * c22744a fix(android): use correct method signature (#917) on 2023-03-31
  * Revert `51b49c54` which hid the webview when minimized on Windows. 
    * f76568a fix(windows): Ignore resize event when minimizing frameless windows (#909) on 2023-03-24


© 2025 Tauri Contributors. CC-BY / MIT
