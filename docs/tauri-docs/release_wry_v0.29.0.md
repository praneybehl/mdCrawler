Skip to content
# wry@0.29.0
ReturnView on GitHub
  * `c09dd7b`(#968) Remove ActionBar handling from wry. If you want to hide the action bar, hide it using the `themes.xml` file in your android project or inherit `WryActivity` class and use `getSupportActionBar()?.hide()` in the `onCreate` method.
  * `2b56bfa`(#966) Add support for `WebViewBuilder::with_html` and `WebViewAttributes.html` on Android.
  * `d2c1819`(#969) On Linux, replace `linux-header` flag with `linux-body` flag. Request headers are enabled by default. Add request body on custom protocol but it’s behind the flag.
  * `f7dded4`(#955) The bug was reported in tauri repo: https://github.com/tauri-apps/tauri/issues/5986
With input method preedit disabled,fcitx can anchor at edit cursor position. the pre-edit text will not disappear,instead it shows in the fcitx selection window below the input area.
  * `2b56bfa`(#966) Set base url and origin to null for `WebViewBuilder::with_html` and `WebViewAttributes.html` for consistency on all platforms.


© 2025 Tauri Contributors. CC-BY / MIT
