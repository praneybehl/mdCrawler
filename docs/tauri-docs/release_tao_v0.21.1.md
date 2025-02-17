Skip to content
# tao@0.21.1
ReturnView on GitHub
  * `9a320882`(#761) On Android, use a lockfree queue (crossbeam channel) to prevent deadlocks inside send_event.
  * `b31cb692`(#772) On macOS, fix `WindowExtMacOS::ns_view` returning an invalid pointer if the view was replaced by a call to `setContentView` later on.
  * `4d0e1862`(#762) Add `WindowExtWindows::set_rtl` and `WindowBuilderExtWindows::with_rtl` to set right-to-left layout on Windows.
  * `75eb0c1e`(#769) Add `WindowBuilderExtWindows::with_window_classname` to set the name of the window class created/used to create windows.
  * `494e4585`(#775) Ensure the macOS app delegate is defined before accessing it.


© 2025 Tauri Contributors. CC-BY / MIT
