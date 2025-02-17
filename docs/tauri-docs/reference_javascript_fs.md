Skip to content
# @tauri-apps/plugin-fs
Access the file system.
## Security
This module prevents path traversal, not allowing parent directory accessors to be used (i.e. “/usr/path/to/../file” or ”../path/to/file” paths are not allowed). Paths accessed with this API must be either relative to one of the base directories or created with the path API.
The API has a scope configuration that forces you to restrict the paths that can be accessed using glob patterns.
The scope configuration is an array of glob patterns describing file/directory paths that are allowed. For instance, this scope configuration allows **all** enabled `fs` APIs to (only) access files in the _databases_ directory of the `$APPDATA` directory:
```

{
"permissions": [
{
"identifier": "fs:scope",
"allow": [{ "path": "$APPDATA/databases/*" }]
}
]
}

```

Scopes can also be applied to specific `fs` APIs by using the API’s identifier instead of `fs:scope`:
```

{
"permissions": [
{
"identifier": "fs:allow-exists",
"allow": [{ "path": "$APPDATA/databases/*" }]
}
]
}

```

Notice the use of the `$APPDATA` variable. The value is injected at runtime, resolving to the app data directory.
The available variables are: `$APPCONFIG`, `$APPDATA`, `$APPLOCALDATA`, `$APPCACHE`, `$APPLOG`, `$AUDIO`, `$CACHE`, `$CONFIG`, `$DATA`, `$LOCALDATA`, `$DESKTOP`, `$DOCUMENT`, `$DOWNLOAD`, `$EXE`, `$FONT`, `$HOME`, `$PICTURE`, `$PUBLIC`, `$RUNTIME`, `$TEMPLATE`, `$VIDEO`, `$RESOURCE`, `$TEMP`.
Trying to execute any API with a URL not configured on the scope results in a promise rejection due to denied access.
## Enumerations
### BaseDirectory
#### Since
2.0.0
#### Enumeration Members
##### AppCache
```

AppCache: 16;

```

**Source** : undefined
##### AppConfig
```

AppConfig: 13;

```

**Source** : undefined
##### AppData
```

AppData: 14;

```

**Source** : undefined
##### AppLocalData
```

AppLocalData: 15;

```

**Source** : undefined
##### AppLog
```

AppLog: 17;

```

**Source** : undefined
##### Audio
```

Audio: 1;

```

**Source** : undefined
##### Cache
```

Cache: 2;

```

**Source** : undefined
##### Config
```

Config: 3;

```

**Source** : undefined
##### Data
```

Data: 4;

```

**Source** : undefined
##### Desktop
```

Desktop: 18;

```

**Source** : undefined
##### Document
```

Document: 6;

```

**Source** : undefined
##### Download
```

Download: 7;

```

**Source** : undefined
##### Executable
```

Executable: 19;

```

**Source** : undefined
##### Font
```

Font: 20;

```

**Source** : undefined
##### Home
```

Home: 21;

```

**Source** : undefined
##### LocalData
```

LocalData: 5;

```

**Source** : undefined
##### Picture
```

Picture: 8;

```

**Source** : undefined
##### Public
```

Public: 9;

```

**Source** : undefined
##### Resource
```

Resource: 11;

```

**Source** : undefined
##### Runtime
```

Runtime: 22;

```

**Source** : undefined
##### Temp
```

Temp: 12;

```

**Source** : undefined
##### Template
```

Template: 23;

```

**Source** : undefined
##### Video
```

Video: 10;

```

**Source** : undefined
### SeekMode
#### Enumeration Members
##### Current
```

Current: 1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L80
##### End
```

End: 2;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L81
##### Start
```

Start: 0;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L79
## Classes
### FileHandle
The Tauri abstraction for reading and writing files.
#### Since
2.0.0
#### Extends
  * `Resource`


#### Constructors
##### new FileHandle()
```

