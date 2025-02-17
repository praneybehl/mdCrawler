Skip to content
# tauri-cli@2.0.0-alpha.18
ReturnView on GitHub
### New Features
  * `50f7ccbb`(#6444) Add suport to SVG input image for the `tauri icon` command.
  * `25e5f91d`(#8200) Merge `src-tauri/Info.plist` and `src-tauri/Info.ios.plist` with the iOS project plist file.


### Enhancements
  * `01a7a983`(#8128) Transform paths to relative to the mobile project for the IDE script runner script.


### Bug Fixes
  * `88dac86f`(#8149) Ensure `tauri add` prints `rust_code` with plugin name in snake case.
  * `977d0e52`(#8202) Fixes `android build --open` and `ios build --open` IDE failing to read CLI options.
  * `bfbbefdb`(#8161) Fix invalid plugin template.
  * `92b50a3a`(#8209) Added support to Xcode’s archive. This requires regenerating the Xcode project.


### Dependencies
  * Upgraded to `tauri-bundler@2.0.0-alpha.12`
  * Upgraded to `tauri-utils@2.0.0-alpha.11`


© 2025 Tauri Contributors. CC-BY / MIT
