Skip to content
# @tauri-apps/cli@2.0.0-beta.5
ReturnView on GitHub
### New Features
  * `06d63d67`(#8827) Add new subcommands for managing permissions and cababilities:
    * `tauri permission new`
    * `tauri permission add`
    * `tauri permission rm`
    * `tauri permission ls`
    * `tauri capability new`


### Breaking Changes
  * `b9e6a018`(#8937) The `custom-protocol` Cargo feature is no longer required on your application and is now ignored. To check if running on production, use `#[cfg(not(dev))]` instead of `#[cfg(feature = &quot;custom-protocol&quot;)]`.


### Enhancements
  * `9be314f0`(#8951) Add plugins to `Cargo.toml` when using `tauri migrate`


### Bug Fixes
  * `cbd9755e`(#8977) Fixes process logs not showing on `ios dev`.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-beta.5`


© 2025 Tauri Contributors. CC-BY / MIT
