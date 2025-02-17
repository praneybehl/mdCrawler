Skip to content
# wry@0.27.1
ReturnView on GitHub
  * On Windows, Linux and macOS, add method `evaluate_script_with_callback` to execute javascipt with a callback. Evaluated result will be serialized into JSON string and pass to the callback. 
    * 2647731 feat: support callback function in eval (#778) on 2023-03-23
  * On iOS, set webview scroll bounce default to NO. 
    * 4d61cf1 fix(ios): set scroll bounce default to NO (#907) on 2023-03-20
  * Update the value returned on a `None` value of `ClassDecl::new(&quot;WryDownloadDelegate&quot;, class!(NSObject))` from `UIViewController` to `WryDownloadDelegate`. 
    * 7795356 fix: WryDownloadDelegate call after first time on 2023-02-20
  * On Linux, disable system appearance for scrollbars. 
    * 530a8b7 fix(linux): disable system appearance for scrollbars (#897) on 2023-03-08
  * On Windows and Linux, implement `WebviewBuilder::with_back_forward_navigation_gestures` and `WebviewAttributes::back_forward_navigation_gestures` to control swipe navigation. Disabled by default. 
    * 15b4ddf feat(win&amp;linux): implement the option to control gesture navigation (#896) on 2023-03-07


© 2025 Tauri Contributors. CC-BY / MIT
