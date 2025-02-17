Skip to content
# tauri-cli@1.4.0
ReturnView on GitHub
### New Features
  * `0ddbb3a1`(#7015) Provide prebuilt CLIs for Windows ARM64 targets.
  * `35cd751a`(#5176) Added the `desktop_template` option on `tauri.conf.json &gt; tauri &gt; bundle &gt; deb`.
  * `6c5ade08`(#4537) Added `tauri completions` to generate shell completions scripts.
  * `29488205`(#6867) Allow specifying custom language files of Tauri’s custom messages for the NSIS installer
  * `e092f799`(#6887) Add `nsis &gt; template` option to specify custom NSIS installer template.


### Enhancements
  * `d75c1b82`(#7181) Print a useful error when `updater` bundle target is specified without an updater-enabled target.
  * `52474e47`(#7141) Enhance injection of Cargo features.
  * `2659ca1a`(#6900) Add `rustls` as default Cargo feature.
  * `c7056d1b`(#6982) Improve Visual Studio installation detection in `tauri info` command to check for the necessary components instead of whole workloads. This also fixes the detection of minimal installations and auto-installations done by `rustup`.


### Bug Fixes
  * `3cb7a3e6`(#6997) Fix built-in devserver adding hot-reload code to non-html files.
  * `fd3b5a16`(#6954) Fix building with a custom cargo profile
  * `1253bbf7`(#7013) Fixes Cargo.toml feature rewriting.


© 2025 Tauri Contributors. CC-BY / MIT
