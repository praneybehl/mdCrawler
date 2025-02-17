Skip to content
# Announcing Tauri 1.7.0
Jul 1, 2024 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
The Tauri team is happy to announce the 1.7 release. This version includes several bug fixes, performance improvements and features backported from the upcoming v2 release.
## Upgrading
Make sure to update both NPM and Cargo dependencies to the 1.7.0 release. You can update the dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@latest@tauri-apps/api@latest

```

```

yarnupgrade@tauri-apps/cli@tauri-apps/api--latest

```

```

pnpmupdate@tauri-apps/cli@tauri-apps/api--latest

```

```

cargoupdate

```

## What’s in 1.7.0
### Shell API performance improvement
The shell’s `Command::execute` API has been optimized to only use the IPC a single time instead of streaming data, improving usage of verbose shell scripts.
### Feature backport from v2
Thanks to community effort we have backported a few bundler features from v2 into the v1 release.
#### Custom Windows codesign script
By default the Windows packaging uses SignTool, which only works on Windows so it’s not useful when cross compiling. In this release we have backported the custom sign command feature, which allows using `osslsigncode`, `relic` and other alternatives that can run on Unix systems and support hardware tokens, Azure Key Vault and more.
#### RPM bundle
RPM packaging have been available to Tauri v2 users for a while, and it is now also available on the v1 channel.
### DMG configuration
DMG installers are now configurable: you can change the position of the icons and the window size to fit better within a custom background.
### Other changes
Check out the entire list of changes:
  * tauri
  * tauri-cli
  * tauri-bundler


Tauri 2.0 Release Candidate
Tauri Board Elections 2024
© 2025 Tauri Contributors. CC-BY / MIT
