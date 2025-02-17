Skip to content
# tao@0.6.0
ReturnView on GitHub
  * Update to gtk 0.15 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Emit errors when parsing an invalid accelerator from a string. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add support for more accelerator keys: `,` `-` `.` `=` `;` `/` `\` `&#39;` ``` `[` `]` `Space` `Tab` and `F13`-`F24`
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Increased Borderless window resizing inset. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Update to 2021 edition and msrv to 1.56 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * **Breaking:** Rename the `Exit` variant of `ControlFlow` to `ExitWithCode`, which holds a value to control the exit code after running. Add an `Exit` constant which aliases to `ExitWithCode(0)` instead to avoid major breakage. This shouldn’t affect most existing programs. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fixes the `MenuItem::Quit` behavior on Windows. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add support for `SPACE` shortcut key on Windows. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  *     * Fix redrawn event that causing infinite lopp on Linux
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix linux native menu items not working. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  *     * Fix resizing undecorated window on Linux.
  * Undecorated window can be resized using touch on Linux.
  * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix focus events not firing on Linux 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add monitor selection when fullscreen on Linux and close possible way to create VideoMode on Linux since gtk doesn’t acutally have such feature. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  *     * Add `RedrawEventsCleared` and `RedrawRequested` on Linux
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add run_return trait on Linux 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * `window.set_skip_taskbar()` on Linux will now also skip the pager (Alt+Tab), this matches the behavior on Windows. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Update tray dependency version. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix deadlock when unregistering shortcut on Linux. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fire `WindowEvent::Resized` and `WindowEvent::Moved` when window is min/maximized on Linux to align with Windows behavior. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix menubar missing on borderless window. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix core-video-sys dependency. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix linking to the `ColorSync` framework on macOS 10.7, and in newer Rust versions. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Allow more strings to parse to keycode, for example `,` is now parsed as a comma. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  *     * Update `raw-window-handle` to `0.4`
  * Add `raw_window_handle()` implementation on linux.
  * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix click events missing whe tray has menu. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add macOS `show_application()` method 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add new_any_thread to Unix event loop. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Replace all of the `winapi` crate references with the `windows` crate. The generated bindings are in the `webview2-com-sys` crate to share types with WRY later. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Implement `Clone` for `EventLoopWindowTarget`. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Update the `windows` crate to 0.25.0, which comes with pre-built libraries. Tao no longer depends on `webview2-com-sys` to generate bindings shared with WRY. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Update the `windows` crate to 0.29.0. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Update the `windows` crate to 0.30.0. This version re-introduced a lot of new-types for things like HWND, LRESULT, WPARAM, LPARAM, etc. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Fix using `WindowBuilder::with_visible` and `WindowBuilder::with_maximized` not behaving correctly. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * On Windows, send correct position on system tray events. 
    * 0dd71973 Merge next back to dev branch (#305) on 2022-02-05
  * Add support for more accelerator keys: `,` `-` `.` `=` `;` `/` `\` `&#39;` ``` `[` `]` `Space` `Tab` and `F13`-`F24`
    * b047ae41 feat: support accelerator key strings `,` `-` `.` `Space` `Tab` and `F13`-`F24` (#228) on 2021-11-15
  * Allow more strings to parse to keycode, for example `,` is now parsed as a comma. 
    * f0a3dcee feat: Allow more strings to parse to keycode (#229) on 2021-11-03
  * Add macOS `show_application()` method 
    * 7e10b0df feat(macos): Add `unhide_application` method, closes #182 (#231) on 2021-11-03


© 2025 Tauri Contributors. CC-BY / MIT
