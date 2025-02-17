Skip to content
# @tauri-apps/plugin-stronghold
## Classes
### Client
#### Constructors
##### new Client()
```

newClient(path, name): Client

```

###### Parameters
Parameter| Type  
---|---  
`path`| `string`  
`name`| `ClientPath`  
###### Returns
`Client`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L265
#### Properties
Property| Type| Defined in  
---|---|---  
`name`| `ClientPath`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L263  
`path`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L262  
#### Methods
##### getStore()
```

getStore(): Store

```

###### Returns
`Store`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L280
##### getVault()
```

getVault(name): Vault

```

Get a vault by name.
###### Parameters
Parameter| Type| Description  
---|---|---  
`name`| `VaultPath`  
###### Returns
`Vault`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L276
### Location
#### Constructors
##### new Location()
```

newLocation(type, payload): Location

```

###### Parameters
Parameter| Type  
---|---  
`type`| `string`  
`payload`| `Record`<`string`, `unknown`>  
###### Returns
`Location`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L86
#### Properties
Property| Type| Defined in  
---|---|---  
`payload`| `Record`<`string`, `unknown`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L84  
`type`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L83  
#### Methods
##### counter()
```

static counter(vault, counter): Location

```

###### Parameters
Parameter| Type  
---|---  
`vault`| `VaultPath`  
`counter`| `number`  
###### Returns
`Location`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L98
##### generic()
```

static generic(vault, record): Location

```

###### Parameters
Parameter| Type  
---|---  
`vault`| `VaultPath`  
`record`| `RecordPath`  
###### Returns
`Location`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L91
### Store
#### Constructors
##### new Store()
```

newStore(path, client): Store

```

###### Parameters
Parameter| Type  
---|---  
`path`| `string`  
`client`| `ClientPath`  
###### Returns
`Store`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L289
#### Properties
Property| Type| Defined in  
---|---|---  
`client`| `ClientPath`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L287  
`path`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L286  
#### Methods
##### get()
```

get(key): Promise<null| Uint8Array<ArrayBufferLike>>

```

###### Parameters
Parameter| Type  
---|---  
`key`| `StoreKey`  
###### Returns
`Promise`<`null` | `Uint8Array`<`ArrayBufferLike`>>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L294
##### insert()
```

insert(
key,
value,
lifetime?):Promise<void>

```

###### Parameters
Parameter| Type  
---|---  
`key`| `StoreKey`  
`value`| `number`[]  
`lifetime`?| `Duration`  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L302
##### remove()
```

remove(key): Promise<null| Uint8Array<ArrayBufferLike>>

```

###### Parameters
Parameter| Type  
---|---  
`key`| `StoreKey`  
###### Returns
`Promise`<`null` | `Uint8Array`<`ArrayBufferLike`>>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L316
### Stronghold
A representation of an access to a stronghold.
#### Properties
Property| Type| Defined in  
---|---|---  
`path`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L388  
#### Methods
##### createClient()
```

createClient(client): Promise<Client>

```

###### Parameters
Parameter| Type  
---|---  
`client`| `ClientPath`  
###### Returns
`Promise`<`Client`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L428
##### loadClient()
```

loadClient(client): Promise<Client>

```

###### Parameters
Parameter| Type  
---|---  
`client`| `ClientPath`  
###### Returns
`Promise`<`Client`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L421
##### save()
```

save(): Promise<void>

```

Persists the stronghold state to the snapshot.
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L439
##### unload()
```

unload(): Promise<void>

```

Remove this instance from the cache.
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L415
##### load()
```

static load(path, password): Promise<Stronghold>

```

Load the snapshot if it exists (password must match), or start a fresh stronghold instance otherwise.
###### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| -  
`password`| `string`  
###### Returns
`Promise`<`Stronghold`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L405
### Vault
A key-value storage that allows create, update and delete operations. It does not allow reading the data, so one of the procedures must be used to manipulate the stored data, allowing secure storage of secrets.
#### Extends
  * `ProcedureExecutor`


#### Constructors
##### new Vault()
```

newVault(
path,
client,
name): Vault

```

###### Parameters
Parameter| Type  
---|---  
`path`| `string`  
`client`| `ClientPath`  
`name`| `VaultPath`  
###### Returns
`Vault`
###### Overrides
`ProcedureExecutor.constructor`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L340
#### Properties
Property| Type| Description| Inherited from| Defined in  
---|---|---|---|---  
`client`| `ClientPath`| -| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L336  
`name`| `VaultPath`| The vault name.| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L338  
`path`| `string`| The vault path.| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L335  
`procedureArgs`| `Record`<`string`, `unknown`>| -| `ProcedureExecutor.procedureArgs`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L107  
#### Methods
##### deriveSLIP10()
```

deriveSLIP10(
chain,
source,
sourceLocation,
outputLocation): Promise<Uint8Array<ArrayBufferLike>>

```

Derive a SLIP10 private key using a seed or key.
###### Parameters
Parameter| Type| Description  
---|---|---  
`chain`| `number`[]| The chain path.  
`source`| `"Seed"` | `"Key"`| The source type, either ‘Seed’ or ‘Key’.  
`sourceLocation`| `Location`| The source location, must be the `outputLocation` of a previous call to `generateSLIP10Seed` or `deriveSLIP10`.  
`outputLocation`| `Location`| Location of the record where the private key will be stored.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
###### Inherited from
`ProcedureExecutor.deriveSLIP10`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L145
##### generateBIP39()
```

generateBIP39(outputLocation, passphrase?):Promise<Uint8Array<ArrayBufferLike>>

```

