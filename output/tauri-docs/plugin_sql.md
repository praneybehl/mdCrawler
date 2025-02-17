Skip to content
# SQL
GitHub npm  crates.io 
API Reference 
Plugin providing an interface for the frontend to communicate with SQL databases through sqlx. It supports the SQLite, MySQL and PostgreSQL drivers, enabled by a Cargo feature.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the SQL plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriaddsql

```

```

yarnruntauriaddsql

```

```

pnpmtauriaddsql

```

```

denotasktauriaddsql

```

```

buntauriaddsql

```

```

cargotauriaddsql

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-sql

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_sql::Builder::default().build())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-sql

```

```

yarnadd@tauri-apps/plugin-sql

```

```

pnpmadd@tauri-apps/plugin-sql

```

```

denoaddnpm:@tauri-apps/plugin-sql

```

```

bunadd@tauri-apps/plugin-sql

```



After installing the plugin, you must select the supported database engine. The available engines are Sqlite, MySQL and PostgreSQL. Run the following command in the `src-tauri` folder to enable your preferred engine:
  * SQLite 
  * MySQL 
  * PostgreSQL 


```

cargoaddtauri-plugin-sql--featuressqlite

```

```

cargoaddtauri-plugin-sql--featuresmysql

```

```

cargoaddtauri-plugin-sql--featurespostgres

```

## Usage
All the plugin’s APIs are available through the JavaScript guest bindings:
  * SQLite 
  * MySQL 
  * PostgreSQL 


The path is relative to `tauri::api::path::BaseDirectory::AppConfig`.
```

import Database from'@tauri-apps/plugin-sql';
// when using `"withGlobalTauri": true`, you may use
// const Database = window.__TAURI__.sql;
const db = await Database.load('sqlite:test.db');
awaitdb.execute('INSERT INTO ...');

```

```

import Database from'@tauri-apps/plugin-sql';
// when using `"withGlobalTauri": true`, you may use
// const Database = window.__TAURI__.sql;
const db = await Database.load('mysql://user:password@host/test');
awaitdb.execute('INSERT INTO ...');

```

```

import Database from'@tauri-apps/plugin-sql';
// when using `"withGlobalTauri": true`, you may use
// const Database = window.__TAURI__.sql;
const db = await Database.load('postgres://user:password@host/test');
awaitdb.execute('INSERT INTO ...');

```

## Syntax
We use sqlx as the underlying library and adopt their query syntax.
  * SQLite 
  * MySQL 
  * PostgreSQL 


Use the ”$#” syntax when substituting query data
```

const result = await db.execute(
"INSERT into todos (id, title, status) VALUES ($1, $2, $3)",
[todos.id, todos.title, todos.status],
);
const result = await db.execute(
"UPDATE todos SET title = $1, status = $2 WHERE id = $3",
[todos.title, todos.status, todos.id],
);

```

Use ”?” when substituting query data
```

const result = await db.execute(
"INSERT into todos (id, title, status) VALUES (?, ?, ?)",
[todos.id, todos.title, todos.status],
);
const result = await db.execute(
"UPDATE todos SET title = ?, status = ? WHERE id = ?",
[todos.title, todos.status, todos.id],
);

```

Use the ”$#” syntax when substituting query data
```

const result = await db.execute(
"INSERT into todos (id, title, status) VALUES ($1, $2, $3)",
[todos.id, todos.title, todos.status],
);
const result = await db.execute(
"UPDATE todos SET title = $1, status = $2 WHERE id = $3",
[todos.title, todos.status, todos.id],
);

```

## Migrations
This plugin supports database migrations, allowing you to manage database schema evolution over time.
### Defining Migrations
Migrations are defined in Rust using the `Migration` struct. Each migration should include a unique version number, a description, the SQL to be executed, and the type of migration (Up or Down).
Example of a migration:
```

use tauri_plugin_sql::{Migration, MigrationKind};
letmigration= Migration {
version:1,
description:"create_initial_tables",
sql:"CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);",
kind: MigrationKind::Up,
};

```

### Adding Migrations to the Plugin Builder
Migrations are registered with the `Builder` struct provided by the plugin. Use the `add_migrations` method to add your migrations to the plugin for a specific database connection.
Example of adding migrations:
src-tauri/src/main.rs```

use tauri_plugin_sql::{Builder, Migration, MigrationKind};
fnmain() {
letmigrations=vec![
// Define your migrations here
Migration {
version:1,
description:"create_initial_tables",
sql:"CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);",
kind: MigrationKind::Up,
}
];
tauri::Builder::default()
.plugin(
tauri_plugin_sql::Builder::default()
.add_migrations("sqlite:mydatabase.db", migrations)
.build(),
)
...
}

```

### Applying Migrations
To apply the migrations when the plugin is initialized, add the connection string to the `tauri.conf.json` file:
src-tauri/tauri.conf.json```

{
"plugins": {
"sql": {
"preload": ["sqlite:mydatabase.db"]
}
}
}

```

Alternatively, the client side `load()` also runs the migrations for a given connection string:
```

import Database from'@tauri-apps/plugin-sql';
const db = await Database.load('sqlite:mydatabase.db');

```

Ensure that the migrations are defined in the correct order and are safe to run multiple times.
### Migration Management
  * **Version Control** : Each migration must have a unique version number. This is crucial for ensuring the migrations are applied in the correct order.
  * **Idempotency** : Write migrations in a way that they can be safely re-run without causing errors or unintended consequences.
  * **Testing** : Thoroughly test migrations to ensure they work as expected and do not compromise the integrity of your database.


## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"sql:default",
"sql:allow-execute",
]
}

```

## Default Permission
### Default Permissions
This permission set configures what kind of database operations are available from the sql plugin.
### Granted Permissions
All reading related operations are enabled. Also allows to load or close a connection.
  * `allow-close`
  * `allow-load`
  * `allow-select`


## Permission Table
Identifier | Description  
---|---  
`sql:allow-close` |  Enables the close command without any pre-configured scope.  
`sql:deny-close` |  Denies the close command without any pre-configured scope.  
`sql:allow-execute` |  Enables the execute command without any pre-configured scope.  
`sql:deny-execute` |  Denies the execute command without any pre-configured scope.  
`sql:allow-load` |  Enables the load command without any pre-configured scope.  
`sql:deny-load` |  Denies the load command without any pre-configured scope.  
`sql:allow-select` |  Enables the select command without any pre-configured scope.  
`sql:deny-select` |  Denies the select command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
