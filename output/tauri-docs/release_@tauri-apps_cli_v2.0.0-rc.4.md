Skip to content
# @tauri-apps/cli@2.0.0-rc.4
ReturnView on GitHub
### New Features
  * `78e22bedc` (#10602 by @amrbashir) Add necessary options to `AndroidManifest.xml` in android template to support AndroidTV.
  * `3bec7b159` (#10544 by @lucasfernog) v1 migrate script now migrates Svelte and Vue.js code.


### Enhancements
  * `bba1a4419` (#10457 by @mmvanheusden) Added `--no-fmt` option to the `add` command to skip formatting the code after applying changes.
  * `71d00646a` (#10504 by @fu050409) Improve the `init` command behavior by detecting the project NPM package manager.
  * `8deb1966a` (#10652 by @lucasfernog) Infer macOS codesign identity from the `APPLE_CERTIFICATE` environment variable when provided, meaning the identity no longer needs to be provided when signing on CI using that option. If the imported certificate name does not match a provided signingIdentity configuration, an error is returned.
  * `f35bcda28` (#10598 by @lucasfernog) `permission add` and `add` commands now check if the plugin is known and if it is either desktop or mobile only we add the permission to a target-specific capability.


### Bug Fixes
  * `f712f31d1` (#10639 by @lucasfernog) Include notarization error output in the error message if it fails.
  * `9f75d0622` (#10604 by @lucasfernog) Fixes `android dev` port forward failing under some conditions, add better logging and error handling.
  * `2d47352a0` (#10418 by @samkearney) CLI commands will now consistently search for the `app_dir` (the directory containing `package.json`) from the current working directory of the command invocation.
  * `f4cd68f04` (#10600 by @lucasfernog) Fixes `android dev` not working when using the builtin dev server.
  * `41c7a6646` (#10572 by @lucasfernog) Exit with code 1 if a panic occurs when running the CLI with `bun`.
  * `9089d9763` (#10605 by @lucasfernog) Fixes `[android|ios] build --config &lt;config&gt;` failing to resolve.
  * `712f1049f` (#10569 by @lucasfernog) Fixes running `ios dev` and `ios build` using `bun`.
  * `3998570fd` (#10540 by @lucasfernog) Fixes v1 migration of Cargo.toml dependencies and features.
  * `3beba92b5` (#10542 by @lucasfernog) Fixes v1 frontend code migration when using plugin default imports.
  * `10fb027b7` (#10656 by @lucasfernog) Migrate v1 plugins to their v2 releases.
  * `10fb027b7` (#10656 by @lucasfernog) Prevent duplicate permissions on v1 migration.
  * `b160f9359` (#10638 by @lucasfernog) Only validate the output iOS library on debug builds.
  * `4bfe4880f` (#10550 by @anatawa12) fails to build universal fat binary if main bin is renamed to another name in `Cargo.toml`
  * `f3837d5b9` (#10539 by @lucasfernog) Improve migration tooling by supporting TOML configs, handle nulls and properly check for updater migration.


### What’s Changed
  * `794cf8234` (#10571 by @lucasfernog) Change iOS template default export method from deprecated `development` to `debugging`.
  * `bfc49cc7a` (#10558 by @ahqsoftwares) Remove targetSdk from gradle files


### Dependencies
  * Upgraded to `tauri-cli@2.0.0-rc.4`


© 2025 Tauri Contributors. CC-BY / MIT
