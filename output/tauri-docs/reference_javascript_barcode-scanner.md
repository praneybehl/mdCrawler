Skip to content
# @tauri-apps/plugin-barcode-scanner
## Enumerations
### Format
#### Enumeration Members
##### Aztec
```

Aztec: "AZTEC";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L24
##### Codabar
```

Codabar: "CODABAR";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L22
##### Code128
```

Code128: "CODE_128";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L21
##### Code39
```

Code39: "CODE_39";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L19
##### Code93
```

Code93: "CODE_93";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L20
##### DataMatrix
```

DataMatrix: "DATA_MATRIX";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L25
##### EAN13
```

EAN13: "EAN_13";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L18
##### EAN8
```

EAN8: "EAN_8";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L17
##### ITF
```

ITF: "ITF";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L23
##### PDF417
```

PDF417: "PDF_417";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L26
##### QRCode
```

QRCode: "QR_CODE";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L14
##### UPC_A
```

UPC_A: "UPC_A";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L15
##### UPC_E
```

UPC_E: "UPC_E";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L16
## Interfaces
### Scanned
#### Properties
Property| Type| Defined in  
---|---|---  
`bounds`| `unknown`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L38  
`content`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L36  
`format`| `Format`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L37  
### ScanOptions
#### Properties
Property| Type| Defined in  
---|---|---  
`cameraDirection?`| `"back"` | `"front"`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L30  
`formats?`| `Format`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L31  
`windowed?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L32  
## Type Aliases
### PermissionState
```

type PermissionState: "granted" | "denied" | "prompt" | "prompt-with-rationale";

```

**Source** : undefined
## Functions
### cancel()
```

functioncancel():Promise<void>

```

Cancel the current scan process.
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L52
### checkPermissions()
```

functioncheckPermissions():Promise<PermissionState>

```

Get permission state.
#### Returns
`Promise`<`PermissionState`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L59
### openAppSettings()
```

functionopenAppSettings():Promise<void>

```

Open application settings. Useful if permission was denied and the user must manually enable it.
#### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L77
### requestPermissions()
```

functionrequestPermissions():Promise<PermissionState>

```

Request permissions to use the camera.
#### Returns
`Promise`<`PermissionState`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L68
### scan()
```

functionscan(options?):Promise<Scanned>

```

Start scanning.
#### Parameters
Parameter| Type| Description  
---|---|---  
`options`?| `ScanOptions`  
#### Returns
`Promise`<`Scanned`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/barcode-scanner/guest-js/index.ts#L45
© 2025 Tauri Contributors. CC-BY / MIT
