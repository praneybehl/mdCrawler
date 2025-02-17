Skip to content
# tauri@2.0.0-alpha.19
ReturnView on GitHub
### New Features
  * `b59f2f54`(#8432) Expose `scope::fs::Scope::new`.
  * `bf095df5`(#8276) Exposed `Manager::resources_table` to access the resources table used by tauri, which could be used by plugins or app authors to store their resources and retrieve it later using an id and can be used to create Rust-backed resources in JS.


### Enhancements
  * `5848b4e8`(#8386) Fixed the deserialisation of a `Channel` in iOS.
  * `11a1529d`(#8419) Include CORS header on custom protocol response errors to ensure frontend can read the error message.
  * `db127777`(#8380) Added `test::get_ipc_response`.


### Bug Fixes
  * `effe5871`(#8420) Fixes file scope checks on Android.
  * `f98ce5aa`(#8328) Fix incorrect menu item for `PredefinedMenuItem::close_window`


© 2025 Tauri Contributors. CC-BY / MIT
