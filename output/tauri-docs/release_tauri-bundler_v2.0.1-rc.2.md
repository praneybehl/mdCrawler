Skip to content
# tauri-bundler@2.0.1-rc.2
ReturnView on GitHub
### New Features
  * `f8d658ea1` (#10588 by @anatawa12) `TAURI_WINDOWS_SIGNTOOL_PATH` environment variable for specifying the path to signtool.exe.


### Enhancements
  * `8deb1966a` (#10652 by @lucasfernog) Infer macOS codesign identity from the `APPLE_CERTIFICATE` environment variable when provided, meaning the identity no longer needs to be provided when signing on CI using that option. If the imported certificate name does not match a provided signingIdentity configuration, an error is returned.


### Bug Fixes
  * `521d1d5cd` (#10619 by @Broken-Deer) Fixed an issue that caused the bundler to not be able to download the AppImage tooling when building for ARM 32bit.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.3`
  * Upgraded to `tauri-macos-sign@0.1.1-rc.0`


© 2025 Tauri Contributors. CC-BY / MIT
