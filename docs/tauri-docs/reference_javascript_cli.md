Skip to content
# @tauri-apps/plugin-cli
Parse arguments from your Command Line Interface.
## Interfaces
### ArgMatch
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`occurrences`| `number`| Number of occurrences| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L26  
`value`| `null` | `string` | `boolean` | `string`[]| string if takes value boolean if flag string[] or null if takes multiple values| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L22  
### CliMatches
#### Since
2.0.0
#### Properties
Property| Type| Defined in  
---|---|---  
`args`| `Record`<`string`, `ArgMatch`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L41  
`subcommand`| `null` | `SubcommandMatch`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L42  
### SubcommandMatch
#### Since
2.0.0
#### Properties
Property| Type| Defined in  
---|---|---  
`matches`| `CliMatches`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L34  
`name`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L33  
## Functions
### getMatches()
```

functiongetMatches():Promise<CliMatches>

```

Parse the arguments provided to the current process and get the matches using the configuration defined `tauri.cli` in `tauri.conf.json`
#### Returns
`Promise`<`CliMatches`>
#### Example
```

import { getMatches } from'@tauri-apps/plugin-cli';
const matches = await getMatches();
if (matches.subcommand?.name==='run') {
// `./your-app run $ARGS` was executed
const args = matches.subcommand?.matches.args
if ('debug'in args) {
// `./your-app run --debug` was executed
}
} else {
const args = matches.args
// `./your-app $ARGS` was executed
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/cli/guest-js/index.ts#L66
© 2025 Tauri Contributors. CC-BY / MIT
