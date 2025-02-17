Skip to content
# tao@0.13.0
ReturnView on GitHub
  * On Linux, receive only one draw event per cycle to prevent receiving infinite draw events. 
    * b86ada73 Receive only one draw event per cycle (#500) on 2022-07-25
  *     * On Linux, add `EventLoopWindowTargetExtUnix` for methods to determine if the backend is x11 or wayland.
  * On Linux, add `x11` module for glutin internal use. This is basically just x11-dl, but winit secretly exports it.
  * On Linux, add `WindowBuilder::with_transparent_draw` to disable the internal draw for transparent window and allows users to draw it manually.
  * db7e5cb4 feat(linux): Add necessary features for creating GL windows (#495) on 2022-07-25
  * **Breaking** Updated `raw-window-handle` to `0.5` and added `Window::raw_display_handle` and `EventLoopWindowTarget::raw_display_handle`. 
    * b905852d chore(deps): update `raw-window-handle` to `0.5` (#493) on 2022-07-24
  * On Windows, respect min/max inner sizes when creating the window. 
    * c1c6822e fix(windows): respect min/max sizes when creating window, closes #498 (#499) on 2022-07-25


© 2025 Tauri Contributors. CC-BY / MIT
