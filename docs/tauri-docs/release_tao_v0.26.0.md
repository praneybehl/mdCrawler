Skip to content
# tao@0.26.0
ReturnView on GitHub
  * `2af91313`(#880) Updated the minimum supported Rust version to 1.70.
  * `90ad07b3`(#878) **Breaking change** : Removed `window::hit_test` function.
  * `2af91313`(#880) Progress bar on Linux no longer relies on zbus. Changed `ProgressBarState`’s field `unity_uri` to `desktop_filename`.
  * `90ad07b3`(#878) On Windows and Linux, disable resizing undecorated windows when in fullscreen.
  * `90ad07b3`(#878) On Windows, fix undecorated window resizing.
  * `89ce9d26`(#874) On Windows, apply `ScaleFactorChanged` if new size is different than what OS reported. This fixes an issue when moving the window to another monitor and immediately maximizing it, resulting in a maximized window (i.e have `WS_MAXIMIZE` window style) but doesn’t cover the monitor work area.


© 2025 Tauri Contributors. CC-BY / MIT
