Skip to content
# tauri@1.0.0-rc.14
ReturnView on GitHub
  * **Breaking change:** `PackageInfo::version` is now a `semver::Version` instead of a `String`. 
    * 2badbd2d refactor: force semver versions, change updater `should_install` sig (#4215) on 2022-05-25
    * a7388e23 fix(ci): adjust change file to include tauri-utils and tauri-codegen on 2022-05-27
  * **Breaking change** : `UpdateBuilder::should_update` now takes the current version as a `semver::Version` and a `RemoteRelease` struct, allowing you to check other release fields. 
    * 2badbd2d refactor: force semver versions, change updater `should_install` sig (#4215) on 2022-05-25
  * **Breaking change:** The `tauri::UpdaterEvent::UpdateEvent` date field is now an `Option&lt;time::OffsetDateTime&gt;`. 
    * ac7656ab refactor(updater): strong type for the `pub_date` field, ref #4162 (#4218) on 2022-05-25
  * **Breaking change:** The updater response `pub_date` now must be a valid RFC 3339 string. 
    * ac7656ab refactor(updater): strong type for the `pub_date` field, ref #4162 (#4218) on 2022-05-25


© 2025 Tauri Contributors. CC-BY / MIT
