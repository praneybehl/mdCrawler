Skip to content
# @tauri-apps/plugin-shell
Access the system shell. Allows you to spawn child processes and manage files and URLs using their default application.
## Security
This API has a scope configuration that forces you to restrict the programs and arguments that can be used.
### Restricting access to the `open` API
On the configuration object, `open: true` means that the open API can be used with any URL, as the argument is validated with the `^((mailto:\w+)|(tel:\w+)|(https?://\w+)).+` regex. You can change that regex by changing the boolean value to a string, e.g. `open: ^https://github.com/`.
### Restricting access to the `Command` APIs
The plugin permissions object has a `scope` field that defines an array of CLIs that can be used. Each CLI is a configuration object `{ name: string, cmd: string, sidecar?: bool, args?: boolean | Arg[] }`.
  * `name`: the unique identifier of the command, passed to the Command.create function. If it’s a sidecar, this must be the value defined on `tauri.conf.json > bundle > externalBin`.
  * `cmd`: the program that is executed on this configuration. If it’s a sidecar, this value is ignored.
  * `sidecar`: whether the object configures a sidecar or a system program.
  * `args`: the arguments that can be passed to the program. By default no arguments are allowed. 
    * `true` means that any argument list is allowed.
    * `false` means that no arguments are allowed.
    * otherwise an array can be configured. Each item is either a string representing the fixed argument value or a `{ validator: string }` that defines a regex validating the argument value.


#### Example scope configuration
CLI: `git commit -m "the commit message"`
Capability:
```

{
"permissions": [
{
"identifier": "shell:allow-execute",
"allow": [
{
"name": "run-git-commit",
"cmd": "git",
"args": ["commit", "-m", { "validator": "\\S+" }]
}
]
}
]
}

```

Usage:
```

import { Command } from'@tauri-apps/plugin-shell'
Command.create('run-git-commit', ['commit', '-m', 'the commit message'])

```

Trying to execute any API with a program not configured on the scope results in a promise rejection due to denied access.
## Classes
### Child
#### Since
2.0.0
#### Constructors
##### new Child()
```

newChild(pid): Child

```

###### Parameters
Parameter| Type  
---|---  
`pid`| `number`  
###### Returns
`Child`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L301
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`pid`| `number`| The child process `pid`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L299  
#### Methods
##### kill()
```

kill(): Promise<void>

```

Kills the child process.
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L336
##### write()
```

write(data): Promise<void>

```

Writes `data` to the `stdin`.
###### Parameters
Parameter| Type| Description  
---|---|---  
`data`| `IOPayload` | `number`[]| The message to write, either a string or a byte array.  
###### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('node');
const child = await command.spawn();
await child.write('message');
await child.write([0, 1, 2, 3, 4, 5]);

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L322
### Command<O>
The entry point for spawning child processes. It emits the `close` and `error` events.
#### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('node');
command.on('close', data=> {
console.log(`command finished with code ${data.code} and signal ${data.signal}`)
});
command.on('error', error=> console.error(`command error: "${error}"`));
command.stdout.on('data', line=> console.log(`command stdout: "${line}"`));
command.stderr.on('data', line=> console.log(`command stderr: "${line}"`));
const child = await command.spawn();
console.log('pid:', child.pid);

```

#### Since
2.0.0
#### Extends
  * `EventEmitter`<`CommandEvents`>


#### Type Parameters
Type Parameter  
---  
`O` _extends_ `IOPayload`  
#### Properties
Property| Modifier| Type| Description| Defined in  
---|---|---|---|---  
`stderr`| `readonly`| `EventEmitter`<`OutputEvents`<`O`>>| Event emitter for the `stderr`. Emits the `data` event.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L384  
`stdout`| `readonly`| `EventEmitter`<`OutputEvents`<`O`>>| Event emitter for the `stdout`. Emits the `data` event.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L382  
#### Methods
##### addListener()
```

addListener<N>(eventName, listener): this

```

Alias for `emitter.on(eventName, listener)`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`addListener`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L118
##### execute()
```

execute(): Promise<ChildProcess<O>>

```

Executes the command as a child process, waiting for it to finish and collecting all of its output.
###### Returns
`Promise`<`ChildProcess`<`O`>>
A promise resolving to the child process output.
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const output = await Command.create('echo', 'message').execute();
assert(output.code===0);
assert(output.signal===null);
assert(output.stdout==='message');
assert(output.stderr==='');

```

