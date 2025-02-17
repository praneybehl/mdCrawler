Skip to content
# tao@0.11.0
ReturnView on GitHub
  * **Breaking change** `SystemTrayBuilder::new` and `SystemTray::set_icon` now takes `system_tray::Icon` on all platforms. 
    * 0a98eb39 refactor: system tray icons (#328) on 2022-06-06
  * Allow to disable system tray menu only on Left Click. 
    * 0858356f feat(macos): allow to disable system tray menu on left click, closes #317 (#329) on 2022-06-09
  * Connect mouse wheel event with GTK window. 
    * f9e0b734 connect mouse wheel event with GTK window (#412) on 2022-06-08
  * Support child window on Linux. 
    * f1e8d755 feat: support child window on linux, closes #273 (#415) on 2022-06-13
  * Support theme on macOS. 
    * 8af4d8f0 feat: support theme on macOS (#408) on 2022-06-01
  * Add `Window::set_ignore_cursor_events`
    * 4fa87617 feat: `Window::set_ignore_cursor_events`, closes #184 (#421) on 2022-06-13


© 2025 Tauri Contributors. CC-BY / MIT
