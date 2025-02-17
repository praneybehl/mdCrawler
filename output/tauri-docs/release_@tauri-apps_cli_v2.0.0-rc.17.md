Skip to content
# @tauri-apps/cli@2.0.0-rc.17
ReturnView on GitHub
### New Features
  * `a944b9b05` (#11118 by @amrbashir) Add `--github-workflows` flag for `tauri plugin new/init`.
  * `f57a729cd` (#11039 by @amrbashir) Add `tauri inspect wix-upgrade-code` to print default Upgrade Code for your MSI installer derived from `productName`.


### Bug Fixes
  * `62b52f60a` (#11064 by @amrbashir) Fix `tauri add` failing to add NPM depenency with `npm` package manager.
  * `56e087471` (#11100 by @lucasfernog) Fix iOS xcode-script usage with `bun`.
  * `b88e22a5f` (#11063 by @FabianLars) The cli now only sets the iOS deployment target environment variable when building for iOS.
  * `8d22c0c81` (#11101 by @lucasfernog) Only modify the iOS Xcode project “sign style” if we need to enforce manual signing.
  * `df24cb944` (#11168 by @lucasfernog) Fixes Xcode pbxproj file parsing not expecting `_` in build configuration IDs.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-rc.17`


### Breaking Changes
  * `a944b9b05` (#11118 by @amrbashir) `tauri plugin init/new` will no longer generate a `.github` directory with workflows by default, instead use the new `--github-workflows` flag.


© 2025 Tauri Contributors. CC-BY / MIT
