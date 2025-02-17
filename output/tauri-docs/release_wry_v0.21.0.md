Skip to content
# wry@0.21.0
ReturnView on GitHub
  * Implement `&lt;input type=&quot;file&quot;&gt;` on Android. 
    * bf39d9d feat(android): implement dialogs and permissions (#685) on 2022-09-05
  * Add `WebviewExtAndroid::handle` which can be used to execute some code using JNI context. 
    * 2bfc6c3 feat(android): JNI execution handle (#689) on 2022-09-07
  * Enable JS alert, confirm, prompt on Android. 
    * bf39d9d feat(android): implement dialogs and permissions (#685) on 2022-09-05
  * Prompt for permissions on Android when needed. 
    * bf39d9d feat(android): implement dialogs and permissions (#685) on 2022-09-05
  * Implement `webview_version` on Android. 
    * 9183de4 feat(android): implement webview_version (#687) on 2022-09-05
  * Enable storage, geolocation, media playback, `window.open`. 
    * 9dfffcf feat(android): enable storage, geolocation, media playback, window.open (#684) on 2022-09-04
  * Improve Android initialization script implementation. 
    * 1b26d60 feat(android): improve initialization scripts implementation (#670) on 2022-08-24
  * WRY will now generate the needed kotlin files at build time but you need to set `WRY_ANDROID_REVERSED_DOMAIN`, `WRY_ANDROID_APP_NAME_SNAKE_CASE` and `WRY_ANDROID_KOTLIN_FILES_OUT_DIR` env vars. 
    * b478903 feat(android): generate kotlin files at build time (#671) on 2022-08-24
    * 103f255 chore: change bump to patch on 2022-08-25
  * **Breaking change** Removed `WebView::focus`. 
    * f338df7 feat(windows): auto-focus the webview (#676) on 2022-08-27
  * Updated tao to `0.14`
    * 483bad0 feat: tao as window dependency (#230) on 2021-05-03
    * 51430e9 publish new versions (#221) on 2021-05-09
    * 0cf0089 Update tao to v0.2.6 (#271) on 2021-05-18
    * a76206c publish new versions (#272) on 2021-05-18
    * 3c4f8b8 Update tao to v0.5 (#365) on 2021-08-09
    * 44aa1dc publish new versions (#351) on 2021-08-09
    * 935cc5f Update tao to 0.13 (#642) on 2022-07-27
    * 657888a Publish New Versions (#632) on 2022-07-27
    * 3a91376 chore(deps): update tao to 0.14 (#691) on 2022-09-13
  * Allow setting the webview background color. 
    * eb1b723 feat: allow setting webview bg color, closes #197 (#682) on 2022-09-05
  * Added the `RustWebView` class on Android. 
    * b1e8560 feat(android): define WebView class in kotlin (#672) on 2022-08-24
  * Update the `windows` crate to the latest 0.39.0 release and `webview2-com` to 0.19.1 to match. 
    * c7d7e1f Update windows to 0.39.0 and webview2-com to 0.19.1 to match (#679) on 2022-08-31
  * On Windows, automatically focus the webview when the window gains focus to match other platforms. 
    * f338df7 feat(windows): auto-focus the webview (#676) on 2022-08-27


© 2025 Tauri Contributors. CC-BY / MIT
