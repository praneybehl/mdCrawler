Skip to content
# tauri-cli@2.0.0-beta.21
ReturnView on GitHub
### New Features
  * `656a64974` (#9318) Added a configuration option to disable hardened runtime on macOS codesign.


### Enhancements
  * `f44a2ec47` (#10030) Enhance the plugin template to include `permissions/default.toml` and default capabilities file for the example application.


### Bug Fixes
  * `019a74e97` (#9931) Fix wrong migration of `clipboard` and `globalShortcut` modules
  * `27838365a` (#10135) Fix parsing of cargo profile when using `--profile=&lt;profile&gt;` syntax.
  * `79542f4d4` (#10039) Fixed an issue that prevented `tauri icon` from rendering `&lt;text&gt;` nodes in SVG files.
  * `40c0f44e1` (#9971) Changed the deployment target of plugin iOS Xcode project to 13.0 so it works on older iOS releases.
  * `f56cdc9e3` (#10016) Add missing dependency `libayatana-appindicator3.so.1` for rpm package.
  * `1601da5b5` (#10114) Removed alpha channel from default icons in iOS template to comply with Apple’s human interface guideline (https://developer.apple.com/design/human-interface-guidelines/app-icons), because transparent icons with alpha channel are not allowed, and will be rejected upon upload to Apple appstore.


### What’s Changed
  * `3cca5c2be` (#9924) Migrate to new Android buildFeatures.buildConfig format.


### Dependencies
  * Upgraded to `tauri-bundler@2.0.1-beta.17`
  * Upgraded to `tauri-utils@2.0.0-beta.18`
  * `f955f7b49` (#9929) Switch from `dirs_next` to `dirs` as `dirs_next` is now unmaintained while `dirs` is


### Breaking Changes
  * `911242f09` (#9883) Move updater target from `bundle &gt; targets` to a separate field `bundle &gt; createUpdaterArtifacts`


© 2025 Tauri Contributors. CC-BY / MIT
