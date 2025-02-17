Skip to content
# tauri@2.0.0-beta.0
ReturnView on GitHub
### New Features
  * `74a2a603`(#8661) Implement access control list for IPC usage.
  * `a2fc3a63`(#8657) Add `visibleOnAllWorkspaces` option when creating the window in JS and `Window.setVisibleOnAllWorkspaces` method.
  * `af610232`(#8710) Added `Window::destroy` to force close a window.
  * `c77b4032`(#8280) Add multiwebview support behind the `unstable` feature flag. See `WindowBuilder` and `WebviewBuilder` for more information.
  * `9eaeb5a8`(#8622) Add `WindowBuilder::parent` which is a convenient wrapper around parent functionality for Windows, Linux and macOS. Also added `WindowBuilder::owner` on Windows only. Also added `WindowBuilder::transient_for` and `WindowBuilder::transient_for_raw` on Linux only.


### Enhancements
  * `e8d3793c`(#8732) Add `common-controls-v6` cargo feature flag (enabled by default).
  * `58fe2e81`(#8670) Allow IPC calls when window origin is a defined custom protocol.


### Bug Fixes
  * `95da1a27`(#8713) Fix calling `set_activation_policy` when the event loop is running.
  * `e1eb911f`(#8582) Ensure initalize logic and dropping of menu item is done on the main thread, this fixes the crash when a menu item is dropped on another thread.
  * `a093682d`(#8621) Fix can not prevent closing a window from another webview.
  * `7f033f6d`(#8537) Fix undecorated window resizing on Windows and Linux.


### What’s Changed
  * `9f8037c2`(#8633) On Windows, fix decorated window not transparent initially until resized.
  * `7f033f6d`(#8537) Add `Window::start_resize_dragging` and `ResizeDirection` enum.
  * `6639a579`(#8441) Added the `WindowConfig::proxy_url` `WebviewBuilder::proxy_url() / WebviewWindowBuilder::proxy_url()` options when creating a webview.


### Dependencies
  * Upgraded to `tauri-build@22.0.0-beta.0`
  * Upgraded to `tauri-utils@2.0.0-beta.0`
  * Upgraded to `tauri-macros@2.0.0-beta.0`
  * Upgraded to `tauri-runtime@2.0.0-beta.0`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.0`


### Breaking Changes
  * `8de308d1`(#8723) Restructured Tauri config per RFC#5:
    * Moved `package.productName`, `package.version` and `tauri.bundle.identifier` fields to the top-level.
    * Removed `package` object.
    * Renamed `tauri` object to `app`.
    * Moved `tauri.bundle` object to the top-level.
    * Renamed `build.distDir` field to `frontendDist`.
    * Renamed `build.devPath` field to `devUrl` and will no longer accepts paths, it will only accept URLs.
    * Moved `tauri.pattern` to `app.security.pattern`.
    * Removed `tauri.bundle.updater` object, and its fields have been moved to the updater plugin under `plugins.updater` object.
    * Moved `build.withGlobalTauri` to `app.withGlobalTauri`.
    * Moved `tauri.bundle.dmg` object to `bundle.macOS.dmg`.
    * Moved `tauri.bundle.deb` object to `bundle.linux.deb`.
    * Moved `tauri.bundle.appimage` object to `bundle.linux.appimage`.
    * Removed all license fields from each bundle configuration object and instead added `bundle.license` and `bundle.licenseFile`.
    * Renamed `AppUrl` to `FrontendDist` and refactored its variants to be more explicit.
  * `c77b4032`(#8280) The `invoke_system`, `on_page_load` hooks now gives you a `Webview` argument instead of a `Window`.
  * `e1eb911f`(#8582) All menu item constructors `accelerator` argument have been changed to `Option&lt;impl AsRef&lt;str&gt;&gt;` so when providing `None` you need to specify the generic argument like `None::&lt;&amp;str&gt;`.
  * `e1eb911f`(#8582) All menu item constructors have been changed to return a `Result&lt;Self&gt;`
  * `aa758a85`(#8716) Moved the `command` module items to the `ipc` module so its import name does not clash with the `command` macro.
  * `00e15675`(#8708) `AppHandle::exit` and `AppHandle::restart` now go triggers `RunEvent::ExitRequested` and `RunEvent::Exit` and cannot be executed on the event loop handler.
  * `ec9818ac`(#8696) Added a callback to the `App::run_iteration` and removed its return value.
  * `a093682d`(#8621) Refactored the event system to better accommodate the new window types:
    * Added `EventTarget` enum.
    * Added `App/AppHandle::listen`, `App/AppHandle::once` and `App/AppHandle::unlisten` to listen to events targeting `App/AppHandle`
    * `App/AppHandle/Window/Webview/WebviewWindow::emit` will now emit to all event listeners.
    * `App/AppHandle/Window/Webview/WebviewWindow::emit_to` will emit to event targets that match the given label, see `EventTarget` enum.
    * `App/AppHandle/Window/Webview/WebviewWindow::emit_filter` will emit to event targets based on a filter callback which now takes `&amp;EventTarget` instead of `&amp;Window`.
    * Renamed `Manager::listen_global` and `Manager::once_global` to `listen_any` and `once_any` respectively to be consistent with `EventTarget::Any`, it will now also listen to any event to any target (aka event sniffer).
  * `9eaeb5a8`(#8622) Renamed `WindowBuilder::owner_window` to `WindowBuilder::owner_raw` and `WindowBuilder::parent_window` to `WindowBuilder::parent_raw`.
  * `9eaeb5a8`(#8622) Changed `WindowBuilder::from_config` to return a `Result&lt;Self&gt;`.
  * `c77b4032`(#8280) Renamed `Window` to `WebviewWindow`, `WindowBuilder` to `WebviewWindowBuilder`, `Manager::windows` to `Manager::webview_windows` and `Manager::get_window` to `Manager::get_webview_window`.
  * `af610232`(#8710) `Window::close` now triggers a close requested event instead of forcing the window to be closed.
  * `c77b4032`(#8280) Renamed the `window-data-url` feature flag to `webview-data-url`.


© 2025 Tauri Contributors. CC-BY / MIT
