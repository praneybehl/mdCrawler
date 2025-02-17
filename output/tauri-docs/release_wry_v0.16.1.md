Skip to content
# wry@0.16.1
ReturnView on GitHub
  * Fixes a crash on macOS below Big Sur due to `titlebarSeparatorStyle` (11+ API) usage. 
    * eb2dddb fix(macos): only use APIs when supported on 2022-05-08
  * Only run `WebView::print` on macOS on v11+. This prevents a crash on older versions. 
    * eb2dddb fix(macos): only use APIs when supported on 2022-05-08


© 2025 Tauri Contributors. CC-BY / MIT
