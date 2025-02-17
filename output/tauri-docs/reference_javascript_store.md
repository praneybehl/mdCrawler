Skip to content
# @tauri-apps/plugin-store
## Classes
### LazyStore
A lazy loaded key-value store persisted by the backend layer.
#### Implements
  * `IStore`


#### Constructors
##### new LazyStore()
```

newLazyStore(path, options?): LazyStore

```

Note that the options are not applied if someone else already created the store
###### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| Path to save the store in `app_data_dir`  
`options`?| `StoreOptions`| Store configuration options  
###### Returns
`LazyStore`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L96
#### Methods
##### clear()
```

clear(): Promise<void>

```

Clears the store, removing all key-value pairs.
Note: To clear the storage and reset it to its `default` value, use `reset` instead.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.clear`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L124
##### close()
```

close(): Promise<void>

```

Close the store and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.close`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L169
##### delete()
```

delete(key): Promise<boolean>

```

Removes a key-value pair from the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`boolean`>
###### Implementation of
`IStore.delete`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L120
##### entries()
```

entries<T>(): Promise<[string, T][]>

```

Returns a list of all entries in the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Returns
`Promise`<[`string`, `T`][]>
###### Implementation of
`IStore.entries`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L140
##### get()
```

get<T>(key): Promise<undefined|T>

```

Returns the value for the given `key` or `undefined` if the key does not exist.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`undefined` | `T`>
###### Implementation of
`IStore.get`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L112
##### has()
```

has(key): Promise<boolean>

```

Returns `true` if the given `key` exists in the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`boolean`>
###### Implementation of
`IStore.has`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L116
##### init()
```

init(): Promise<void>

```

Init/load the store if it’s not loaded already
###### Returns
`Promise`<`void`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L104
##### keys()
```

keys(): Promise<string[]>

```

Returns a list of all keys in the store.
###### Returns
`Promise`<`string`[]>
###### Implementation of
`IStore.keys`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L132
##### length()
```

length(): Promise<number>

```

Returns the number of key-value pairs in the store.
###### Returns
`Promise`<`number`>
###### Implementation of
`IStore.length`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L144
##### onChange()
```

onChange<T>(cb): Promise<UnlistenFn>

```

Listen to changes on the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`cb`| (`key`, `value`) => `void`  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event.
###### Since
2.0.0
###### Implementation of
`IStore.onChange`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L163
##### onKeyChange()
```

onKeyChange<T>(key, cb): Promise<UnlistenFn>

```

Listen to changes on a store key.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
`cb`| (`value`) => `void`  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event.
###### Since
2.0.0
###### Implementation of
`IStore.onKeyChange`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L156
##### reload()
```

reload(): Promise<void>

```

Attempts to load the on-disk state at the store’s `path` into memory.
This method is useful if the on-disk state was edited by the user and you want to synchronize the changes.
Note: This method does not emit change events.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.reload`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L148
##### reset()
```

reset(): Promise<void>

```

Resets the store to its `default` value.
If no default value has been set, this method behaves identical to `clear`.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.reset`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L128
##### save()
```

save(): Promise<void>

```

Saves the store to disk at the store’s `path`.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.save`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L152
##### set()
```

set(key, value): Promise<void>

```

Inserts a key-value pair into the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
`value`| `unknown`  
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.set`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L108
##### values()
```

values<T>(): Promise<T[]>

```

Returns a list of all values in the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Returns
`Promise`<`T`[]>
###### Implementation of
`IStore.values`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L136
### Store
A key-value store persisted by the backend layer.
#### Extends
  * `Resource`


#### Implements
  * `IStore`


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
##### clear()
```

clear(): Promise<void>

```

Clears the store, removing all key-value pairs.
Note: To clear the storage and reset it to its `default` value, use `reset` instead.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.clear`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L259
##### close()
```

close(): Promise<void>

```

Destroys and cleans up this resource from memory. **You should not call any method on this object anymore and should drop any reference to it.**
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.close`
###### Inherited from
`Resource.close`
**Source** : undefined
##### delete()
```

delete(key): Promise<boolean>

```

Removes a key-value pair from the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`boolean`>
###### Implementation of
`IStore.delete`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L252
##### entries()
```

entries<T>(): Promise<[string, T][]>

```

Returns a list of all entries in the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Returns
`Promise`<[`string`, `T`][]>
###### Implementation of
`IStore.entries`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L275
##### get()
```

get<T>(key): Promise<undefined|T>

```

Returns the value for the given `key` or `undefined` if the key does not exist.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`undefined` | `T`>
###### Implementation of
`IStore.get`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L237
##### has()
```

has(key): Promise<boolean>

```

