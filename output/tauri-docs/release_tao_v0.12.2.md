Skip to content
# tao@0.12.2
ReturnView on GitHub
  * On Windows, fix assigning the wrong mintor rect to undecorated maximized window. This caused a blank window downstream in wry and tauri. 
    * 9d97e4a6 fix(windows): get correct monitor in `WM_NCCALCSIZE`, closes #471 (#472) on 2022-07-12
  * Fixed set_inner_size is reset when resizable is set to false. 
    * 17203d08 fix: fixed inner_size even if resizable is set to false (#461) on 2022-07-05
  * On Windows, prevent ghost window from showing up in the taskbar after either several hours of use or restarting `explorer.exe`. 
    * feb21272 fix(windows): prevent ghost window from showing up on taskbar (#489) on 2022-07-21
  * Add theme feature on Linux. 
    * 74425e8e feat: add theme feature on Linux (#468) on 2022-07-10
  * Fix maximizing window on Linux. 
    * 01fb1d6c fix: maximizing window on linux, closes #442 (#456) on 2022-07-12
  * On macOS, fallback resize event for NSWindow to handle. 
    * ab2e57e9 On macOS, fallback resize event for NSWindow to handle on 2022-07-12
  * Add `CustomMenuItem::set_icon`. Only implemented on macOS for now. 
    * 13f9f182 feat(macos): implement CustomMenuItem::set_icon() (#459) on 2022-07-07
  * On Windows, subscribe to taskbar restart event and re-add the system tray icon. Also skip the window from the taskbar if it was already skipped. 
    * 9450329e fix(windows): subscribe to taskbar restart event, closes #476 (#487) on 2022-07-21
  * On Windows, fix focus events being sent to inactive windows. 
    * 23ae71b7 fix(windows): fix focus events being sent to inactive windows. (#488) on 2022-07-21


© 2025 Tauri Contributors. CC-BY / MIT
