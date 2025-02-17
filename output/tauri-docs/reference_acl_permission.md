Skip to content
# Permission
Descriptions of explicit privileges of commands.
It can enable commands to be accessible in the frontend of the application.
If the scope is defined it can be used to fine grain control the access of individual or multiple commands.
**Object Properties** :
  * commands
  * description
  * identifier (required)
  * platforms
  * scope
  * version


### commands
`Commands`
Allowed or denied commands when using this permission.
Default```

{
"allow": [],
"deny": []
}

```

### description
`string` | `null`
Human-readable description of what the permission does. Tauri internal convention is to use <h4> headings in markdown content for Tauri documentation generation purposes.
### identifier
`string`
A unique identifier for the permission.
### platforms
`Target`[] | `null`
Target platforms this permission applies. By default all platforms are affected by this permission.
### scope
`Scopes`
Allowed or denied scoped when using this permission.
### version
`integer` | `null` minimum of `1`, formatted as `uint64`
The version of the permission.
## Definitions
### Commands
Allowed and denied commands inside a permission.
If two commands clash inside of `allow` and `deny`, it should be denied by default.
**Object Properties** :
  * allow
  * deny


##### allow
`string`[]
Allowed command.
**Default** : `[]`
##### deny
`string`[]
Denied command, which takes priority.
**Default** : `[]`
### Number
**Any of the following** :
  * `integer` formatted as `int64` Represents an [`i64`].
  * `number` formatted as `double` Represents a [`f64`].


A valid ACL number.
### Scopes
An argument for fine grained behavior control of Tauri commands.
It can be of any serde serializable type and is used to allow or prevent certain actions inside a Tauri command. The configured scope is passed to the command and will be enforced by the command implementation.
##### Example
```

{
"allow": [{ "path": "$HOME/**" }],
"deny": [{ "path": "$HOME/secret.txt" }]
}

```

**Object Properties** :
  * allow
  * deny


##### allow
`Value`[] | `null`
Data that defines what is allowed by the scope.
##### deny
`Value`[] | `null`
Data that defines what is denied by the scope. This should be prioritized by validation logic.
### Target
**One of the following** :
  * `"macOS"` MacOS.
  * `"windows"` Windows.
  * `"linux"` Linux.
  * `"android"` Android.
  * `"iOS"` iOS.


Platform target.
### Value
**Any of the following** :
  * `null` Represents a null JSON value.
  * `boolean` Represents a [`bool`].
  * `Number` Represents a valid ACL [`Number`].
  * `string` Represents a [`String`].
  * `Value`[] Represents a list of other [`Value`]s.
  * Represents a map of [`String`] keys to [`Value`]s. **Allows additional properties** : `Value`


All supported ACL values.
© 2025 Tauri Contributors. CC-BY / MIT