newFileHandle(rid): FileHandle

```

###### Parameters
Parameter| Type  
---|---  
`rid`| `number`  
###### Returns
`FileHandle`
###### Inherited from
`Resource.constructor`
**Source** : undefined
#### Accessors
##### rid
###### Get Signature
```

get rid(): number

```

###### Returns
`number`
###### Inherited from
`Resource.rid`
**Source** : undefined
#### Methods
##### close()
```

close(): Promise<void>

```

Destroys and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
###### Inherited from
`Resource.close`
**Source** : undefined
##### read()
```

read(buffer): Promise<null| number>

```

Reads up to `p.byteLength` bytes into `p`. It resolves to the number of bytes read (`0` < `n` <= `p.byteLength`) and rejects if any error encountered. Even if `read()` resolves to `n` < `p.byteLength`, it may use all of `p` as scratch space during the call. If some data is available but not `p.byteLength` bytes, `read()` conventionally resolves to what is available instead of waiting for more.
When `read()` encounters end-of-file condition, it resolves to EOF (`null`).
When `read()` encounters an error, it rejects with an error.
Callers should always process the `n` > `0` bytes returned before considering the EOF (`null`). Doing so correctly handles I/O errors that happen after reading some bytes and also both of the allowed EOF behaviors.
###### Parameters
Parameter| Type  
---|---  
`buffer`| `Uint8Array`<`ArrayBufferLike`>  
###### Returns
`Promise`<`null` | `number`>
###### Example
```

import { open, BaseDirectory } from"@tauri-apps/plugin-fs"
// if "$APPCONFIG/foo/bar.txt" contains the text "hello world":
const file = await open("foo/bar.txt", { baseDir: BaseDirectory.AppConfig });
const buf = newUint8Array(100);
const numberOfBytesRead = await file.read(buf); // 11 bytes
const text = newTextDecoder().decode(buf); // "hello world"
await file.close();

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L314
##### seek()
```

seek(offset, whence): Promise<number>

```

Seek sets the offset for the next `read()` or `write()` to offset, interpreted according to `whence`: `Start` means relative to the start of the file, `Current` means relative to the current offset, and `End` means relative to the end. Seek resolves to the new offset relative to the start of the file.
Seeking to an offset before the start of the file is an error. Seeking to any positive offset is legal, but the behavior of subsequent I/O operations on the underlying object is implementation-dependent. It returns the number of cursor position.
###### Parameters
Parameter| Type  
---|---  
`offset`| `number`  
`whence`| `SeekMode`  
###### Returns
`Promise`<`number`>
###### Example
```

import { open, SeekMode, BaseDirectory } from'@tauri-apps/plugin-fs';
// Given hello.txt pointing to file with "Hello world", which is 11 bytes long:
const file = await open('hello.txt', { read: true, write: true, truncate: true, create: true, baseDir: BaseDirectory.AppLocalData });
await file.write(newTextEncoder().encode("Hello world"));
// Seek 6 bytes from the start of the file
console.log(await file.seek(6, SeekMode.Start)); // "6"
// Seek 2 more bytes from the current position
console.log(await file.seek(2, SeekMode.Current)); // "8"
// Seek backwards 2 bytes from the end of the file
console.log(await file.seek(-2, SeekMode.End)); // "9" (e.g. 11-2)
await file.close();

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L369
##### stat()
```

stat(): Promise<FileInfo>

```

Returns a `FileInfo` for this file.
###### Returns
`Promise`<`FileInfo`>
###### Example
```

import { open, BaseDirectory } from'@tauri-apps/plugin-fs';
const file = await open("file.txt", { read: true, baseDir: BaseDirectory.AppLocalData });
const fileInfo = await file.stat();
console.log(fileInfo.isFile); // true
await file.close();

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L391
##### truncate()
```

truncate(len?):Promise<void>

```

