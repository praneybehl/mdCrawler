Skip to content
# Announcing Tauri 1.4.0
Jun 14, 2023 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tauri 1.4 Launch Hero Image](https://v2.tauri.app/_astro/header.pm2INrN3_Z1cGUnz.webp)
The Tauri team is excited to announce the 1.4 release. This version includes several new features and important bug fixes such as CLI completions, unit testing capabilities and Windows installer improvements.
## Upgrading
Make sure to update both NPM and Cargo dependencies to the 1.4.0 release. You can update the dependencies with:
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

## What’s in 1.4.0
### CLI completions
The Tauri CLI now can generate shell completions for Bash, Zsh, PowerShell and Fish. See the documentation for more information.
### Disabling window controls
The window’s maximize, minimize and close buttons now can be disabled via configuration or API calls. Check out `set_maximizable`, `set_minimizable` and `set_closable` for the Rust APIs and `setMaximizable`, `setMinimizable` and `setClosable` for the JavaScript APIs.
### NSIS improvements
The 1.4.0 release includes several NSIS bundle enhancements:
  * Custom language files
  * Custom installer template (.nsi file)
  * Support for the dutch, japanese, korean, persian, swedish and turkish languages
  * If your application is installed via WiX, the installer will prompt the user to uninstall it
  * Improved support to updater install modes


See the installer customization guide and installer internationalization for more information.
### MSRV change
Tauri 1.4 still has a minimum supported Rust version of 1.60, but due to some dependency incompatibility issues we are no longer pinning the patch version of the `time`, `ignore`, and `winnow` crates. If you are still using Rust 1.60, you will need to pin these versions manually with cargo update.
### Unit tests
The `tauri` crate now exposes the `test` module under the `test` Cargo feature. This module is still unstable but allows you to unit test your application by creating a `tauri::App` instance that can execute without spawning windows. See the documentation for more information and examples.
### Other changes
Starting on v1.4.0, our changelog format has been improved. Check out the entire list of changes:
  * tauri
  * tauri-cli
  * tauri-bundler


## Audit
The _internal_1 audit was performed by Tillmann @tillmann-crabnebula and Chip @chip-crabnebula, who are also involved in security topics at the project under their private handles (@tweidinger and @chippers).
It was performed during paid time at CrabNebula Ltd. and we are grateful to be able to spend parts of our work time contributing to the open source project and making it a more secure environment :heart:.
For this release we manually audited a selection of PRs instead of all PRs coming into the release. The new approach means the reviewers and developers need to decide on their own if a PR is introducing any security relevant change. A review can be triggered by anyone involved in the change, by adding a label to the PR.
For the first time we also audited after the official release due to time constraints. This resulted in a security patch release, fixing the only impactful issue (CVE-2023-34460) discovered during auditing. In general this release was more focused on fixing and improving the NSIS features and introduced less new features and security relevant changes.
## Footnotes
  1. It is internal in the sense that we are also involved in the project itself but performed with the help of an external entity. Calling it external security audit would create false impressions. ↩


Tauri Board Elections & Governance Update
Announcing Tauri 1.3.0
© 2025 Tauri Contributors. CC-BY / MIT
