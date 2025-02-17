Skip to content
# @tauri-apps/cli@2.1.0
ReturnView on GitHub
### New Features
  * `6bf917941` (#11322 by @ShaunSHamilton) Add `tauri remove` to remove plugins from projects.
  * `058c0db72` (#11584 by @amrbashir) Add `bundle &gt; linux &gt; rpm &gt; compression` config option to control RPM bundle compression type and level.


### Enhancements
  * `1f311832a` (#11405 by @amrbashir) Add more context for errors when decoding secret and public keys for signing updater artifacts.
  * `e0d1307d3` (#11414 by @Czxck001) Migrate the `$schema` Tauri configuration to the v2 format.
  * `c43d5df15` (#11512 by @lucasfernog) Associate a newly created capability file with the `main` window on the `tauri add` and `tauri permission add` commands.


### Bug Fixes
  * `7af01ff2c` (#11523 by @amrbashir) Fix `tauri migrate` failing to install NPM depenencies when running from Deno.
  * `100a4455a` (#11529 by @amrbashir) Fix detecting yarn berry (v2 and higher) in various tauri cli commands.
  * `60e86d5f6` (#11624 by @lucasfernog) Use the public network IP address on `android dev` by default on Windows.


### Dependencies
  * Upgraded to `tauri-cli@2.1.0`


© 2025 Tauri Contributors. CC-BY / MIT
