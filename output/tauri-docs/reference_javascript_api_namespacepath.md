Skip to content
# path
The path module provides utilities for working with file and directory paths.
This package is also accessible with `window.__TAURI__.path` when `app.withGlobalTauri` in `tauri.conf.json` is set to `true`.
It is recommended to allowlist only the APIs you use for optimal bundle size and security.
## Enumerations
### BaseDirectory
#### Since
2.0.0
#### Enumeration Members
##### AppCache
```

AppCache: 16;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L35
##### AppConfig
```

AppConfig: 13;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L32
##### AppData
```

AppData: 14;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L33
##### AppLocalData
```

AppLocalData: 15;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L34
##### AppLog
```

AppLog: 17;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L36
##### Audio
```

Audio: 1;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L20
##### Cache
```

Cache: 2;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L21
##### Config
```

Config: 3;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L22
##### Data
```

Data: 4;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L23
##### Desktop
```

Desktop: 18;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L37
##### Document
```

Document: 6;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L25
##### Download
```

Download: 7;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L26
##### Executable
```

Executable: 19;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L38
##### Font
```

Font: 20;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L39
##### Home
```

Home: 21;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L40
##### LocalData
```

LocalData: 5;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L24
##### Picture
```

Picture: 8;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L27
##### Public
```

Public: 9;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L28
##### Resource
```

Resource: 11;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L30
##### Runtime
```

Runtime: 22;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L41
##### Temp
```

Temp: 12;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L31
##### Template
```

Template: 23;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L42
##### Video
```

Video: 10;

```

**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L29
## Functions
### appCacheDir()
```

functionappCacheDir():Promise<string>

```

Returns the path to the suggested directory for your app’s cache files. Resolves to `${cacheDir}/${bundleIdentifier}`, where `bundleIdentifier` is the `identifier` value configured in `tauri.conf.json`.
#### Returns
`Promise`<`string`>
#### Example
```

import { appCacheDir } from'@tauri-apps/api/path';
const appCacheDirPath = await appCacheDir();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L107
### appConfigDir()
```

functionappConfigDir():Promise<string>

```

Returns the path to the suggested directory for your app’s config files. Resolves to `${configDir}/${bundleIdentifier}`, where `bundleIdentifier` is the `identifier` value configured in `tauri.conf.json`.
#### Returns
`Promise`<`string`>
#### Example
```

import { appConfigDir } from'@tauri-apps/api/path';
const appConfigDirPath = await appConfigDir();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L56
### appDataDir()
```

functionappDataDir():Promise<string>

```

Returns the path to the suggested directory for your app’s data files. Resolves to `${dataDir}/${bundleIdentifier}`, where `bundleIdentifier` is the `identifier` value configured in `tauri.conf.json`.
#### Returns
`Promise`<`string`>
#### Example
```

import { appDataDir } from'@tauri-apps/api/path';
const appDataDirPath = await appDataDir();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L73
### appLocalDataDir()
```

functionappLocalDataDir():Promise<string>

```

Returns the path to the suggested directory for your app’s local data files. Resolves to `${localDataDir}/${bundleIdentifier}`, where `bundleIdentifier` is the `identifier` value configured in `tauri.conf.json`.
#### Returns
`Promise`<`string`>
#### Example
```

import { appLocalDataDir } from'@tauri-apps/api/path';
const appLocalDataDirPath = await appLocalDataDir();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L90
### appLogDir()
```

functionappLogDir():Promise<string>

```

Returns the path to the suggested directory for your app’s log files.
#### Platform-specific
  * **Linux:** Resolves to `${configDir}/${bundleIdentifier}/logs`.
  * **macOS:** Resolves to `${homeDir}/Library/Logs/{bundleIdentifier}`
  * **Windows:** Resolves to `${configDir}/${bundleIdentifier}/logs`.


#### Returns
`Promise`<`string`>
#### Example
```

import { appLogDir } from'@tauri-apps/api/path';
const appLogDirPath = await appLogDir();

```

#### Since
1.2.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L519
### audioDir()
```

functionaudioDir():Promise<string>

```

Returns the path to the user’s audio directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_MUSIC_DIR`.
  * **macOS:** Resolves to `$HOME/Music`.
  * **Windows:** Resolves to `{FOLDERID_Music}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { audioDir } from'@tauri-apps/api/path';
const audioDirPath = await audioDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L129
### basename()
```

functionbasename(path, ext?):Promise<string>

```

Returns the last portion of a `path`. Trailing directory separators are ignored.
#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| -  
`ext`?| `string`| An optional file extension to be removed from the returned path.  
#### Returns
`Promise`<`string`>
#### Example
```

import { basename } from'@tauri-apps/api/path';
const base = await basename('path/to/app.conf');
assert(base ==='app.conf');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L649
### cacheDir()
```

functioncacheDir():Promise<string>

```

Returns the path to the user’s cache directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_CACHE_HOME` or `$HOME/.cache`.
  * **macOS:** Resolves to `$HOME/Library/Caches`.
  * **Windows:** Resolves to `{FOLDERID_LocalAppData}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { cacheDir } from'@tauri-apps/api/path';
const cacheDirPath = await cacheDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L151
### configDir()
```

