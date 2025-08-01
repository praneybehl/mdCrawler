Logging
`$app.logger()` could be used to writes any logs into the database so that they can be later explored from the PocketBase _Dashboard > Logs_ section.
For better performance and to minimize blocking on hot paths, logs are written with debounce and on batches:
  * 3 seconds after the last debounced log write
  * when the batch threshold is reached (currently 200)
  * right before app termination to attempt saving everything from the existing logs queue


###  Logger methods 
All standard `slog.Logger` methods are available but below is a list with some of the most notable ones. Note that attributes are represented as key-value pair arguments.
#####  debug(message, attrs...) 
`$app.logger().debug("Debug message!") $app.logger().debug( "Debug message with attributes!", "name", "John Doe", "id", 123, )`
#####  info(message, attrs...) 
`$app.logger().info("Info message!") $app.logger().info( "Info message with attributes!", "name", "John Doe", "id", 123, )`
#####  warn(message, attrs...) 
`$app.logger().warn("Warning message!") $app.logger().warn( "Warning message with attributes!", "name", "John Doe", "id", 123, )`
#####  error(message, attrs...) 
`$app.logger().error("Error message!") $app.logger().error( "Error message with attributes!", "id", 123, "error", err, )`
#####  with(attrs...) 
`with(atrs...)` creates a new local logger that will "inject" the specified attributes with each following log.
`const l = $app.logger().with("total", 123) // results in log with data {"total": 123} l.info("message A") // results in log with data {"total": 123, "name": "john"} l.info("message B", "name", "john")`
#####  withGroup(name) 
`withGroup(name)` creates a new local logger that wraps all logs attributes under the specified group name.
`const l = $app.logger().withGroup("sub") // results in log with data {"sub": { "total": 123 }} l.info("message A", "total", 123)`
###  Logs settings 
You can control various log settings like logs retention period, minimal log level, request IP logging, etc. from the logs settings panel:
![Logs settings screenshot](https://pocketbase.io/images/screenshots/logs.png)
###  Custom log queries 
The logs are usually meant to be filtered from the UI but if you want to programmatically retrieve and filter the stored logs you can make use of the `$app.logQuery()` query builder method. For example:
`let logs = arrayOf(new DynamicModel({ id: "", created: "", message: "", level: 0, data: {}, })) // see https://pocketbase.io/docs/js-database/#query-builder $app.logQuery(). // target only debug and info logs andWhere($dbx.in("level", -4, 0)). // the data column is serialized json object and could be anything andWhere($dbx.exp("json_extract(data, '$.type') = 'request'")). orderBy("created DESC"). limit(100). all(logs)`
Prev: Filesystem Next: Types reference