Truncates or extends this file, to reach the specified `len`. If `len` is not specified then the entire file contents are truncated.
###### Parameters
Parameter| Type  
---|---  
`len`?| `number`  
###### Returns
`Promise`<`void`>
###### Example
```

import { open, BaseDirectory } from'@tauri-apps/plugin-fs';
// truncate the entire file
const file = await open("my_file.txt", { read: true, write: true, create: true, baseDir: BaseDirectory.AppLocalData });
await file.truncate();
// truncate part of the file
const file = await open("my_file.txt", { read: true, write: true, create: true, baseDir: BaseDirectory.AppLocalData });
await file.write(newTextEncoder().encode("Hello World"));
await file.truncate(7);
const data = newUint8Array(32);
await file.read(data);
console.log(newTextDecoder().decode(data)); // Hello W
await file.close();

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L423
##### write()
```

write(data): Promise<number>

```

Writes `data.byteLength` bytes from `data` to the underlying data stream. It resolves to the number of bytes written from `data` (`0` <= `n` <= `data.byteLength`) or reject with the error encountered that caused the write to stop early. `write()` must reject with a non-null error if would resolve to `n` < `data.byteLength`. `write()` must not modify the slice data, even temporarily.
###### Parameters
Parameter| Type  
---|---  
`data`| `Uint8Array`<`ArrayBufferLike`>  
###### Returns
`Promise`<`number`>
###### Example
```

import { open, write, BaseDirectory } from'@tauri-apps/plugin-fs';
const encoder = newTextEncoder();
const data = encoder.encode("Hello world");
const file = await open("bar.txt", { write: true, baseDir: BaseDirectory.AppLocalData });
const bytesWritten = await file.write(data); // 11
await file.close();

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L450
## Interfaces
### CopyFileOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`fromPathBaseDir?`| `BaseDirectory`| Base directory for `fromPath`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L586  
`toPathBaseDir?`| `BaseDirectory`| Base directory for `toPath`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L588  
### CreateOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L463  
### DebouncedWatchOptions
#### Since
2.0.0
#### Extends
  * `WatchOptions`


