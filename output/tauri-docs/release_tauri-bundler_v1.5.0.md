Skip to content
# tauri-bundler@1.5.0
ReturnView on GitHub
### New Features
  * `7aa30dec`(#8620) Add `priority`, `section` and `changelog` options in Debian config.
  * `89911296`(#8259) On macOS, support for signing nested .dylib, .app, .xpc and .framework under predefined directories inside the bundled frameworks (“MacOS”, “Frameworks”, “Plugins”, “Helpers”, “XPCServices” and “Libraries”).
  * `8ce51cec`(#7718) On Windows, NSIS installer now supports `/ARGS` flag to pass arguments to be used when launching the app after installation, only works if `/R` is used.


### Enhancements
  * `06890c70`(#8611) Support using socks proxy from environment when downloading files.


### Bug Fixes
  * `6bdba1f3`(#8585) Fix the `non-standard-file-perm` and `non-standard-dir-perm` issue in Debian packages


### Dependencies
  * `49266487`(#8618) Replace `libflate` with `flate2` , this will help to provide additional functionalities and features.


© 2025 Tauri Contributors. CC-BY / MIT
