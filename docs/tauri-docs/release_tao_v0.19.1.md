Skip to content
# tao@0.19.1
ReturnView on GitHub
  * On Windows, fix auto-hide taskbar can’t be shown when maximizing undecorated window. 
    * c5d606df fix(windows): leave space for auto-hidden taskbar for undecorated windows (#726) on 2023-04-19
  * On Linux, fix `ShortcutManager::unregister_all` making `ShortcutManager::register` succeed but no events are triggered. 
    * ee5dc41f fix(linux): clear shortcuts instead of replacing it (#724) on 2023-04-18
  * On macOS, fix window frozed when starting with fullscreen. 
    * 71594667 fix(macOS): windows frozen when starting in fullscreen (#727) on 2023-05-04


© 2025 Tauri Contributors. CC-BY / MIT