#### Properties
Property| Type| Description| Inherited from| Defined in  
---|---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| `WatchOptions`.`baseDir`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1162  
`delayMs?`| `number`| Debounce delay| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1170  
`recursive?`| `boolean`| Watch a directory recursively| `WatchOptions`.`recursive`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1160  
### DirEntry
A disk entry which is either a file, a directory or a symlink.
This is the result of the `readDir`.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`isDirectory`| `boolean`| Specifies whether this entry is a directory or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L677  
`isFile`| `boolean`| Specifies whether this entry is a file or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L679  
`isSymlink`| `boolean`| Specifies whether this entry is a symlink or not.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L681  
`name`| `string`| The name of the entry (file name with extension or directory name).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L675  
### ExistsOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1127  
### FileInfo
A FileInfo describes a file and is returned by `stat`, `lstat` or `fstat`.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`atime`| `null` | `Date`| The last access time of the file. This corresponds to the `atime` field from `stat` on Unix and `ftLastAccessTime` on Windows. This may not be available on all platforms.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L120  
`birthtime`| `null` | `Date`| The creation time of the file. This corresponds to the `birthtime` field from `stat` on Mac/BSD and `ftCreationTime` on Windows. This may not be available on all platforms.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L126  
`blksize`| `null` | `number`| Blocksize for filesystem I/O. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L203  
`blocks`| `null` | `number`| Number of blocks allocated to the file, in 512-byte units. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L211  
`dev`| `null` | `number`| ID of the device containing the file. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L146  
`fileAttributes`| `null` | `number`| This field contains the file system attribute information for a file or directory. For possible values and their descriptions, see File Attribute Constants in the Windows Dev Center #### Platform-specific - **macOS / Linux / Android / iOS:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L138  
`gid`| `null` | `number`| Group ID of the owner of this file. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L187  
`ino`| `null` | `number`| Inode number. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L154  
`isDirectory`| `boolean`| True if this is info for a regular directory. Mutually exclusive to `FileInfo.isFile` and `FileInfo.isSymlink`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L99  
`isFile`| `boolean`| True if this is info for a regular file. Mutually exclusive to `FileInfo.isDirectory` and `FileInfo.isSymlink`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L94  
`isSymlink`| `boolean`| True if this is info for a symlink. Mutually exclusive to `FileInfo.isFile` and `FileInfo.isDirectory`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L104  
`mode`| `null` | `number`| The underlying raw `st_mode` bits that contain the standard Unix permissions for this file/directory. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L163  
`mtime`| `null` | `Date`| The last modification time of the file. This corresponds to the `mtime` field from `stat` on Linux/Mac OS and `ftLastWriteTime` on Windows. This may not be available on all platforms.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L114  
`nlink`| `null` | `number`| Number of hard links pointing to this file. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L171  
`rdev`| `null` | `number`| Device ID of this file. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L195  
`readonly`| `boolean`| Whether this is a readonly (unwritable) file.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L128  
`size`| `number`| The size of the file, in bytes.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L108  
`uid`| `null` | `number`| User ID of the owner of this file. #### Platform-specific - **Windows:** Unsupported.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L179  
### MkdirOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L631  
`mode?`| `number`| Permissions to use when creating the directory (defaults to `0o777`, before the process’s umask). Ignored on Windows.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L625  
`recursive?`| `boolean`| Defaults to `false`. If set to `true`, means that any intermediate directories will also be created (as with the shell command `mkdir -p`).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L629  
### OpenOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`append?`| `boolean`| Sets the option for the append mode. This option, when `true`, means that writes will append to a file instead of overwriting previous contents. Note that setting `{ write: true, append: true }` has the same effect as setting only `{ append: true }`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L518  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L546  
`create?`| `boolean`| Sets the option to allow creating a new file, if one doesn’t already exist at the specified path. Requires write or append access to be used.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L531  
`createNew?`| `boolean`| Defaults to `false`. If set to `true`, no file, directory, or symlink is allowed to exist at the target location. Requires write or append access to be used. When createNew is set to `true`, create and truncate are ignored.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L538  
`mode?`| `number`| Permissions to use if creating the file (defaults to `0o666`, before the process’s umask). Ignored on Windows.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L544  
`read?`| `boolean`| Sets the option for read access. This option, when `true`, means that the file should be read-able if opened.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L504  
`truncate?`| `boolean`| Sets the option for truncating a previous file. If a file is successfully opened with this option set it will truncate the file to `0` size if it already exists. The file must be opened with write access for truncate to work.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L525  
`write?`| `boolean`| Sets the option for write access. This option, when `true`, means that the file should be write-able if opened. If the file already exists, any write calls on it will overwrite its contents, by default without truncating it.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L511  
### ReadDirOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L663  
### ReadFileOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L725  
### RemoveOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L862  
`recursive?`| `boolean`| Defaults to `false`. If set to `true`, path will be removed even if it’s a non-empty directory.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L860  
### RenameOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`newPathBaseDir?`| `BaseDirectory`| Base directory for `newPath`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L898  
`oldPathBaseDir?`| `BaseDirectory`| Base directory for `oldPath`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L896  
### StatOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L940  
### TruncateOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L999  
### WatchEvent
#### Since
2.0.0
#### Properties
Property| Type| Defined in  
---|---|---  
`attrs`| `unknown`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1179  
`paths`| `string`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1178  
`type`| `WatchEventKind`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1177  
### WatchOptions
#### Since
2.0.0
#### Extended by
  * `DebouncedWatchOptions`


