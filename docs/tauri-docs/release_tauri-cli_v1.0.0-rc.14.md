Skip to content
# tauri-cli@1.0.0-rc.14
ReturnView on GitHub
  * Set the `TRAY_LIBRARY_PATH` environment variable to make the bundle copy the appindicator library to the AppImage. 
    * 34552444 feat(cli): bundle appindicator library in the AppImage, closes #3859 (#4267) on 2022-06-07
  * Set the `APPIMAGE_BUNDLE_GSTREAMER` environment variable to make the bundler copy additional gstreamer files to the AppImage. 
    * d335fae9 feat(bundler): bundle additional gstreamer files, closes #4092 (#4271) on 2022-06-10
  * Configure the AppImage bundler to copy the `/usr/bin/xdg-open` binary if it exists and the shell `open` API is enabled. 
    * 2322ac11 fix(bundler): bundle `/usr/bin/xdg-open` in appimage if open API enabled (#4265) on 2022-06-04
  * Fixes multiple occurrences handling of the `bundles` and `features` arguments. 
    * f685df39 fix(cli): parsing of arguments with multiple values, closes #4231 (#4233) on 2022-05-29
  * Log command output in real time instead of waiting for it to finish. 
    * 76d1eaae feat(cli): debug command output in real time (#4318) on 2022-06-12
  * Configure the `STATIC_VCRUNTIME` environment variable so `tauri-build` statically links it on the build command. 
    * d703d27a fix(build): statically link VC runtime only on `tauri build` (#4292) on 2022-06-07
  * Use the `TAURI_TRAY` environment variable to determine which package should be added to the Debian `depends` section. Possible values are `ayatana` and `gtk`. 
    * 6216eb49 refactor(core): drop `ayatana-tray` and `gtk-tray` Cargo features (#4247) on 2022-06-02


© 2025 Tauri Contributors. CC-BY / MIT
