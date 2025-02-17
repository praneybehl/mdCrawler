Skip to content
# wry@0.11.0
ReturnView on GitHub
  * Allow resizing of borderless window on Windows 
    * bd10b8e feat(Windows): resize borderless window (#333) on 2021-07-15
  * Mark enums as `#[non_exhaustive]` to prevent breaking changes on enum update. 
    * f07ae14 refactor: add `#[non_exhaustive]` attributes to enums (#304) on 2021-07-08
  * Bump tao to `0.4`. Please refer to `tao` changelog for more details. 
    * 6eb10d4 bump `tao` to 0.4 and fix examples (#329) on 2021-07-14
  *     * Add `focus` method to `Webview`
  * Add `WebviewExtWindows` trait with `controller` method
  * 621ed1f feat: add `.focus()` to `Webview` (#325) on 2021-07-05
  * 96b7b94 Add controller method instead (#326) on 2021-07-07
  * macOS: Remove handler in the webview as it should be handled with the menu. 
    * 5a9df15 fix(macos): Remove keypress handler in the webview for copy/paste/cut (#328) on 2021-07-07
  * Fixes multiple custom protocols registration on Windows. 
    * 923d346 fix(windows): multiple custom protocols, closes #323 (#324) on 2021-07-02


© 2025 Tauri Contributors. CC-BY / MIT
