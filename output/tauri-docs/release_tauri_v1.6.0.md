Skip to content
# tauri@1.6.0
ReturnView on GitHub
### New Features
  * `6e488378`(#8474) Re-export `Url` type.


### Enhancements
  * `8ce51cec`(#7718) On Windows, retain command line args when relaunching the app after an update. Supports NSIS and WiX (without elevated update task).


### Bug Fixes
  * `cc3d8e77`(#8539) Fixes a deadlock when reading a stdout or stderr line returns an error.
  * `b546b42d`(#8577) Preserve the order of JS object/map keys in IPC calls. This also fixes issues with the JS `http` module when calling to servers that required a specific order of `FormBody` contents.
  * `8f8729d9`(#8312) On macOS, allow cancelling maximization when doubleclick happens on `data-tauri-drag-region` by simply keeping the left moust button pressed and then moving the mouse away of the starting position of the click, which is consistent with the native behavior of macOS.


### Dependencies
  * Upgraded to `tauri-runtime-wry@0.14.4`


© 2025 Tauri Contributors. CC-BY / MIT
