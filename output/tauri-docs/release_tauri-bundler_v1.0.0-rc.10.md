Skip to content
# tauri-bundler@1.0.0-rc.10
ReturnView on GitHub
  * Bundle the tray library file (`.so` extension) in the AppImage if the `TRAY_LIBRARY_PATH` environment variable is set. 
    * 34552444 feat(cli): bundle appindicator library in the AppImage, closes #3859 (#4267) on 2022-06-07
  * Bundle additional gstreamer files needed for audio and video playback if the `APPIMAGE_BUNDLE_GSTREAMER` environment variable is set. 
    * d335fae9 feat(bundler): bundle additional gstreamer files, closes #4092 (#4271) on 2022-06-10
  * Cache bundling tools in a directory shared by all tauri projects. Usually in `$XDG_HOME/.cache/tauri` on Linux and `$HOME\AppData\Local\tauri` on Windows. 
    * f48b1b0b feat(bundler): cache bundling tools in a common dir for all projects (#4305) on 2022-06-09
  * Pull correct linuxdeploy AppImage when building for 32-bit targets. 
    * 53ae13d9 fix(bundler): Pull correct 32bit linuxdeploy appimage, closes #4260 (#4269) on 2022-06-04
  * Copy the `/usr/bin/xdg-open` binary if it exists and the `APPIMAGE_BUNDLE_XDG_OPEN` environment variable is set. 
    * 2322ac11 fix(bundler): bundle `/usr/bin/xdg-open` in appimage if open API enabled (#4265) on 2022-06-04
  * On Linux, high-dpi icons are now placed in the correct directory and should be recognized by the desktop environment. 
    * c2b7c775 fix: put linux high dpi icons in the correct dir (#4281) on 2022-06-10
  * Only png files from tauri.conf.json > tauri.bundle.icon are used for app icons for linux targets. Previously, all sizes from all source files (10 files using tauricon defaults) were used. This also prevents unexpectedly mixed icons in cases where platform-specific icons are used. 
    * a6f45d52 Debian icon no fallback, fixes #4280 (#4282) on 2022-06-09
  * Log command output in real time instead of waiting for it to finish. 
    * 76d1eaae feat(cli): debug command output in real time (#4318) on 2022-06-12


© 2025 Tauri Contributors. CC-BY / MIT
