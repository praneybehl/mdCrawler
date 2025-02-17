Skip to content
# tauri-bundler@2.0.1-beta.15
ReturnView on GitHub
### New Features
  * `5462e5cad`(#9731) Add support for NSIS installer hooks providing a path to a `.nsh` file in `bundle &gt; windows &gt; nsis &gt; installer_hooks` key in `tauri.conf.json`.
  * `d6d3efbd1`(#9865) On Windows, add option to specify a custom signing command to be used. This opens an endless possibilities, for example use `osslsigncode` on non-Windows or use hardware tokens and HSM or even using Azure Trusted Signing.


### Enhancements
  * `418d72d72`(#9559) Added `/UPDATE` flag for NSIS installer which will make the installer avoid deleting app data and re-creating shortcuts.


### Bug Fixes
  * `4754786aa`(#9885) Fixed an issue causing the deep link feature to create invalid `Info.plist` values on macOS.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.17`


### Breaking Changes
  * `fc1543c65`(#9864) Removed `skip_webview_install` (`skipWebviewInstall`) option from config, which has been deprecated for a while now and planned to be removed in v2. Use `webview_install_mode` (`webviewInstallMode`) instead.


© 2025 Tauri Contributors. CC-BY / MIT
