Skip to content
# @tauri-apps/plugin-clipboard-manager
Read and write to the system clipboard.
## Functions
### clear()
```

functionclear():Promise<void>

```

Clears the clipboard.
#### Platform-specific
  * **Android:** Only supported on SDK 28+. For older releases we write an empty string to the clipboard instead.


#### Returns
`Promise`<`void`>
#### Example
```

import { clear } from'@tauri-apps/plugin-clipboard-manager';
awaitclear();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L147
### readImage()
```

functionreadImage():Promise<Image>

```

Gets the clipboard content as Uint8Array image.
#### Platform-specific
  * **Android / iOS:** Not supported.


#### Returns
`Promise`<`Image`>
#### Example
```

import { readImage } from'@tauri-apps/plugin-clipboard-manager';
const clipboardImage = await readImage();
const blob = newBlob([await clipboardImage.rbga()], { type: 'image' })
const url = URL.createObjectURL(blob)

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L99
### readText()
```

functionreadText():Promise<string>

```

Gets the clipboard content as plain text.
#### Returns
`Promise`<`string`>
#### Example
```

import { readText } from'@tauri-apps/plugin-clipboard-manager';
const clipboardText = await readText();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L46
### writeHtml()
```

functionwriteHtml(html, altText?):Promise<void>

```

  * Writes HTML or fallbacks to write provided plain text to the clipboard.


#### Platform-specific
  * **Android / iOS:** Not supported.


#### Parameters
Parameter| Type  
---|---  
`html`| `string`  
`altText`?| `string`  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { writeHtml } from'@tauri-apps/plugin-clipboard-manager';
awaitwriteHtml('<h1>Tauri is awesome!</h1>', 'plaintext');
// The following will write "<h1>Tauri is awesome</h1>" as plain text
awaitwriteHtml('<h1>Tauri is awesome!</h1>', '<h1>Tauri is awesome</h1>');
// we can read html data only as a string so there's just readText(), no readHtml()
assert(awaitreadText(), '<h1>Tauri is awesome!</h1>');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L126
### writeImage()
```

functionwriteImage(image):Promise<void>

```

Writes image buffer to the clipboard.
#### Platform-specific
  * **Android / iOS:** Not supported.


#### Parameters
Parameter| Type  
---|---  
`image`| | `string` | `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`> | `Image`  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { writeImage } from'@tauri-apps/plugin-clipboard-manager';
const buffer = [
// A red pixel
255, 0, 0, 255,
// A green pixel
0, 255, 0, 255,
];
awaitwriteImage(buffer);

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L74
### writeText()
```

functionwriteText(text, opts?):Promise<void>

```

Writes plain text to the clipboard.
#### Parameters
Parameter| Type  
---|---  
`text`| `string`  
`opts`?| `object`  
`opts.label`?| `string`  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { writeText, readText } from'@tauri-apps/plugin-clipboard-manager';
awaitwriteText('Tauri is awesome!');
assert(awaitreadText(), 'Tauri is awesome!');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/clipboard-manager/guest-js/index.ts#L27
© 2025 Tauri Contributors. CC-BY / MIT
