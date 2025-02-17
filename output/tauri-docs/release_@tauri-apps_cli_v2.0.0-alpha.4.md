Skip to content
# @tauri-apps/cli@2.0.0-alpha.4
ReturnView on GitHub
  * Fix android project build crashing when using `pnpm` caused by extra `--`. 
    * c787f749 fix(cli): only add `--` to generated android template for npm (#6508) on 2023-03-21
  * Fixes the Android build gradle plugin implementation on Windows. 
    * 00241fa9 fix(cli): append .cmd on the gradle plugin binary on Windows, fix #6502 (#6503) on 2023-03-21
  * Update `napi-rs` dependencies to latest to fix CLI hanging up forever. 
    * d5ac76b5 chore(deps): update napi-rs, closes #6502 (#6513) on 2023-03-21


© 2025 Tauri Contributors. CC-BY / MIT
