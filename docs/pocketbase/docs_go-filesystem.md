Filesystem
PocketBase comes with a thin abstraction between the local filesystem and S3.
To configure which one will be used you can adjust the storage settings from _Dashboard > Settings > Files storage_ section.
The filesystem abstraction can be accessed programmatically via the `app.NewFilesystem()` method.
Below are listed some of the most common operations but you can find more details in the `filesystem` subpackage.
Always make sure to call `Close()` at the end for both the created filesystem instance and the retrieved file readers to prevent leaking resources.
###  Reading files 
To retrieve the file content of a single stored file you can use `GetReader(key)` . Note that file keys often contain a **prefix** (aka. the "path" to the file). For record files the full key is `collectionId/recordId/filename`. To retrieve multiple files matching a specific _prefix_ you can use `List(prefix)` .
The below code shows a minimal example how to retrieve a single record file and copy its content into a `bytes.Buffer`.
`record, err := app.FindAuthRecordByEmail("users", "test@example.com") if err != nil { return err } // construct the full file key by concatenating the record storage path with the specific filename avatarKey := record.BaseFilesPath() + "/" + record.GetString("avatar") // initialize the filesystem fsys, err := app.NewFilesystem() if err != nil { return err } defer fsys.Close() // retrieve a file reader for the avatar key r, err := fsys.GetReader(avatarKey) if err != nil { return err } defer r.Close() // do something with the reader... content := new(bytes.Buffer) _, err = io.Copy(content, r) if err != nil { return err }`
###  Saving files 
There are several methods to save _(aka. write/upload)_ files depending on the available file content source:
  * `Upload([]byte, key)`
  * `UploadFile(*filesystem.File, key)`
  * `UploadMultipart(*multipart.FileHeader, key)`


Most users rarely will have to use the above methods directly because for collection records the file persistence is handled transparently when saving the record model (it will also perform size and MIME type validation based on the collection `file` field options). For example:
`record, err := app.FindRecordById("articles", "RECORD_ID") if err != nil { return err } // Other available File factories // - filesystem.NewFileFromBytes(data, name) // - filesystem.NewFileFromURL(ctx, url) // - filesystem.NewFileFromMultipart(mh) f, err := filesystem.NewFileFromPath("/local/path/to/file") // set new file (can be single *filesytem.File or multiple []*filesystem.File) // (if the record has an old file it is automatically deleted on successful Save) record.Set("yourFileField", f) err = app.Save(record) if err != nil { return err }`
###  Deleting files 
Files can be deleted from the storage filesystem using `Delete(key)` .
Similar to the previous section, most users rarely will have to use the `Delete` file method directly because for collection records the file deletion is handled transparently when removing the existing filename from the record model (this also ensure that the db entry referencing the file is also removed). For example:
`record, err := app.FindRecordById("articles", "RECORD_ID") if err != nil { return err } // if you want to "reset" a file field (aka. deleting the associated single or multiple files) // you can set it to nil record.Set("yourFileField", nil) // OR if you just want to remove individual file(s) from a multiple file field you can use the "-" modifier // (the value could be a single filename string or slice of filename strings) record.Set("yourFileField-", "example_52iWbGinWd.txt") err = app.Save(record) if err != nil { return err }`
Prev: Realtime messaging Next: Logging
