Skip to content
# tauri-bundler@2.0.1-beta.10
ReturnView on GitHub
### New Features
  * `05088b067`(#9494) Expose `{{long_description}}` variable for custom templates.


### Enhancements
  * `de7bcf3cc`(#9478) Append product name automatically when choosing a new install path using browse for nsis installer


### Bug Fixes
  * `e64b8f1dc`(#9479) The NSIS uninstaller now won’t mindlessly try to remove the whole installation folder when the “Remove application data” checkbox was ticked. This prevents data loss when the app was installed in a folder which contained other files.
  * `e64b8f1dc`(#9479) Fixed an issue causing the NSIS bundler to install resources incorrectly when the installer was built on a non-Windows system.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.13`


© 2025 Tauri Contributors. CC-BY / MIT
