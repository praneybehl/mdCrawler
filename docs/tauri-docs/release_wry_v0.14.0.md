Skip to content
# wry@0.14.0
ReturnView on GitHub
  * Added `close_devtools` function to `Webview`. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28
  * Hide the devtool functions behind the `any(debug_assertions, feature = &quot;devtools&quot;)` flag. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28
  * **Breaking change:** Renamed the `devtool` function to `open_devtools`. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28
  * Enable tab navigation on macOS. 
    * 28ebedc fix(macOS): enable tab navigation on all elements, fixes #406 (#512) on 2022-03-03
  * Added `is_devtools_open` function to `Webview`. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28
  *     * Expose methods to access the underlying native handles of the webview.
  * **Breaking change** : `WebviewExtWindows::controller` now returns the controller directly and not wrapped in an `Option`
  * e54afec feat: expose webview native handles, closes #495 (#513) on 2022-03-03
  * Add navigation handler to decide if an url is allowed to navigate. 
    * aa8af02 feat: Implement navigation event and cancellation, closes #456 (#519) on 2022-03-18
  * **Breaking change** : Renamed the `devtool` feature to `devtools`. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28
  * **Breaking change:** Renamed the `with_dev_tool` function to `with_devtools`. 
    * bf3b710 feat: add function to close the devtool and check if it is opened (#529) on 2022-03-28


© 2025 Tauri Contributors. CC-BY / MIT
