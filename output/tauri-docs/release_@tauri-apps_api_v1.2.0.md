Skip to content
# @tauri-apps/api@1.2.0
ReturnView on GitHub
  * Added the `acceptFirstMouse` window option. 
    * 95f467ad feat(core): add window `accept_first_mouse` option, closes #5347 (#5374) on 2022-10-17
  * Fix incorrect return type on `fs/exists`
    * ca3cd8b3 fix(api): fs/exists return type previously set to void when it should be boolean (#5252) on 2022-09-29
  * Initialize `Monitor` instances with the correct classes for `position` and `size` fields instead of plain object. 
    * 6f41a271 fix(api.js): fix `Monitor` initialization, closes #4672 (#5314) on 2022-09-30
  * **Breaking change:** Node.js v12 is no longer supported. 
    * 1129f4f5 refactor: simplify api.js bundling (#4277) on 2022-10-04
  * Add new app-specific `BaseDirectory` enum variants `AppConfig`, `AppData`, `AppLocalData`, `AppCache` and `AppLog` along with equivalent functions in `path` module and deprecated ambiguous variants `Log` and `App` along with their equivalent functions in `path` module. 
    * 5d89905e feat(api): add app-specific directory APIs, closes #5263 (#5272) on 2022-09-28
  * Fix `dialog.save` return type 
    * 8357ce5b Fix dialog.save return type (#5373) on 2022-10-08
  * Added support to `FormData` on the `Body.form` function. 
    * aa119f28 feat(api): add FormData support on Body.form, closes #5545 (#5546) on 2022-11-04
  * Added `show` and `hide` methods on the `app` module. 
    * 39bf895b feat(macOS): Add application `show` and `hide` methods (#3689) on 2022-10-03
  * Added `tabbingIdentifier` window option for macOS. 
    * 4137ab44 feat(macos): add `tabbing_identifier` option, closes #2804, #3912 (#5399) on 2022-10-19
  * Added `tabbing_identifier` to the window builder on macOS. 
    * 4137ab44 feat(macos): add `tabbing_identifier` option, closes #2804, #3912 (#5399) on 2022-10-19
  * Added the `user_agent` option when creating a window. 
    * a6c94119 feat(core): expose user_agent to window config (#5317) on 2022-10-02


© 2025 Tauri Contributors. CC-BY / MIT
