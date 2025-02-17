Skip to content
# tao@0.31.0
ReturnView on GitHub
  * `5d6d7da0` (#1017 by @amrbashir) On Windows, fix regression caused undecorated window with shadows to be slightly larger on creation.
  * `2e6cf1a4` (#1022 by @Jnschrber) On Windows, fix crash on older windows versions that doesn’t support dark mode.
  * `6b49f55a` (#1016 by @Legend-Master) Expose raw gdk monitor through `MonitorHandleExtUnix::gdk_monitor`
  * `720bd93f` (#1018 by @amrbashir) On Windows, fix regression in initial window position when using logical positions.
  * `73741a75` (#1008 by @amrbashir) Remove `instant` dependency, changed `StartCause::ResumeTimeReached`, `StartCause::WaitCancelled` and `ControlFlow::WaitUntil` to use `std::time::Instant` instead.
  * `fa9aaa60` (#1019 by @amrbashir) On Windows, fix fullscreen for undecorated window have white borders.


© 2025 Tauri Contributors. CC-BY / MIT