#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1162  
`recursive?`| `boolean`| Watch a directory recursively| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1160  
### WriteFileOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`append?`| `boolean`| Defaults to `false`. If set to `true`, will append to a file instead of overwriting previous contents.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1043  
`baseDir?`| `BaseDirectory`| Base directory for `path`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1051  
`create?`| `boolean`| Sets the option to allow creating a new file, if one doesn’t already exist at the specified path (defaults to `true`).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1045  
`createNew?`| `boolean`| Sets the option to create a new file, failing if it already exists.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1047  
`mode?`| `number`| File permissions. Ignored on Windows.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1049  
## Type Aliases
### UnwatchFn()
```

type UnwatchFn: () => void;

```

#### Returns
`void`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1243
### WatchEventKind
```

type WatchEventKind:
| "any"
| object
| object
| object
| object
| "other";

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1185
### WatchEventKindAccess
```

type WatchEventKindAccess: object | object | object | object;

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1196
### WatchEventKindCreate
```

type WatchEventKindCreate: object | object | object | object;

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1205
### WatchEventKindModify
```

type WatchEventKindModify:
| object
| object
| object
| object
| object;

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1214
### WatchEventKindRemove
```

type WatchEventKindRemove: object | object | object | object;

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1234
## Functions
### copyFile()
```

functioncopyFile(
fromPath,
toPath,
options?):Promise<void>

