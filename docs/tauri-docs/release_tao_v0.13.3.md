Skip to content
# tao@0.13.3
ReturnView on GitHub
  * Implement custom protocol on Android. 
    * b464b8ae feat(android): implement custom protocol (#527) on 2022-08-13
  * Changed `WebViewMessage::Eval` to evaluate an specific script. 
    * 903c7e7f feat(android): change WebViewMessage::Eval to run specific script (#529) on 2022-08-13
  * Fix webview initialization scripts implementation on Android. 
    * 3d66ad0b fix(android): run initialization scripts before page loads (#528) on 2022-08-13
  * Removed the webview logic from the Android glue. 
    * 152aaa44 refactor(android): remove WebView logic, allow wry to hook into it (#530) on 2022-08-14
  * Implement `SystemTray::set_tooltip` and `SystemTrayBuilder::with_tooltip` on Windows. 
    * 06949a79 feat(windows): implement `with_tooltip`&`set_tooltip`, closes #205 (#524) on 2022-08-10


© 2025 Tauri Contributors. CC-BY / MIT
