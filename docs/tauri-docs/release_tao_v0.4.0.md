Skip to content
# tao@0.4.0
ReturnView on GitHub
  * On Windows, Allow resizing of `decorations: false` aka borderless window. 
    * f35dd03d fix(windows): fix aero-snap and resizing of borderless window, fixes #103 #104 (#110) on 2021-07-07
  * Do not close the window on `CloseRequested` event and let the user handle it, keeping compatibility with macOS and Windows behavior. 
    * ea7330ef fix(linux): do not close window on `CloseRequested` event (#114) on 2021-07-05
  * On Windows, fix Aero-Snap for `decorations: false` aka borderless window. 
    * f35dd03d fix(windows): fix aero-snap and resizing of borderless window, fixes #103 #104 (#110) on 2021-07-07
  * Implement `MonitorHandle` and related methods on Linux. 
    * 6fcfa629 feat(linux): implement `MonitorHandle` and related methods (#125) on 2021-07-12
  * Add `is_menu_visilbe` getter on `Window`
    * 308411ca feat: add `is_menu_visible` (#108) on 2021-07-06
  * On macOS, make sure the `set_focus` is triggered even if the window is not visible. 
    * 3da167aa fix(macos): `set_focus` should be triggered even if the window isn’t visible (#128) on 2021-07-14
  * Fix `with_visible(bool)` in `WindowBuilder` for macOS. 
    * a0ac7075 fix(macos): Window state (`visible`) (#119) on 2021-07-06
  * Mark enums as `#[non_exhaustive]` to prevent breaking changes on enum update. 
    * 9b906f50 refactor: add `#[non_exhaustive]` attributes to enums (#90) on 2021-07-07
  * Remove `with_focus` and `focus` field in `WindowAttribute`. Use `set_focus` instead in most cases. 
    * e2399bc9 Remove `with_focus` and `focus` field in `WindowAttribute` (#121) on 2021-07-06
  * Revert d344825 and move `set_skip_taskbar` back behind a `WindowExtWindows` and `WindowExtUnix`. 
    * a641d3a3 refactor: Revert d344825, move `set_skip_taskbar` behind platform-ext (#118) on 2021-07-06
  * `SystemTray` expose `set_menu` to update the system tray menu once created. 
    * 578dd23e feat: implement `set_menu` for system tray (#106) on 2021-07-14
  * Only show window behaviour when it is visible. winuser::ShowWindow will show the window and make with_visible(false) obsolete. 
    * ff0903f6 Only show window behaviour when it is visible (#126) on 2021-07-14
  * Add `with_skip_taskbar` behind `WindowBuilderExtWindows` and `WindowBuilderExtUnix`. 
    * e7cdb950 feat(taskbar): add `with_skip_taskbar` for windows and linux (#127) on 2021-07-14


© 2025 Tauri Contributors. CC-BY / MIT
