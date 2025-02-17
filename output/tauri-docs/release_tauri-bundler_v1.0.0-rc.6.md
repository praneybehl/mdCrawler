Skip to content
# tauri-bundler@1.0.0-rc.6
ReturnView on GitHub
  * Remove `Settings::verbose` option. You may now bring your own `log` frontend to receive logging output from the bundler while remaining in control of verbosity and formatting. 
    * 35f21471 feat(cli): Improve CLI logging (#4060) on 2022-05-07
  * Ignore errors when loading `icns` files in the `.deb` package generation. 
    * de444b15 fix(bundler): debian failing to load icns icon, closes #3062 (#4009) on 2022-04-30
  * Fix app downgrades when using the Windows installer. 
    * 72e577dc fix(bundler): properly reinstall files on MSI downgrades, closes #3868 (#4044) on 2022-05-04


© 2025 Tauri Contributors. CC-BY / MIT
