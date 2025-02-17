Skip to content
# tauri-cli@1.1.0
ReturnView on GitHub
  * Allow adding `build &gt; beforeBundleCommand` in tauri.conf.json to run a shell command before the bundling phase. 
    * 57ab9847 feat(cli): add `beforeBundleCommand`, closes #4879 (#4893) on 2022-08-09
  * Change `before_dev_command` and `before_build_command` config value to allow configuring the current working directory. 
    * d6f7d3cf Add cwd option to `before` commands, add wait option to dev #4740 #3551 (#4834) on 2022-08-02
  * Allow configuring the `before_dev_command` to force the CLI to wait for the command to finish before proceeding. 
    * d6f7d3cf Add cwd option to `before` commands, add wait option to dev #4740 #3551 (#4834) on 2022-08-02
  * Check if the default build target is set in the Cargo configuration. 
    * 436f3d8d feat(cli): load Cargo configuration to check default build target (#4990) on 2022-08-21
  * Add support to cargo-binstall. 
    * 90d5929f feat(cli.rs): add support to cargo-binstall, closes #4651 (#4817) on 2022-08-02
  * Use `cargo metadata` to detect the workspace root and target directory. 
    * fea70eff refactor(cli): Use `cargo metadata` to detect the workspace root and target directory, closes #4632, #4928. (#4932) on 2022-08-21
  * Prompt for `beforeDevCommand` and `beforeBuildCommand` in `tauri init`. 
    * 6d4945c9 feat(cli): prompt for before*Command, closes #4691 (#4721) on 2022-07-25
  * Add `icon` command to generate icons. 
    * 12e9d811 feat(cli): Add `icon` command (tauricon) (#4992) on 2022-09-03
  * Added support to configuration files in TOML format (Tauri.toml file). 
    * ae83d008 feat: add support to TOML config file `Tauri.toml`, closes #4806 (#4813) on 2022-08-02
  * Automatically use any `.taurignore` file as ignore rules for dev watcher and app path finder. 
    * 596fa08d feat(cli): automatically use `.taurignore`, ref #4617 (#4623) on 2022-07-28
  * Enable WiX FIPS compliance when the `TAURI_FIPS_COMPLIANT` environment variable is set to `true`. 
    * d88b9de7 feat(core): add `fips_compliant` wix config option, closes #4541 (#4843) on 2022-08-04
  * Fixes dev watcher incorrectly exiting the CLI when sequential file updates are detected. 
    * 47fab680 fix(cli): dev watcher incorrectly killing process on multiple file write (#4684) on 2022-07-25
  * Set the `MACOSX_DEPLOYMENT_TARGET` environment variable with the configuration `minimum_system_version` value. 
    * fa23310f fix(cli): set MACOSX_DEPLOYMENT_TARGET env var, closes #4704 (#4842) on 2022-08-02
  * Added `--no-watch` argument to the `dev` command to disable the file watcher. 
    * 0983d7ce feat(cli): add `--no-watch` argument to the dev command, closes #4617 (#4793) on 2022-07-29
  * Validate updater signature matches configured public key. 
    * b2a8930b feat(cli): validate updater private key when signing (#4754) on 2022-07-25


© 2025 Tauri Contributors. CC-BY / MIT
