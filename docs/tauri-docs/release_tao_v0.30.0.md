Skip to content
# tao@0.30.0
ReturnView on GitHub
  * `222d5786` (#971 by @amrbashir) On Windows, fix `Window::monitor_from_point` and `EventLoopTargetWindow::monitor_from_point` returning invalid monitor handle.
  * `e47d4c4a` (#967 by @amrbashir) On Linux, removed internal check for current desktop environment before applying `Window::set_progress_bar` API. This should allow `Window::set_progress_bar` to work on KDE Plasma and similar environments that support `libunity` APIs.
  * `9b5aa60b` (#970 by @amrbashir) Changed `WindowExtWindows::set_skip_taskbar` and `WindowExtUnix::set_skip_taskbar` to return a result instead of panicing internally.


© 2025 Tauri Contributors. CC-BY / MIT
