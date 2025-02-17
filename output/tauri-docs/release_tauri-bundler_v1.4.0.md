Skip to content
# tauri-bundler@1.4.0
ReturnView on GitHub
### New Features
  * `4dd4893d`(#5950) Allow using a resource map instead of a simple array in `BundleSettings::resources_map`.


### Enhancements
  * `764968ab`(#7398) Sign NSIS uninstaller as well.
  * `2f8881c0`(#7775) Read the `APPLE_TEAM_ID` environment variable for macOS notarization arguments.
  * `cb1d4164`(#7487) On Windows, code sign the application binaries before trying to create the WiX and NSIS bundles to always sign the executables even if no bundle types are enabled.
On Windows, code sign the sidecar binaries if they are not signed already.
  * `57f73f1b`(#7486) On Windows, NSIS installer will write webview2 installer file to the well-known temp dir instead of the install dir, so we don’t pollute the install dir.
  * `a7777ff4`(#7626) Added Bulgarian language support to the NSIS bundler.
  * `e3bfb014`(#7776) Add `compression` configuration option under `tauri &gt; bundle &gt; windows &gt; nsis`.


### Bug Fixes
  * `46df2c9b`(#7360) Fix bundler skipping updater artifacts if `updater` target shows before other updater-enabled targets in the list, see #7349.
  * `2d35f937`(#7481) Fix bundler skipping updater artifacts if only a macOS DMG bundle target is specified.
  * `dcdbe3eb`(#7774) Remove extended attributes on the macOS app bundle using `xattr -cr $PATH`.
  * `dcdbe3eb`(#7774) Code sign sidecars and frameworks on macOS.
  * `eba8e131`(#7386) On Windows, fix installation packages not showing correct copyright information.
  * `32218a6f`(#7326) On Windows, fix NSIS installer identifying a previous NSIS-installed app as WiX-installed app and then fails to uninstall it.
  * `ca977f4b`(#7591) On Windows, Fix NSIS uninstaller deleting the wrong application data if the delete the application data checkbox is checked.
  * `0ae53f41`(#7361) On Windows, fix NSIS installer showing an error dialog even when the previous version was uninstalled sucessfully.
  * `09f7f57e`(#7711) On Windows, fix NSIS installer trying to kill itself if the installer file name and the app `productName` are the same.
  * `6e36ebbf`(#7342) On Windows, fix NSIS uninstaller failing to remove Start Menu shortcut if `perMachine` mode is used.


### Dependencies
  * Upgraded to `tauri-utils@1.5.0`
  * `a2be88a2`(#7405) Removed the `bitness` dependency to speed up compile time.


### Breaking Changes
  * `964d81ff`(#7616) The macOS notarization now uses `notarytool` as `altool` will be discontinued on November 2023. When authenticating with an API key, the key `.p8` file path must be provided in the `APPLE_API_KEY_PATH` environment variable. To prevent a breaking change, we will try to find the key path in the `altool` default search paths.


© 2025 Tauri Contributors. CC-BY / MIT
