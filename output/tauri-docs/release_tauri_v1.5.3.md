Skip to content
# tauri@1.5.3
ReturnView on GitHub
### Enhancements
  * `b3e53e72`(#8288) Added `AssetResolver::iter` to iterate on all embedded assets.
  * `5e05236b`(#8289) Added tracing for window startup, plugins, `Window::eval`, events, IPC, updater and custom protocol request handlers behind the `tracing` feature flag.


### Bug Fixes
  * `2ba88563`(#8095) Fix docs.rs build for `x86_64-apple-darwin`.
  * `4b6a602a`(#8234) Escape path of the updater msi to avoid crashing on installers with spaces.


### Dependencies
  * Upgraded to `tauri-runtime-wry@0.14.2`
  * Upgraded to `tauri-macros@1.4.2`


© 2025 Tauri Contributors. CC-BY / MIT
