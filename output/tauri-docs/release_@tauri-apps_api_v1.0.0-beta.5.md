Skip to content
# @tauri-apps/api@1.0.0-beta.5
ReturnView on GitHub
  * Adds `convertFileSrc` helper to the `tauri` module, simplifying the process of using file paths as webview source (`img`, `video`, etc). 
    * 51a5cfe4 feat(api): add `convertFileSrc` helper (#2138) on 2021-07-02
  * You can now use `emit`, `listen` and `once` using the `appWindow` exported by the window module. 
    * 5d7626f8 feat(api): WindowManager extends WebviewWindowHandle, add events docs (#2146) on 2021-07-03
  * Allow manipulating a spawned window directly using `WebviewWindow`, which now extends `WindowManager`. 
    * d69b1cf6 feat(api): allow managing windows created on JS (#2154) on 2021-07-05


© 2025 Tauri Contributors. CC-BY / MIT
