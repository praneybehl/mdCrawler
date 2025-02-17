Skip to content
# wry@0.42.0
ReturnView on GitHub
  * `556a359` (#1301 by @pewsheen) On macOS, emit an error when the URL scheme registration fails.
  * `19d83d7` (#1332 by @lucasfernog) Fixes a crash on the Android custom protocol handler when the request URL is invalid.
  * `38abcb9` (#1340 by @lucasfernog) Fixes custom protocols not triggered on Android on external redirects.
  * `d1f1e7e` (#1299 by @kanatapple) Fix `Webview::bounds` returning logical values where it should have been physical.
  * `03cdf93` (#1311 by @bukowa) Handle `webkit2gtk` close signal (when `window.close` is called from js)
  * `68413e8` (#1296 by @MarijnS95) **Breaking change** : Upgrade `ndk` crate to `0.9` and delete unused `ndk-sys` and `ndk-context` dependencies. Types from the `ndk` crate are used in public API surface. **Breaking change** : The public `android_setup()` function now takes `&amp;ThreadLooper` instead of `&amp;ForeignLooper`, signifying that the setup function must be called on the thread where the looper is attached (and the `JNIEnv` argument is already thread-local as well).
  * `39fc82c` (#1306 by @Legend-Master) Support WebView2 version older than 101.0.1210.39 and document `incognito` and `theme` will not work for versions before it
  * `5231a37` (#1322 by @Legend-Master) Support WebView2 version older than 86.0.616.0 and document version requirements for `back_forward_navigation_gestures`, `with_user_agent`, `with_hotkeys_zoom`, `with_browser_accelerator_keys`
  * `a23a28d` (#1341 by @amrbashir) Updated `windows` to 0.58.


© 2025 Tauri Contributors. CC-BY / MIT
