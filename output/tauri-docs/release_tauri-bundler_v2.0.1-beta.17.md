Skip to content
# tauri-bundler@2.0.1-beta.17
ReturnView on GitHub
### New Features
  * `fafc238f7` (#9977) Add `bundle &gt; homepage` option, if unset, it will fallback to `homepage` defined in `Cargo.toml`.
  * `656a64974` (#9318) Added a configuration option to disable hardened runtime on macOS codesign.
  * `3ab170917` (#9932) Add an option to disable NSIS compression `bundle &gt; nsis &gt; compression: &quot;none&quot;`
  * `f21029b1b` (#9994) Add `bundle &gt; nsis &gt; startMenuFolder` option to customize start menu folder for NSIS installer


### Enhancements
  * `61bbd8373` (#10117) Added a public property to the msi to tell the installer to launch the app after installation. This was added for the updater plugin.
  * `ea78bf555` (#9915) For NSIS installer, migrate old shortcuts by setting the path only instead of re-creating a new one


### Bug Fixes
  * `b9e11a8b9` (#10036) Fixed an issue that caused the AppImage to segfault on start due to an incorrect .desktop file.
  * `3fd84cb3c` (#10049) Fix encoding of NSIS license page when using a license file without a BOM.
  * `de7da04a6` (#9974) Use the `productName` for `rpm` package name instead of main binary name, to be consistent with other bundle types.
  * `faf282ca6` (#10103) Fix NSIS uninstaller failing to clean up deep links
  * `58821fc0e` (#10086) Fix NSIS esitmated size unit being in kB (1000 bytes) not KB (1024 bytes)
  * `6f469534b` (#9944) Fix NSIS installer runs the app as admin when using `perMachine` install mode


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-beta.18`
  * `f955f7b49` (#9929) Switch from `dirs_next` to `dirs` as `dirs_next` is now unmaintained while `dirs` is


### Breaking Changes
  * `f21029b1b` (#9994) Changed NSIS start menu shortcut to be placed directly inside `%AppData%\Microsoft\Windows\Start Menu\Programs` without an additional folder. You can get the old behavior by setting `bundle &gt; nsis &gt; startMenuFolder` to the same value as your `productName`
  * `911242f09` (#9883) Move updater target from `bundle &gt; targets` to a separate field `bundle &gt; createUpdaterArtifacts`


© 2025 Tauri Contributors. CC-BY / MIT
