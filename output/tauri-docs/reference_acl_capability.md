Skip to content
# Capability
A grouping and boundary mechanism developers can use to isolate access to the IPC layer.
It controls application windows fine grained access to the Tauri core, application, or plugin commands. If a window is not matching any capability then it has no access to the IPC layer at all.
This can be done to create groups of windows, based on their required system access, which can reduce impact of frontend vulnerabilities in less privileged windows. Windows can be added to a capability by exact name (e.g. `main-window`) or glob patterns like `*` or `admin-*`. A Window can have none, one, or multiple associated capabilities.
### Example
```

{
"identifier": "main-user-files-write",
"description": "This capability allows the `main` window on macOS and Windows access to `filesystem` write related commands and `dialog` commands to enable programatic access to files selected by the user.",
"windows": [
"main"
],
"permissions": [
"core:default",
"dialog:open",
{
"identifier": "fs:allow-write-text-file",
"allow": [{ "path": "$HOME/test.txt" }]
},
],
"platforms": ["macOS","windows"]
}

```

**Object Properties** :
  * description
  * identifier (required)
  * local
  * permissions (required)
  * platforms
  * remote
  * webviews
  * windows


### description
`string`
Description of what the capability is intended to allow on associated windows.
It should contain a description of what the grouped permissions should allow.
#### Example
This capability allows the `main` window access to `filesystem` write related commands and `dialog` commands to enable programatic access to files selected by the user.
### identifier
`string`
Identifier of the capability.
#### Example
`main-user-files-write`
### local
`boolean`
Whether this capability is enabled for local app URLs or not. Defaults to `true`.
**Default** : `true`
### permissions
`PermissionEntry`[] each item must be unique
List of permissions attached to this capability.
Must include the plugin name as prefix in the form of `${plugin-name}:${permission-name}`. For commands directly implemented in the application itself only `${permission-name}` is required.
#### Example
```

[
"core:default",
"shell:allow-open",
"dialog:open",
{
"identifier": "fs:allow-write-text-file",
"allow": [{ "path": "$HOME/test.txt" }]
}
]

```

### platforms
`Target`[] | `null`
Limit which target platforms this capability applies to.
By default all platforms are targeted.
#### Example
`["macOS","windows"]`
### remote
`CapabilityRemote` | `null`
Configure remote URLs that can use the capability permissions.
This setting is optional and defaults to not being set, as our default use case is that the content is served from our local application.
#### Example
```

{
"urls": ["https://*.mydomain.dev"]
}

```

### webviews
`string`[]
List of webviews that are affected by this capability. Can be a glob pattern.
This is only required when using on multiwebview contexts, by default all child webviews of a window that matches [`Self::windows`] are linked.
#### Example
`["sub-webview-one", "sub-webview-two"]`
### windows
`string`[]
List of windows that are affected by this capability. Can be a glob pattern.
On multiwebview windows, prefer [`Self::webviews`] for a fine grained access control.
#### Example
`["main"]`
## Definitions
### CapabilityRemote
Configuration for remote URLs that are associated with the capability.
**Object Properties** :
  * urls (required)


##### urls
`string`[]
Remote domains this capability refers to using the URLPattern standard.
###### Examples
  * “https://*.mydomain.dev”: allows subdomains of mydomain.dev
  * “https://mydomain.dev/api/*”: allows any subpath of mydomain.dev/api


### Identifier
`string`
### Number
**Any of the following** :
  * `integer` formatted as `int64` Represents an [`i64`].
  * `number` formatted as `double` Represents a [`f64`].


A valid ACL number.
### PermissionEntry
**Any of the following** :
  * `Identifier` Reference a permission or permission set by identifier.
  * Reference a permission or permission set by identifier and extends its scope. **Object Properties** : - allow - deny - identifier (required) ##### allow `Value`[] | `null` Data that defines what is allowed by the scope. ##### deny `Value`[] | `null` Data that defines what is denied by the scope. This should be prioritized by validation logic. ##### identifier `Identifier` Identifier of the permission or permission set.


An entry for a permission value in a [`Capability`] can be either a raw permission [`Identifier`] or an object that references a permission and extends its scope.
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
