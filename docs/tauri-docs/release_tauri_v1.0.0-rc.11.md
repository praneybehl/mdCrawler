Skip to content
# tauri@1.0.0-rc.11
ReturnView on GitHub
  * Added the `App::get_cli_matches` helper function. 
    * 617f1144 feat(core): add `App::get_cli_matches` helper ref #4145 on 2022-05-17
  * Fixes `fileDropEnabled` option not working. 
    * 706fcbd3 fix(core): fileDropEnabled option is not working when creating a new WebviewWindow (#4146) on 2022-05-18
  * Prepare window icon and menu even when loading remote URLs. Previously it was behind a `is local URL?` condition. 
    * 25aa4347 fix(core): prepare window icon and menu on remote URLs, closes #4131 (#4140) on 2022-05-16
  * Fix `.mjs` not being recognised as a file extension for JavaScript files (`text/javascript`). 
    * 45c45253 fix: add mjs mime type (fix: #4098) (#4108) on 2022-05-13
  * Added `PathResolver::resolve_resource` API. 
    * e35aaebc feat(core): add `PathResolver::resolve_resource` API (#4116) on 2022-05-13
  * Allow configuring the display options for the MSI execution allowing quieter updates. 
    * 9f2c3413 feat(core): configure msiexec display options, closes #3951 (#4061) on 2022-05-15


© 2025 Tauri Contributors. CC-BY / MIT
