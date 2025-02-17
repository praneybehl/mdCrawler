Skip to content
# @tauri-apps/cli@1.3.0
ReturnView on GitHub
  * Add `--ci` flag and respect the `CI` environment variable on the `signer generate` command. In this case the default password will be an empty string and the CLI will not prompt for a value. 
    * 8fb1df8a feat(cli): add `--ci` flag to `signer generate`, closes #6089 (#6097) on 2023-01-19
  * Fix Outdated Github Actions in the Plugin Templates `with-api` and `backend`
    * a926b49a Fix Github Actions of Tauri Plugin with-api template (#6603) on 2023-04-03
  * Do not crash on Cargo.toml watcher. 
    * e8014a7f fix(cli): do not crash on watcher (#6303) on 2023-02-17
  * Fix crash when nodejs binary has the version in its name, for example `node-18`
    * 1c8229fb fix(cli.js): detect `node-&lt;version&gt;` binary, closes #6427 (#6432) on 2023-03-16
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
  * Add initial support for building `nsis` bundles on non-Windows platforms. 
    * 60e6f6c3 feat(bundler): Add support for creating NSIS bundles on unix hosts (#5788) on 2023-01-19
  * Add `nsis` bundle target 
    * c94e1326 feat(bundler): add `nsis`, closes #4450, closes #2319 (#4674) on 2023-01-03
  * Remove default features from Cargo.toml template. 
    * b08ae637 fix(cli): remove default features from template (#6074) on 2023-01-17
  * Use Ubuntu 20.04 to compile the CLI, increasing the minimum libc version required.


© 2025 Tauri Contributors. CC-BY / MIT
