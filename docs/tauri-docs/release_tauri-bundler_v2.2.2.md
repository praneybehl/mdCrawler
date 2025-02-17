Skip to content
# tauri-bundler@2.2.2
ReturnView on GitHub
### Bug Fixes
  * `72748cc45` (#12365 by @don41382) Fixed an issue that caused the `.msi` installer not to lookup the `INSTALLDIR` set in the `nsis` installer.
  * `cf771bf69` (#12402 by @FabianLars) Fixed an issue that caused the .msi installer to not contain root resources when there were .dll files present in the target directory.
  * `07ccdc499` (#12324 by @FabianLars) Fixed an issue leading to NSIS based installers to not contain the `WebView2Loader.dll` file when targetting `windows-gnu`.


© 2025 Tauri Contributors. CC-BY / MIT
