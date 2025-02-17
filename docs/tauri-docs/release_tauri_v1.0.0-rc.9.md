Skip to content
# tauri@1.0.0-rc.9
ReturnView on GitHub
  * The `dangerous_allow_asset_csp_modification` configuration value has been changed to allow a list of CSP directives to disable. 
    * 164078c0 feat: allow limiting dangerousDisableAssetCspModification, closes #3831 (#4021) on 2022-05-02
  * The file drop event payloads are now percent-decoded. 
    * a0ecd81a fix(core): percent decode file drop payloads, closes #4034 (#4035) on 2022-05-03
  * Fix dialog crash on macOS when the `default_path` value is just the file name. 
    * d31167c5 fix(core): dialog crashing on macOS when the parent is empty (#4028) on 2022-05-02
  * Fixes the `title` option being ignored in the dialog API endpoints. 
    * 220e7460 fix(core): set dialog title via API, closes #4029 (#4030) on 2022-05-02
  * Fixes nested isolation iframe injection. 
    * 022eed46 fix(core): nested isolation iframes, closes #4015 (#4020) on 2022-05-01
  * Deserialize numeric values (seconds) in the http API `ClientBuilder.connect_timeout` and `HttpRequestBuilder.timeout` fields. 
    * f3c5ca89 fix(core): http api `connect_timeout` deserialization, closes #4004 (#4006) on 2022-04-29
  * Fix updater dialog removing single and double quotes from the release notes 
    * 0180dcc8 fix(updater): remove single&amp;double quotes escaping in updater dialog … (#4047) on 2022-05-04
  * Expose methods to access the underlying native handles of the webview. 
    * c82b4761 feat(core): expose `with_webview` API to access the platform webview (#4058) on 2022-05-04


© 2025 Tauri Contributors. CC-BY / MIT
