Skip to content
# tauri-bundler@2.2.3
ReturnView on GitHub
### Bug Fixes
  * `de8600b4d` (#12471 by @anatawa12) Bumped `nsis-tauri-utils` to `0.4.2` which fixes the following bugs:
    * Fixed launch on start checkbox in nsis installer does not work well with applications that require elevated permissions
    * Fixed nsis installer may fail to install if launched by updater plugin
  * `fbe7c9ead` (#12466 by @FabianLars) Fixed an issue that caused the compiled AppImage to miss webkitgtk’s internal `libwebkit2gtkinjectedbundle.so` file.
  * `f5a59b93b` (#12136 by @unknovvn) The NSIS bundler will now replace non-numeric build metadata with `0` instead of returning an error.
  * `9dac2863a` (#12323 by @FabianLars) Skip signing the .dmg if self signing via `&quot;signingIdentity&quot;: &quot;-&quot;` is used.
  * `b8eb28877` (#12427 by @Legend-Master) Clean up `Software\$\{MANUFACTURER}\$\{PRODUCTNAME}` registry key in the NSIS uninstaller if “Delete application data” option is checked when uninstalling.


© 2025 Tauri Contributors. CC-BY / MIT
