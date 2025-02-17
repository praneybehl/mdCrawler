Skip to content
# tao@0.30.3
ReturnView on GitHub
  * `4dcd2312` (#979 by @Zamoca42) On Linux Wayland, changed the event handling for maximizing to process events sequentially to avoid “Error 71(Protocol error): dispatching to Wayland display”.
  * `2ee007a5` (#981 by @thep0y) Add `Window::is_always_on_top` method to check if a window is always on top on macOS, Linux and Windows.
  * `4dcd2312` (#979 by @Zamoca42) On Linux Wayland, fixed an issue where the window was not moving when dragging the header bar area.
  * `4dcd2312` (#979 by @Zamoca42) On Linux Wayland, fixed an issue where the window was not resizing when dragging the window borders.
  * `4dcd2312` (#979 by @Zamoca42) On Linux Wayland, added buttons for maximize and minimize in the title bar.
  * `2fffdc9d` (#983 by @Legend-Master) Fix blinking title bar when changing system settings on Windows


© 2025 Tauri Contributors. CC-BY / MIT
