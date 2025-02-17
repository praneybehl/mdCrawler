Skip to content
# @tauri-apps/api@1.0.0-rc.2
ReturnView on GitHub
  * Do not crash if `__TAURI_METADATA__` is not set, log an error instead. 
    * 9cb1059a fix(api): do not throw an exception if **TAURI_METADATA** is not set, fixes #3554 (#3572) on 2022-03-03
  * Reimplement endpoint to read file as string for performance. 
    * 834ccc51 feat(core): reimplement `readTextFile` for performance (#3631) on 2022-03-07
  * Fixes a regression on the `unlisten` command. 
    * 76c791bd fix(core): regression on the unlisten function (#3623) on 2022-03-06


© 2025 Tauri Contributors. CC-BY / MIT
