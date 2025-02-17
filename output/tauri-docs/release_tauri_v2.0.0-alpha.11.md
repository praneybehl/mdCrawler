Skip to content
# tauri@2.0.0-alpha.11
ReturnView on GitHub
### New Features
  * `4db363a0`(#6589) Added `visible_on_all_workspaces` configuration option to `WindowBuilder`, `Window`, and `WindowConfig`.
  * `84c41597`(#6394) Add `App::primary_monitor`, `App::available_monitors`, `AppHandle::primary_monitor`, and `AppHandle::available_monitors`
  * `2a000e15`(#7235) Added `Window::navigate`.
  * `3b98141a`(#3736) Added support to file associations.
  * `3a2c3e74`(#7306) Added `PluginBuilder::on_navigation`. Added `Plugin::on_navigation`.
  * `753900dd`(#7440) Expose `RunEvent::Opened` on macOS and iOS for deep link support.
  * `7fb419c3`(#7535) Add `App::cleanup_before_exit` and `AppHandle::cleanup_before_exit` to manually call the cleanup logic. **You should always exit the tauri app immediately after this function returns and not use any tauri-related APIs.**
  * `7fb419c3`(#7535) On Linux, add `Window::default_vbox` to get a reference to the `gtk::Box` that contains the menu bar and the webview.
  * `7fb419c3`(#7535) Add `linux-libxdo` feature flag (disabled by default) to enable linking to `libxdo` which is used to make `Cut`, `Copy`, `Paste` and `SelectAll` native menu items work on Linux.
  * `7fb419c3`(#7535) On macOS, add `Window::ns_view` to get a pointer to the NSWindow content view.
  * `7fb419c3`(#7535) Expose `run_on_main_thread` method on `App` that is similar to `AppHandle::run_on_main_thread`.


### Enhancements
  * `a5752db9`(#7436) Listen to `onNewIntent` and forward it to registered plugins.
  * `fbeb5b91`(#7170) Added `Channel::new` allowing communication from a mobile plugin with Rust.
  * `fbeb5b91`(#7170) Use custom protocols on the IPC implementation to enhance performance.


### Dependencies
  * Upgraded to `tauri-runtime@1.0.0-alpha.0`
  * Upgraded to `tauri-utils@2.0.0-alpha.7`
  * Upgraded to `tauri-macros@2.0.0-alpha.7`
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.0`
  * Upgraded to `tauri-build@2.0.0-alpha.7`
  * `d1a6e2f3`(#7252) Update `state` to v0.6.


### Breaking Changes
  * `fd5dc788`(#7352) - Removed `tauri::api::file` and `tauri::api::dir` modules, use `std::fs` instead.
    * Removed `tauri::api::version` module, use `semver` crate instead.
  * `fbeb5b91`(#7170) Moved `tauri::api::ipc` to `tauri::ipc` and refactored all types.
  * `fbeb5b91`(#7170) Removed the `linux-protocol-headers` feature (now always enabled) and added `linux-ipc-protocol`.
  * `7fb419c3`(#7535) Changed `App::handle` and `Manager::app_handle` to return a reference to an `AppHandle` instead of an owned value.
  * `7fb419c3`(#7535) The tray icon and menu have received a huge refactor with a lot of breaking changes in order to add new functionalities and improve the DX around using them and here is an overview of the changes:
    * All menu and tray types are now exported from `tauri::menu` and `tauri::tray` modules with new names so make sure to check the new types.
    * Removed `tauri::Builder::system_tray`, instead you should use `tauri::tray::TrayIconBuilder` inside `tauri::Builder::setup` hook to create your tray icons.
    * Changed `tauri::Builder::menu` to be a function to accommodate for new menu changes, you can passe `tauri::menu::Menu::default` to it to create a default menu.
    * Renamed `tauri::Context` methods `system_tray_icon`, `tauri::Context::system_tray_icon_mut` and `tauri::Context::set_system_tray_icon` to `tauri::Context::tray_icon`, `tauri::Context::tray_icon_mut` and `tauri::Context::set_tray_icon` to be consistent with new type names.
    * Added `RunEvent::MenuEvent` and `RunEvent::TrayIconEvent`.
    * Added `App/AppHandle::set_menu`, `App/AppHandle::remove_menu`, `App/AppHandle::show_menu`, `App/AppHandle::hide_menu` and `App/AppHandle::menu` to access, remove, hide or show the app-wide menu that is used as the global menu on macOS and on all windows that don’t have a specific menu set for it on Windows and Linux.
    * Added `Window::set_menu`, `Window::remove_menu`, `Window::show_menu`, `Window::hide_menu`, `Window::is_menu_visible` and `Window::menu` to access, remove, hide or show the menu on this window.
    * Added `Window::popup_menu` and `Window::popup_menu_at` to show a context menu on the window at the cursor position or at a specific position. You can also popup a context menu using `popup` and `popup_at` methods from `ContextMenu` trait which is implemented for `Menu` and `Submenu` types.
    * Added `App/AppHandle::tray`, `App/AppHandle::tray_by_id`, `App/AppHandle::remove_tray` and `App/AppHandle::remove_tray_by_id` to access or remove a registered tray.
    * Added `WindowBuilder/App/AppHandle::on_menu_event` to register a new menu event handler.
    * Added `App/AppHandle::on_tray_icon_event` to register a new tray event handler.
  * `7fb419c3`(#7535) Renamed `system-tray` feature flag to `tray-icon`.
  * `3a2c3e74`(#7306) The `Window#on_navigation` closure now receives a `&amp;Url` argument instead of `Url`.


© 2025 Tauri Contributors. CC-BY / MIT
