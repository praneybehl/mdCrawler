Skip to content
# wry@0.23.2
ReturnView on GitHub
  * On macOS, remove all custom keydown implementations. This will bring back keydown regression but should allow all accelerator working. 
    * fee4bf2 Remove all keydown implementations (#798) on 2022-12-10
  * Suppress `unused_variables` warning reported only in release build. 
    * 4e23c0f fix(macos): suppress `unused_variables` warning reported only in release build (#790) on 2022-12-07
  * Add `WebViewBuilderExtWindows::with_browser_accelerator_keys` method to allow disabling browser-specific accelerator keys enabled in WebView2 by default. When `false` is passed, it disables all accelerator keys that access features specific to a web browser. See the official WebView2 document for more details. 
    * 6e622ff feat(windows): Allow disabling browser-specific accelerator keys (#792) on 2022-12-07


© 2025 Tauri Contributors. CC-BY / MIT