###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L530
##### listenerCount()
```

listenerCount<N>(eventName): number

```

Returns the number of listeners listening to the event named `eventName`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
###### Returns
`number`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`listenerCount`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L241
##### off()
```

off<N>(eventName, listener): this

```

Removes the all specified listener from the listener array for the event eventName Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`off`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L186
##### on()
```

on<N>(eventName, listener): this

```

Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName`and `listener` will result in the `listener` being added, and called, multiple times.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`on`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L147
##### once()
```

once<N>(eventName, listener): this

```

Adds a **one-time**`listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`once`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L169
##### prependListener()
```

prependListener<N>(eventName, listener): this

```

Adds the `listener` function to the _beginning_ of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName`and `listener` will result in the `listener` being added, and called, multiple times.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`prependListener`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L258
##### prependOnceListener()
```

prependOnceListener<N>(eventName, listener): this

```

Adds a **one-time**`listener` function for the event named `eventName` to the_beginning_ of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`prependOnceListener`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L280
##### removeAllListeners()
```

removeAllListeners<N>(event?):this

```

Removes all listeners, or those of the specified eventName.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`event`?| `N`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`removeAllListeners`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L206
##### removeListener()
```

removeListener<N>(eventName, listener): this

```

Alias for `emitter.off(eventName, listener)`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ keyof `CommandEvents`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
###### Inherited from
`EventEmitter`.`removeListener`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L130
##### spawn()
```

spawn(): Promise<Child>

```

Executes the command as a child process, returning a handle to it.
###### Returns
`Promise`<`Child`>
A promise resolving to the child process handle.
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L479
##### create()
Creates a command to execute the given program.
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('my-app', ['run', 'tauri']);
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
###### create(program, args)
```

static create(program, args?): Command<string>

```

Creates a command to execute the given program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
###### Returns
`Command`<`string`>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('my-app', ['run', 'tauri']);
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L406
###### create(program, args, options)
```

static create(
program,
args?,
options?): Command<Uint8Array<ArrayBufferLike>>

```

Creates a command to execute the given program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
`options`?| `SpawnOptions` & `object`  
###### Returns
`Command`<`Uint8Array`<`ArrayBufferLike`>>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('my-app', ['run', 'tauri']);
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L407
###### create(program, args, options)
```

static create(
program,
args?,
options?): Command<string>

```

Creates a command to execute the given program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
`options`?| `SpawnOptions`  
###### Returns
`Command`<`string`>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.create('my-app', ['run', 'tauri']);
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L412
##### sidecar()
Creates a command to execute the given sidecar program.
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.sidecar('my-sidecar');
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
###### sidecar(program, args)
```

static sidecar(program, args?): Command<string>

```

Creates a command to execute the given sidecar program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
###### Returns
`Command`<`string`>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.sidecar('my-sidecar');
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L438
###### sidecar(program, args, options)
```

static sidecar(
program,
args?,
options?): Command<Uint8Array<ArrayBufferLike>>

```

Creates a command to execute the given sidecar program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
`options`?| `SpawnOptions` & `object`  
###### Returns
`Command`<`Uint8Array`<`ArrayBufferLike`>>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.sidecar('my-sidecar');
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L439
###### sidecar(program, args, options)
```

static sidecar(
program,
args?,
options?): Command<string>

```

Creates a command to execute the given sidecar program.
###### Parameters
Parameter| Type  
---|---  
`program`| `string`  
`args`?| `string` | `string`[]  
`options`?| `SpawnOptions`  
###### Returns
`Command`<`string`>
###### Example
```

import { Command } from'@tauri-apps/plugin-shell';
const command = Command.sidecar('my-sidecar');
const output = await command.execute();

```

###### Param
The program to execute. It must be configured on `tauri.conf.json > plugins > shell > scope`.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L444
### EventEmitter<E>
#### Since
2.0.0
#### Extended by
  * `Command`


#### Type Parameters
Type Parameter  
---  
`E` _extends_ `Record`<`string`, `any`>  
#### Constructors
##### new EventEmitter()
```

newEventEmitter<E>(): EventEmitter<E>

```

###### Returns
`EventEmitter`<`E`>
#### Methods
##### addListener()
```

addListener<N>(eventName, listener): this

