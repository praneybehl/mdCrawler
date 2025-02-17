Skip to content
# Persisted Scope
GitHub crates.io 
API Reference 
Save filesystem and asset scopes and restore them when the app is reopened.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the persisted-scope plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriaddpersisted-scope

```

```

yarnruntauriaddpersisted-scope

```

```

pnpmtauriaddpersisted-scope

```

```

denotasktauriaddpersisted-scope

```

```

buntauriaddpersisted-scope

```

```

cargotauriaddpersisted-scope

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-persisted-scope

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_persisted_scope::init())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```



## Usage
After setup the plugin will automatically save and restore filesystem and asset scopes.
© 2025 Tauri Contributors. CC-BY / MIT
