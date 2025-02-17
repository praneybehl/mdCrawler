Skip to content
# tauri@1.0.0-rc.8
ReturnView on GitHub
  * **Breaking change:** Removed the `ayatana-tray` from the default features. You must select one of `ayatana-tray` and `gtk-tray` to use system tray on Linux. 
    * 62cdb2b3 refactor(tauri): remove ayatana-tray from the default features (#3976) on 2022-04-26
  * Re-export the `GlobalShortcutManager` when the `global-shortcut` feature is enabled. 
    * 62cdb2b3 refactor(tauri): remove ayatana-tray from the default features (#3976) on 2022-04-26
  * Fixes `docs.rs` documentation build. 
    * dd94917b fix(tauri): docs.rs build error (#3974) on 2022-04-26


© 2025 Tauri Contributors. CC-BY / MIT
