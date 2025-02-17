Skip to content
# @tauri-apps/api@2.0.0-alpha.13
ReturnView on GitHub
### New Features
  * `428ea652`(#8370) Exposed `Resource` class which should be extended for Rust-backed resources created through `tauri::Manager::resources_table`.


### Bug Fixes
  * `ef21b681`(#8391) Fix a regression where typescript could not find types when using `&quot;moduleResolution&quot;: &quot;node&quot;`
  * `46451aee`(#8268) Add top-level `main`, `module` and `types` fields in `package.json` to be compliant with typescripts’s `&quot;moduleResolution&quot;: &quot;node&quot;`


### Breaking Changes
  * `c2ad4d28`(#8273) Changed former `tauri` module from `primitives` to `core`.


© 2025 Tauri Contributors. CC-BY / MIT
