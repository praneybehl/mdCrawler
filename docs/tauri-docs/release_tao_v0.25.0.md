Skip to content
# tao@0.25.0
ReturnView on GitHub
  * `ae4b693d`(#864) On Windows, Remove `WS_CAPTION` and `WS_EX_WINDOWEDGE` window styles when creating a child window.
  * `e10f6a68`(#862) **Breaking Change** : Changed `WindowBuilderExtUnix::with_transient_for` signature to take `&amp;impl gtk::glib::IsA&lt;gtk::Window&gt;` instead of `gtk::ApplicationWindow` which covers more gtk window types and matches the underlying API call signature.


© 2025 Tauri Contributors. CC-BY / MIT
