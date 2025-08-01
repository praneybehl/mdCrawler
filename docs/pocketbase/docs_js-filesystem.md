Filesystem
PocketBase comes with a thin abstraction between the local filesystem and S3.
To configure which one will be used you can adjust the storage settings from _Dashboard > Settings > Files storage_ section.
The filesystem abstraction can be accessed programmatically via the `$app.newFilesystem()` method.
Below are listed some of the most common operations but you can find more details in the `filesystem.System` interface.
Always make sure to call `close()` at the end for both the created filesystem instance and the retrieved file readers to prevent leaking resources.
###  Reading files 
To retrieve the file content of a single stored file you can use `getReader(key)` . Note that file keys often contain a **prefix** (aka. the "path" to the file). For record files the full key is `collectionId/recordId/filename`. To retrieve multiple files matching a specific _prefix_ you can use `list(prefix)` .
The below code shows a minimal example how to retrieve the content of a single record file as string.
`let record = $app.findAuthRecordByEmail("users", "test@example.com") // construct the full file key by concatenating the record storage path with the specific filename let avatarKey = record.baseFilesPath() + "/" + record.get("avatar") let fsys, reader, content; try { // initialize the filesystem   fsys = $app.newFilesystem(); // retrieve a file reader for the avatar key   reader = fsys.getReader(avatarKey) // copy as plain string   content = toString(reader) } finally {   reader?.close();   fsys?.close(); }`
###  Saving files 
There are several methods to save _(aka. write/upload)_ files depending on the available file content source:
  * `upload(content, key)`
  * `uploadFile(file, key)`
  * `uploadMultipart(mfh, key)`


Most users rarely will have to use the above methods directly because for collection records the file persistence is handled transparently when saving the record model (it will also perform size and MIME type validation based on the collection `file` field options). For example:
`let record = $app.findRecordById("articles", "RECORD_ID") // Other available File factories // - $filesystem.fileFromBytes(content, name) // - $filesystem.fileFromURL(url) // - $filesystem.fileFromMultipart(mfh) let file = $filesystem.fileFromPath("/local/path/to/file") // set new file (can be single or array of File values) // (if the record has an old file it is automatically deleted on successful save) record.set("yourFileField", file) $app.save(record)`
###  Deleting files 
Files can be deleted from the storage filesystem using `delete(key)` .
Similar to the previous section, most users rarely will have to use the `delete` file method directly because for collection records the file deletion is handled transparently when removing the existing filename from the record model (this also ensure that the db entry referencing the file is also removed). For example:
`let record = $app.findRecordById("articles", "RECORD_ID") // if you want to "reset" a file field (aka. deleting the associated single or multiple files) // you can set it to null record.set("yourFileField", null) // OR if you just want to remove individual file(s) from a multiple file field you can use the "-" modifier // (the value could be a single filename string or slice of filename strings) record.set("yourFileField-", "example_52iWbGinWd.txt") $app.save(record)`
Prev: Realtime messaging Next: Logging
