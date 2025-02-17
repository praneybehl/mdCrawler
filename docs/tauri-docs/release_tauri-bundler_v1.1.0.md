Skip to content
# tauri-bundler@1.1.0
ReturnView on GitHub
  * Use correct code `ja-JP` for japanese instead of `jp-JP`. 
    * d4cac202 fix(bundler): fix japanese lang code, closes #5342 (#5346) on 2022-10-04
  * Fix WiX DLL load on Windows Server. 
    * 7aaf27ce fix(bundler): load WiX DLLs on Github Actions (#5552) on 2022-11-04
  *     * 7d9aa398 feat: bump MSRV to 1.59 (#5296) on 2022-09-28
  * Add `tauri.conf.json &gt; bundle &gt; publisher` field to specify the app publisher. 
    * 628285c1 feat(bundler): add `publisher` field, closes #5273 (#5283) on 2022-09-28
  * Clear environment variables on the WiX light.exe and candle.exe commands to avoid “Windows Installer Service could not be accessed” error. Variables prefixed with `TAURI` are propagated. 
    * 7c0fa1f3 fix(bundler): clear env before calling wix, closes #4791 (#4819) on 2022-10-03


© 2025 Tauri Contributors. CC-BY / MIT
