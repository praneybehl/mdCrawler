Skip to content
# tauri@1.1.0
ReturnView on GitHub
  * Implement `api::http::ClientBuilder::max_redirections` for the default attohttpc client. 
    * ba5560b2 feat(core): implement max_redirections for attohttpc, ref #4795 (#4811) on 2022-07-31
  * Implement `From&lt;api::process::Command&gt; for std::process::Command`. 
    * 9f1d34c2 feat: implement From<Command> for std::process::Command, closes #4673 (#4836) on 2022-08-02
  * Added support to configuration files in TOML format (Tauri.toml file). 
    * ae83d008 feat: add support to TOML config file `Tauri.toml`, closes #4806 (#4813) on 2022-08-02
  * Enhance `SystemTray::with_icon` to accept `tauri::Icon`. 
    * 964926ff feat(core): enhance `SystemTray::with_icon` (#4849) on 2022-08-03
  * Fixes CLI parser ignoring inner subcommands. 
    * dcd50667 fix(core): parse inner CLI subcommands, closes #4688 (#4841) on 2022-08-02
  * Fix `fs.readDir` recursive option reading symlinked directories that are not allowed by the scope. 
    * f4121c12 fix(endpoints/fs/readDir): don’t read symlinks that are not allowed b… (#5123) on 2022-09-08
  * Fix typo in invalid state access panic message. 
    * c7fec3e1 fix typo in state.rs (#4699) on 2022-07-25
  * Fixes updater breaking the app icon in Finder. 
    * 58fc1f21 fix(updater): blank icon after update on macOS, closes #4613 (#4861) on 2022-08-04
  * Implement theme APIs for Linux. 
    * f21cbecd feat(core): implement theme APIs for Linux (#4808) on 2022-08-02
  * Implement `raw_window_handle::HasRawDisplayHandle` for `App` and `AppHandle`
    * 0ad9531d chore(deps): update tao to 0.13, wry to 0.20, rfd to 0.10, raw-window-handle to 0.5 (#4804) on 2022-07-31
  * Retain command line arguments in `api::process::restart`. 
    * 6218c31e fix(core): retain command line arguments on restart, closes #4760 (#4763) on 2022-07-25
  * Added APIs to create a system tray at runtime. 
    * 4d063ae9 feat(core): create system tray at runtime, closes #2278 (#4862) on 2022-08-09
  * Add `api::Command::encoding` method to set the stdout/stderr encoding. 
    * d8cf9f9f Command support for specified character encoding, closes #4644 (#4772) on 2022-07-28
  * Do not follow redirects when `api::http::ClientBuilder::max_redirections` is `0`. 
    * d576e8ae feat(core): do not follow redirects if `max_redirects` is 0 closes #4795 (#4812) on 2022-07-31
  * Added the `SystemTrayHandle::destroy` method. 
    * 4d063ae9 feat(core): create system tray at runtime, closes #2278 (#4862) on 2022-08-09
  * Added `native-tls-vendored` and `reqwest-native-tls-vendored` Cargo features to compile and statically link to a vendored copy of OpenSSL on Linux. 
    * 331f3460 feat(core): add option to use vendored openssl, closes #4470 (#4809) on 2022-08-02
  * Update windows to 0.39.0 and webview2-com to 0.19.1. 
    * e6d9b670 refactor: remove unneeded focus code (#5065) on 2022-09-03
  * Add `exists` function to the fs module. 
    * 3c62dbc9 feat(api): Add `exists` function to the fs module. (#5060) on 2022-09-15


© 2025 Tauri Contributors. CC-BY / MIT
