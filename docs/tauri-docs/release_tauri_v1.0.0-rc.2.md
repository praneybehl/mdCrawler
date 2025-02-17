Skip to content
# tauri@1.0.0-rc.2
ReturnView on GitHub
  * Ease the requirements for plugin hooks. `setup` and `setup_with_config` can now be `FnOnce` and `on_webview_ready`, `on_event` and `on_page_load` can be `FnMut`. 
    * fd557e98 Ease plugin hook restrictions (#3404) on 2022-02-13
  * Fixes an issue with the updater when replacing the `{{target}}` and `{{current_version}}` variables due to percent-encoding on the `Url` that is parsed from the configuration. 
    * 20f0477f fix(core): updater not replacing variables, closes #3428 (#3432) on 2022-02-13


© 2025 Tauri Contributors. CC-BY / MIT
