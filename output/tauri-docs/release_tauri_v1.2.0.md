Skip to content
# tauri@1.2.0
ReturnView on GitHub
  * Add `accept_first_mouse` option for macOS windows. 
    * 95f467ad feat(core): add window `accept_first_mouse` option, closes #5347 (#5374) on 2022-10-17
  * Add new app-specific `BaseDirectory` enum variants `AppConfig`, `AppData`, `AppLocalData`, `AppCache` and `AppLog` along with equivalent functions in `path` module and deprecated ambiguous variants `Log` and `App` along with their equivalent functions in `path` module. 
    * 5d89905e feat(api): add app-specific directory APIs, closes #5263 (#5272) on 2022-09-28
  * Set the correct mimetype when streaming files through `asset:` protocol 
    * 39443b43 fix(core): set correct mimetype for asset protocol streams, closes #5203 (#5210) on 2022-09-30
    * 2d9c2b47 Revert “fix(core): set correct mimetype for asset protocol streams, closes #5203 (#5210)” on 2022-09-30
    * 9b1a6a1c fix(core): set correct mimetype for asset protocol streams, #5203 (#5536) on 2022-11-04
  * Disable automatic window tabbing on macOS when the `tabbing_identifier` option is not defined, the window is transparent or does not have decorations. 
    * 4137ab44 feat(macos): add `tabbing_identifier` option, closes #2804, #3912 (#5399) on 2022-10-19
  * The custom protocol now validates the request URI. This has implications when using the `asset` protocol without the `convertFileSrc` helper, the URL must now use the `asset://localhost/$filePath` format. 
    * 357480f4 feat(core): custom protocol headers on Linux, closes #4496 (#5421) on 2022-10-17
  * Escape glob special characters in files/directories when dropping files or using the open/save dialogs. 
    * 4cbdf0fb fix(core): escape glob characters in drop/dialogs , closes #5234 (#5237) on 2022-10-05
  * Properly emit events with object payload. 
    * 79dd6e16 fix(core): properly emit events with object payload, closes #5482 (#5492) on 2022-10-27
  * Fixes access to the `WebviewWindow.getByLabel` function in a `tauri://window-created` event listener. 
    * e00b1e5f fix(core): update metadata before window-created listeners, closes #5191 (#5458) on 2022-10-22
  * Fixes resource reading being always rejected by the scope. 
    * a06dc699 fix(core): canonicalize resource dir to fix scope check, closes #5196 (#5218) on 2022-09-29
  * Fixes `__TAURI_PATTERN__` object freeze. 
    * 49f06ca4 fix: deepfreeze check by prop (#5407) on 2022-10-17
  * Readd the option to create an unfocused window via the `focused` method. The `focus` function has been deprecated. 
    * 4036e15f feat(core): reimplement window initial focus flag, closes #5120 (#5338) on 2022-10-08
  * Add `hidden_title` option for macOS windows. 
    * 321f3fed feat(macos): `title_bar_style` and `hidden_title` window options, closes #2663 (#3965) on 2022-09-30
  * Custom protocol headers are now implemented on Linux when running on webkit2gtk 2.36 or above. 
    * 357480f4 feat(core): custom protocol headers on Linux, closes #4496 (#5421) on 2022-10-17
  * Add `App::show()`, `AppHandle::show()`, `App::hide()` and `AppHandle::hide()` for hiding/showing the entire application on macOS. 
    * 39bf895b feat(macOS): Add application `show` and `hide` methods (#3689) on 2022-10-03
  * Fix a deadlock when modifying the menu in the `on_menu_event` closure. 
    * ae65951b fix(core): fix deadlock in `on_menu_event`, closes #5254 (#5257) on 2022-09-28
  *     * 7d9aa398 feat: bump MSRV to 1.59 (#5296) on 2022-09-28
  * Resolve base system directory in shell scope. 
    * 99fe1c56 fix(core): resolve base dir in shell scope, closes #5480 (#5508) on 2022-11-04
  * Added `tabbing_identifier` to the window builder on macOS. 
    * 4137ab44 feat(macos): add `tabbing_identifier` option, closes #2804, #3912 (#5399) on 2022-10-19
  * Add `title_bar_style` option for macOS windows. 
    * 321f3fed feat(macos): `title_bar_style` and `hidden_title` window options, closes #2663 (#3965) on 2022-09-30
  * Added methods to set the system tray title on macOS. 
    * 8f1ace77 feat: expose `set_title` for MacOS tray (#5182) on 2022-09-30
  * Added the `user_agent` option when creating a window. 
    * a6c94119 feat(core): expose user_agent to window config (#5317) on 2022-10-02


© 2025 Tauri Contributors. CC-BY / MIT
