Skip to content
# tao@0.15.0
ReturnView on GitHub
  * Add support for parsing `ArrowUp`, `ArrowDown`, `ArrowLeft` and `ArrowRight` in a str as valid key. Previously only `Up`, `Down`, `Left` and `Right` worked. 
    * 5e85dbef fix: parse `Arrow*` in a accelerator string (#609) on 2022-10-31
  * Add `WindowBuilder::with_content_protection`. 
    * 8084c800 feat: add `WindowBuilder::with_content_protection` (#605) on 2022-10-30
  * On macOS, fix default cursor always being arrow cursor 
    * 1359fccf On macOS, fix default cursor always being arrow cursor (#614) on 2022-11-06
  * On Windows, fixed focus event emission on minimize. 
    * 37bca310 fix(windows): fix focus event emission on minimize (#559) on 2022-09-21
  * Update jni to 0.20. 
    * 38fef108 feat(android): update to jni 0.20 (#610) on 2022-10-31
  * On Linux, add DeviceEvent::Key. 
    * 775974d7 feat(linux): add DeviceEvent::Key (#600) on 2022-10-21
  * fix(linux): Improve event loop process on Linux a bit. This changes only a few check and should make dragging windows on egui smoother. 
    * b529eec9 fix(linux): improve event loop process on Linux (#587) on 2022-10-12
  * Fix inverted delta in `WindowEvent::MouseWheel` on Linux 
    * 8451f754 fix: Inverse mouse scroll wheel on Linux (#585) on 2022-10-11
  * Add `EventLoopExtMacOS::set_activate_ignoring_other_apps` on macOS. 
    * d2c6a91c feat: add `EventLoopExtMacOS::set_activate_ignoring_other_apps` (#612) on 2022-11-01
  * Add `WindowExtMacOS::set_allows_automatic_window_tabbing`, `WindowExtMacOS::allows_automatic_window_tabbing`, and `WindowBuilderExtMacOS::with_automatic_window_tabbing` on macOS. 
    * 7c7ce8ab feat(macos): add `allows_automatic_window_tabbing` APIs (#586) on 2022-10-12
  * Support cross compiling for macos from a non macos host. 
    * 2edc7418 Fix cross compilation. (#601) on 2022-10-25
  * Add `WindowExtMacOS::is_doucmented_edited` and `WindowExtMacOS::set_is_doucmented_edited` on macOS. 
    * 33fdeab6 feat(macos): add document edited apis, closes #268 (#287) on 2022-10-03
  * On macOS, scale menu item icons height to 18. 
    * 5e3d344c fix(macos): scale menu item icon height to 18, closes #584 (#590) on 2022-10-15
  * Add support for the ”+” key in menu accelerators using `KeyCode::Plus` or the “Plus” keyword. See documentation for `KeyCode::Plus` for notes on platform-dependent behaviour. 
    * 937aba7b feat(menus): add support for Plus key in accelerators, closes #227 (#573) on 2022-09-27
  * Add the application name to the “Quit” and “Hide” native menu items on macOS. 
    * 65f768e5 fix(menus): add app name to native Quit and Hide items on macOS, closes #536 (#570) on 2022-09-25
  * Fix the native Services menu on macOS. 
    * d343abf8 fix(menus): fix macOS Services menu not working, closes #243 (#569) on 2022-09-25
  * Scale the tray icon according to its aspect ratio on macOS. 
    * dbbfd97c feat(macos): support to change tray icon aspect ratio, close #564 (#565) on 2022-09-25
  * Add builder methods on Linux to control the drawing behavior of the window. `WindowBuilderExtUnix::with_double_buffered`, `WindowBuilderExtUnix::with_rgba_visual` and `WindowBuilderExtUnix::with_app_paintable`
    * 0637c605 feat(linux): add drawing behavior builder methods, closes #567 (#572) on 2022-09-27
  * On Windows, show Window menu (also known as the System menu or Control menu) in response to <kbd>Alt+Space</kbd>. 
    * 0d76094e fix(Windows): show window menu on alt+space, closes 547 (#593) on 2022-10-19
  * On Windows, fix icons specified on `WindowBuilder` not taking effect for windows created after the firt one. 
    * d72b1e1a fix(Windows): fix icons specified on `WindowBuilder` not taking effect for windows created after the first one (#604) on 2022-10-27
  * Added tabbing identifier APIs on macOS. 
    * 8815291e feat(macos): add tabbing identifier APIs (#592) on 2022-10-18
  * On Linux, reduce channel redirect. Now sending user events and redraw request will send to event loops directly. 
    * dd86a9eb refactor(linux): reduce channel redirect (#588) on 2022-10-16
  * Add `WindowBuilder::with_focused` to specify whether to initially focus the window or not. 
    * e42ff071 feat: add `WindowBuilder::with_focused` (#576) on 2022-10-03
  * Add APIs for disabling the individual window controls on desktop platforms, `Window::set_closable`, `Window::is_closable`, `WindowBuilder::with_closable`, `Window::set_minimizable`, `Window::is_minimizable`, `WindowBuilder::with_minimizable`, `Window::set_maximizable`, `Window::is_maximizable`, `WindowBuilder::with_maximizable`. See the docs for platform-specific notes, especially regarding Linux. 
    * a50fd867 feat: options to disable individual window controls, closes #116 (#574) on 2022-10-11
  * Add `Window::title` to get the current window title. 
    * c50529b3 feat: add `Window::title` getter, closes #546 (#579) on 2022-10-04
  * Default to MOD_NOREPEAT for registering global shortcuts / hotkeys via win32 RegisterHotKey on Windows. This prevents shortcuts from repeatedly activating when the accelerator is pressed and held down, and ensures that we maintain platform-agnostic consistency. 
    * d15a756c Prevent global shortcut activation from repeating on Windows (#602) on 2022-10-23


© 2025 Tauri Contributors. CC-BY / MIT
