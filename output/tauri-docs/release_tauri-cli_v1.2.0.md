Skip to content
# tauri-cli@1.2.0
ReturnView on GitHub
  * Keep `tauri dev` watcher alive when the configuration is invalid. 
    * cc186c7a fix(cli): keep dev watcher alive if config is incorrect, closes #5173 (#5495) on 2022-10-28
  * Ignore workspace members in dev watcher if they are ignored by `.taurignore`
    * 9417ce40 fix(cli): apply `.taurignore` rules to workspace members, closes #5355 (#5460) on 2022-10-28
  * Detect JSON5 and TOML configuration files in the dev watcher. 
    * e7ccbd85 feat(cli): detect JSON5 and TOML configuration files in the dev watcher (#5439) on 2022-10-19
  * Fix cli passing `--no-default-features` to the app instead of the runner (Cargo). 
    * a3a70218 fix(cli): pass `--no-default-features` to runner instead of app, closes #5415 (#5474) on 2022-10-25
  * Validate `package &gt; productName` in the tauri config and produce errors if it contains one of the following characters `/\:*?\&quot;&lt;&gt;|`
    * b9316a64 fix(cli): validate `productName` in config, closes #5233 (#5262) on 2022-09-28
  * Hot-reload the frontend when `tauri.conf.json &gt; build &gt; devPath` points to a directory. 
    * 54c337e0 feat(cli): hotreload support for frontend static files, closes #2173 (#5256) on 2022-09-28
  * Expose `TAURI_TARGET_TRIPLE` to `beforeDevCommand`, `beforeBuildCommand` and `beforeBundleCommand`
    * a4aec9f0 feat(cli): expose `TAURI_TARGET_TRIPLE` to before*Commands, closes #5091 (#5101) on 2022-10-03
  * Log dev watcher file change detection. 
    * 9076d5d2 feat(cli): add prompt information when file changing detected, closes #5417 (#5428) on 2022-10-19
  * Set `TAURI_PLATFORM_TYPE`, `TAURI_FAMILY`, `TAURI_ARCH` and `TAURI_PLATFORM` env vars for hook commands to based on the app not the cli. 
    * a4aec9f0 feat(cli): expose `TAURI_TARGET_TRIPLE` to before*Commands, closes #5091 (#5101) on 2022-10-03
  *     * 7d9aa398 feat: bump MSRV to 1.59 (#5296) on 2022-09-28
  * Add `tauri.conf.json &gt; bundle &gt; publisher` field to specify the app publisher. 
    * 628285c1 feat(bundler): add `publisher` field, closes #5273 (#5283) on 2022-09-28
  * Changed the project template to not enable all APIs by default. 
    * 582c25a0 refactor(cli): disable api-all on templates (#5538) on 2022-11-03


© 2025 Tauri Contributors. CC-BY / MIT
