Skip to content
# tao@0.17.0
ReturnView on GitHub
  * Bump gtk version: 0.15 -> 0.16 
    * b59f1b49 Bump gtk version 0.15 -> 0.16 (#679) on 2023-01-26
  * Add `Window::cursor_position` and `EventLoopWindowTarget::cursor_position` to get the current mouse position. 
    * 5d8bf51d feat: add `cursor_position` (#668) on 2023-01-12
  * On Linux, spawn device event thread only once instead of a new thread on each iteration of the event loop. 
    * ca1ed5de fix(linux): spawn device thread only once (#678) on 2023-01-23
  * On Windows, fix `Window::set_minimized(false)` not working when the window was minimized using `Win + D` hotkey. 
    * e1149563 fix(Windows): fix `set_minimized` with `Win + D` (#676) on 2023-01-21


© 2025 Tauri Contributors. CC-BY / MIT
