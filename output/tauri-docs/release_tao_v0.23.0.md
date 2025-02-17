Skip to content
# tao@0.23.0
ReturnView on GitHub
  * `cf22c902`(#85) **Breaking change** : Removed clipboard implementation. Use `arboard` crate instead.
  * `081ba16a`(#800) Fix `Window::theme` may return a theme different from the actual window’s theme on Linux.
  * `32ce759e`(#801) Updated to gtk 0.18 and Bump MSRV to 1.70.0.
  * `f569bbab`(#815) Fix `Window::current_monitor` sometimes panicking on Linux when the window is invisible.
  * `7e854cb1`(#817) On Windows, fix incorrect delta reported for `DeviceEvent::MouseWheel` event.
  * `7e854cb1`(#817) On Windows, fix `Window::set_progress_bar` incorrect states.
  * `7e854cb1`(#817) Update `windows` and `windows-implement` crate to `0.51`


© 2025 Tauri Contributors. CC-BY / MIT
