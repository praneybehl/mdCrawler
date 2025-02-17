Skip to content
# @tauri-apps/cli@2.0.0-alpha.21
ReturnView on GitHub
### New Features
  * `27bad32d`(#7798) Add `files` object on the `tauri &gt; bundle &gt; macOS` configuration option.
  * `0ec28c39`(#8529) Include tauri-build on the migration script.


### Enhancements
  * `091100ac`(#5202) Add RPM packaging


### Bug Fixes
  * `4f73057e`(#8486) Prevent `Invalid target triple` warnings and correctly set `TAURI_ENV_` vars when target triple contains 4 components.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-alpha.21`


### Breaking Changes
  * `4f73057e`(#8486) Removed `TAURI_ENV_PLATFORM_TYPE` which will not be set for CLI hook commands anymore, use `TAURI_ENV_PLATFORM` instead. Also Changed value of `TAURI_ENV_PLATFORM` and `TAURI_ENV_ARCH` values to match the target triple more accurately:
    * `darwin` and `androideabi` are no longer replaced with `macos` and `android` in `TAURI_ENV_PLATFORM`.
    * `i686` and `i586` are no longer replaced with `x86` in `TAURI_ENV_ARCH`.


© 2025 Tauri Contributors. CC-BY / MIT
