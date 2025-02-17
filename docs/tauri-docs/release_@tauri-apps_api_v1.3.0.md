Skip to content
# @tauri-apps/api@1.3.0
ReturnView on GitHub
  * Return correct type for `event.payload` in `onResized` and `onMoved` window event handlers. 
    * 0b46637e fix(api): construct correct object for onResized and onMoved, closes #6507 (#6509) on 2023-04-03
  * Added the `WindowOptions::contentProtected` option and `WebviewWindow#setContentProtected` to change it at runtime. 
    * 4ab5545b feat: add content protection api, closes #5132 (#5513) on 2022-12-13
  * Allow setting the text of the dialog buttons. 
    * 00e1efaa feat: customize button texts of message dialog (#4383) on 2022-12-28
  * Add `is_minimized()` window method. 
    * 62144ef3 feat: add is_minimized (fix #3878) (#5618) on 2022-12-13
  * Add `title` getter on window. 
    * 233e43b0 feat: add `title` getter on window, closes #5023 (#5515) on 2022-12-13


© 2025 Tauri Contributors. CC-BY / MIT
