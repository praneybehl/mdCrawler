Skip to content
# wry@0.22.1
ReturnView on GitHub
  * Fix `WebViewBuilder::with_accept_first_mouse` taking behavior of first initalized webview. 
    * 0647c0e fix(macos): fix `acceptFirstMouse` for subsequent webviews, closes #751 (#752) on 2022-11-13
  * Fix download implementation on macOS older than 11.3. 
    * e69ddc6 fix(macos): download breaking app on macOS older than 11.3, closes #755 (#756) on 2022-11-15
  * On macOS, remove webview from window’s NSView before dropping. 
    * 3d3ea80 On macOS, remove webview from window’s NSView before dropping (#754) on 2022-11-14


© 2025 Tauri Contributors. CC-BY / MIT
