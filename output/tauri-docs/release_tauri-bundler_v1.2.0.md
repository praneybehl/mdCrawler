Skip to content
# tauri-bundler@1.2.0
ReturnView on GitHub
  * Add dylib support to `tauri.bundle.macOS.frameworks`. 
    * ce76d95a feat(tauri-cli): add dylib support to `tauri.bundle.macOS.frameworks`, closes #4615 (#5732) on 2022-12-31
  * Added support for pre-release identifiers and build numbers for the `.msi` bundle target. Only one of each can be used and it must be numeric only. The version must still be semver compatible according to https://semver.org/. 
    * 20ff1f45 feat(bundler): Add support for numeric-only build numbers in msi version (#6096) on 2023-01-19
  * On Windows, printing consistent paths on Windows with backslashs only. 
    * 9da99607 fix(cli): fix printing paths on Windows (#6137) on 2023-01-26
  * Fixed error during bundling process for the appimage target on subsequent bundling attempts. 
    * 2f70d8da fix: symlink issue bundling for linux #5781 (#6391) on 2023-03-17
  * Fixes DMG bundling not finding bundle to set icon position. 
    * 7489f966 fix(bundler): fix problem of macOS bunder while i18n is set, closes #6614 (#6615) on 2023-04-03
  * Use escaping on Handlebars templates. 
    * 6d6b6e65 feat: configure escaping on handlebars templates (#6678) on 2023-05-02
  * Bump minimum supported Rust version to 1.60. 
    * 5fdc616d feat: Use the zbus-backed of notify-rust (#6332) on 2023-03-31
  * Add initial support for building `nsis` bundles on non-Windows platforms. 
    * 60e6f6c3 feat(bundler): Add support for creating NSIS bundles on unix hosts (#5788) on 2023-01-19
  * Add `nsis` bundle target 
    * c94e1326 feat(bundler): add `nsis`, closes #4450, closes #2319 (#4674) on 2023-01-03
  * On Windows, the `msi` installer’s `Launch App` checkbox will be checked by default. 
    * 89602cdc feat(bundler): check `Launch app` by default for WiX, closes #5859 (#5871) on 2022-12-26


© 2025 Tauri Contributors. CC-BY / MIT
