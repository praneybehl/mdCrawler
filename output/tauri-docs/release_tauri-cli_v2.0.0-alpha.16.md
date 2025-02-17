Skip to content
# tauri-cli@2.0.0-alpha.16
ReturnView on GitHub
### New Features
  * `8b166e9b`(#7949) Add `--no-dev-server-wait` option to skip waiting for the dev server to start when using `tauri dev`.
  * `880266a7`(#8031) Bump the MSRV to 1.70.


### Dependencies
  * Upgraded to `tauri-utils@2.0.0-alpha.9`
  * Upgraded to `tauri-bundler@2.0.0-alpha.10`


### Breaking Changes
  * `8b166e9b`(#7949) Changed a number of environment variables used by tauri CLI for consistency and clarity:
    * `TAURI_PRIVATE_KEY` -> `TAURI_SIGNING_PRIVATE_KEY`
    * `TAURI_KEY_PASSWORD` -> `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`
    * `TAURI_SKIP_DEVSERVER_CHECK` -> `TAURI_CLI_NO_DEV_SERVER_WAIT`
    * `TAURI_DEV_SERVER_PORT` -> `TAURI_CLI_PORT`
    * `TAURI_PATH_DEPTH` -> `TAURI_CLI_CONFIG_DEPTH`
    * `TAURI_FIPS_COMPLIANT` -> `TAURI_BUNDLER_WIX_FIPS_COMPLIANT`
    * `TAURI_DEV_WATCHER_IGNORE_FILE` -> `TAURI_CLI_WATCHER_IGNORE_FILENAME`
    * `TAURI_TRAY` -> `TAURI_LINUX_AYATANA_APPINDICATOR`
    * `TAURI_APPLE_DEVELOPMENT_TEAM` -> `APPLE_DEVELOPMENT_TEAM`
  * `4caa1cca`(#7990) The `tauri plugin` subcommand is receving a couple of consitency and quality of life improvements:
    * Renamed `tauri plugin android/ios add` command to `tauri plugin android/ios init` to match the `tauri plugin init` command.
    * Removed the `-n/--name` argument from the `tauri plugin init`, `tauri plugin android/ios init`, and is now parsed from the first positional argument.
    * Added `tauri plugin new` to create a plugin in a new directory.
    * Changed `tauri plugin init` to initalize a plugin in an existing directory (defaults to current directory) instead of creating a new one.
    * Changed `tauri plugin init` to NOT generate mobile projects by default, you can opt-in to generate them using `--android` and `--ios` flags or `--mobile` flag or initalize them later using `tauri plugin android/ios init`.
  * `8b166e9b`(#7949) Removed checking for a new version of the CLI.
  * `ebcc21e4`(#8057) Renamed the beforeDevCommand, beforeBuildCommand and beforeBundleCommand hooks environment variables from `TAURI_PLATFORM, TAURI_ARCH, TAURI_FAMILY, TAURI_PLATFORM_VERSION, TAURI_PLATFORM_TYPE and TAURI_DEBUG` to `TAURI_ENV_PLATFORM, TAURI_ENV_ARCH, TAURI_ENV_FAMILY, TAURI_ENV_PLATFORM_VERSION, TAURI_ENV_PLATFORM_TYPE and TAURI_ENV_DEBUG` to differentiate the prefix with other CLI environment variables.


© 2025 Tauri Contributors. CC-BY / MIT
