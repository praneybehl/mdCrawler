Skip to content
# tauri@2.0.0-rc.10
ReturnView on GitHub
### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.9`
  * Upgraded to `tauri-runtime@2.0.0-rc.9`
  * Upgraded to `tauri-runtime-wry@2.0.0-rc.9`
  * Upgraded to `tauri-macros@2.0.0-rc.8`
  * Upgraded to `tauri-build@2.0.0-rc.9`
  * `d9c8d3cc8` (#10902 by @Legend-Master) Update infer to 0.16, tray icon to 0.17, urlpattern to 0.3, image to 0.25


### Breaking Changes
  * `faa259bac` (#10907 by @lucasfernog) The `Assets::iter` function now must return a iterator with `Item = (Cow&lt;&#39;_, str&gt;, Cow&lt;&#39;_, [u8]&gt;)` to be more flexible on contexts where the assets are not `&#39;static`.


© 2025 Tauri Contributors. CC-BY / MIT
