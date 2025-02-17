Skip to content
# wry@0.27.0
ReturnView on GitHub
  * Add function to dispatch closure with the Android context. 
    * a9e186c feat(android): add function to dispatch closure to the Android context (#864) on 2023-02-06
  * On macOS, fix crash when getting dragging position. 
    * a8f7cef Fix crash when getting drag position (#867) on 2023-02-04
  * On Android, `wry` can again load assets from the apk’s `asset` folder via a custom protocol. This is set by `WebViewBuilder`’s method `with_asset_loader`, which is exclusive to Android (by virtue of existing within `WebViewBuilderExtAndroid`). 
    * 077eb3a fix(android): restore asset loading functionality to android (fix: #846) (#854) on 2023-02-07
  * Update `webview2-com` to `0.22` and `windows-rs` to `0.44` which bumps the MSRV of this crate on Windows to `1.64`. 
    * 496bfb5 chore(deps): update to windows-rs 0.44 and webview2-com 0.22 (#871) on 2023-02-06


© 2025 Tauri Contributors. CC-BY / MIT
