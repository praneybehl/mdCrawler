Skip to content
# @tauri-apps/api@1.0.0-beta.0
ReturnView on GitHub
  * CommonJS chunks are now properly exported with `.cjs` extension 
    * ddcd923 fix(api): export commonjs chunks with `.cjs` extension, fix #1625 (#1627) on 2021-04-26
  * Adds `transparent?: boolean` to the `WindowOptions` interface. 
    * 08c1c5c fix(api): missing `transparent` flag on `WindowOptions` (#1764) on 2021-05-10
  * Adds `options` argument to the shell command API (`env` and `cwd` configuration). 
    * 721e98f feat(core): add env, cwd to the command API, closes #1634 (#1635) on 2021-04-28
  * Adds `startDragging` API on the window module. 
    * c31f097 refactor: update to wry 0.9 (#1630) on 2021-04-28
  * Move `exit` and `relaunch` APIs from `app` to `process` module. 
    * b0bb796 refactor: rename `command` mod to `process`, move restart_application (#1667) on 2021-04-30
  * The window management API was refactored: removed `setX`, `setY`, `setWidth`, `setHeight` APIs, renamed `resize` to `setSize` and the size and position APIs now allow defining both logical and physical values. 
    * 6bfac86 refactor(core): add window getters, physical & logical sizes/positions (#1723) on 2021-05-05
  * Adds window getters. 
    * 6bfac86 refactor(core): add window getters, physical & logical sizes/positions (#1723) on 2021-05-05


© 2025 Tauri Contributors. CC-BY / MIT
