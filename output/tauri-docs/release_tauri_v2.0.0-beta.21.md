Skip to content
# tauri@2.0.0-beta.21
ReturnView on GitHub
### New Features
  * `8a1ae2dea`(#9843) Added an option to use a Xcode project for the iOS plugin instead of a plain SwiftPM project.


### Bug Fixes
  * `276c4b143`(#9832) On Windows, fix wrong menubar theme when window is using an explicit theme.
  * `ccc3ea729`(#9646) Parse the correct platform `tauri.&lt;platform&gt;.conf.json` config file when building or developing for mobile.
  * `aa55e0335`(#9899) Set default window origin to `null`. Prevent window crash when loading `about:blank`.


### What’s Changed
  * `9ac930380`(#9850) Emit `cargo:rustc-check-cfg` instruction so Cargo validates custom cfg attributes on Rust 1.80 (or nightly-2024-05-05).
  * `80aa50498`(#9870) Updated Android target SDK to 34.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-beta.17`
  * Upgraded to `tauri-macros@2.0.0-beta.17`
  * Upgraded to `tauri-utils@2.0.0-beta.17`
  * Upgraded to `tauri-runtime@2.0.0-beta.18`
  * Upgraded to `tauri-runtime-wry@2.0.0-beta.18`


### Breaking Changes
  * `e8f6eb59a`(#9552) Include binary path in `Env.args_os`, previously it was skipped.
  * `1df5cdeb0`(#9858) Use `tauri.conf.json &gt; identifier` to set the `PackageName` in Android and `BundleId` in iOS.
  * `aaecb6a72`(#9890) Renamed `dev` function to `is_dev` and marked it as `const fn`
  * `c4410daa8`(#9777) This release contains breaking changes to the tray event structure because of newly added events:
    * Changed `TrayIconEvent` to be an enum instead of a struct.
    * Added `MouseButtonState` and `MouseButton` enums.
    * Removed `ClickType` enum and replaced it with `MouseButton` enum.
    * Added `MouseButtonState` enum.


© 2025 Tauri Contributors. CC-BY / MIT
