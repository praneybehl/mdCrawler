Collection operations
Collections are usually managed via the Dashboard interface, but there are some situations where you may want to create or edit a collection programmatically (usually as part of a DB migration). You can find all available Collection related operations and methods in `$app` and `Collection` , but below are listed some of the most common ones:
###  Fetch collections 
#####  Fetch single collection 
All single collection retrieval methods throw an error if no collection is found.
`let collection = $app.findCollectionByNameOrId("example")`
#####  Fetch multiple collections 
All multiple collections retrieval methods return an empty array if no collections are found.
`let allCollections = $app.findAllCollections(/* optional types */) // only specific types let authAndViewCollections := $app.findAllCollections("auth", "view")`
#####  Custom collection query 
In addition to the above query helpers, you can also create custom Collection queries using `$app.collectionQuery()` method. It returns a SELECT DB builder that can be used with the same methods described in the Database guide.
`let collections = arrayOf(new Collection) $app.collectionQuery(). andWhere($dbx.hashExp({"viewRule": null})). orderBy("created DESC"). all(collections)`
###  Field definitions 
All collection fields _(with exception of the`JSONField`)_ are non-nullable and uses a zero-default for their respective type as fallback value when missing.
  * `new BoolField({ ... })`
  * `new NumberField({ ... })`
  * `new TextField({ ... })`
  * `new EmailField({ ... })`
  * `new URLField({ ... })`
  * `new EditorField({ ... })`
  * `new DateField({ ... })`
  * `new AutodateField({ ... })`
  * `new SelectField({ ... })`
  * `new FileField({ ... })`
  * `new RelationField({ ... })`
  * `new JSONField({ ... })`
  * `new GeoPointField({ ... })`


###  Create new collection 
`// missing default options, system fields like id, email, etc. are initialized automatically // and will be merged with the provided configuration let collection = new Collection({ type: "base", // base | auth | view name: "example", listRule: null, viewRule: "@request.auth.id != ''", createRule: "", updateRule: "@request.auth.id != ''", deleteRule: null, fields: [ { name: "title", type: "text", required: true, max: 10, }, { name: "user", type: "relation", required: true, maxSelect: 1, collectionId: "ae40239d2bc4477", cascadeDelete: true, }, ], indexes: [ "CREATE UNIQUE INDEX idx_user ON example (user)" ], }) // validate and persist // (use saveNoValidate to skip fields validation) $app.save(collection)`
###  Update existing collection 
`let collection = $app.findCollectionByNameOrId("example") // change the collection name collection.name = "example_update" // add new editor field collection.fields.add(new EditorField({ name: "description", required: true, })) // change existing field // (returns a pointer and direct modifications are allowed without the need of reinsert) let titleField = collection.fields.getByName("title") titleField.min = 10 // or: collection.indexes.push("CREATE INDEX idx_example_title ON example (title)") collection.addIndex("idx_example_title", false, "title", "") // validate and persist // (use saveNoValidate to skip fields validation) $app.save(collection)`
###  Delete collection 
`let collection = $app.findCollectionByNameOrId("example") $app.delete(collection)`
Prev: Record operations Next: Migrations
