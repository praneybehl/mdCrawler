Skip to content
# @tauri-apps/api@1.1.0
ReturnView on GitHub
  * Update `mockIPC()` handler signature to allow async handler functions. 
    * 4fa968dc fix(api): add async `mockIPC()` handler signature (#5056) on 2022-08-26
  * Improve shell’s `Command`, `Command.stdout` and `Command.stderr` events with new `once`, `off`, `listenerCount`, `prependListener`, `prependOnceListener` and `removeAllListeners` functions. 
    * aa9f1243 Improved EventEmitter for tauri api shell (#4697) on 2022-07-26
  * Added the `encoding` option to the `Command` options. 
    * d8cf9f9f Command support for specified character encoding, closes #4644 (#4772) on 2022-07-28
  * Add `exists` function to the fs module. 
    * 3c62dbc9 feat(api): Add `exists` function to the fs module. (#5060) on 2022-09-15


© 2025 Tauri Contributors. CC-BY / MIT
