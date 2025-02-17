Skip to content
# wry@0.27.3
ReturnView on GitHub
  * Adds a way to launch a WebView as incognito through a new API at WebViewBuilder named as `with_incognito`. 
    * 8698836 feat: Add a way to launch WebViews as incognito `WebView::as_incognito`, closes #908 (#916) on 2023-04-06
  * On macOS and iOS, remove webcontext implementation since we don’t actually use it. This also fix segfault if users drop webcontext early. 
    * 3cc45cb Remove webcontext implementation on wkwebview (#922) on 2023-04-07
  * Use the new WKWebView `inspectable` property if available (iOS 16.4, macOS 13.3). 
    * c3f7304 feat(macos): use WKWebView’s inspectable property (#923) on 2023-04-08


© 2025 Tauri Contributors. CC-BY / MIT
