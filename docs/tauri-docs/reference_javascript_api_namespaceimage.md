Skip to content
# image
## Classes
### Image
An RGBA Image in row-major order from top to bottom.
#### Extends
  * `Resource`


#### Accessors
##### rid
###### Get Signature
```

get rid(): number

```

###### Returns
`number`
###### Inherited from
`Resource`.`rid`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L286
#### Methods
##### close()
```

close(): Promise<void>

```

Destroys and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
###### Inherited from
`Resource`.`close`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/core.ts#L298
##### rgba()
```

rgba(): Promise<Uint8Array<ArrayBufferLike>>

```

Returns the RGBA data for this image, in row-major order from top to bottom.
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L79
##### size()
```

size(): Promise<ImageSize>

```

Returns the size of this image.
###### Returns
`Promise`<`ImageSize`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L86
##### fromBytes()
```

static fromBytes(bytes): Promise<Image>

```

Creates a new image using the provided bytes by inferring the file format. If the format is known, prefer [@link Image.fromPngBytes] or [@link Image.fromIcoBytes].
Only `ico` and `png` are supported (based on activated feature flag).
Note that you need the `image-ico` or `image-png` Cargo features to use this API. To enable it, change your Cargo.toml file:
```

[dependencies]
tauri = { version = "...", features = ["...", "image-png"] }

```

###### Parameters
Parameter| Type  
---|---  
`bytes`| `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`>  
###### Returns
`Promise`<`Image`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L52
##### fromPath()
```

static fromPath(path): Promise<Image>

```

Creates a new image using the provided path.
Only `ico` and `png` are supported (based on activated feature flag).
Note that you need the `image-ico` or `image-png` Cargo features to use this API. To enable it, change your Cargo.toml file:
```

[dependencies]
tauri = { version = "...", features = ["...", "image-png"] }

```

###### Parameters
Parameter| Type  
---|---  
`path`| `string`  
###### Returns
`Promise`<`Image`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L72
##### new()
```

static new(
rgba,
width,
height): Promise<Image>

```

Creates a new Image using RGBA data, in row-major order from top to bottom, and with specified width and height.
###### Parameters
Parameter| Type  
---|---  
`rgba`| `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`>  
`width`| `number`  
`height`| `number`  
###### Returns
`Promise`<`Image`>
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L27
## Interfaces
### ImageSize
#### Properties
Property| Type| Defined in  
---|---|---  
`height`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L12  
`width`| `number`| **Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L10  
## Functions
### transformImage()
```

functiontransformImage<T>(image):T

```

Transforms image from various types into a type acceptable by Rust.
See tauri::image::JsImage for more information. Note the API signature is not stable and might change.
#### Type Parameters
Type Parameter  
---  
`T`  
#### Parameters
Parameter| Type  
---|---  
`image`| | `null` | `string` | `number`[] | `ArrayBuffer` | `Uint8Array`<`ArrayBufferLike`> | `Image`  
#### Returns
`T`
**Source** : https://github.com/tauri-apps/tauri/blob/dev/packages/api/src/image.ts#L97
© 2025 Tauri Contributors. CC-BY / MIT
