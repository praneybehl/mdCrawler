Skip to content
# tauri-cli@2.2.6
ReturnView on GitHub
### Enhancements
  * `1a86974aa` (#12406 by @bradleat) `ios build --open` will now let xcode start the rust build process.
  * `9a30bed98` (#12423 by @tr3ysmith) Added conditional logic to MacOS codesigning where only executables get the entitlements file when being signed. This solves an issue where the app may not launch when using 3rd party frameworks if certain entitlements are added. Ex: multicast support (must be applied for through apple developer, and the framework would not have that capability).
  * `0b79af711` (#12438 by @3lpsy) Log the command used to start the rust app in development.


### Bug Fixes
  * `bc43c738b` (#12442 by @FabianLars) Fixed an issue that prevented `tauri add` to work for the `clipboard-manager` plugin.
  * `27096cdc0` (#12445 by @FabianLars) Fixed an issue that caused Tauri’s CLI to enable tauri’s `native-tls` feature even though it wasn’t needed. Moved `reqwest` to a mobile-only dependency in `tauri` and enabled its `rustls-tls` feature flag.


### Dependencies
  * Upgraded to `tauri-bundler@2.2.3`


© 2025 Tauri Contributors. CC-BY / MIT
