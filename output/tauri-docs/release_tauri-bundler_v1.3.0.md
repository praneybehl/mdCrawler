Skip to content
# tauri-bundler@1.3.0
ReturnView on GitHub
### New Features
  * `35cd751a`(#5176) Added `desktop_template` option on `DebianSettings`.
  * `29488205`(#6867) Allow specifying custom language files of Tauri’s custom messages for the NSIS installer
  * `e092f799`(#6887) Add `nsis &gt; template` option to specify custom NSIS installer template.
  * `df89ccc1`(#6955) For NSIS, Add support for `/P` to install or uninstall in passive mode, `/R` to (re)start the app and `/NS` to disable creating shortcuts in `silent` and `passive` modes.


### Enhancements
  * `3327dd64`(#7081) Remove macOS app bundles from the output if they are not requested by the user.
  * `fc7f9eba`(#7001) Added Copyright field as BrandingText to the NSIS bundler.
  * `540ddd4e`(#6906) Added Dutch language support to the NSIS bundler.
  * `b257bebf`(#6906) Added Japanese language support to the NSIS bundler.
  * `61e3ad89`(#7010) Added Korean language support to the NSIS bundler.
  * `21d5eb84`(#6965) Added Persian language support to the NSIS bundler.
  * `df89ccc1`(#6955) NSIS `silent` and `passive` installer/updater will auto-kill the app if its running.
  * `43858a31`(#7038) Added Swedish language support to the NSIS bundler.
  * `ac183948`(#7018) Added Turkish language support to the NSIS bundler.
  * `60334f9e`(#6859) NSIS installer will now check if a previous WiX `.msi` installation exist and will prompt users to uninstall it.
  * `db7c5fbf`(#7143) Remove `attohttpc` in favor of `ureq`.


### Bug Fixes
  * `0302138f`(#6992) - Updated the AppImage bundler to follow symlinks for `/usr/lib*`. 
    * Fixes AppImage bundling for Void Linux, which was failing to bundle webkit2gtk because the `/usr/lib64` is a symlink to `/usr/lib`.
  * `1b8001b8`(#7056) Fix incorrect estimated app size for NSIS bundler when installed to a non-empty directory.
  * `df89ccc1`(#6955) Fix NSIS installer disabling `do not uninstall` button and silent installer aborting, if `allowDowngrades` was disabled even when we are not downgrading.
  * `17da87d3`(#7036) Fix NSIS bundler failing to build when `productName` contained chinsese characters.
  * `4d4b72ba`(#7086) Fix missing quote in Japanese NSIS language file.
  * `3cc295e9`(#6928) Fix NSIS installer not using the old installation path as a default when using `perMachine` or `currentUser` install modes. Also fixes NSIS not respecting the `/D` flag which used to set the installation directory from command line.
  * `df89ccc1`(#6955) Fix NSIS silent installer not creating Desktop and StartMenu shortcuts. Pass `/NS` to disable creating them.


© 2025 Tauri Contributors. CC-BY / MIT
