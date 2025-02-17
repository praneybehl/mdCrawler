Skip to content
# @tauri-apps/plugin-dialog
## Interfaces
### ConfirmDialogOptions
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`cancelLabel?`| `string`| The label of the cancel button.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L100  
`kind?`| `"info"` | `"warning"` | `"error"`| The kind of the dialog. Defaults to `info`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L96  
`okLabel?`| `string`| The label of the confirm button.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L98  
`title?`| `string`| The title of the dialog. Defaults to the app name.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L94  
### DialogFilter
Extension filters for the file dialog.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`extensions`| `string`[]| Extensions to filter, without a `.` prefix. **Example** `extensions: ['svg', 'png']`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L22  
`name`| `string`| Filter name.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L14  
### MessageDialogOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`kind?`| `"info"` | `"warning"` | `"error"`| The kind of the dialog. Defaults to `info`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L87  
`okLabel?`| `string`| The label of the confirm button.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L89  
`title?`| `string`| The title of the dialog. Defaults to the app name.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L85  
### OpenDialogOptions
Options for the open dialog.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`canCreateDirectories?`| `boolean`| Whether to allow creating directories in the dialog. Enabled by default. **macOS Only**| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L54  
`defaultPath?`| `string`| Initial directory or file path. If it’s a directory path, the dialog interface will change to that folder. If it’s not an existing directory, the file name will be set to the dialog’s file name input and the dialog will be set to the parent folder. On mobile the file name is always used on the dialog’s file name input. If not provided, Android uses `(invalid).txt` as default file name.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L43  
`directory?`| `boolean`| Whether the dialog is a directory selection or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L47  
`filters?`| `DialogFilter`[]| The filters of the dialog.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L34  
`multiple?`| `boolean`| Whether the dialog allows multiple selection or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L45  
`recursive?`| `boolean`| If `directory` is true, indicates that it will be read recursively later. Defines whether subdirectories will be allowed on the scope or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L52  
`title?`| `string`| The title of the dialog window (desktop only).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L32  
### SaveDialogOptions
Options for the save dialog.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`canCreateDirectories?`| `boolean`| Whether to allow creating directories in the dialog. Enabled by default. **macOS Only**| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L77  
`defaultPath?`| `string`| Initial directory or file path. If it’s a directory path, the dialog interface will change to that folder. If it’s not an existing directory, the file name will be set to the dialog’s file name input and the dialog will be set to the parent folder. On mobile the file name is always used on the dialog’s file name input. If not provided, Android uses `(invalid).txt` as default file name.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L75  
`filters?`| `DialogFilter`[]| The filters of the dialog.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L66  
`title?`| `string`| The title of the dialog window (desktop only).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L64  
## Type Aliases
### OpenDialogReturn<T>
```

type OpenDialogReturn<T>: T["directory"] extends true ? T["multiple"] extends true ? string[] | null : string | null : T["multiple"] extends true ? string[] | null : string | null;

```

#### Type Parameters
Type Parameter  
---  
`T` _extends_ `OpenDialogOptions`  
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L103
## Functions
### ask()
```

functionask(message, options?):Promise<boolean>

```

Shows a question dialog with `Yes` and `No` buttons.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| The message to show.  
`options`?| `string` | `ConfirmDialogOptions`| The dialog’s options. If a string, it represents the dialog title.  
#### Returns
`Promise`<`boolean`>
A promise resolving to a boolean indicating whether `Yes` was clicked or not.
#### Example
```

import { ask } from'@tauri-apps/plugin-dialog';
const yes = await ask('Are you sure?', 'Tauri');
const yes2 = await ask('This action cannot be reverted. Are you sure?', { title: 'Tauri', kind: 'warning' });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L251
### confirm()
```

functionconfirm(message, options?):Promise<boolean>

```

Shows a question dialog with `Ok` and `Cancel` buttons.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| The message to show.  
`options`?| `string` | `ConfirmDialogOptions`| The dialog’s options. If a string, it represents the dialog title.  
#### Returns
`Promise`<`boolean`>
A promise resolving to a boolean indicating whether `Ok` was clicked or not.
#### Example
```

import { confirm } from'@tauri-apps/plugin-dialog';
const confirmed = await confirm('Are you sure?', 'Tauri');
const confirmed2 = await confirm('This action cannot be reverted. Are you sure?', { title: 'Tauri', kind: 'warning' });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L281
### message()
```

functionmessage(message, options?):Promise<void>

```

Shows a message dialog with an `Ok` button.
#### Parameters
Parameter| Type| Description  
---|---|---  
`message`| `string`| The message to show.  
`options`?| `string` | `MessageDialogOptions`| The dialog’s options. If a string, it represents the dialog title.  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { message } from'@tauri-apps/plugin-dialog';
awaitmessage('Tauri is awesome', 'Tauri');
awaitmessage('File not found', { title: 'Tauri', kind: 'error' });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L222
### open()
```

functionopen<T>(options):Promise<OpenDialogReturn<T>>

```

Open a file/directory selection dialog.
The selected paths are added to the filesystem and asset protocol scopes. When security is more important than the easy of use of this API, prefer writing a dedicated command instead.
Note that the scope change is not persisted, so the values are cleared when the application is restarted. You can save it to the filesystem using tauri-plugin-persisted-scope.
#### Type Parameters
Type Parameter  
---  
`T` _extends_ `OpenDialogOptions`  
#### Parameters
Parameter| Type  
---|---  
`options`| `T`  
#### Returns
`Promise`<`OpenDialogReturn`<`T`>>
A promise resolving to the selected path(s)
#### Examples
```

import { open } from'@tauri-apps/plugin-dialog';
// Open a selection dialog for image files
const selected = await open({
multiple: true,
filters: [{
name: 'Image',
extensions: ['png', 'jpeg']
}]
});
if (Array.isArray(selected)) {
// user selected multiple files
} elseif (selected ===null) {
// user cancelled the selection
} else {
// user selected a single file
}

```

```

import { open } from'@tauri-apps/plugin-dialog';
import { appDir } from'@tauri-apps/api/path';
// Open a selection dialog for directories
const selected = await open({
directory: true,
multiple: true,
defaultPath: await appDir(),
});
if (Array.isArray(selected)) {
// user selected multiple directories
} elseif (selected ===null) {
// user cancelled the selection
} else {
// user selected a single directory
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L163
### save()
```

functionsave(options):Promise<string|null>

```

Open a file/directory save dialog.
The selected path is added to the filesystem and asset protocol scopes. When security is more important than the easy of use of this API, prefer writing a dedicated command instead.
Note that the scope change is not persisted, so the values are cleared when the application is restarted. You can save it to the filesystem using tauri-plugin-persisted-scope.
#### Parameters
Parameter| Type  
---|---  
`options`| `SaveDialogOptions`  
#### Returns
`Promise`<`string` | `null`>
A promise resolving to the selected path.
#### Example
```

import { save } from'@tauri-apps/plugin-dialog';
const filePath = await save({
filters: [{
name: 'Image',
extensions: ['png', 'jpeg']
}]
});

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/dialog/guest-js/index.ts#L197
© 2025 Tauri Contributors. CC-BY / MIT
