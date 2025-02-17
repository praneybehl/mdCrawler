Skip to content
# @tauri-apps/cli@1.4.0
ReturnView on GitHub
### New Features
  * `0ddbb3a1`(#7015) Provide prebuilt CLIs for Windows ARM64 targets.
  * `35cd751a`(#5176) Added the `desktop_template` option on `tauri.conf.json &gt; tauri &gt; bundle &gt; deb`.
  * `6c5ade08`(#4537) Added `tauri completions` to generate shell completions scripts.
  * `e092f799`(#6887) Add `nsis &gt; template` option to specify custom NSIS installer template.


### Enhancements
  * `d75c1b82`(#7181) Print a useful error when `updater` bundle target is specified without an updater-enabled target.
  * `52474e47`(#7141) Enhance injection of Cargo features.
  * `2659ca1a`(#6900) Add `rustls` as default Cargo feature.


### Bug Fixes
  * `3cb7a3e6`(#6997) Fix built-in devserver adding hot-reload code to non-html files.
  * `fb7ef8da`(#6667) Fix nodejs binary regex when `0` is in the version name, for example `node-20`
  * `1253bbf7`(#7013) Fixes Cargo.toml feature rewriting.


© 2025 Tauri Contributors. CC-BY / MIT
