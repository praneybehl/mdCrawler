Skip to content
# tauri-cli@1.0.0-rc.13
ReturnView on GitHub
  * Check if `$CWD/src-tauri/tauri.conf.json` exists before walking through the file tree to find the tauri dir in case the whole project is gitignored. 
    * bd8f3e29 fix(cli): manual config lookup to handle gitignored folders, fixes #3527 (#4224) on 2022-05-26
  * Statically link the Visual C++ runtime instead of using a merge module on the installer. 
    * bb061509 refactor(core): statically link vcruntime, closes #4122 (#4227) on 2022-05-27


© 2025 Tauri Contributors. CC-BY / MIT
