Skip to content
# tauri@1.2.2
ReturnView on GitHub
  * Invoke event listener in windows safely to avoid causing uncaught errors in windows that have loaded external urls 
    * c14b1df3 fix(core): Invoke event listener in windows safely to avoid causing uncaught errors in windows that have loaded external urls (#5563) on 2022-12-08
  * Cleanup sidecar and tray icons when calling `app.exit()` from JS. 
    * 0f269608 fix(core/api): cleanup before exit (#5765) on 2022-12-07
  * Fix compatibility with older Linux distributions. 
    * b490308c fix(core): compilation error on older Linux versions, fixes #5684 (#5697) on 2022-11-28
  * Add `tauri::Builder::enable_macos_default_menu` to enable or disable the default menu creation on macOS. 
    * 8866ecac feat(core): add `tauri::Builder::enable_macos_default_menu` (#5756) on 2022-12-07
    * b293da35 fix(changes): change `enable_macos_default_menu` bump to patch on 2022-12-08


© 2025 Tauri Contributors. CC-BY / MIT
