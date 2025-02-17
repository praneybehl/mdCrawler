Skip to content
# tao@0.28.1
ReturnView on GitHub
  * `7e8f75e9` (#926 by @pewsheen) On macOS, add `set_fullsize_content_view` and `set_titlebar_transparent` to `Window` to set the title bar style.
  * `3bbddc64` (#931 by @muwoo) **Breaking Change** : On Windows, `UserAttentionType::Informational` will flash the taskbar icon 4 times only and not until the app recieves focus.
  * `29bee151` (#935 by @renovate) Update `windows` crate to `0.57`
  * `ab792dbd` (#928 by @amrbashir) On Windows, always allow dark theme for app and window through `AllowDarkModeForApp` and `AllowDarkModeForWindow`, which fixes an issue when calling `IsDarkModeAllowedForWindow()`


© 2025 Tauri Contributors. CC-BY / MIT
