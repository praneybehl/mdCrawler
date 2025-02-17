Skip to content
# @tauri-apps/cli@1.0.0-rc.8
ReturnView on GitHub
  * Allows the `tauri.conf.json` file to be git ignored on the path lookup function. 
    * cc7c2d77 feat(cli): allow conf path to be gitignored, closes #3636 (#3683) on 2022-03-13
  * Remove `minimumSystemVersion: null` from the application template configuration. 
    * c81534eb feat(cli): use default macOS minimum system version when it is empty (#3658) on 2022-03-13
  * Improve readability of the `info` subcommand output. 
    * 49d2f13f feat(cli): colorful cli (#3635) on 2022-03-08
  * Fixes DMG bundling on macOS 12.3. 
    * 348a1ab5 fix(bundler): DMG bundling on macOS 12.3 cannot use bless, closes #3719 (#3721) on 2022-03-18
  * Fixes resources bundling on Windows when the path is on the root of the Tauri folder. 
    * 4c84559e fix(cli): root resource bundling on Windows, closes #3539 (#3685) on 2022-03-13


© 2025 Tauri Contributors. CC-BY / MIT
