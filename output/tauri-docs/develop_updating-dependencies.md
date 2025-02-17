Skip to content
# Updating Dependencies
## Update npm Packages
If you are using the `tauri` package:
  * npm 
  * yarn 
  * pnpm 


```

npminstall@tauri-apps/cli@latest@tauri-apps/api@latest

```

```

yarnup@tauri-apps/cli@tauri-apps/api

```

```

pnpmupdate@tauri-apps/cli@tauri-apps/api--latest

```

You can also detect what the latest version of Tauri is on the command line, using:
  * npm 
  * yarn 
  * pnpm 


```

npmoutdated@tauri-apps/cli

```

```

yarnoutdated@tauri-apps/cli

```

```

pnpmoutdated@tauri-apps/cli

```

## Update Cargo Packages
You can check for outdated packages with `cargo outdated` or on the crates.io pages: tauri / tauri-build.
Go to `src-tauri/Cargo.toml` and change `tauri` and `tauri-build` to
```

[build-dependencies]
tauri-build = "%version%"
[dependencies]
tauri = { version = "%version%" }

```

where `%version%` is the corresponding version number from above.
Then do the following:
Terminal window```

cdsrc-tauri
cargoupdate

```

Alternatively, you can run the `cargo upgrade` command provided by cargo-edit which does all of this automatically.
© 2025 Tauri Contributors. CC-BY / MIT
