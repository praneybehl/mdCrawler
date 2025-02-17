Skip to content
# tao@0.7.0
ReturnView on GitHub
  * Fire `Event::LoopDestroyed` when the macOS dock `Quit` menu item is clicked. 
    * 34257a75 feat(macos): fire `LoopDestroyed` when the dock’s `Quit` item is clicked (#351) on 2022-03-27
  * Added `Event::DecorationsClick` (Windows only). 
    * 411af5b1 feat(windows): add `Event::DecorationsClick` (#352) on 2022-03-27
  * Enhance the `MenuItem::About` menu on Linux. **Breaking change:** The About variant now uses an struct instead of a string. 
    * 84c677fd refactor: fix and enhance the about menu on Linux (#347) on 2022-03-25
  * Fixes the About menu on Linux not being shown. 
    * 84c677fd refactor: fix and enhance the about menu on Linux (#347) on 2022-03-25
  * Properly fire `WindowEvent::Destroyed` on Linux when the `Window` is dropped. 
    * cdd4ac32 fix(events): properly fire `WindowEvent::Destroyed` on Linux (#349) on 2022-03-25
  * Properly change the window to fullscreen state if the builder instructs it to use `Fullscreen::Borderless(None)`. 
    * 5ecbac19 fix(window): fullscreen on Linux when builder is set to Borderless(None) (#348) on 2022-03-25
  * Fixes system tray item titles on Windows by forcing the string to be null-terminated. 
    * 7f900a16 fix(tray): force item title string to be null-terminated (#340) on 2022-03-09
  * Properly fire `WindowEvent::Destroyed` on macOS when the `Window` is dropped. 
    * efd3eecc fix(window): properly fire `WindowEvent::Destroyed` on macOS (#350) on 2022-03-25
  * Fix inconsist behaviour when setting menu on mac. 
    * 5abdbd1f Fix inconsist behaviour when setting menu on mac (#345) on 2022-03-17


© 2025 Tauri Contributors. CC-BY / MIT