functionconfigDir():Promise<string>

```

Returns the path to the user’s config directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_CONFIG_HOME` or `$HOME/.config`.
  * **macOS:** Resolves to `$HOME/Library/Application Support`.
  * **Windows:** Resolves to `{FOLDERID_RoamingAppData}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { configDir } from'@tauri-apps/api/path';
const configDirPath = await configDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L173
### dataDir()
```

functiondataDir():Promise<string>

```

Returns the path to the user’s data directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_DATA_HOME` or `$HOME/.local/share`.
  * **macOS:** Resolves to `$HOME/Library/Application Support`.
  * **Windows:** Resolves to `{FOLDERID_RoamingAppData}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { dataDir } from'@tauri-apps/api/path';
const dataDirPath = await dataDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L195
### delimiter()
```

functiondelimiter():string

```

Returns the platform-specific path segment delimiter:
  * `;` on Windows
  * `:` on POSIX


#### Returns
`string`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L559
### desktopDir()
```

functiondesktopDir():Promise<string>

```

Returns the path to the user’s desktop directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_DESKTOP_DIR`.
  * **macOS:** Resolves to `$HOME/Desktop`.
  * **Windows:** Resolves to `{FOLDERID_Desktop}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { desktopDir } from'@tauri-apps/api/path';
const desktopPath = await desktopDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L217
### dirname()
```

functiondirname(path):Promise<string>

```

Returns the directory name of a `path`. Trailing directory separators are ignored.
#### Parameters
Parameter| Type  
---|---  
`path`| `string`  
#### Returns
`Promise`<`string`>
#### Example
```

import { dirname } from'@tauri-apps/api/path';
const dir = await dirname('/path/to/somedir/');
assert(dir ==='somedir');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L618
### documentDir()
```

functiondocumentDir():Promise<string>

```

Returns the path to the user’s document directory.
#### Returns
`Promise`<`string`>
#### Example
```

import { documentDir } from'@tauri-apps/api/path';
const documentDirPath = await documentDir();

```

#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_DOCUMENTS_DIR`.
  * **macOS:** Resolves to `$HOME/Documents`.
  * **Windows:** Resolves to `{FOLDERID_Documents}`.


#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L239
### downloadDir()
```

functiondownloadDir():Promise<string>

```

Returns the path to the user’s download directory.
#### Platform-specific
  * **Linux** : Resolves to `xdg-user-dirs`’ `XDG_DOWNLOAD_DIR`.
  * **macOS** : Resolves to `$HOME/Downloads`.
  * **Windows** : Resolves to `{FOLDERID_Downloads}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { downloadDir } from'@tauri-apps/api/path';
const downloadDirPath = await downloadDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L261
### executableDir()
```

functionexecutableDir():Promise<string>

```

Returns the path to the user’s executable directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_BIN_HOME/../bin` or `$XDG_DATA_HOME/../bin` or `$HOME/.local/bin`.
  * **macOS:** Not supported.
  * **Windows:** Not supported.


#### Returns
`Promise`<`string`>
#### Example
```

import { executableDir } from'@tauri-apps/api/path';
const executableDirPath = await executableDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L283
### extname()
```

functionextname(path):Promise<string>

```

Returns the extension of the `path`.
#### Parameters
Parameter| Type  
---|---  
`path`| `string`  
#### Returns
`Promise`<`string`>
#### Example
```

import { extname } from'@tauri-apps/api/path';
const ext = await extname('/path/to/file.html');
assert(ext ==='html');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L633
### fontDir()
```

functionfontDir():Promise<string>

```

Returns the path to the user’s font directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_DATA_HOME/fonts` or `$HOME/.local/share/fonts`.
  * **macOS:** Resolves to `$HOME/Library/Fonts`.
  * **Windows:** Not supported.


#### Returns
`Promise`<`string`>
#### Example
```

import { fontDir } from'@tauri-apps/api/path';
const fontDirPath = await fontDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L305
### homeDir()
```

functionhomeDir():Promise<string>

```

Returns the path to the user’s home directory.
#### Platform-specific
  * **Linux:** Resolves to `$HOME`.
  * **macOS:** Resolves to `$HOME`.
  * **Windows:** Resolves to `{FOLDERID_Profile}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { homeDir } from'@tauri-apps/api/path';
const homeDirPath = await homeDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L327
### isAbsolute()
```

functionisAbsolute(path):Promise<boolean>

```

Returns whether the path is absolute or not.
#### Parameters
Parameter| Type  
---|---  
`path`| `string`  
#### Returns
`Promise`<`boolean`>
#### Example
```

import { isAbsolute } from'@tauri-apps/api/path';
assert(awaitisAbsolute('/home/tauri'));

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L663
### join()
```

functionjoin(...paths):Promise<string>

```

Joins all given `path` segments together using the platform-specific separator as a delimiter, then normalizes the resulting path.
#### Parameters
Parameter| Type  
---|---  
…`paths`| `string`[]  
#### Returns
`Promise`<`string`>
#### Example
```

import { join, appDataDir } from'@tauri-apps/api/path';
const appDataDirPath = await appDataDir();
const path = await join(appDataDirPath, 'users', 'tauri', 'avatar.png');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L603
### localDataDir()
```

