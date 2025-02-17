Skip to content
# wry@0.9.0
ReturnView on GitHub
  * Refactor signatures of most closure types 
    * b8823fe refactor: signature of closure types (#167) on 2021-04-19
  * Drop handler closures properly on macOS. 
    * f905503 fix: #160 drop handler closures properly (#211) on 2021-04-27
  * Fix `history.pushState` in webview2. 
    * dd0fa46 Use http instead of file for windows custom protocol workaround (#173) on 2021-04-20
  * The `data_directory` field now affects the IndexedDB and LocalStorage directories on Linux. 
    * 1a6c821 feat(linux): implement custom user data path (#188) on 2021-04-22
  * Fix runtime panic on macOS, when no file handler are defined. 
    * 22a4991 bug(macOS): Runtime panic when no file_drop_handler (#177) on 2021-04-20
  * Add position field on WindowAttribute 
    * 2b3be7a Add position field on WindowAttribute (#219) on 2021-04-28
  * Fix panic on multiple custom protocols registration. 
    * 01647a2 Fix custom protocol registry on mac (#205) on 2021-04-26
  * Fix SVG render with the custom protocol. 
    * 890cfe5 fix(custom-protocol): SVG mime type - close #168 (#169) on 2021-04-19
  * Initial custom WindowExtWindows trait. 
    * 1ef1f58 feat: custom WindowExtWindow trait (#191) on 2021-04-23
  * Fix transparency on Windows 
    * e278556 fix: transparency on Windows (#217) on 2021-04-28
  * Add platform module and WindowExtUnix trait on Linux 
    * 004e298 feat: WindowExtUnix trait (#192) on 2021-04-23
  * Make sure custom protocol on Windows is over HTTPS. 
    * c36db35 fix(custom-protocol): Make sure custom protocol on Windows is over HTTPS. (#179) on 2021-04-20
  * Initial winit interface for gtk backend 
    * fa15076 feat: winit interface for gtk (#163) on 2021-04-19


© 2025 Tauri Contributors. CC-BY / MIT
