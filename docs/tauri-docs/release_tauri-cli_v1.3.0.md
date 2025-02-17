Skip to content
# tauri-cli@1.3.0
ReturnView on GitHub
  * Look for available port when using the built-in dev server for static files. 
    * a7ee5ca7 fix(cli): look for available ports for built-in dev server, closes #6511 (#6514) on 2023-03-31
  * Add `--port` to specify the port used for static files dev server. It can also be specified through `TAURI_DEV_SERVER_PORT` env var. 
    * b7a2ce2c feat(cli): add —port, closes #6186 (#6283) on 2023-03-16
  * Fix `tauri info` panicking when parsing crates version on a newly created project without a `Cargo.lock` file. 
    * c2608423 fix(cli): don’t panic when a crate version couldn’t be parsed (#5873) on 2022-12-26
  * Improve the error message when `rustc` couldn’t be found. 
    * 7aab3e20 fix(cli.rs): improve `rustc` not found error msg (#6021) on 2023-01-17
  * Add `--ci` flag and respect the `CI` environment variable on the `signer generate` command. In this case the default password will be an empty string and the CLI will not prompt for a value. 
    * 8fb1df8a feat(cli): add `--ci` flag to `signer generate`, closes #6089 (#6097) on 2023-01-19
  * Fix Outdated Github Actions in the Plugin Templates `with-api` and `backend`
    * a926b49a Fix Github Actions of Tauri Plugin with-api template (#6603) on 2023-04-03
  * Do not crash on Cargo.toml watcher. 
    * e8014a7f fix(cli): do not crash on watcher (#6303) on 2023-02-17
  * On Windows, printing consistent paths on Windows with backslashs only. 
    * 9da99607 fix(cli): fix printing paths on Windows (#6137) on 2023-01-26
  * Add `--png` option for the `icon` command to generate custom icon sizes. 
    * 9d214412 feat(cli): add option to make custom icon sizes, closes #5121 (#5246) on 2022-12-27
  * Skip the password prompt on the build command when `TAURI_KEY_PASSWORD` environment variable is empty and the `--ci` argument is provided or the `CI` environment variable is set. 
    * d4f89af1 feat: skip password prompt on the build command if CI is set fixes #6089 on 2023-01-18
  * Fix `default-run` not deserialized. 
    * 57c6bf07 fix(cli): fix default-run not deserialized (#6584) on 2023-03-30
  * Fixes HTML serialization removing template tags on the dev server. 
    * 314f0e21 fix(cli): web_dev_server html template serialization (fix #6165) (#6166) on 2023-01-29
  * Use escaping on Handlebars templates. 
    * 6d6b6e65 feat: configure escaping on handlebars templates (#6678) on 2023-05-02
  * Fix building apps with unicode characters in their `productName`. 
    * 72621892 fix(cli): use `unicode` feature for `heck` crate, closes #5860 (#5872) on 2022-12-26
  * Bump minimum supported Rust version to 1.60. 
    * 5fdc616d feat: Use the zbus-backed of notify-rust (#6332) on 2023-03-31
  * Add initial support for building `nsis` bundles on non-Windows platforms. 
    * 60e6f6c3 feat(bundler): Add support for creating NSIS bundles on unix hosts (#5788) on 2023-01-19
  * Add `nsis` bundle target 
    * c94e1326 feat(bundler): add `nsis`, closes #4450, closes #2319 (#4674) on 2023-01-03
  * Remove default features from Cargo.toml template. 
    * b08ae637 fix(cli): remove default features from template (#6074) on 2023-01-17
  * Added support for Cargo’s workspace inheritance for package information. The cli now also detects inherited `tauri` and `tauri-build` dependencies and disables manifest rewrites accordingly. 
    * cd8c074a feat(cli): add support for Cargo’s workspace inheritance for the package version, closes #5070 (#5775) on 2022-12-14
    * d20a7288 feat: Further improve workspace inheritance, closes #6122, #5070 (#6144) on 2023-01-26
  * Use Ubuntu 20.04 to compile the CLI for cargo-binstall, increasing the minimum libc required.


© 2025 Tauri Contributors. CC-BY / MIT