Generate a BIP39 seed.
###### Parameters
Parameter| Type| Description  
---|---|---  
`outputLocation`| `Location`| The location of the record where the BIP39 seed will be stored.  
`passphrase`?| `string`| The optional mnemonic passphrase.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
###### Inherited from
`ProcedureExecutor.generateBIP39`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L200
##### generateSLIP10Seed()
```

generateSLIP10Seed(outputLocation, sizeBytes?):Promise<Uint8Array<ArrayBufferLike>>

```

Generate a SLIP10 seed for the given location.
###### Parameters
Parameter| Type| Description  
---|---|---  
`outputLocation`| `Location`| Location of the record where the seed will be stored.  
`sizeBytes`?| `number`| The size in bytes of the SLIP10 seed.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
###### Inherited from
`ProcedureExecutor.generateSLIP10Seed`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L120
##### getEd25519PublicKey()
```

getEd25519PublicKey(privateKeyLocation): Promise<Uint8Array<ArrayBufferLike>>

```

Gets the Ed25519 public key of a SLIP10 private key.
###### Parameters
Parameter| Type| Description  
---|---|---  
`privateKeyLocation`| `Location`| The location of the private key. Must be the `outputLocation` of a previous call to `deriveSLIP10`.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
A promise resolving to the public key hex string.
###### Since
2.0.0
###### Inherited from
`ProcedureExecutor.getEd25519PublicKey`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L223
##### insert()
```

insert(recordPath, secret): Promise<void>

```

Insert a record to this vault.
###### Parameters
Parameter| Type  
---|---  
`recordPath`| `RecordPath`  
`secret`| `number`[]  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L358
##### recoverBIP39()
```

recoverBIP39(
mnemonic,
outputLocation,
passphrase?):Promise<Uint8Array<ArrayBufferLike>>

```

Store a BIP39 mnemonic.
###### Parameters
Parameter| Type| Description  
---|---|---  
`mnemonic`| `string`| The mnemonic string.  
`outputLocation`| `Location`| The location of the record where the BIP39 mnemonic will be stored.  
`passphrase`?| `string`| The optional mnemonic passphrase.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
###### Inherited from
`ProcedureExecutor.recoverBIP39`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L175
##### remove()
```

remove(location): Promise<void>

```

Remove a record from the vault.
###### Parameters
Parameter| Type| Description  
---|---|---  
`location`| `Location`| The record location.  
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L374
##### signEd25519()
```

signEd25519(privateKeyLocation, msg): Promise<Uint8Array<ArrayBufferLike>>

```

Creates a Ed25519 signature from a private key.
###### Parameters
Parameter| Type| Description  
---|---|---  
`privateKeyLocation`| `Location`| The location of the record where the private key is stored. Must be the `outputLocation` of a previous call to `deriveSLIP10`.  
`msg`| `string`| The message to sign.  
###### Returns
`Promise`<`Uint8Array`<`ArrayBufferLike`>>
A promise resolving to the signature hex string.
###### Since
2.0.0
###### Inherited from
`ProcedureExecutor.signEd25519`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L244
## Interfaces
### AddressInfo
#### Properties
Property| Type| Defined in  
---|---|---  
`peers`| `Map`<`string`, `PeerAddress`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L43  
`relays`| `string`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L44  
### ClientAccess
#### Properties
Property| Type| Defined in  
---|---|---  
`cloneVaultDefault?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L52  
`cloneVaultExceptions?`| `Map`<`VaultPath`, `boolean`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L53  
`readStore?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L54  
`useVaultDefault?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L48  
`useVaultExceptions?`| `Map`<`VaultPath`, `boolean`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L49  
`writeStore?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L55  
`writeVaultDefault?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L50  
`writeVaultExceptions?`| `Map`<`VaultPath`, `boolean`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L51  
### ConnectionLimits
#### Properties
Property| Type| Defined in  
---|---|---  
`maxEstablishedIncoming?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L31  
`maxEstablishedOutgoing?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L32  
`maxEstablishedPerPeer?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L33  
`maxEstablishedTotal?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L34  
`maxPendingIncoming?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L29  
`maxPendingOutgoing?`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L30  
### Duration
A duration definition.
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`nanos`| `number`| The fractional part of this Duration, in nanoseconds. Must be greater or equal to 0 and smaller than 1e+9 (the max number of nanoseoncds in a second)| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L79  
`secs`| `number`| The number of whole seconds contained by this Duration.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L77  
### NetworkConfig
#### Properties
Property| Type| Defined in  
---|---|---  
`addresses?`| `AddressInfo`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L69  
`connectionsLimit?`| `ConnectionLimits`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L66  
`connectionTimeout?`| `Duration`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L65  
`enableMdns?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L67  
`enableRelay?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L68  
`peerPermissions?`| `Map`<`string`, `Permissions`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L70  
`permissionsDefault?`| `Permissions`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L71  
`requestTimeout?`| `Duration`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L64  
### PeerAddress
#### Properties
Property| Type| Defined in  
---|---|---  
`known`| `string`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L38  
`use_relay_fallback`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L39  
### Permissions
#### Properties
Property| Type| Defined in  
---|---|---  
`default?`| `ClientAccess`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L59  
`exceptions?`| `Map`<`VaultPath`, `ClientAccess`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L60  
## Type Aliases
### ClientPath
```

type ClientPath: string | Iterable<number> | ArrayLike<number> | ArrayBuffer;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L7
### RecordPath
```

type RecordPath: string | Iterable<number> | ArrayLike<number> | ArrayBuffer;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L17
### StoreKey
```

type StoreKey: string | Iterable<number> | ArrayLike<number> | ArrayBuffer;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L22
### VaultPath
```

type VaultPath: string | Iterable<number> | ArrayLike<number> | ArrayBuffer;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/stronghold/guest-js/index.ts#L12
© 2025 Tauri Contributors. CC-BY / MIT