```

Alias for `emitter.on(eventName, listener)`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L118
##### listenerCount()
```

listenerCount<N>(eventName): number

```

Returns the number of listeners listening to the event named `eventName`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
###### Returns
`number`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L241
##### off()
```

off<N>(eventName, listener): this

```

Removes the all specified listener from the listener array for the event eventName Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L186
##### on()
```

on<N>(eventName, listener): this

```

Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName`and `listener` will result in the `listener` being added, and called, multiple times.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L147
##### once()
```

once<N>(eventName, listener): this

```

Adds a **one-time**`listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L169
##### prependListener()
```

prependListener<N>(eventName, listener): this

```

Adds the `listener` function to the _beginning_ of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName`and `listener` will result in the `listener` being added, and called, multiple times.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L258
##### prependOnceListener()
```

prependOnceListener<N>(eventName, listener): this

```

Adds a **one-time**`listener` function for the event named `eventName` to the_beginning_ of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L280
##### removeAllListeners()
```

removeAllListeners<N>(event?):this

```

Removes all listeners, or those of the specified eventName.
Returns a reference to the `EventEmitter`, so that calls can be chained.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`event`?| `N`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L206
##### removeListener()
```

removeListener<N>(eventName, listener): this

```

Alias for `emitter.off(eventName, listener)`.
###### Type Parameters
Type Parameter  
---  
`N` _extends_ `string` | `number` | `symbol`  
###### Parameters
Parameter| Type  
---|---  
`eventName`| `N`  
`listener`| (`arg`) => `void`  
###### Returns
`this`
###### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L130
## Interfaces
### ChildProcess<O>
#### Since
2.0.0
#### Type Parameters
Type Parameter  
---  
`O` _extends_ `IOPayload`  
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`code`| `null` | `number`| Exit code of the process. `null` if the process was terminated by a signal on Unix.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L94  
`signal`| `null` | `number`| If the process was terminated by a signal, represents that signal.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L96  
`stderr`| `O`| The data that the process wrote to `stderr`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L100  
`stdout`| `O`| The data that the process wrote to `stdout`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L98  
### CommandEvents
#### Properties
Property| Type| Defined in  
---|---|---  
`close`| `TerminatedPayload`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L345  
`error`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L346  
### OutputEvents<O>
#### Type Parameters
Type Parameter  
---  
`O` _extends_ `IOPayload`  
#### Properties
Property| Type| Defined in  
---|---|---  
`data`| `O`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L350  
### SpawnOptions
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`cwd?`| `string`| Current working directory.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L73  
`encoding?`| `string`| Character encoding for stdout/stderr **Since** 2.0.0| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L81  
`env?`| `Record`<`string`, `string`>| Environment variables. set to `null` to clear the process env.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L75  
### TerminatedPayload
Payload for the `Terminated` command event.
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`code`| `null` | `number`| Exit code of the process. `null` if the process was terminated by a signal on Unix.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L560  
`signal`| `null` | `number`| If the process was terminated by a signal, represents that signal.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L562  
## Type Aliases
### IOPayload
```

type IOPayload: string | Uint8Array;

```

Event payload type
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L566
## Functions
### open()
```

functionopen(path, openWith?):Promise<void>

```

Opens a path or URL with the system’s default app, or the one specified with `openWith`.
The `openWith` value must be one of `firefox`, `google chrome`, `chromium` `safari`, `open`, `start`, `xdg-open`, `gio`, `gnome-open`, `kde-open` or `wslview`.
#### Parameters
Parameter| Type| Description  
---|---|---  
`path`| `string`| The path or URL to open. This value is matched against the string regex defined on `tauri.conf.json > plugins > shell > open`, which defaults to `^((mailto:\w+)  
`openWith`?| `string`| The app to open the file or URL with. Defaults to the system default application for the specified path type.  
#### Returns
`Promise`<`void`>
#### Example
```

import { open } from'@tauri-apps/plugin-shell';
// opens the given URL on the default browser:
awaitopen('https://github.com/tauri-apps/tauri');
// opens the given URL using `firefox`:
awaitopen('https://github.com/tauri-apps/tauri', 'firefox');
// opens a file using the default program:
awaitopen('/path/to/file');

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/shell/guest-js/index.ts#L601
© 2025 Tauri Contributors. CC-BY / MIT
