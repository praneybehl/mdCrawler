Skip to content
# tauri-bundler@1.0.0-beta.0
ReturnView on GitHub
  * Fixes the `Installed-Size` value on the debian package. 
    * 8e0d4f6 fix(bundler): debian package `Installed-Size` value (#1735) on 2021-05-07
  * Use `armhf` as Debian package architecture on `arm` CPUs. 
    * 894643c feat(bundler): use `armhf` as Debian package architecture on arm CPUs (#1663) on 2021-04-30
  * Adds basic library documentation. 
    * fcee4c2 refactor(bundler): finish initial documentation, reorganize modules (#1662) on 2021-04-30
  * The `PackageTypes` enum now includes all options, including Windows packages. 
    * fcee4c2 refactor(bundler): finish initial documentation, reorganize modules (#1662) on 2021-04-30
  * Adds `icon_path` field to the `WindowsSettings` struct (defaults to `icons/icon.ico`). 
    * 314936e feat(bundler): add icon path config instead of enforcing icons/icon.ico (#1698) on 2021-05-03
  * Pull latest changes from `create-dmg`, fixing unmount issue. 
    * f1aa120 fix(bundler): update create-dmg, fixes #1571 (#1729) on 2021-05-06
  * Fixes DMG volume icon. 
    * e37e187 fix(bundler): dmg volume icon (#1730) on 2021-05-06
  * Added the `#[non_exhaustive] attribute where appropriate. 
    * e087f0f feat: add `#[non_exhaustive]` attribute (#1725) on 2021-05-05


© 2025 Tauri Contributors. CC-BY / MIT
