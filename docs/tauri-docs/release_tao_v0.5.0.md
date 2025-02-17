Skip to content
# tao@0.5.0
ReturnView on GitHub
  * Move `global_shortcut` mod to the lib root.
    * 6e72e54c refactor: move `global_shortcut` mod to lib roo (#145) on 2021-07-20
  * Bump gtk-rs to version 0.14. This also introduces a new feature `ayatana` for developers to use updated `libayatana-appindicator` since the original `libappindicator` is no longer maintained.
    * 1c0f5274 chore: bump gtk to v0.14 (#173) on 2021-08-06
  * Remove Clipboard MenuItem on Linux since they only work on a few sepcific widget.
    * 969052ab fix(linux): remove clipboard menuitems on Linux (#150) on 2021-07-21
  * Fixes incorrect monitor size on Linux.
    * eb051931 fix(linux): incorrect monitor size, fixes: #175 (#176) on 2021-08-08
  * Fix `no key equivalent for Accelerator` for `Space`, `Escape`, `Minus` and `Equal` keycode.
    * ecd3c405 fix(accelerator): add missing KeyCode to prevent `no key equivalent for Accelerator` (#148) on 2021-07-20
  * Fix incorrect macOS Redo and Close Window shortcuts
    * f4d718a8 fix(macos): Fix incorrect Redo and CloseWindow accelerators (#166) on 2021-08-03
  *     * Support macOS tray icon template to adjust automatically based on taskbar color.
  * Images you mark as template images should consist of only black and clear colors. You can use the alpha channel in the image to adjust the opacity of black content, however.
  * 577458c4 feat(tray): Support macOS icon template (#162) on 2021-07-29
  * macOS: Add `with_parent_window()` on `WindowBuilder`.
    * 73c7aac7 feat(macOS): Allow creation of child Window (#160) on 2021-08-04
  * Removed `SystemTrayExtWindows::remove()`, the icon will be automatically removed when `SystemTray` is dropped.
    * cc9d2b17 refactor: refactor `system_tray` impl on windows (#153) on 2021-07-22
  * Add `MenuItem::SelectAll` implementation on windows.
    * 222adeb2 feat(window): add `Select all` native menu item (#146) on 2021-07-21
  * Add flags to support all other possible unix systems.
    * 546f51a3 Add flags to support other unix systems. (#142) on 2021-07-20
  * Fix confliction between `set_skip_taksbar(true)` and `set_visible(false)`.
    * 226e6611 fix(Windows): conflict between taskbar and visible (#172) on 2021-08-06


© 2025 Tauri Contributors. CC-BY / MIT
