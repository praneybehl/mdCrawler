Skip to content
# tauri-cli@1.0.0-beta.2
ReturnView on GitHub
  * Support `cargo tauri build` on Apple M1 chip. 
    * 3bf853d7 feat(cli.rs): support tauri build on M1 chip (#1915) on 2021-05-29
  * Infer `app name` and `window title` from `package.json &gt; productName` or `package.json &gt; name`. Infer `distDir` and `devPath` by reading the package.json and trying to determine the UI framework (Vue.js, Angular, React, Svelte and some UI frameworks). 
    * 21a971c3 feat(cli.rs): infer devPath/distDir/appName from package.json (#1930) on 2021-05-31
  * Watch workspace crates on `dev` command. 
    * 86a23ff3 added support for cargo workspaces for `dev` command (#1827) on 2021-05-13
  * Adds `features` argument to the `dev` and `build` commands. 
    * 6ec8e84d feat(cli.rs): add `features` arg to dev/build (#1828) on 2021-05-13
  * Fixes the libwebkit2gtk package name. 
    * e08065d7 fix: deb installation error (#1844) on 2021-05-18
  * Properly keep all `tauri` features that are not managed by the CLI. 
    * 17c7c439 refactor(core): use `attohttpc` by default (#1861) on 2021-05-19
  * Copy resources and binaries to `OUT_DIR` on `tauri dev` command. 
    * 8f29a260 fix(cli.rs): copy resources and binaries on dev, closes #1298 (#1946) on 2021-06-04
  * Read cargo features from `tauri.conf.json &gt; build &gt; features` and propagate them on `dev` and `build`. 
    * 2b814e9c added cargo features to tauri config (#1824) on 2021-05-13
  * Fixes `tauri.conf.json &gt; tauri &gt; bundle &gt; targets` not applying to the bundler. 
    * 8be35ced fix(cli.rs): `tauri.conf.json &gt; tauri &gt; bundle &gt; targets` being ignored (#1945) on 2021-06-04
  * Fixes `info` command not striping `\r` from child process version output. 
    * 6a95d7ac fix(cli.rs): `info` version checks not striping `\r` on Windows (#1952) on 2021-06-05
  * Allow setting a path to a license file for the Windows Installer (`tauri.conf.json &gt; bundle &gt; windows &gt; wix &gt; license`). 
    * b769c7f7 feat(bundler): windows installer license, closes #2009 (#2027) on 2021-06-21
  * Change the `csp` value on the template to include `wss:` and `tauri:` to the `default-src` attribute. 
    * 463fd00d fix(csp): add wss and tauri to conf template (#1974) on 2021-06-15
  * Adds `tauri &gt; bundle &gt; windows &gt; wix &gt; language` config option. See https://docs.microsoft.com/en-us/windows/win32/msi/localizing-the-error-and-actiontext-tables. 
    * 47919619 feat(bundler): allow setting wix language, closes #1976 (#1988) on 2021-06-15


© 2025 Tauri Contributors. CC-BY / MIT
