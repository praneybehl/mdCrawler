Skip to content
# tao@0.14.0
ReturnView on GitHub
  * Implement “always on bottom” as contrary to “always on top”. 
    * a2a7b726 Always on bottom (#522) on 2022-08-22
  * Fix calling android functions when package name contained escaped underscore. 
    * 6d8cc7e3 fix(android): unescape escaped underscore in package name (#531) on 2022-08-16
  * Add `Window::set_content_protection` for macOS and Windows. 
    * 802146fb feat: implement set_content_protection, closes #550 (#551) on 2022-09-04
  *     * Add DeviceEventFilter on Windows.
  * **Breaking** : On Windows, device events are now ignored for unfocused windows by default, use `EventLoopWindowTarget::set_device_event_filter` to set the filter level.
  * 5bbd4f8f Add DeviceEventFilter on Windows (#465) on 2022-08-17
  * Fix system tray creation after event loop starts on macOS. 
    * 759b7db3 fix(macos): retain tray to prevent segfault when event loop is running (#539) on 2022-08-20
  * Fix resize doesn’t work when calling with resizable. Also add platform specific note to `set_resizable`. On Linux, most size methods like maximized are async and do not work well with calling sequentailly. For setting inner or outer size, you don’t need to set resizable to true before it. It can resize no matter what. But if you insist to do so, it has a `100, 100` minimum limitation somehow. For maximizing, it requires resizable is true. If you really want to set resizable to false after it. You might need a mechanism to check the window is really maximized. 
    * 4524d5d3 fix(Linux): resize doesn’t work when calling with resizable, fix #545 (#553) on 2022-09-08
  * Add `Window::is_focused`. 
    * 7d2eeeeb feat: Window::is_focused (#533) on 2022-08-17
  * On Linux, fix global shortcut are never triggered when a Lock key is ON, eg. NumLock, CapsLock. 
    * 07e3c1f5 fix(linux/globalShorcut): extract needed mods from event state, closes #307, closes #537 (#538) on 2022-08-19
    * 871ad037 chore: remove changefile, bug still exists on 2022-08-20
    * 7e5556e0 fix(linux/globalShortcut): grab the shortcut with extra mods, closes #307 (#540) on 2022-08-20
  * Disables the global shortcut manager on wayland as its X11-specific. 
    * 27ab6f4d fix(linux/globalShortcut): disable on wayland (#543) on 2022-08-26
  * Added `SystemTrayExtMacOS::set_title` to `SystemTray` and `SystemTrayBuilderExtMacOS::with_title` to set the tray icon title on MacOS 
    * 972307dd feat: added text support to system tray for macos, closes #65 (#554) on 2022-09-10
  * Update `windows-rs` to the latest 0.39.0 release.


The `alloc` feature has been removed, which means it no longer accepts Rust `String` or `&amp;str` parameters and implicitly converts them to `PWSTR` or `PSTR`.
For string literals, that feature was replaced with `s!()` and `w!()` macros which null terminate the string literal at compile time and convert to UTF-16 if necessary. The `s!()` macro is fine, however the `w!()` macro uses `HSTRING` types from WinRT for maximum compatibility with WinRT types. Since Tao only uses Win32 APIs, this change relies on `util::encode_wide` to convert to a `Vec&lt;u16&gt;` instead.
  * 84e1a9f9 Update windows to 0.39.0 (#544) on 2022-08-31


© 2025 Tauri Contributors. CC-BY / MIT
