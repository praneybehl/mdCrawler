Skip to content
# @tauri-apps/api@1.0.0-rc.4
ReturnView on GitHub
  * Encode the file path in the `convertFileSrc` function. 
    * 42e8d9cf fix(api): encode file path in `convertFileSrc` function, closes #3841 (#3846) on 2022-04-02
  * Added `theme` getter to `WebviewWindow`. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21
  * Added `theme` field to `WindowOptions`. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21
  * Added the `setCursorGrab`, `setCursorVisible`, `setCursorIcon` and `setCursorPosition` methods to the `WebviewWindow` class. 
    * c54ddfe9 feat: expose window cursor APIs, closes #3888 #3890 (#3935) on 2022-04-21
  * **Breaking change:** The process Command API stdio lines now includes the trailing `\r`. 
    * b5622882 fix(cli): exit on non-compilation Cargo errors, closes #3930 (#3942) on 2022-04-22
  * Added the `tauri://theme-changed` event. 
    * 4cebcf6d feat: expose theme APIs, closes #3903 (#3937) on 2022-04-21


© 2025 Tauri Contributors. CC-BY / MIT
