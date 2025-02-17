Skip to content
# tauri-cli@2.0.0-beta.14
ReturnView on GitHub
### Enhancements
  * `8a63ceb4f`(#9473) Ignore `.DS_Store` by default for `tauri dev` hot reloads.


### Bug Fixes
  * `e64b8f1dc`(#9479) Upgrade `heck` to v0.5 to better support Chinese and Japanese product name, because Chinese do not have word separation.
  * `aaa332c6e`(#9540) Fix `tauri migrate` trying to migrate to a non-existing plugin.
  * `e64b8f1dc`(#9479) Fixed an issue causing the `build.runner` and `build.features` configs to not take effect.


### Dependencies
  * Upgraded to `tauri-bundler@2.0.1-beta.10`
  * Upgraded to `tauri-utils@2.0.0-beta.13`


© 2025 Tauri Contributors. CC-BY / MIT
