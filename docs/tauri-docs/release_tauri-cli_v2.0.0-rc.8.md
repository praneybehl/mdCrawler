Skip to content
# tauri-cli@2.0.0-rc.8
ReturnView on GitHub
### New Features
  * `91e9e784a` (#10729 by @amrbashir) Add plugins information in `tauri info` output
  * `09e9dc1aa` (#10752 by @lucasfernog) Allow Xcode to manage iOS code sign and provisioning profiles by default. On CI, the `APPLE_API_KEY`, `APPLE_API_ISSUER` and `APPLE_API_KEY_PATH` environment variables must be provided for authentication.


### Enhancements
  * `3a4972b39` (#10793 by @lucasfernog) Include architecture in the `tauri info` output.
  * `fd68b7fde` (#10785 by @lucasfernog) Remove the `.cargo/config` file creation that used to fix mobile build caches.
  * `f67a9eb6d` (#10802 by @lucasfernog) Synchronize identifier, development team and lib name with the iOS Xcode project.


### Bug Fixes
  * `83ed090bf` (#10790 by @lucasfernog) Do not quit `ios dev` and `android dev` process when we fail to attach the logger.
  * `2d31aef75` (#10751 by @lucasfernog) Ensure gradlew is executable and does not use CRLF so it can be used on UNIX systems.
  * `02b2f964a` (#10795 by @lucasfernog) Fix the `add` command NPM version specifier for known plugins from `2.0.0-rc` (unknown version requirement) to `^2.0.0-rc`.
  * `84070bae9` (#10792 by @lucasfernog) Fix `tauri plugin ios init` not generating the iOS folder.
  * `edb2ca31f` (#10794 by @lucasfernog) Migrate v1 plugins NPM packages.
  * `9718dc9e8` (#10791 by @lucasfernog) Reintroduce the `targetSdk` value in the Android application template.


### What’s Changed
  * `fb6bf3142` (#10763 by @rdlabo) Update plugin template Android code to match documentation on Android package ID usage.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.7`
  * Upgraded to `tauri-bundler@2.0.1-rc.6`


### Breaking Changes
  * `073bb4f45` (#10772 by @lucasfernog) Removed the deprecated `webview_fixed_runtime_path` config option, use the `webview_install_mode` instead.


© 2025 Tauri Contributors. CC-BY / MIT
