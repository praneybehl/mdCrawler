Skip to content
# @tauri-apps/plugin-os
Provides operating system-related utility methods and properties.
## Type Aliases
### Arch
```

type Arch:
| "x86"
| "x86_64"
| "arm"
| "aarch64"
| "mips"
| "mips64"
| "powerpc"
| "powerpc64"
| "riscv64"
| "s390x"
| "sparc64";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L42
### Family
```

type Family: "unix" | "windows";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L97
### OsType
```

type OsType:
| "linux"
| "windows"
| "macos"
| "ios"
| "android";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L40
### Platform
```

type Platform:
| "linux"
| "macos"
| "ios"
| "freebsd"
| "dragonfly"
| "netbsd"
| "openbsd"
| "solaris"
| "android"
| "windows";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L28
## Functions
### arch()
```

functionarch():Arch

```

Returns the current operating system architecture. Possible values are `'x86'`, `'x86_64'`, `'arm'`, `'aarch64'`, `'mips'`, `'mips64'`, `'powerpc'`, `'powerpc64'`, `'riscv64'`, `'s390x'`, `'sparc64'`.
#### Returns
`Arch`
#### Example
```

import { arch } from'@tauri-apps/plugin-os';
const archName = arch();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L138
### eol()
```

functioneol():string

```

Returns the operating system-specific end-of-line marker.
  * `\n` on POSIX
  * `\r\n` on Windows


#### Returns
`string`
#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L62
### exeExtension()
```

functionexeExtension():string

```

Returns the file extension, if any, used for executable binaries on this platform. Possible values are `'exe'` and `''` (empty string).
#### Returns
`string`
#### Example
```

import { exeExtension } from'@tauri-apps/plugin-os';
const exeExt = exeExtension();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L152
### family()
```

functionfamily():Family

```

Returns the current operating system family. Possible values are `'unix'`, `'windows'`.
#### Returns
`Family`
#### Example
```

import { family } from'@tauri-apps/plugin-os';
const family = family();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L109
### hostname()
```

functionhostname():Promise<string|null>

```

Returns the host name of the operating system.
#### Returns
`Promise`<`string` | `null`>
#### Example
```

import { hostname } from'@tauri-apps/plugin-os';
const hostname = await hostname();

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L181
### locale()
```

functionlocale():Promise<string|null>

```

Returns a String with a `BCP-47` language tag inside. If the locale couldn’t be obtained, `null` is returned instead.
#### Returns
`Promise`<`string` | `null`>
#### Example
```

import { locale } from'@tauri-apps/plugin-os';
const locale = await locale();
if (locale) {
// use the locale string here
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L169
### platform()
```

functionplatform():Platform

```

Returns a string describing the specific operating system in use. The value is set at compile time. Possible values are `'linux'`, `'macos'`, `'ios'`, `'freebsd'`, `'dragonfly'`, `'netbsd'`, `'openbsd'`, `'solaris'`, `'android'`, `'windows'`
#### Returns
`Platform`
#### Example
```

import { platform } from'@tauri-apps/plugin-os';
const platformName = platform();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L79
### type()
```

functiontype():OsType

```

Returns the current operating system type. Returns `'linux'` on Linux, `'macos'` on macOS, `'windows'` on Windows, `'ios'` on iOS and `'android'` on Android.
#### Returns
`OsType`
#### Example
```

import { type } from'@tauri-apps/plugin-os';
const osType = type();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L123
### version()
```

functionversion():string

```

Returns the current operating system version.
#### Returns
`string`
#### Example
```

import { version } from'@tauri-apps/plugin-os';
const osVersion = version();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/os/guest-js/index.ts#L93
© 2025 Tauri Contributors. CC-BY / MIT
