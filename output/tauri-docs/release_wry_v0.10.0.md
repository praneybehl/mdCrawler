Skip to content
# wry@0.10.0
ReturnView on GitHub
  * Add WebViewAttributes 
    * 81f3218 Add WebViewAttributes (#286) on 2021-06-04
  * Add `with_web_context` method that can work well with builder pattern. 
    * 48f53a3 Add `with_web_context` method (#292) on 2021-06-13
  * Change the custom protocol handler on macOS so it returns a response on error and a status code on success. 
    * 6b869b1 fix(macos): custom protocol response with status code + error response (#279) on 2021-05-20
  * Update signature of custom protocol closure. It should return a mime type string now. 
    * cc9fc4b Add mimetype to return type of custom protocol (#296) on 2021-06-13
  * Fix webview creation when using new_any_thread of event loop. 
    * 4d62cf5 Fix webview creation when using new_any_thread on Windows (#298) on 2021-06-18
  * Remove `Dispatcher`, `dispatch_script` and `dispatcher` in the `webview` module and add a `js` parameter to `evaluate_script`. 
    * de4a5fa refactor: remove `Dispatcher` and related methods, closes #290 (#291) on 2021-06-09
  * Removes the `image` dependency. 
    * 1d5cc59 chore(deps): remove `image` dependency (#274) on 2021-05-19
  * Bump tao to `0.3` and add more examples.


_For more details, please refer to`tao` changelog._
  * cd4697e bump `tao` to 0.3 with examples (#294) on 2021-06-21
  * Add `wry::webview::WebContext`. It’s now a required argument on `WebViewBuilder::build`. 
    * 761b2b5 webdriver support (#281) on 2021-06-08


© 2025 Tauri Contributors. CC-BY / MIT