functionlocalDataDir():Promise<string>

```

Returns the path to the user’s local data directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_DATA_HOME` or `$HOME/.local/share`.
  * **macOS:** Resolves to `$HOME/Library/Application Support`.
  * **Windows:** Resolves to `{FOLDERID_LocalAppData}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { localDataDir } from'@tauri-apps/api/path';
const localDataDirPath = await localDataDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L349
### normalize()
```

functionnormalize(path):Promise<string>

```

Normalizes the given `path`, resolving `'..'` and `'.'` segments and resolve symbolic links.
#### Parameters
Parameter| Type  
---|---  
`path`| `string`  
#### Returns
`Promise`<`string`>
#### Example
```

import { normalize, appDataDir } from'@tauri-apps/api/path';
const appDataDirPath = await appDataDir();
const path = await normalize(`${appDataDirPath}/../users/tauri/avatar.png`);

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L588
### pictureDir()
```

functionpictureDir():Promise<string>

```

Returns the path to the user’s picture directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_PICTURES_DIR`.
  * **macOS:** Resolves to `$HOME/Pictures`.
  * **Windows:** Resolves to `{FOLDERID_Pictures}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { pictureDir } from'@tauri-apps/api/path';
const pictureDirPath = await pictureDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L371
### publicDir()
```

functionpublicDir():Promise<string>

```

Returns the path to the user’s public directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_PUBLICSHARE_DIR`.
  * **macOS:** Resolves to `$HOME/Public`.
  * **Windows:** Resolves to `{FOLDERID_Public}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { publicDir } from'@tauri-apps/api/path';
const publicDirPath = await publicDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L393
### resolve()
```

functionresolve(...paths):Promise<string>

```

Resolves a sequence of `paths` or `path` segments into an absolute path.
#### Parameters
Parameter| Type  
---|---  
…`paths`| `string`[]  
#### Returns
`Promise`<`string`>
#### Example
```

import { resolve, appDataDir } from'@tauri-apps/api/path';
const appDataDirPath = await appDataDir();
const path = await resolve(appDataDirPath, '..', 'users', 'tauri', 'avatar.png');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L573
### resolveResource()
```

functionresolveResource(resourcePath):Promise<string>

```

Resolve the path to a resource file.
#### Parameters
Parameter| Type| Description  
---|---|---  
`resourcePath`| `string`| The path to the resource. Must follow the same syntax as defined in `tauri.conf.json > bundle > resources`, i.e. keeping subfolders and parent dir components (`../`).  
#### Returns
`Promise`<`string`>
The full path to the resource.
#### Example
```

import { resolveResource } from'@tauri-apps/api/path';
const resourcePath = await resolveResource('script.sh');

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L430
### resourceDir()
```

functionresourceDir():Promise<string>

```

Returns the path to the application’s resource directory. To resolve a resource path, see the [[resolveResource | `resolveResource API`]].
#### Returns
`Promise`<`string`>
#### Example
```

import { resourceDir } from'@tauri-apps/api/path';
const resourceDirPath = await resourceDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L410
### runtimeDir()
```

functionruntimeDir():Promise<string>

```

Returns the path to the user’s runtime directory.
#### Platform-specific
  * **Linux:** Resolves to `$XDG_RUNTIME_DIR`.
  * **macOS:** Not supported.
  * **Windows:** Not supported.


#### Returns
`Promise`<`string`>
#### Example
```

import { runtimeDir } from'@tauri-apps/api/path';
const runtimeDirPath = await runtimeDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L453
### sep()
```

functionsep():string

```

Returns the platform-specific path segment separator:
  * `\` on Windows
  * `/` on POSIX


#### Returns
`string`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L548
### tempDir()
```

functiontempDir():Promise<string>

```

Returns a temporary directory.
#### Returns
`Promise`<`string`>
#### Example
```

import { tempDir } from'@tauri-apps/api/path';
const temp = await tempDir();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L535
### templateDir()
```

functiontemplateDir():Promise<string>

```

Returns the path to the user’s template directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_TEMPLATES_DIR`.
  * **macOS:** Not supported.
  * **Windows:** Resolves to `{FOLDERID_Templates}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { templateDir } from'@tauri-apps/api/path';
const templateDirPath = await templateDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L475
### videoDir()
```

functionvideoDir():Promise<string>

```

Returns the path to the user’s video directory.
#### Platform-specific
  * **Linux:** Resolves to `xdg-user-dirs`’ `XDG_VIDEOS_DIR`.
  * **macOS:** Resolves to `$HOME/Movies`.
  * **Windows:** Resolves to `{FOLDERID_Videos}`.


#### Returns
`Promise`<`string`>
#### Example
```

import { videoDir } from'@tauri-apps/api/path';
const videoDirPath = await videoDir();

```

#### Since
1.0.0
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/path.ts#L497
© 2025 Tauri Contributors. CC-BY / MIT
