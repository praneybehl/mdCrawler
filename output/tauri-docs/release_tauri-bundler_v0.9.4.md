Skip to content
# tauri-bundler@0.9.4
ReturnView on GitHub
  * `dirs` crate is unmaintained, now using `dirs-next` instead. 
    * 82cda98 chore(tauri) `dirs` crate is unmaintained, use `dirst-next` instead (#1057) on 2020-10-17
    * 72996be apply version updates (#1024) on 2020-10-21
  * Force IPv4 on `wget` so AppImage bundling doesn’t hang. 
    * 6f5667b fix: #1018 Force IPv4 on wget requests (#1019) on 2020-10-11
    * 72996be apply version updates (#1024) on 2020-10-21
  * Set the Windows installer (WiX) `WorkingDirectory` field to `INSTALLDIR` so the app can read paths relatively (previously resolving to `C:\Windows\System32`). 
    * 5cf3402 fix: add working directory to wix’s shortcut (#1021) on 2020-09-24
    * 72996be apply version updates (#1024) on 2020-10-21


© 2025 Tauri Contributors. CC-BY / MIT
