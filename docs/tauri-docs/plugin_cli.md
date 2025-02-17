Skip to content
# Command Line Interface (CLI)
GitHub npm  crates.io 
API Reference 
Tauri enables your app to have a CLI through clap, a robust command line argument parser. With a simple CLI definition in your `tauri.conf.json` file, you can define your interface and read its argument matches map on JavaScript and/or Rust.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
  * Windows 
    * Due to an OS limitation, production apps are not able to write text back to the calling console by default. Please check out tauri#8305 for a workaround.


## Setup
Install the CLI plugin to get started.
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

npmruntauriaddcli

```

```

yarnruntauriaddcli

```

```

pnpmtauriaddcli

```

```

denotasktauriaddcli

```

```

buntauriaddcli

```

```

cargotauriaddcli

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-cli--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

    1. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_cli::init());
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

    1. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-cli

```

```

yarnadd@tauri-apps/plugin-cli

```

```

pnpmadd@tauri-apps/plugin-cli

```

```

denoaddnpm:@tauri-apps/plugin-cli

```

```

bunadd@tauri-apps/plugin-cli

```



## Base Configuration
Under `tauri.conf.json`, you have the following structure to configure the interface:
src-tauri/tauri.conf.json```

{
"plugins": {
"cli": {
"description": "Tauri CLI Plugin Example",
"args": [
{
"short": "v",
"name": "verbose",
"description": "Verbosity level"
}
],
"subcommands": {
"run": {
"description": "Run the application",
"args": [
{
"name": "debug",
"description": "Run application in debug mode"
},
{
"name": "release",
"description": "Run application in release mode"
}
]
}
}
}
}
}

```

## Adding Arguments
The `args` array represents the list of arguments accepted by its command or subcommand.
### Positional Arguments
A positional argument is identified by its position in the list of arguments. With the following configuration:
src-tauri/tauri.conf.json```

{
"args": [
{
"name": "source",
"index": 1,
"takesValue": true
},
{
"name": "destination",
"index": 2,
"takesValue": true
}
]
}

```

Users can run your app as `./app tauri.txt dest.txt` and the arg matches map will define `source` as `"tauri.txt"` and `destination` as `"dest.txt"`.
### Named Arguments
A named argument is a (key, value) pair where the key identifies the value. With the following configuration:
tauri-src/tauri.conf.json```

{
"args": [
{
"name": "type",
"short": "t",
"takesValue": true,
"multiple": true,
"possibleValues": ["foo", "bar"]
}
]
}

```

Users can run your app as `./app --type foo bar`, `./app -t foo -t bar` or `./app --type=foo,bar` and the arg matches map will define `type` as `["foo", "bar"]`.
### Flag Arguments
A flag argument is a standalone key whose presence or absence provides information to your application. With the following configuration:
tauri-src/tauri.conf.json```

{
"args": [
{
"name": "verbose",
"short": "v"
}
]
}

```

Users can run your app as `./app -v -v -v`, `./app --verbose --verbose --verbose` or `./app -vvv` and the arg matches map will define `verbose` as `true`, with `occurrences = 3`.
## Subcommands
Some CLI applications have additional interfaces as subcommands. For instance, the `git` CLI has `git branch`, `git commit` and `git push`. You can define additional nested interfaces with the `subcommands` array:
tauri-src/tauri.conf.json```

{
"cli": {
...
"subcommands": {
"branch": {
"args": []
},
"push": {
"args": []
}
}
}
}

```

Its configuration is the same as the root application configuration, with the `description`, `longDescription`, `args`, etc.
## Usage
The CLI plugin is available in both JavaScript and Rust.
  * JavaScript 
  * Rust 


```

import { getMatches } from'@tauri-apps/plugin-cli';
// when using `"withGlobalTauri": true`, you may use
// const { getMatches } = window.__TAURI__.cli;
const matches = await getMatches();
if (matches.subcommand?.name==='run') {
// `./your-app run $ARGS` was executed
const args = matches.subcommand.matches.args;
if (args.debug?.value===true) {
// `./your-app run --debug` was executed
}
if (args.release?.value===true) {
// `./your-app run --release` was executed
}
}

```

src-tauri/src/lib.rs```

use tauri_plugin_cli::CliExt;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_cli::init())
.setup(|app| {
matchapp.cli().matches() {
// `matches` here is a Struct with { args, subcommand }.
// `args` is `HashMap<String, ArgData>` where `ArgData` is a struct with { value, occurrences }.
// `subcommand` is `Option<Box<SubcommandMatches>>` where `SubcommandMatches` is a struct with { name, matches }.
Ok(matches) => {
println!("{:?}", matches)
}
Err(_) => {}
}
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": ["cli:default"]
}

```

## Default Permission
Allows reading the CLI matches
  * `allow-cli-matches`


## Permission Table
Identifier | Description  
---|---  
`cli:allow-cli-matches` |  Enables the cli_matches command without any pre-configured scope.  
`cli:deny-cli-matches` |  Denies the cli_matches command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
