Skip to content
# @tauri-apps/cli@2.0.0-rc.2
ReturnView on GitHub
### New Features
  * `8dc81b6cc` (#10496 by @lucasfernog) Added `bundle &gt; ios &gt; template` configuration option for custom Xcode project YML Handlebars template using XcodeGen.
  * `02c00abc6` (#10495 by @lucasfernog) Added `bundle &gt; ios &gt; minimumSystemVersion` configuration option.


### Enhancements
  * `8e1e15304` (#10483 by @lucasfernog) Check if the Rust library contains the symbols required at runtime for Android and iOS apps.
  * `ca6868956` (#10479 by @lucasfernog) Check if identifier or lib name changed when running mobile commands.


### Bug Fixes
  * `2e8ab7bac` (#10481 by @lucasfernog) Migration from v1 to v2 now adds the updater plugin when it is active.


### What’s Changed
  * `a3cd9779a` (#10480 by @lucasfernog) Removed the `[android|ios] open` command. It is recommended to use `[android|ios] dev --open` or `[android|ios] build --open` instead.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-rc.2`


© 2025 Tauri Contributors. CC-BY / MIT
