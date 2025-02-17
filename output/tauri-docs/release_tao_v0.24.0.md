Skip to content
# tao@0.24.0
ReturnView on GitHub
  * `43c94f0b`(#830) This patch contains a couple of changes to how the anroid macros:
    * Changed `android_binding` macro 4th argument signature, which is a setup function that is called once when the event loop is first created, from `unsafe fn(JNIEnv, &amp;ForeignLooper, GlobalRef)` to `unsafe fn(&amp;str, JNIEnv, &amp;ForeignLooper, GlobalRef)`.
    * Moved `android_fn!` and `generate_package_name` macro from crate root `platform::android::prelude`
  * `f497b5dc`(#829) Add `Window::drag_resize_window` and `ResizeDirection` enum to initialize window resizing. Supported on Windows and Linux only.
  * `28b53f80`(#705) Fix `Window::primary_monitor` panicking on Linux when there is no primary monitor, e.g. with Wayland.
  * `e33104c2`(#831) On macOS, fix `WindowEvent::Destroyed` may fire twice.
  * `853101be`(#821) This release includes an update to `raw-window-handle` crate to `0.6` but will also provide a feature flags to select which `raw-window-handle` to use:
    * `rwh_06` (default): `raw-window-handle@0.6`
    * `rwh_05: `raw-window-handle@0.5`
    * `rwh_04: `raw-window-handle@0.4`
  * `fce9d260`(#844) On Windows, fix `WindowBuilder::with_theme` has no effect when forcing light theme on a dark mode system.
  * `c0278d83`(#839) On Windows, remove `WS_CLIPCHILDREN` from window style


© 2025 Tauri Contributors. CC-BY / MIT
