Skip to content
# @tauri-apps/api@2.0.0-beta.13
ReturnView on GitHub
### Breaking Changes
  * `c4410daa8`(#9777) This release contains breaking changes to the tray event structure because of newly added events:
    * Changed `TrayIconEvent` to be an enum instead of a struct.
    * Added `MouseButtonState` and `MouseButton` enums.
    * Removed `ClickType` enum and replaced it with `MouseButton` enum.
    * Added `MouseButtonState` enum.


© 2025 Tauri Contributors. CC-BY / MIT
