Skip to content
# @tauri-apps/cli@2.0.0-alpha.3
ReturnView on GitHub
  * Added `plugin android add` and `plugin ios add` commands to add mobile plugin functionality to existing projects. 
    * 14d03d42 refactor(cli): enhance plugin commands for mobile (#6289) on 2023-02-16
  * Add commands to add native Android and iOS functionality to plugins. 
    * 05dad087 feat: initial work for iOS plugins (#6205) on 2023-02-11
  * Use temp file instead of environment variable to pass CLI IPC websocket address to the IDE. 
    * 894a8d06 refactor(cli): use temp file to communicate IPC websocket address (#6219) on 2023-02-08
  * Change the Android template to enable minification on release and pull ProGuard rules from proguard-tauri.pro. 
    * bef4ef51 feat(android): enable minify on release, add proguard rules (#6257) on 2023-02-13
  * Print an error if the Android project was generated with an older bundle identifier or package name. 
    * 79eb0542 feat(cli): handle Android package identifier change (#6314) on 2023-02-19
  * Fixes the generated mobile build script when using an NPM runner. 
    * 62f15265 fix(cli): generate build script using NPM runner if it was used (#6233) on 2023-02-10
  * Resolve Android package name from single word bundle identifiers. 
    * 60a8b07d fix: handle single word bundle identifier when resolving Android domain (#6313) on 2023-02-19
  * Update Android project template with fix to crash on orientation change. 
    * 947eb391 fix(android): crash on orientation change due to activity recreation (#6261) on 2023-02-13
  * Added `--ios-color` option to the `tauri icon` command. 
    * 67755425 feat(cli): add `--ios-color` option to set iOS icon background color (#6247) on 2023-02-12
  * Fixes HMR on mobile when devPath is configured to load a filesystem path. 
    * 4a82da29 fix(cli): use local ip address for reload (#6285) on 2023-02-16
  * Ignore the `gen` folder on the dev watcher. 
    * cab4ff95 fix(cli): ignore the `gen` folder on the dev watcher (#6232) on 2023-02-09
  * Correctly pass arguments from `npm run` to `tauri`. 
    * 1b343bd1 fix(cli): use `npm run tauri -- foo` for correctly passing args to tauri (#6448) on 2023-03-16
  * Changed the `--api` flag on `plugin init` to `--no-api`. 
    * 14d03d42 refactor(cli): enhance plugin commands for mobile (#6289) on 2023-02-16


© 2025 Tauri Contributors. CC-BY / MIT
