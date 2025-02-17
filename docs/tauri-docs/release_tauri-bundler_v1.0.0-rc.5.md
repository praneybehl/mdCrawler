Skip to content
# tauri-bundler@1.0.0-rc.5
ReturnView on GitHub
  * Set the Debian control file `Priority` field to `optional`. 
    * 3bd3d923 fix: add priority field in debian/control (#3865) on 2022-04-20
  * Fixes DLL resource usage on Windows. 
    * f66bc3c2 fix(bundler): DLL resources, closes #3948 (#3949) on 2022-04-23
  * **Breaking change:** Removed the `useBootstrapper` option. Use https://github.com/tauri-apps/fix-path-env-rs instead. 
    * 6a5ff08c refactor: remove bootstrapper, closes #3786 (#3832) on 2022-03-31


© 2025 Tauri Contributors. CC-BY / MIT
