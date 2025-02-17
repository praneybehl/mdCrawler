Skip to content
# tauri-cli@2.0.0-alpha.11
ReturnView on GitHub
### New Features
  * `522de0e7`(#7447) Expose an environment variable `TAURI_$\{PLUGIN_NAME}_PLUGIN_CONFIG` for each defined plugin configuration object.
  * `c7dacca4`(#7446) Expose the `TAURI_IOS_PROJECT_PATH` and `TAURI_IOS_APP_NAME` environment variables when using `ios` commands.
  * `aa94f719`(#7445) Generate empty entitlements file for the iOS project.
  * `d010bc07`(#7554) Set the iOS project PRODUCT_NAME value to the string under `tauri.conf.json &gt; package &gt; productName` if it is set.
  * `8af24974`(#7561) The `migrate` command now automatically reads all JavaScript files and updates `@tauri-apps/api` import paths and install the missing plugins.


### Enhancements
  * `fbeb5b91`(#7170) Update migrate command to update the configuration CSP to include `ipc:` on the `connect-src` directive, needed by the new IPC using custom protocols.


### Bug Fixes
  * `5eb85543`(#7282) Fix `tauri info` failing when there is no available iOS code signing certificate.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-alpha.7`
  * Upgraded to `tauri-bundler@2.0.0-alpha.7`


© 2025 Tauri Contributors. CC-BY / MIT
