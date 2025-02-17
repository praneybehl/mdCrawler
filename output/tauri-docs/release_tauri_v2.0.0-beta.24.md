Skip to content
# tauri@2.0.0-beta.24
ReturnView on GitHub
### New Features
  * `7bc6a2a1d` (#9788 by @pewsheen) Add a new method to set title bar style dynamically on macOS.


### Enhancements
  * `a7354f9a8` (#10171 by @amrbashir) Mark `AppHandle::restart` and `process::restart` as diverging functions.


### Bug Fixes
  * `4c239729c` (#10167 by @amrbashir) Fix deserialization of raw invoke requests when using `isolation` pattern.
  * `55733aba9` (#10176 by @lucasfernog) Move `PluginApi::register_ios_plugin` behind the `wry` Cargo feature as `Webview::with_webview` is only available when that feature is enabled.


### Dependencies
  * Upgraded to `tauri-macros@2.0.0-beta.19`
  * Upgraded to `tauri-build@2.0.0-beta.19`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.20`
  * Upgraded to `tauri-utils@2.0.0-beta.19`
  * Upgraded to `tauri-runtime@2.0.0-beta.20`


### Breaking Changes
  * `ba9590aa9` (#9640 by @amrbashir) Added `Emitter` and `Listener` traits that defines what an emitter or a listener can do, this however comes with a few breaking changes:
    * Removed `Manager::listen_any`, use `Listener::listen_any` instead.
    * Removed `Manager::once_any`, use `Listener::once_any` instead.
    * Removed `Manager::unlisten`, use `Listener::unlisten` instead.
    * Removed `Manager::emit`, use `Emitter::emit` instead.
    * Removed `Manager::emit_to`, use `Emitter::emit_to` instead.
    * Removed `Manager::emit_filter`, use `Emitter::emit_filter` instead.
    * Removed `App/AppHandle::listen`, `WebviewWindow::listen`, `Window::listen` and `Webview::listen`, use `Listener::listen` instead.
    * Removed `App/AppHandle::once`, `WebviewWindow::once`, `Window::once` and `Webview::once`, use `Listener::once` instead.
    * Removed `App/AppHandle::unlisten`, `WebviewWindow::unlisten`, `Window::unlisten` and `Webview::unlisten`, use `Listener::unlisten` instead.
  * `261c9f942` (#10170 by @amrbashir) Renamed `DragDropEvent` enum variants to better convey when they are triggered:
    * `DragDropEvent::Dragged` -> `DragDropEvent::Enter`
    * `DragDropEvent::DragOver` -> `DragDropEvent::Over`
    * `DragDropEvent::Dropped` -> `DragDropEvent::Drop`
    * `DragDropEvent::Cancelled` -> `DragDropEvent::Leave`
This also comes with a change in the events being emitted to JS and Rust event listeners:
    * `tauri://drag` -> `tauri://drag-enter`
    * `tauri://drop-over` -> `tauri://drag-over`
    * `tauri://drop` -> `tauri://drag-drop`
    * `tauri://drag-cancelled` -> `tauri://drag-leave`
  * `2b1ceb40d` (#10229 by @amrbashir) Renamed the JS `getCurrent` and `getAll` functions to a clearer name to avoid ambiguity:
    * `getCurrent` in `window` module has been renamed to `getCurrentWindow`
    * `getCurrent` in `webview` module has been renamed to `getCurrentWebview`
    * `getCurrent` in `webviewWindow` module has been renamed to `getCurrentWebviewWindow`
    * `getAll` in `window` module has been renamed to `getAllWindows`
    * `getAll` in `webview` module has been renamed to `getAllWebviews`
    * `getAll` in `webviewWindow` module has been renamed to `getAllWebviewWindows`
  * `57612ab24` (#10139 by @Brendonovich) Add `TSend` generic to `ipc::Channel` for typesafe `send` calls and type inspection in `tauri-specta`


© 2025 Tauri Contributors. CC-BY / MIT
