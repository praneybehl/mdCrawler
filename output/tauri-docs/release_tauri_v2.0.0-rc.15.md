Skip to content
# tauri@2.0.0-rc.15
ReturnView on GitHub
### New Features
  * `ad294d274` (#11032 by @amrbashir) Add `app &gt; windows &gt; create` option to choose whether to create this window at app startup or not.


### Enhancements
  * `e7fd676c2` (#11025 by @lucasfernog) Inject `__INVOKE_KEY__` into custom invoke systems so their implementations can properly construct `tauri::webview::InvokeRequest`.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.12`
  * Upgraded to `tauri-runtime@2.0.0-rc.12`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.13`
  * Upgraded to `tauri-macros@2.0.0-rc.11`
  * Upgraded to `tauri-build@2.0.0-rc.12`


### Breaking Changes
  * `551e0624a` (#11027 by @lucasfernog) Remove the `responder` part of a custom invoke system now that the responder can be set directly in the `tauri::WebviewWindow::on_message` function.


© 2025 Tauri Contributors. CC-BY / MIT
