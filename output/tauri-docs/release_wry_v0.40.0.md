Skip to content
# wry@0.40.0
ReturnView on GitHub
  * `a424a0b`(#1270) On Windows, fix child webview invisible after creation because it was created with `0,0` size
  * `d6f8dd7`(#1271) On Windows, create child webview at the top of z-order to align with other platforms.
  * `03d2535`(#1269) On macOS, disable initialization script injection into subframes.
  * `1e65049`(#1267) On macOS, fixed a crash when sending empty body by IPC.
  * `0f3c886`(#1260) On macOS, fixed an issue of not being able to listen to the cmd+key event in javascript in single WebView.
  * `0f14e2a`(#1259) Default the margin when printing on MacOS to 0 so it is closer to the behavior of when printing on the web.
  * `0f14e2a`(#1259) Add `WebViewExtMacOS::print_with_options` which allows to modify the margins that will be used on the print dialog.
  * `f516122`(#1262) On Windows, enable webview2 non client region support which allows using `app-region` CSS style.


© 2025 Tauri Contributors. CC-BY / MIT
