Skip to content
# tauri@1.0.0-rc.15
ReturnView on GitHub
  * Fixes filesystem scope check when using the HTTP API to upload files. 
    * 8ce5b762 fix: scope check when using the HTTP API to upload files closes #4312 on 2022-06-10
  * Fixes a memory leak in the command system. 
    * f72cace3 fix: never remove ipc callback & mem never be released (#4274) on 2022-06-05
  * Fixes the `Content-Type` header value when sending multipart requests using the `reqwest-client` feature. 
    * f6205afc fix(core): wrong Content-Type when using reqwest’s multipart, ref #4312 on 2022-06-10
  * Kill sidecar processes on app exit even when only the `shell-sidecar` feature is enabled. 
    * 6ba91272 Fix: sidecar cleanup when only `shell-sidecar` is enabled (#4254) on 2022-06-04
  * Fixes a crash when a request is made to `https://tauri.$URL` on Windows where `$URL` is not `localhost/**` e.g. `https://tauri.app`. 
    * 74457222 fix(core): handle requests to `https://tauri.*` on Windows (#4270) on 2022-06-05
  * Set notification icon to app icon on Linux. 
    * 235e448d fix: add a default icon to notifications on linux (#4283) on 2022-06-09
  * **Breaking change:** Revert the window creation to be blocking in the main thread. This ensures the window is created before using other methods, but has an issue on Windows where the program deadlocks when creating a window in a Tauri command if it is not `async`. The documentation now states that commands must be `async` in other to prevent it until the issue is fixed in Webview2. 
    * 69ae6f14 refactor(window): block main thread when creating a new window (#4298) on 2022-06-08
  * No longer ask for permission to send notifications and always allow it. 
    * f482b094 fix: remove notification permission prompt (#4302) on 2022-06-09
  * **Breaking change:** Removed the `settings` module. 
    * f482b094 fix: remove notification permission prompt (#4302) on 2022-06-09
  * **Breaking change** : Removed the `gtk-tray` and `ayatana-tray` Cargo features. 
    * 6216eb49 refactor(core): drop `ayatana-tray` and `gtk-tray` Cargo features (#4247) on 2022-06-02
  * Call `preventDefault()` in the mousedown event handler for `[data-tauri-drag-region]` elements. 
    * a0e20621 fix: preventDefault mousedown on data-tauri-drag-region, closes #4059 on 2022-06-13
  * Set permission to `0o700` for the tmp folder used to move the current AppImage on the updater process. 
    * b77877fd fix(updater): set tmp folder permissions (#4311) on 2022-06-12


© 2025 Tauri Contributors. CC-BY / MIT
