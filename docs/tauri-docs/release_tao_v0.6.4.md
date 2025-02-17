Skip to content
# tao@0.6.4
ReturnView on GitHub
  * Fix a deadlock on Windows when using `Window::set_visible(true)` in the `EventLoop::run` closure. 
    * 475e64d2 fix(Windows): fix a deadlock in `WindowState` (#338) on 2022-03-06
  * On Windows, apply maximize state before minimize. Fixes `Window::set_minimized` not working when the window is maximized. 
    * 11dac102 fix(windows): apply maximize state before minimize (#334) on 2022-03-01


© 2025 Tauri Contributors. CC-BY / MIT
