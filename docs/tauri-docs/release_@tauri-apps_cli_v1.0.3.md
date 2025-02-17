Skip to content
# @tauri-apps/cli@1.0.3
ReturnView on GitHub
  * Changed the app template to not set the default app menu as it is now set automatically on macOS which is the platform that needs a menu to function properly. 
    * 91055883 feat: add implicit default menu for macOS only, closes #4551 (#4570) on 2022-07-04
  * Improved bundle identifier validation showing the exact source of the configuration value. 
    * 8e3e7fc6 feat(cli): improve bundle identifier validation, closes #4589 (#4596) on 2022-07-05
  * Improve configuration deserialization error messages. 
    * 9170c920 feat(core): improve config deserialization error messages (#4607) on 2022-07-06
  * Revert the `run` command to run in a separate thread. 
    * f65eb4f8 fix(cli.js): revert `run` command to be nonblocking on 2022-07-04
  * Skip the static link of the `vcruntime140.dll` if the `STATIC_VCRUNTIME` environment variable is set to `false`. 
    * 2e61abaa feat(cli): allow dynamic link vcruntime, closes #4565 (#4601) on 2022-07-06
  * The `TAURI_CONFIG` environment variable now represents the configuration to be merged instead of the entire JSON. 
    * fa028ebf refactor: do not pass entire config from CLI to core, send patch instead (#4598) on 2022-07-06
  * Watch for Cargo workspace members in the `dev` file watcher. 
    * dbb8c87b feat(cli): watch Cargo workspaces in the dev command, closes #4222 (#4572) on 2022-07-03


© 2025 Tauri Contributors. CC-BY / MIT
