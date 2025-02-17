Skip to content
# @tauri-apps/cli@2.0.0-alpha.10
ReturnView on GitHub
### New Features
  * `7e5905ae`(#7023) Added `tauri plugin add` command to add a plugin to the Tauri project.
  * `b0f94775`(#7008) Added `migrate` command.


### Enhancements
  * `aa6c9164`(#7007) Don’t build library files when building desktop targets.
  * `a28fdf7e`(#7044) Skip Rust target installation if they are already installed.
  * `735db1ce`(#7044) Add `--skip-targets-install` flag for `tauri android init` and `tauri ios init` to skip installing needed rust targets vie rustup.


### Bug Fixes
  * `1ed2600d`(#6771) Set current directory to tauri directory before reading config file.
  * `4847b87b`(#7209) Fix `tauri (android|ios) (dev|build)` failing when using `npx tauri`
  * `655c714e`(#7240) Fixes panic when exiting the `ios dev` command with Ctrl + C.
  * `6252380f`(#7241) Exit `beforeDevCommand` process if the android or iOS `dev` command fails.


© 2025 Tauri Contributors. CC-BY / MIT
