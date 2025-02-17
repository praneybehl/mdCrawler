Skip to content
# tauri@1.4.1
ReturnView on GitHub
### Bug Fixes
  * `6afd3472`(#6680) Revert #6680 which added a default sound for notifications on Windows. This introduced inconsistency with other platforms that has silent notifications by default. In the upcoming releases, we will add support for modifying the notification sound across all platforms.


### Security fixes
  * `066c09a6`(#7227) Fix regression in `1.4` where the default behavior of the file system scope was changed to allow reading hidden files and directories by default.


© 2025 Tauri Contributors. CC-BY / MIT
