Skip to content
# tao@0.12.0
ReturnView on GitHub
  * On macOS, fix native file dialogs hanging the event loop and having multiple windows would prevent `run_return` from ever returning. 
    * 5c9cc21a Fix native file dialogs freezing the event loop (#440) on 2022-06-22
  * Fix maximizing window.
  * On Windows, fix wrong fullscreen monitors being recognized when handling `WM_WINDOWPOSCHANGING` messages 
    * 054a34ec fix: fix assigning the wrong monitor when receiving Windows move events (#438) on 2022-06-22
  * Fix global hide others shortcut. 
    * dfae373e fix: global hide others shortcut (#447) on 2022-06-25
  * Fix window can’t be hidden when maximized. 
    * cd9ad33a Fix window can’t be hidden when maximized (#384) on 2022-06-15
  * On macOS, `WindowEvent::Resized` is now emitted in `frameDidChange` instead of `windowDidResize`. 
    * 54062ca1 fix: emit resize event on frame_did_change on macOS, closes #436 (#439) on 2022-06-22
  * On Linux, adds `SystemTrayBuilderExtLinux::with_temp_icon_dir` which sets a custom temp icon dir to store generated icon files. This may be useful when the application requires icons to be stored in a specific location, such as when running in a Flatpak sandbox. 
    * ce209d39 feat(linux) add `with_temp_icon_dir` builder extension (#452) on 2022-06-26
  * On Linux, store tray icons in `$XDG_RUNTIME_DIR`. This is preferred over `/tmp`, because this directory (typically `/run/user/{uid}`) is only readable for the current user. While `/tmp` is shared with all users. 
    * 01253829 feat(linux): store tray icons in `XDG_RUNTIME_DIR` (#449) on 2022-06-25
  * Do not emit the `ThemeChanged` event when the window theme is set and the system theme changes (the window keeps its theme in this scenario). 
    * aae6bec9 fix(macos): do not emit ThemeChanged event if window theme didn’t change (#430) on 2022-06-20
  * Remvoe `core-video-sys` dependency. 
    * 3bb09aa6 fix: remove core-video-sys dependency, closes #435 (#441) on 2022-06-22
  * The `theme` function now `Theme::Light` on macOS older than 10.14 and the initial theme setter has no effect instead of crashing the application. 
    * ba9c5571 fix(macos): guard theme APIs to not crash when running on 10.13 or older (#429) on 2022-06-20
  * Reduce `WM_PAINT` singal on event target window to prevent from webview2 delay. 
    * 5ca39af1 Remove most RedrawWindow to event target window (#427) on 2022-06-28


© 2025 Tauri Contributors. CC-BY / MIT
