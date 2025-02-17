Skip to content
# tao@0.30.6
ReturnView on GitHub
  * `1f72c246` (#1002 by @ahqsoftwares) Add `WindowExtUnix::set_badge_count` for Linux, `WindowExtIos::set_badge_count` for iOS, `WindowExtMacos::set_badge_label` for Macos, `MacdowExtWindows::set_overlay_icon` for Windows
  * `946f8049` (#1005 by @lucasfernog) Fix memory leak on Android.
  * `aff33fbb` (#1001 by @amrbashir) On Linux, `Window::outer_position`, `Window::outer_size` and `WindowEvent::Moved` to include/account for borders and titlebar.
  * `06d109fe` (#993 by @amrbashir) On Windows, fix `Window::inner_size` returns slightly larger than what’s visible for undecorated windows but have shadows.
  * `edfbd364` (#992 by @amrbashir) On Windows, fix `WindowBuilder::with_position` with a position on a non-primary monitor resulting in an incorrectly positioned window.


© 2025 Tauri Contributors. CC-BY / MIT
