Skip to content
# tauri@0.8.0
ReturnView on GitHub
  * Use native dialog on `window.alert` and `window.confirm`. Since every communication with the webview is asynchronous, the `window.confirm` returns a Promise resolving to a boolean value. - 0245833 feat(tauri) make `window.alert` and `window.confirm` available, fix #848 (#854) on 2020-07-18 - dac0ae9 chore(changes) add tauri-api to JS dialogs changefile on 2020-07-19
  * The notification’s `body` is now optional, closes #793. 
    * dac1db3 fix(tauri) notification body optional, requestPermission() regression, closes #793 (#844) on 2020-07-16
  * Fixes a regression on the storage of requestPermission response. ß - dac1db3 fix(tauri) notification body optional, requestPermission() regression, closes #793 (#844) on 2020-07-16
  * Plugin system added. You can hook into the webview lifecycle (`created`, `ready`) and extend the API adding logic to the `invoke_handler` by implementing the `tauri::plugin::Plugin` trait. 
    * 78afee9 feat(tauri) add plugin system for rust (#494) on 2020-07-12
  * Renaming `whitelist` to `allowlist` (see #645). 
    * a6bb3b5 refactor(tauri) rename `whitelist` to `allowlist`, ref #645 (#858) on 2020-07-19
  * Moving the webview implementation to webview, with the official Rust binding. This is a breaking change. IE support has been dropped, so the `edge` object on `tauri.conf.json &gt; tauri` no longer exists and you need to remove it. `webview.handle()` has been replaced with `webview.as_mut()`. - cd5b401 feature: import official webview rust binding (#846) on 2020-07-18


© 2025 Tauri Contributors. CC-BY / MIT
