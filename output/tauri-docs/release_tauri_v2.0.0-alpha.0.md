Skip to content
# tauri@2.0.0-alpha.0
ReturnView on GitHub
  * Added the `default-tls` and `reqwest-default-tls` Cargo features for enabling TLS suppport to connect over HTTPS. 
    * f6f9192a fix(core): Android compilation on Windows (#5658) on 2022-11-20
  * **Breaking change:** Use the custom protocol as a proxy to the development server on all platforms except Linux. 
    * 6f061504 feat(cli): add `android dev` and `ios dev` commands (#4982) on 2022-08-20
  * Support `with_webview` for Android platform alowing execution of JNI code in context. 
    * 8ea87e9c feat(android): with_webview access for jni execution (#5148) on 2022-09-08
  * First mobile alpha release! 
    * fa3a1098 feat(ci): prepare 2.0.0-alpha.0 (#5786) on 2022-12-08
  * **Breaking change:** The window creation and setup hook are now called when the event loop is ready. 
    * b4622ea4 refactor(app): run setup and window creation when event loop is ready (#4914) on 2022-08-11
  * Export types required by the `mobile_entry_point` macro. 
    * 98904863 feat(core): add `mobile_entry_point` macro (#4983) on 2022-08-21


© 2025 Tauri Contributors. CC-BY / MIT
