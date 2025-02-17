Skip to content
# tauri-cli@2.0.0-rc.7
ReturnView on GitHub
### Enhancements
  * `da8c9a7d3` (#10669 by @lucasfernog) Modify both ExportOptions.plist and project.pbxproj to reflect changes for the `IOS_CERTIFICATE`, `IOS_CERTIFICATE_PASSWORD` and `IOS_MOBILE_PROVISION` environment variables.


### Bug Fixes
  * `793ee0531` (#10700 by @lucasfernog) Allow hyphens and underscores on app identifiers.
  * `da8c9a7d3` (#10669 by @lucasfernog) Synchronize Xcode project changes with the ExportOptions.plist file so `ios build` calls can work with code signing changes made in Xcode.


### What’s Changed
  * `f4d5241b3` (#10731 by @amrbashir) Update documentation icon path.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.6`
  * Upgraded to `tauri-bundler@2.0.1-rc.5`


### Breaking Changes
  * `da8c9a7d3` (#10669 by @lucasfernog) The `IOS_CERTIFICATE`, `IOS_CERTIFICATE_PASSWORD` and `IOS_MOBILE_PROVISION` environment variables are now read by the `ios build` command instead of `ios init`.


© 2025 Tauri Contributors. CC-BY / MIT
