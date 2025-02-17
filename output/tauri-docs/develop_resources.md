Skip to content
# Embedding Additional Files
You may need to include additional files in your application bundle that aren’t part of your frontend (your `frontendDist`) directly or which are too big to be inlined into the binary. We call these files `resources`.
To bundle the files of your choice, you can add the `resources` property to the `bundle` object in your `tauri.conf.json` file.
See more about `tauri.conf.json` configuration here.
`resources` expects a list of strings targeting files or directories either with absolute or relative paths. It supports glob patterns in case you need to include multiple files from a directory.
Here is a sample to illustrate the configuration. This is not a complete `tauri.conf.json` file:
tauri.conf.json```

{
"bundle": {
"resources": [
"/absolute/path/to/textfile.txt",
"relative/path/to/jsonfile.json",
"resources/**/*"
]
}
}

```

Alternatively the `resources` config also accepts a map object if you want to change where the files will be copied to. Here is a sample that shows how to include files from different sources into the same `resources` folder:
tauri.conf.json```

{
"bundle": {
"resources": {
"/absolute/path/to/textfile.txt": "resources/textfile.txt",
"relative/path/to/jsonfile.json": "resources/jsonfile.json",
"resources/**/*": "resources/"
}
}
}

```

## Source path syntax
In the following explanations “target resource directory” is either the value after the colon in the object notation, or a reconstruction of the original file paths in the array notation.
  * `"dir/file.txt"`: copies the `file.txt` file into the target resource directory.
  * `"dir/"`: copies all files **and directories** _recursively_ into the target resource directory. Use this if you also want to preserve the file system structure of your files and directories.
  * `"dir/*"`: copies all files in the `dir` directory _non-recursively_ (sub-directories will be ignored) into the target resource directory.
  * `"dir/**`: throws an error because `**` only matches directories and therefore no files can be found.
  * `"dir/**/*"`: copies all files in the `dir` directory _recursively_ (all files in `dir/` and all files in all sub-directories) into the target resource directory.
  * `"dir/**/**`: throws an error because `**` only matches directories and therefore no files can be found.


## Accessing files in Rust
In this example we want to bundle additional i18n json files that look like this:
de.json```

{
"hello": "Guten Tag!",
"bye": "Auf Wiedersehen!"
}

```

In this case, we store these files in a `lang` directory next to the `tauri.conf.json`. For this we add `"lang/*"` to `resources` as shown above.
On the Rust side, you need an instance of the `PathResolver` which you can get from `App` and `AppHandle`:
```

tauri::Builder::default()
.setup(|app| {
// The path specified must follow the same syntax as defined in
// `tauri.conf.json > bundle > resources`
letresource_path=app.path().resolve("lang/de.json", BaseDirectory::Resource)?;
letfile= std::fs::File::open(&resource_path).unwrap();
letlang_de: serde_json::Value = serde_json::from_reader(file).unwrap();
// This will print 'Guten Tag!' to the terminal
println!("{}", lang_de.get("hello").unwrap());
Ok(())
})

```

```

#[tauri::command]
fnhello(handle: tauri::AppHandle) -> String {
letresource_path=handle.path().resolve("lang/de.json", BaseDirectory::Resource)?;
letfile= std::fs::File::open(&resource_path).unwrap();
letlang_de: serde_json::Value = serde_json::from_reader(file).unwrap();
lang_de.get("hello").unwrap()
}

```

## Accessing files in JavaScript
This is based on the example above.
Note that you must configure the access control list to enable any `plugin-fs` APIs you will need as well as permissions to access the `$RESOURCE` folder:
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": [
"path:default",
"event:default",
"window:default",
"app:default",
"resources:default",
"menu:default",
"tray:default",
"fs:allow-read-text-file",
"fs:allow-resource-read-recursive"
]
}

```

```

import { resolveResource } from'@tauri-apps/api/path';
import { readTextFile } from'@tauri-apps/plugin-fs';
const resourcePath = await resolveResource('lang/de.json');
const langDe = JSON.parse(await readTextFile(resourcePath));
console.log(langDe.hello); // This will print 'Guten Tag!' to the devtools console

```

© 2025 Tauri Contributors. CC-BY / MIT
