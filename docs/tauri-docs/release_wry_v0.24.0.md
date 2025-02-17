Skip to content
# wry@0.24.0
ReturnView on GitHub
  * Changed env vars used when building for Android; changed `WRY_ANDROID_REVERSED_DOMAIN` to `WRY_ANDROID_PACKAGE` and `WRY_ANDROID_APP_NAME_SNAKE_CASE` to `WRY_ANDROID_LIBRARY`. 
    * dfe6a5e refactor: improve android env vars naming (#829) on 2022-12-30
  * Fixes Android initialization scripts order. 
    * 7f819c0 fix(android): initialization scripts order (#808) on 2022-12-12
  * Remove redundant `.clone()` calls and avoid unnecessary heap allocations. 
    * 45f2b21 perf: remove redundant `.clone()` calls and avoid unnecessary heap allocations (#812) on 2022-12-14
  * Change return type of custom protocol handlers from `Result&lt;Response&lt;Vec&lt;u8&gt;&gt;&gt;` to `Result&lt;Response&lt;Cow&lt;&#39;static, [u8]&gt;&gt;&gt;`. This allows the handlers to return static resources without heap allocations. This is effective when you embed some large files like bundled JavaScript source as `&amp;&#39;static [u8]` using `include_bytes!`. 
    * ddd3461 perf: Change return type of custom protocol handler from `Vec&lt;u8&gt;` to `Cow&lt;&#39;static, [u8]&gt;`, closes #796 (#797) on 2022-12-12
  * Ensures that the script passed to `.with_initialization_script(&quot;here&quot;)` is not empty. 
    * ceb209e fix empty string bug (fix: #833) (#836) on 2023-01-08
  * Add APIs to process webview document title change. 
    * 14a0ee3 feat: add document title changed handler, closes #804 (#825) on 2022-12-30
  * Evaluate scripts after the page load starts on Linux and macOS. 
    * ca7c8e4 fix(unix): race condition on script eval (#815) on 2022-12-14
  * Improve panic error messages on the build script. 
    * 5b9f21d feat: improve build script panic messages (#807) on 2022-12-12
  * Add `WebViewBuilder::with_url_and_headers` and `WebView::load_url_with_headers` to navigate to urls with headers. 
    * 8ae93b9 feat: add headers when loading URLs, closes #816 (#826) on 2023-01-01
    * e246bd1 chore: update headers change file on 2023-01-01
  * Change class declare name from `UIViewController` to `WryNavigationDelegate` to avoid class name conflict on iOS. 
    * fca42a0 fix(ios): navigation delegate class name conflict (#824) on 2022-12-27
  * Rerun build script if the `WRY_ANDROID_KOTLIN_FILES_OUT_DIR` directory changes. 
    * 1cf92e2 feat(build): rerun if kotlin out directory changes (#839) on 2023-01-10
  * On Windows, Add `WebviewBuilderExtWindows::with_theme` and `WebviewExtWindows::set_theme` to change webview2 theme. 
    * 563a497 feat(webview2): add theme API, closes #806 (#809) on 2022-12-13


© 2025 Tauri Contributors. CC-BY / MIT
