Skip to content
# tauri-bundler@1.0.0-rc.3
ReturnView on GitHub
  * Added `tsp` config option under `tauri &gt; bundle &gt; windows`, which enables Time-Stamp Protocol (RFC 3161) for the timestamping server under code signing on Windows if set to `true`. 
    * bdd5f7c2 fix: add support for Time-Stamping Protocol for Windows codesigning (fix #3563) (#3570) on 2022-03-07
  * Properly create the updater bundle for all generated Microsoft Installer files. 
    * 6a6f1e7b fix(bundler): build updater bundle for all .msi files (#3520) on 2022-02-24
  * Fixes the Microsoft Installer launch path. 
    * 8d699283 fix(bundler): Auto-launch app from install location, closes #3547 (#3553) on 2022-02-24


© 2025 Tauri Contributors. CC-BY / MIT
