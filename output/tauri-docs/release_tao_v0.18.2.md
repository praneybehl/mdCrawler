Skip to content
# tao@0.18.2
ReturnView on GitHub
  * fix not get actual ns_view when it’s replace by setContentView 
    * 76ae625b fix: not get actual ns_view when it’s replace by setContentView (#710) on 2023-03-07
  * Fix `Window::cursor_position` and `EventLoopWindowTarget::cursor_position` scale on Linux and macOS. 
    * dc913cd5 fix: scale cursor_position (#712) on 2023-03-08
  * On macOS, Fix `cursor_position` return incorrect position. 
    * ea2e60d9 fix(macOS): `cursor_position` returns incorrect position (#711) on 2023-03-07
  * Fix arrow cursor icon on Linux 
    * e9eba855 chore: rename change file on 2023-02-22
  * Attempt to get primary monitor on linux will now return None rather than panicking if monitor not found. 
    * 28b53f80 fix: don’t panic if primary monitor not discoverable. (#705) on 2023-02-22
  * On macOS, Remove linking to `ColorSync`
    * a1e96d1b feat: remove linking to `ColorSync` (#713) on 2023-03-15


© 2025 Tauri Contributors. CC-BY / MIT
