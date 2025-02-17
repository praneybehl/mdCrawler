Skip to content
# tao@0.15.5
ReturnView on GitHub
  * Change `WebviewAttributes::focused` default to `true`. 
    * ece3e8f6 fix: default `focused` to true on 2022-11-20
  * On Linux, wake the main context in `EventLoopProxy::send_event()`. 
    * b7b5f04d Gtk: wake the main context in EventLoopProxy::send_event(), closes #625 (#626) on 2022-11-16


© 2025 Tauri Contributors. CC-BY / MIT
