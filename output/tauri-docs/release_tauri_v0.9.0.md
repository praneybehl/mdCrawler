Skip to content
# tauri@0.9.0
ReturnView on GitHub
  * Make sure CSS content loaded with the `loadAsset` API is inside a template string and not injected raw. 
    * e3e2e39 fix(tauri) ensure css content is loaded inside a string (#884) on 2020-07-22
    * b96b1fb inject css with template string to allow for line breaks (#894) on 2020-07-25
  * Pin the `tauri-api` dependency on the `tauri` crate so updates doesn’t crash the build. 
    * ad717c6 chore(tauri) pin tauri-api dep version (#872) on 2020-07-21
  * Fixes the Webview initialization on Windows. 
    * 4abd12c fix(tauri) webview initialization on windows, fixes #879 (#885) on 2020-07-23


© 2025 Tauri Contributors. CC-BY / MIT
