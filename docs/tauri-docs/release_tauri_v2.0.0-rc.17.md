Skip to content
# tauri@2.0.0-rc.17
ReturnView on GitHub
### Breaking Changes
  * `354be36d4` (#11163 by @amrbashir) Changed uri scheme protocol handler to take `UriSchemeContext` as first argument instead of `AppHandle`. `UriSchemeContext` can be used to access an app handle or the webview label that made the request. The following methods are affected:
    * `tauri::Builder::register_uri_scheme_protocol`
    * `tauri::Builder::register_asynchronous_uri_scheme_protocol`
    * `tauri::plugin::Builder::register_uri_scheme_protocol`
    * `tauri::plugin::Builder::register_asynchronous_uri_scheme_protocol`


© 2025 Tauri Contributors. CC-BY / MIT