Returns `true` if the given `key` exists in the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
###### Returns
`Promise`<`boolean`>
###### Implementation of
`IStore.has`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L245
##### keys()
```

keys(): Promise<string[]>

```

Returns a list of all keys in the store.
###### Returns
`Promise`<`string`[]>
###### Implementation of
`IStore.keys`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L267
##### length()
```

length(): Promise<number>

```

Returns the number of key-value pairs in the store.
###### Returns
`Promise`<`number`>
###### Implementation of
`IStore.length`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L279
##### onChange()
```

onChange<T>(cb): Promise<UnlistenFn>

```

Listen to changes on the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`cb`| (`key`, `value`) => `void`  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event.
###### Since
2.0.0
###### Implementation of
`IStore.onChange`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L302
##### onKeyChange()
```

onKeyChange<T>(key, cb): Promise<UnlistenFn>

```

Listen to changes on a store key.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
`cb`| (`value`) => `void`  
###### Returns
`Promise`<`UnlistenFn`>
A promise resolving to a function to unlisten to the event.
###### Since
2.0.0
###### Implementation of
`IStore.onKeyChange`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L291
##### reload()
```

reload(): Promise<void>

```

Attempts to load the on-disk state at the store’s `path` into memory.
This method is useful if the on-disk state was edited by the user and you want to synchronize the changes.
Note: This method does not emit change events.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.reload`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L283
##### reset()
```

reset(): Promise<void>

```

Resets the store to its `default` value.
If no default value has been set, this method behaves identical to `clear`.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.reset`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L263
##### save()
```

save(): Promise<void>

```

Saves the store to disk at the store’s `path`.
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.save`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L287
##### set()
```

set(key, value): Promise<void>

```

Inserts a key-value pair into the store.
###### Parameters
Parameter| Type| Description  
---|---|---  
`key`| `string`  
`value`| `unknown`  
###### Returns
`Promise`<`void`>
###### Implementation of
`IStore.set`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L229
##### values()
```

values<T>(): Promise<T[]>

```

Returns a list of all values in the store.
###### Type Parameters
Type Parameter  
---  
`T`  
###### Returns
`Promise`<`T`[]>
###### Implementation of
`IStore.values`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L271
##### get()
```

static get(path): Promise<null| Store>

```

Gets an already loaded store.
If the store is not loaded, returns `null`. In this case you must load it.
This function is more useful when you already know the store is loaded and just need to access its instance. Prefer Store.load otherwise.
###### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| Path of the store.  
###### Returns
`Promise`<`null` | `Store`>
###### Example
```

import { Store } from'@tauri-apps/api/store';
let store = await Store.get('store.json');
if (!store) {
store =await Store.load('store.json');
}

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L223
##### load()
```

static load(path, options?):Promise<Store>

```

Create a new Store or load the existing store with the path.
###### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| Path to save the store in `app_data_dir`  
`options`?| `StoreOptions`| Store configuration options  
###### Returns
`Promise`<`Store`>
###### Example
```

import { Store } from'@tauri-apps/api/store';
const store = await Store.load('store.json');

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L196
## Type Aliases
### StoreOptions
```

type StoreOptions: object;

```

Options to create a store
#### Type declaration
Name| Type| Description| Defined in  
---|---|---|---  
`autoSave`?| `boolean` | `number`| Auto save on modification with debounce duration in milliseconds, it’s 100ms by default, pass in `false` to disable it| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L24  
`createNew`?| `boolean`| Force create a new store with default values even if it already exists.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L36  
`deserializeFnName`?| `string`| Name of a deserialize function registered in the rust side plugin builder| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L32  
`serializeFnName`?| `string`| Name of a serialize function registered in the rust side plugin builder| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L28  
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L20
## Functions
### getStore()
```

functiongetStore(path):Promise<Store|null>

```

Gets an already loaded store.
If the store is not loaded, returns `null`. In this case you must load it.
This function is more useful when you already know the store is loaded and just need to access its instance. Prefer Store.load otherwise.
#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| Path of the store.  
#### Returns
`Promise`<`Store` | `null`>
#### Example
```

import { getStore } from'@tauri-apps/api/store';
const store = await getStore('store.json');

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L74
### load()
```

functionload(path, options?):Promise<Store>

```

Create a new Store or load the existing store with the path.
#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| Path to save the store in `app_data_dir`  
`options`?| `StoreOptions`| Store configuration options  
#### Returns
`Promise`<`Store`>
#### Example
```

import { Store } from'@tauri-apps/api/store';
const store = await Store.load('store.json');

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/store/guest-js/index.ts#L51
© 2025 Tauri Contributors. CC-BY / MIT
