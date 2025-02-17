Skip to content
# tao@0.13.2
ReturnView on GitHub
  * Remove the NSStatusItem from the menu bar when the `SystemTray` instance is dropped. 
    * aca4d3fb feat(tray): remove from tray on `Drop` on macOS (#520) on 2022-08-04
  * Fixes `Window::is_decorated` always returning `true` on macOS. 
    * c3e076e9 fix(window): `is_decorated` wrong return value, closes #518 (#519) on 2022-08-04
  * Fix theme feature to support Darker theme on Linux. 
    * c6d6c011 fix: support Darker theme on Linux (#511) on 2022-08-03
  * Add `Window::is_minimized()`. 
    * 9c348154 feat: add `Window::is_minimized()`, closes #257 (#486) on 2022-08-06
  * Implement `SystemTrayBuilder::with_tooltip` and `SystemTray::set_tooltip` on macOS. 
    * 14e26568 feat(macos): add `SystemTray::set_tooltip`, ref #409 (#410) on 2022-08-03
  * On Windows, fix a ghost window appearing occasionally when clicking the tray icon. 
    * ad1f641f fix(windows): fix tray event window showing up on click, closes #506 (#507) on 2022-08-02
  * Added `SystemTrayBuilder::with_id` and the `id` field to `Event::TrayEvent` for better multitray support. 
    * 4ea78bcb feat(tray): add identifier to allow multiple tray setup (#514) on 2022-08-04
  * Hide the app indicator when dropping `SystemTray` on Linux 
    * 9c6a543c feat(tray): hide indicator on drop on Linux (#521) on 2022-08-04


© 2025 Tauri Contributors. CC-BY / MIT
