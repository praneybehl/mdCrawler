Skip to content
# tauri-bundler@2.0.1-rc.14
ReturnView on GitHub
### New Features
  * `06718b456` (#11096 by @thep0y) Add the `TAURI_BUNDLER_TOOLS_GITHUB_MIRROR_TEMPLATE` environment variable to specify a more accessible mirror template, facilitating companies, organizations, or individuals who cannot access GitHub to download the necessary files through their own mirror servers.
  * `f57a729cd` (#11039 by @amrbashir) Add `upgradeCode` in `wix` configuration to set an upgrade code for your MSI installer. This is recommended to be set if you plan to change your `productName`.


### Bug Fixes
  * `dfba0ede6` (#11084 by @olivierlemasle) Detect ARM gnueabi as soft-float (armel) instead of hard-float (armhf). Also change the signature of `tauri_bundler::bundle::Settings::binary_arch` to return an enum instead of a `&amp;str`.
  * `544328d5a` (#11139 by @amrbashir) Fix NSIS installer failing to determine whether webview installer downloaded correctly or not.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.13`


© 2025 Tauri Contributors. CC-BY / MIT
