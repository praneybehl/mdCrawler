Skip to content
# wry@0.17.0
ReturnView on GitHub
  * Add option to enable/disable zoom shortcuts for WebView2, disabled by default. 
    * 494a110 WebView2: Enable/disable platform default zooming shortcuts, closes #569 (#574) on 2022-05-15
  * Prevent memory leak on macOS. 
    * 16d1924 fix: prevent memory leak on macOS, closes #536 (#587) on 2022-05-20
  * Update the `windows` crate to the latest 0.37.0 release and `webview2-com` to 0.16.0 to match.


The `#[implement]` macro in `windows-implement` and the `implement` feature in `windows` depend on some `const` generic features which stabilized in `rustc` 1.61. The MSRV on Windows targets is effectively 1.61, but other targets do not require these features.
The `webview2-com` crate specifies `rust-version = &quot;1.61&quot;`, so `wry` will inherit that MSRV and developers on Windows should get a clear error message telling them to update their toolchain when building `wry` or anything that depends on `wry`. Developers targeting other platforms should be able to continue using whatever toolchain they were using before.
  * 9d9d9d8 Update windows-rs to 0.37.0 and webview2-com to 0.16.0 to match (#592) on 2022-05-23


© 2025 Tauri Contributors. CC-BY / MIT
