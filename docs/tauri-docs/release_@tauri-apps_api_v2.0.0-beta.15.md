Skip to content
# @tauri-apps/api@2.0.0-beta.15
ReturnView on GitHub
### New Features
  * `7bc6a2a1d` (#9788 by @pewsheen) Add a new method to set title bar style dynamically on macOS.


### Enhancements
  * `080b6e127` (#10246 by @Legend-Master) Use `EventName` on `Window`, `Webview` and `WebviewWindow`’s `once` so you can get auto complete for tauri’s built-in events


### Bug Fixes
  * `080b6e127` (#10246 by @Legend-Master) Fix `once` doesn’t detached after one callback if event handler throws


### Breaking Changes
  * `261c9f942` (#10170 by @amrbashir) Renamed drag and drop events in `TauriEvent` enum to better convey when they are triggered:
    * `TauriEvent.DRAG` -> `TauriEvent.DRAG_ENTER`
    * `TauriEvent.DROP_OVER` -> `TauriEvent.DRAG_OVER`
    * `TauriEvent.DROP` -> `TauriEvent.DRAG_DROP`
    * `TauriEvent.DROP_CANCELLED` -> `TauriEvent::DRAG_LEAVE`
Also the `type` field values in `Window/Webview/WebviewWindow.onDropEvent` and `DragDropEvent` have changed:
    * `dragged` -> `enter`
    * `dragOver` -> `over`
    * `dropped` -> `drop`
    * `cancelled` -> `leave`
  * `2b1ceb40d` (#10229 by @amrbashir) Renamed the JS `getCurrent` and `getAll` functions to a clearer name to avoid ambiguity:
    * `getCurrent` in `window` module has been renamed to `getCurrentWindow`
    * `getCurrent` in `webview` module has been renamed to `getCurrentWebview`
    * `getCurrent` in `webviewWindow` module has been renamed to `getCurrentWebviewWindow`
    * `getAll` in `window` module has been renamed to `getAllWindows`
    * `getAll` in `webview` module has been renamed to `getAllWebviews`
    * `getAll` in `webviewWindow` module has been renamed to `getAllWebviewWindows`


© 2025 Tauri Contributors. CC-BY / MIT
