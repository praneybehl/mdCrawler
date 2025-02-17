Skip to content
# Localhost
GitHub crates.io 
API Reference 
Expose your app’s assets through a localhost server instead of the default custom protocol.
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
Install the localhost plugin to get started.
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

npmruntauriaddlocalhost

```

```

yarnruntauriaddlocalhost

```

```

pnpmtauriaddlocalhost

```

```

denotasktauriaddlocalhost

```

```

buntauriaddlocalhost

```

```

cargotauriaddlocalhost

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-localhost

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_localhost::Builder::new().build())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```



## Usage
The localhost plugin is available in Rust.
src-tauri/src/lib.rs```

use tauri::{webview::WebviewWindowBuilder, WebviewUrl};
pubfnrun() {
letport: u16 =9527;
tauri::Builder::default()
.plugin(tauri_plugin_localhost::Builder::new(port).build())
.setup(move|app| {
leturl=format!("http://localhost:{}", port).parse().unwrap();
WebviewWindowBuilder::new(app, "main".to_string(), WebviewUrl::External(url))
.title("Localhost Example")
.build()?;
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

© 2025 Tauri Contributors. CC-BY / MIT
