Skip to content
# tauri@1.0.0-rc.3
ReturnView on GitHub
  * `tauri::plugin::Builder` closures are no longer required to implement `Sync`. 
    * fb7ee2c9 drop Sync req from `setup` and `setup_with_config` (#3471) on 2022-02-16
    * b8e4d651 fix(core): drop all plugin builder Sync requirements (#3490) on 2022-02-17
  * Added context to the file system endpoint errors. 
    * 06053833 feat(core): add context to the filesystem APIs errors, closes #3457 (#3480) on 2022-02-16
  * Changed the default value for `tauri &gt; bundle &gt; macOS &gt; minimumSystemVersion` to `10.13`. 
    * fce344b9 feat(core): set default value for `minimum_system_version` to 10.13 (#3497) on 2022-02-17


© 2025 Tauri Contributors. CC-BY / MIT
