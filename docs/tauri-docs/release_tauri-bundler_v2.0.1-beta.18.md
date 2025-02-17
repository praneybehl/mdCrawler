Skip to content
# tauri-bundler@2.0.1-beta.18
ReturnView on GitHub
### New Features
  * `c734b9e3c` (#10072 by @FabianLars) Upgraded the WiX version to 3.14 which fixes vulnerability issues and adds support for Arm targets.


### Bug Fixes
  * `96f65fef3` (#10188 by @FabianLars) On macOS, the bundler will now correctly print a warning when the updater is enabled while the `.app` bundle is disabled.
  * `5998a90f3` (#10184 by @amrbashir) Fix NSIS installer failing to launch apps that contain spaces after installation.


### Dependencies
  * Upgraded to `tauri-macos-sign@0.1.0-beta.0`
  * Upgraded to `tauri-utils@2.0.0-beta.19`


### Breaking Changes
  * `11aa7743e` (#10177 by @Legend-Master) Changed NSIS installer hooks from `!define` to `!macro`


© 2025 Tauri Contributors. CC-BY / MIT
