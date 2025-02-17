Skip to content
# Scope
An argument for fine grained behavior control of Tauri commands.
It can be of any serde serializable type and is used to allow or prevent certain actions inside a Tauri command. The configured scope is passed to the command and will be enforced by the command implementation.
### Example
```

{
"allow": [{ "path": "$HOME/**" }],
"deny": [{ "path": "$HOME/secret.txt" }]
}

```

**Object Properties** :
  * allow
  * deny


### allow
`Value`[] | `null`
Data that defines what is allowed by the scope.
### deny
`Value`[] | `null`
Data that defines what is denied by the scope. This should be prioritized by validation logic.
## Definitions
### Number
**Any of the following** :
  * `integer` formatted as `int64` Represents an [`i64`].
  * `number` formatted as `double` Represents a [`f64`].


A valid ACL number.
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
