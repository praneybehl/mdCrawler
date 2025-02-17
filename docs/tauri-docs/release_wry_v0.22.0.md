Skip to content
# wry@0.22.0
ReturnView on GitHub
  * Added `WebViewAttributes::with_accept_first_mouse` method for macOS. 
    * 2c23440 feat(macos): add `accept_first_mouse` option, closes #714 (#715) on 2022-10-04
  * **Breaking change** Custom protocol now takes `Request` and returns `Response` types from `http` crate. 
    * 1510e45 refactor: use `http` crate primitives instead of a custom impl (#706) on 2022-09-29
  * Enabled devtools in debug mode by default. 
    * fea0638 feat: enable devtools in debug mode by default (#741) on 2022-10-27
  * On Desktop, add `download_started_handler` and `download_completed_handler`. See `blob_download` and `download_event` example for their usages. 
    * 3691c4f feat: Add download started and download completed callbacks (#530) on 2022-10-19
  * Fix double permission dialog on macOS 12+ and iOS 15+. 
    * 8aa7d61 Fix: Remove extra soft prompt asking for media permission on every app launch in macOS (#694) on 2022-09-29
  * Focus webview when window starts moving or resizing on Windows to automatically close `&lt;select&gt;` dropdowns. Also notify webview2 whenever the window position/size changes which fixes the `&lt;select&gt;` dropdown position 
    * a1001dd fix(windows): focus webview on `WM_ENTERSIZEMOVE` and call `NotifyParentChanged` on `WM_WINDOWPOSCHANGED`. (#695) on 2022-09-16
  * On Windows, hide the webview when the window is minimized to reduce memory and cpu usage. 
    * 51b49c5 feat(webview2): hide the webview when the window is minimized (#702) on 2022-09-27
  * Internally return with error from custom protocol if an invalid uri was requseted such as `wry://` which doesn’t contain a host. 
    * 818ce99 fix: don’t panic on invalid uri (#712) on 2022-09-30
  * Support cross compiling ios on a non macos host. 
    * cd08410 Fix cross compilation. (#731) on 2022-10-29
  * On Linux, Improve custom protocol with http headers / method added to request, and status code / http headers added to response. This feature is 2.36 only, version below it will fallback to previous implementation. 
    * 2944d91 feat(linux): add headers to URL scheme request (#721) on 2022-10-17
  * On macOS, add WKWebview as subview of existing NSView directly. 
    * 008eca8 On macOS, add WKWebview as subview of existing NSView directly (#745) on 2022-11-07
  * Keypress on non-input element no longer triggers unsupported key feedback sound. 
    * 51c7f12 fix(macos): do not trigger unsupported key feedback sound on keypress (#742) on 2022-10-30
  * Remove the IPC script message handler when the WebView is dropped on macOS. 
    * 818ce99 fix: don’t panic on invalid uri (#712) on 2022-09-30
  * **Breaking change** Removed http error variants from `wry::Error` and replaced with generic `HttpError` variant that can be used to convert `http` crate errors. 
    * 1510e45 refactor: use `http` crate primitives instead of a custom impl (#706) on 2022-09-29
  * Disabled Microsoft SmartScreen by default on Windows. 
    * a617c5b feat(webview2): disable smartscreen & allow disabling internal webview2 args, closes #704 (#705) on 2022-09-28
  * Add `WebView::url` to get the current url. 
    * 38e49bd feat: add `WebView::url()` to access the current url (#732) on 2022-10-25
  * **Breaking change** Removed `http` module and replaced with re-export of `http` crate. 
    * 1510e45 refactor: use `http` crate primitives instead of a custom impl (#706) on 2022-09-29
  * Add `WebviewBuilderExtWindows::with_additionl_browser_args` method to pass additional browser args to Webview2 On Windows. By default wry passes `--disable-features=msWebOOUI,msPdfOOUI,msSmartScreenProtection` so if you use this method, you also need to disable these components by yourself if you want. 
    * 683f866 feat(webview2): add method to pass additional args, closes #415 (#711) on 2022-09-29
  * On Windows, fix canonical reason for custom protocol response. 
    * 9d5595c fix(webview2): set response reason correctly, closes #733 (#734) on 2022-10-24
  * On macOS, make the webview first responder. 
    * e64ad21 fix(wkwebview): make webview first responder (#740) on 2022-10-28


© 2025 Tauri Contributors. CC-BY / MIT
