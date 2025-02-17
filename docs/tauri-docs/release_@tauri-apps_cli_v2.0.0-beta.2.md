Skip to content
# @tauri-apps/cli@2.0.0-beta.2
ReturnView on GitHub
### Enhancements
  * `83a68deb`(#8797) Update app template following capabilities configuration change.


### Bug Fixes
  * `aa06a053`(#8810) Fix `tauri plugin android init` printing invalid code that has a missing closing `&quot;`.
  * `3cee26a5`(#8865) On Windows, fixed `tauri info` fails to detect the build tool when the system language is CJK.
  * `052e8b43`(#8838) Downgrade minisign dependency fixing updater signing key bug and prevent it from happening in the future.
  * `fb0d9971`(#8783) Fixes a regression on the `--config` argument not accepting file paths.
  * `baca704d`(#8768) Do not migrate updater configuration if the active flag is set to false.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-beta.2`


© 2025 Tauri Contributors. CC-BY / MIT
