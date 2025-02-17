Skip to content
# tauri-bundler@1.0.0-rc.7
ReturnView on GitHub
  * Change `tsp` value from `Option&lt;bool&gt;` to `bool`. 
    * 29d8e768 feat(config): adjust schema for documentation website, closes #4139 (#4142) on 2022-05-17
  * Fixes processing of resources with glob patterns when there are nested directories on Windows. 
    * 3e702cf8 fix(bundler): ignore duplicated files in resource iter, closes #4126 (#4129) on 2022-05-15
  * Fixes resource bundling on Windows when the resource path includes root or parent directory components. 
    * 787ea09a fix: generate windows resource directories using resource_relpath, closes #4087. (#4111) on 2022-05-13
  * Set the application name when signing the Windows MSI. 
    * 8e1daad1 fix(bundler): set app name when signing MSI, closes #3945 (#3950) on 2022-05-17
  * Change WiX MajorUpgrade element’s `Schedule` to `afterInstallExecute` to prevent removal of existing configuration such as the executable’s pin to taskbar. 
    * d965b921 fix(bundler): prevent removal of `pin to taskbar` on Windows (#4144) on 2022-05-17
  * Change the MSI reinstall mode so it only reinstall missing or different version files. 
    * 1948ae53 fix(bundler): only reinstall missing or != version files, closes #4122 (#4125) on 2022-05-15
  * Allow configuring the display options for the MSI execution allowing quieter updates. 
    * 9f2c3413 feat(core): configure msiexec display options, closes #3951 (#4061) on 2022-05-15


© 2025 Tauri Contributors. CC-BY / MIT
