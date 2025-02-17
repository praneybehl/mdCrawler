Skip to content
# wry@0.47.0
ReturnView on GitHub
  * `7221256` (#1365 by @Norbiros) Add `WebViewBuilder::with_initialization_script_for_main_only` to enable injecting JavaScript code into main frame only or all subframes.
  * `c1b26b9` (#1394 by @amrbashir) Add `WebView::cookies` and `WebView::cookies_for_url` APIs.
  * `c193e2a` (#1408 by @amrbashir) Fix `DragDropEvent::Drop` event never fired on Wayland (and sometimes on X11).
  * `1d63fa3` (#1403 by @SpikeHD) Add `WebViewBuilder::with_extension_path` API to Windows and Linux.
  * `0c192f4` (#1414 by @lucasfernog) Fix Android static handlers not being replaced when the application UI is relaunched while still running in the foreground.
  * `9a2a2d4` (#1412 by @amrbashir) Fix icons of dragged items getting stuck when using `WebViewBuilder::with_drag_drop_handler` on some distros like Gnome.
  * `fa9875b` (#1409 by @amrbashir) On Windows, disable Webview2’s file drop when using `WebViewBuilder::with_drag_drop_handler` which fix drag events for files from “Recent files” view.
  * `6007608` (#1400 by @amrbashir) On Windows, fix webview slightly larger than the window inner size, which resulted in a hidden 1px in the right and bottom borders of the webview


© 2025 Tauri Contributors. CC-BY / MIT
