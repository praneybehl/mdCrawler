Skip to content
# tauri-bundler@2.0.1-rc.11
ReturnView on GitHub
### New Features
  * `656618225` (#10866 by @thep0y) Add `TAURI_BUNDLER_TOOLS_GITHUB_MIRROR` environment variable to specify a GitHub mirror to download files and tools used by tauri bundler. This is designed for areas like Mainland China where GitHub access can be unreliable.
  * `35bd9dd3d` (#10977 by @amrbashir) Add `mainBinaryName` config option to set the file name for the main binary.
  * `b13cb208a` (#10962 by @amrbashir) Store main binary name in registry for NSIS installer and delete old main binary on updates if the name changes.


### Enhancements
  * `a1e88d2b5` (#10969 by @amrbashir) Generate a consistent Product code for MSI installer derived from `identifier` instead of generating random one each build.


### Bug Fixes
  * `44d54a071` (#11005 by @goenning) Use appimage files instead of debian files when building appimage
  * `9d468774a` (#10975 by @FabianLars) The executable and NSIS installer on Windows will now use the `productName` config for the `FileDescription` property instead of `shortDescription`.
  * `7eb1171e3` (#10967 by @amrbashir) Fix generated `UpgradeCode` for MSI not matching MSI installers created with tauri-bundler@v1.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-rc.11`


### Breaking Changes
  * `35bd9dd3d` (#10977 by @amrbashir) Changed changelog file location in `deb` to `usr/share/doc/&lt;product_name&gt;/changelog.gz` instead of `usr/share/doc/&lt;main_binary_name&gt;/changelog.gz`. For tauri v1 users, the path is unchanged as `product_name` and `main_binary_name` used the same value.
  * `35bd9dd3d` (#10977 by @amrbashir) Changed resources directory location in `deb` and `rpm` to `/usr/lib/&lt;product_name&gt;` instead of `/usr/lib/&lt;main_binary_name&gt;`. For tauri v1 users, the path is unchanged as `product_name` and `main_binary_name` used the same value.


© 2025 Tauri Contributors. CC-BY / MIT
