Skip to content
# @tauri-apps/cli@2.0.0-rc.0
ReturnView on GitHub
### New Features
  * `d5511c311` (#10395) Added migration from `2.0.0-beta` to `2.0.0-rc`.
  * `a5bfbaa62`(#9962) Added `bundle &gt; iOS &gt; frameworks` configuration to define a list of frameworks that are linked to the Xcode project when it is generated.


### Enhancements
  * `a0841d509` (#10421) Changes the default behavior of the `dev` command to only expose to localhost (`127.0.0.1`) instead of the default system interface.


### Security fixes
  * `289ae5555` (#10386) Re-enable TLS checks that were previously disabled to support an insecure HTTPS custom protocol on Android which is no longer used.


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-rc.0`


### Breaking Changes
  * `758d28c8a` (#10390) Core plugin permissions are now prefixed with `core:`, the `core:default` permission set can now be used and the `core` plugin name is reserved. The `tauri migrate` tool will automate the migration process, which involves prefixing all `app`, `event`, `image`, `menu`, `path`, `resources`, `tray`, `webview` and `window` permissions with `core:`.
  * `7ba67b4ac`(#10437) `ios dev` and `android dev` now uses localhost for the development server unless running on an iOS device, which still requires connecting to the public network address. To conditionally check this on your frontend framework’s configuration you can check for the existence of the `TAURI_DEV_HOST` environment variable instead of checking if the target is iOS or Android (previous recommendation).


© 2025 Tauri Contributors. CC-BY / MIT
