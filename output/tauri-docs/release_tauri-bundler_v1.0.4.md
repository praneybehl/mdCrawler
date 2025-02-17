Skip to content
# tauri-bundler@1.0.4
ReturnView on GitHub
  * Reduce the amount of allocations when converting cases. 
    * bc370e32 feat: reduce the amount of `heck`-related allocations (#4634) on 2022-07-11
  * Automatically load WiX extensions referenced in fragments. 
    * 261d1bc9 feat(bundler): load WiX extensions used on fragments, closes #4546 (#4656) on 2022-07-12
  * Fix AppImage builds by pinning the linuxdeploy version. 
    * 89cb2526 fix(bundler): pin linuxdeploy version on 2022-07-14
  * Use `Bin_$\{sidecarFilename}` as the `Id` of sidecar file on WiX so you can reference it in your WiX fragments. 
    * 597c9820 feat(bundler): use known Id for the sidecar files on WiX, ref #4546 (#4658) on 2022-07-12


© 2025 Tauri Contributors. CC-BY / MIT
