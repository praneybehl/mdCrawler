Skip to content
# tao@0.21.0
ReturnView on GitHub
  * `81329013`(#743) On macOS, fix the unexpected shifting of the window when dragging after closing the share dialog.
  * `baa02977`(#418) Added APIs for setting progress bars for the application icon on Linux (Unity only) and macOS, along with progress indicator for specific window on Windows.
  * `8f361f0c`(#752) Handle universal links on iOS and send `Event::Opened { urls }`.
  * `bb3c53d1`(#764) On macOS, fix `SystemTrayEvent` not emitted after calling `set_menu`.
  * `5af3da4a`(#746) On macOS, force `NativeImage` height to be `18` to have consistent size for all icons and match custom icons.
  * `093d8fbc`(#422) Implement `Event::Opened` on macOS for file association and deeplink support.
  * `e9875fe5`(#755) On Windows, fix leak of `tao::system_tray::Icon` when calling `tao::system_tray::SystemTray::set_icon` and leak of `String` when calling `tao::system_tray::SystemTray::set_tooltip`.
  * `50e69d71`(#749) On Windows, fix disabling `resizable` also disabling maximize button and messing up `Window::set_maximized`.


© 2025 Tauri Contributors. CC-BY / MIT
