Skip to content
# wry@0.9.1
ReturnView on GitHub
  * Correctly set visibility when building `Window` on gtk-backend 
    * 4395ad1 fix: only call `show_all` when needed (#227) on 2021-05-02
  * Fix `macOS` cursors and other minors UI glitch. 
    * d550b2f fix(macOS): Window layers (#220) on 2021-04-28
  * Expose `print()` function to the webview. Work only on macOS for now. 
    * 5206db6 fix(macOS): Printing (#235) (#236) on 2021-05-06
  * Fix macOS windows order for tray (statusbar) applications. 
    * 229275f fix: macOS windows order (#242) on 2021-05-07
  * Add `request_redraw` method of `Window` on Linux 
    * 03abfa0 Add request_redraw method on Linux (#222) on 2021-04-30
  * Add tao as window dependency. 
    * 483bad0 feat: tao as window dependency (#230) on 2021-05-03
  * Close the window when the instance is dropped on Linux and Windows. 
    * 3f2cc28 fix: close window when the instance is dropped (#228) on 2021-05-02
  * Remove winit dependency on Linux 
    * fa15076 feat: winit interface for gtk (#163) on 2021-04-19
    * 39d6f59 publish new versions (#166) on 2021-04-29
    * 4ef8330 Remove winit dependency on Linux (#226) on 2021-04-30


© 2025 Tauri Contributors. CC-BY / MIT
