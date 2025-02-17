Skip to content
# tauri-cli@2.0.0-rc.13
ReturnView on GitHub
### New Features
  * `656618225` (#10866 by @thep0y) Add `TAURI_BUNDLER_TOOLS_GITHUB_MIRROR` environment variable to specify a GitHub mirror to download files and tools used by tauri bundler. This is designed for areas like Mainland China where GitHub access can be unreliable.
  * `35bd9dd3d` (#10977 by @amrbashir) Add `mainBinaryName` config option to set the file name for the main binary.


### Enhancements
  * `6c5340f8b` (#11004 by @lucasfernog) Added the `log` plugin to the app template, which is required to visualize logs on Android and iOS.
  * `3ad2427dc` (#10961 by @lucasfernog) Only render app logs on iOS unless `-vv` is provided to the `ios dev` command.


### Dependencies
  * Upgraded to `tauri-bundler@2.0.1-rc.11`
  * Upgraded to `tauri-utils@2.0.0-rc.11`


© 2025 Tauri Contributors. CC-BY / MIT