```

Copies the contents and permissions of one file to another specified path, by default creating a new file if needed, else overwriting.
#### Parameters
Parameter| Type  
---|---  
`fromPath`| `string` | `URL`  
`toPath`| `string` | `URL`  
`options`?| `CopyFileOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { copyFile, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitcopyFile('app.conf', 'app.conf.bk', { fromPathBaseDir: BaseDirectory.AppConfig, toPathBaseDir: BaseDirectory.AppConfig });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L601
### create()
```

functioncreate(path, options?):Promise<FileHandle>

```

Creates a file if none exists or truncates an existing file and resolves to an instance of `FileHandle`.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `CreateOptions`  
#### Returns
`Promise`<`FileHandle`>
#### Example
```

import { create, BaseDirectory } from"@tauri-apps/plugin-fs"
const file = await create("foo/bar.txt", { baseDir: BaseDirectory.AppConfig });
await file.write(newTextEncoder().encode("Hello world"));
await file.close();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L480
### exists()
```

functionexists(path, options?):Promise<boolean>

```

Check if a path exists.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `ExistsOptions`  
#### Returns
`Promise`<`boolean`>
#### Example
```

import { exists, BaseDirectory } from'@tauri-apps/plugin-fs';
// Check if the `$APPDATA/avatar.png` file exists
awaitexists('avatar.png', { baseDir: BaseDirectory.AppData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1141
### lstat()
```

functionlstat(path, options?):Promise<FileInfo>

```

Resolves to a `FileInfo` for the specified `path`. If `path` is a symlink, information for the symlink will be returned instead of what it points to.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `StatOptions`  
#### Returns
`Promise`<`FileInfo`>
#### Example
```

import { lstat, BaseDirectory } from'@tauri-apps/plugin-fs';
const fileInfo = await lstat("hello.txt", { baseDir: BaseDirectory.AppLocalData });
console.log(fileInfo.isFile); // true

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L982
### mkdir()
```

functionmkdir(path, options?):Promise<void>

```

Creates a new directory with the specified path.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `MkdirOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { mkdir, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitmkdir('users', { baseDir: BaseDirectory.AppLocalData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L644
### open()
```

functionopen(path, options?):Promise<FileHandle>

```

Open a file and resolve to an instance of `FileHandle`. The file does not need to previously exist if using the `create` or `createNew` open options. It is the callers responsibility to close the file when finished with it.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `OpenOptions`  
#### Returns
`Promise`<`FileHandle`>
#### Example
```

import { open, BaseDirectory } from"@tauri-apps/plugin-fs"
const file = await open("foo/bar.txt", { read: true, write: true, baseDir: BaseDirectory.AppLocalData });
// Do work with file
await file.close();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L565
### readDir()
```

functionreadDir(path, options?):Promise<DirEntry[]>

```

Reads the directory given by path and returns an array of `DirEntry`.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `ReadDirOptions`  
#### Returns
`Promise`<`DirEntry`[]>
#### Example
```

import { readDir, BaseDirectory } from'@tauri-apps/plugin-fs';
import { join } from'@tauri-apps/api/path';
const dir = "users"
const entries = await readDir('users', { baseDir: BaseDirectory.AppLocalData });
processEntriesRecursively(dir, entries);
asyncfunctionprocessEntriesRecursively(parent, entries) {
for (const entryof entries) {
console.log(`Entry: ${entry.name}`);
if (entry.isDirectory) {
const dir = await join(parent,entry.name);
processEntriesRecursively(dir,awaitreadDir(dir, { baseDir: BaseDirectory.AppLocalData }))
}
}
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L706
### readFile()
```

functionreadFile(path, options?):Promise<Uint8Array>

```

Reads and resolves to the entire contents of a file as an array of bytes. TextDecoder can be used to transform the bytes to string if required.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `ReadFileOptions`  
#### Returns
`Promise`<`Uint8Array`>
#### Example
```

import { readFile, BaseDirectory } from'@tauri-apps/plugin-fs';
const contents = await readFile('avatar.png', { baseDir: BaseDirectory.Resource });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L739
### readTextFile()
```

functionreadTextFile(path, options?):Promise<string>

```

Reads and returns the entire contents of a file as UTF-8 string.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `ReadFileOptions`  
#### Returns
`Promise`<`string`>
#### Example
```

import { readTextFile, BaseDirectory } from'@tauri-apps/plugin-fs';
const contents = await readTextFile('app.conf', { baseDir: BaseDirectory.AppConfig });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L765
### readTextFileLines()
```

functionreadTextFileLines(path, options?):Promise<AsyncIterableIterator<string>>

```

Returns an async AsyncIterableIterator over the lines of a file as UTF-8 string.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `ReadFileOptions`  
#### Returns
`Promise`<`AsyncIterableIterator`<`string`>>
#### Example
```

import { readTextFileLines, BaseDirectory } from'@tauri-apps/plugin-fs';
const lines = await readTextFileLines('app.conf', { baseDir: BaseDirectory.AppConfig });
forawait (const lineof lines) {
console.log(line);
}

```

You could also call AsyncIterableIterator.next to advance the iterator so you can lazily read the next line whenever you want.
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L798
### remove()
```

functionremove(path, options?):Promise<void>

```

Removes the named file or directory. If the directory is not empty and the `recursive` option isn’t set to true, the promise will be rejected.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `RemoveOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { remove, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitremove('users/file.txt', { baseDir: BaseDirectory.AppLocalData });
awaitremove('users', { baseDir: BaseDirectory.AppLocalData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L877
### rename()
```

functionrename(
oldPath,
newPath,
options?):Promise<void>

```

Renames (moves) oldpath to newpath. Paths may be files or directories. If newpath already exists and is not a directory, rename() replaces it. OS-specific restrictions may apply when oldpath and newpath are in different directories.
On Unix, this operation does not follow symlinks at either path.
#### Parameters
Parameter| Type  
---|---  
`oldPath`| `string` | `URL`  
`newPath`| `string` | `URL`  
`options`?| `RenameOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { rename, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitrename('avatar.png', 'deleted.png', { oldPathBaseDir: BaseDirectory.App, newPathBaseDir: BaseDirectory.AppLocalData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L916
### size()
```

functionsize(path):Promise<number>

```

Get the size of a file or directory. For files, the `stat` functions can be used as well.
If `path` is a directory, this function will recursively iterate over every file and every directory inside of `path` and therefore will be very time consuming if used on larger directories.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
#### Returns
`Promise`<`number`>
#### Example
```

import { size, BaseDirectory } from'@tauri-apps/plugin-fs';
// Get the size of the `$APPDATA/tauri` directory.
const dirSize = await size('tauri', { baseDir: BaseDirectory.AppData });
console.log(dirSize); // 1024

```

#### Since
2.1.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1340
### stat()
```

functionstat(path, options?):Promise<FileInfo>

```

Resolves to a `FileInfo` for the specified `path`. Will always follow symlinks but will reject if the symlink points to a path outside of the scope.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`options`?| `StatOptions`  
#### Returns
`Promise`<`FileInfo`>
#### Example
```

import { stat, BaseDirectory } from'@tauri-apps/plugin-fs';
const fileInfo = await stat("hello.txt", { baseDir: BaseDirectory.AppLocalData });
console.log(fileInfo.isFile); // true

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L956
### truncate()
```

functiontruncate(
path,
len?,
options?):Promise<void>

```

Truncates or extends the specified file, to reach the specified `len`. If `len` is `0` or not specified, then the entire file contents are truncated.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`len`?| `number`  
`options`?| `TruncateOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { truncate, readTextFile, writeTextFile, BaseDirectory } from'@tauri-apps/plugin-fs';
// truncate the entire file
awaittruncate("my_file.txt", 0, { baseDir: BaseDirectory.AppLocalData });
// truncate part of the file
const filePath = "file.txt";
awaitwriteTextFile(filePath, "Hello World", { baseDir: BaseDirectory.AppLocalData });
awaittruncate(filePath, 7, { baseDir: BaseDirectory.AppLocalData });
const data = await readTextFile(filePath, { baseDir: BaseDirectory.AppLocalData });
console.log(data); // "Hello W"

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1022
### watch()
```

functionwatch(
paths,
cb,
options?):Promise<UnwatchFn>

```

Watch changes (after a delay) on files or directories.
#### Parameters
Parameter| Type  
---|---  
`paths`| `string` | `URL` | `string`[] | `URL`[]  
`cb`| (`event`) => `void`  
`options`?| `DebouncedWatchOptions`  
#### Returns
`Promise`<`UnwatchFn`>
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1254
### watchImmediate()
```

functionwatchImmediate(
paths,
cb,
options?):Promise<UnwatchFn>

```

Watch changes on files or directories.
#### Parameters
Parameter| Type  
---|---  
`paths`| `string` | `URL` | `string`[] | `URL`[]  
`cb`| (`event`) => `void`  
`options`?| `WatchOptions`  
#### Returns
`Promise`<`UnwatchFn`>
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1292
### writeFile()
```

functionwriteFile(
path,
data,
options?):Promise<void>

```

Write `data` to the given `path`, by default creating a new file if needed, else overwriting.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`data`| `Uint8Array`<`ArrayBufferLike`> | `ReadableStream`<`Uint8Array`<`ArrayBufferLike`>>  
`options`?| `WriteFileOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { writeFile, BaseDirectory } from'@tauri-apps/plugin-fs';
let encoder = newTextEncoder();
let data = encoder.encode("Hello World");
awaitwriteFile('file.txt', data, { baseDir: BaseDirectory.AppLocalData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1067
### writeTextFile()
```

functionwriteTextFile(
path,
data,
options?):Promise<void>

```

Writes UTF-8 string `data` to the given `path`, by default creating a new file if needed, else overwriting.
#### Parameters
Parameter| Type  
---|---  
`path`| `string` | `URL`  
`data`| `string`  
`options`?| `WriteFileOptions`  
#### Returns
`Promise`<`void`>
#### Example
```

import { writeTextFile, BaseDirectory } from'@tauri-apps/plugin-fs';
awaitwriteTextFile('file.txt', "Hello world", { baseDir: BaseDirectory.AppLocalData });

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/fs/guest-js/index.ts#L1103
© 2025 Tauri Contributors. CC-BY / MIT
