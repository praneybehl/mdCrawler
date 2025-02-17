Skip to content
# wry@0.15.0
ReturnView on GitHub
  * On Windows and Linux, disable resizing maximized borderless windows. 
    * 313eaea fix(win,linux): disable resizing maximized borderless windows (#533) on 2022-03-30
  * Fixes a memory leak on the custom protocol response body on macOS. 
    * 36b985e fix(macos): custom protocol memory leak (#539) on 2022-04-03
  * Update tao to v0.8.0. 
    * 1c540b0 feat: update tao to 0.8, refactor tray features (#541) on 2022-04-07
  * The `tray` and `ayatana-tray` Cargo features are not enabled by default. 
    * 1c540b0 feat: update tao to 0.8, refactor tray features (#541) on 2022-04-07
  * **Breaking change:** Renamed the `ayatana` Cargo feature to `ayatana-tray` and added the `gtk-tray` feature. The default tray on Linux is now `libayatana-appindicator`. 
    * 1c540b0 feat: update tao to 0.8, refactor tray features (#541) on 2022-04-07


© 2025 Tauri Contributors. CC-BY / MIT
