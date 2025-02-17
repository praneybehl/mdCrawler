Skip to content
# tauri@1.0.0-beta-rc.3
ReturnView on GitHub
  * `tauri::error::CreateWebview` now has the error string message attached. 
    * 7471e34 feat(core): add error message on `error::CreateWebview` (#1602) on 2021-04-23
  * If the dialog `defaultPath` is a file, use it as starting file path. 
    * aa7e273 feat: use `rfd::FileDialog#set_file_name` if `default_path` is a file (#1598) on 2021-04-23
  * Validate dialog option `defaultPath` - it must exists. 
    * cfa74eb feat(core): validate dialog `default_path` (it must exist) (#1599) on 2021-04-23
  * Expose `async_runtime` module. 
    * d3fdeb4 feat(core): expose `async_runtime` module (#1576) on 2021-04-21
  * Expose `PageLoadPayload` struct. 
    * 5e65b76 fix(core): expose `PageLoadPayload` struct (#1590) on 2021-04-22
  * Fixes the Message `command` name value on plugin invoke handler. 
    * 422dd5e fix(core): command name on plugin invoke handler (#1577) on 2021-04-21
  * Allow `window.__TAURI__.invoke` to be moved to another variable. 
    * be65f04 fix(core): make window.**TAURI**.invoke context free, fixes #1547 (#1565) on 2021-04-21
  * Make sure custom protocol is treated as secure content on macOS. 
    * 5909c1e Make sure custom protocol is handled as secure context on macOS (#1551) on 2021-04-22
  * Fixes macOS shortcut modifiers keycodes. 
    * ceadf2f fix(core): macos shortcut modifiers, closes #1542 (#1560) on 2021-04-21
  * Adds APIs to determine global and webview-specific URI scheme handlers. 
    * 938fb62 feat(core): expose custom protocol handler APIs (#1553) on 2021-04-21
    * a868cb7 refactor(core): clear `uri_scheme_protocol` registration function names (#1617) on 2021-04-25
  * The package info APIs now checks the `package` object on `tauri.conf.json`. 
    * 8fd1baf fix(core): pull package info from tauri.conf.json if set (#1581) on 2021-04-22
  * Change plugin trait `initialization` return type to `std::result::Result&lt;(), Box&lt;dyn std::error::Error&gt;&gt;`. 
    * 508eddc refactor(core): plugin initialization return value (#1575) on 2021-04-21
  * Fixes `sidecar` Command API. 
    * 99307d0 fix(core): sidecar command path (#1584) on 2021-04-22
  * Set LocalStorage and IndexedDB files path on Linux to `$HOME/.local/$\{bundleIdentifier}`. 
    * 5f033db feat(core): use bundle identifier on user data path (#1580) on 2021-04-22
  * Use bundle identifier instead of `Tauri` for user data path on Windows. 
    * 5f033db feat(core): use bundle identifier on user data path (#1580) on 2021-04-22


© 2025 Tauri Contributors. CC-BY / MIT
