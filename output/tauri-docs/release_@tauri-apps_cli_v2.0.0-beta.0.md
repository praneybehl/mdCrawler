Skip to content
# @tauri-apps/cli@2.0.0-beta.0
ReturnView on GitHub
### New Features
  * `7fcc0bcd`(#8490) Add plugin initialization rust code when using `tauri add`
  * `1878766f`(#8667) Migrate the allowlist config to the new capability file format.


### Enhancements
  * `d6c7568c`(#8720) Add `files` option to the AppImage Configuration.
  * `b3209bb2`(#8688) Ignore global `.gitignore` when searching for tauri directory.
  * `e691208e`(#7837) Prevent unneeded double Cargo.toml rewrite on `dev` and `build`.
  * `f492efd7`(#8666) Update app and plugin template following the new access control permission model.


### Bug Fixes
  * `9cb9aa79`(#8672) Allow license field in Cargo.toml to be `{ workspace = true }`


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-beta.0`


### Breaking Changes
  * `8de308d1`(#8723) Restructured Tauri config per RFC#5:
    * Moved `package.productName`, `package.version` and `tauri.bundle.identifier` fields to the top-level.
    * Removed `package` object.
    * Renamed `tauri` object to `app`.
    * Moved `tauri.bundle` object to the top-level.
    * Renamed `build.distDir` field to `frontendDist`.
    * Renamed `build.devPath` field to `devUrl` and will no longer accepts paths, it will only accept URLs.
    * Moved `tauri.pattern` to `app.security.pattern`.
    * Removed `tauri.bundle.updater` object, and its fields have been moved to the updater plugin under `plugins.updater` object.
    * Moved `build.withGlobalTauri` to `app.withGlobalTauri`.
    * Moved `tauri.bundle.dmg` object to `bundle.macOS.dmg`.
    * Moved `tauri.bundle.deb` object to `bundle.linux.deb`.
    * Moved `tauri.bundle.appimage` object to `bundle.linux.appimage`.
    * Removed all license fields from each bundle configuration object and instead added `bundle.license` and `bundle.licenseFile`.
    * Renamed `AppUrl` to `FrontendDist` and refactored its variants to be more explicit.


© 2025 Tauri Contributors. CC-BY / MIT
