Logging
`app.Logger()` provides access to a standard `slog.Logger` implementation that writes any logs into the database so that they can be later explored from the PocketBase _Dashboard > Logs_ section.
For better performance and to minimize blocking on hot paths, logs are written with debounce and on batches:
  * 3 seconds after the last debounced log write
  * when the batch threshold is reached (currently 200)
  * right before app termination to attempt saving everything from the existing logs queue


###  Log methods 
All standard `slog.Logger` methods are available but below is a list with some of the most notable ones.
#####  Debug(message, attrs...) 
`app.Logger().Debug("Debug message!") app.Logger().Debug( "Debug message with attributes!", "name", "John Doe", "id", 123, )`
#####  Info(message, attrs...) 
`app.Logger().Info("Info message!") app.Logger().Info( "Info message with attributes!", "name", "John Doe", "id", 123, )`
#####  Warn(message, attrs...) 
`app.Logger().Warn("Warning message!") app.Logger().Warn( "Warning message with attributes!", "name", "John Doe", "id", 123, )`
#####  Error(message, attrs...) 
`app.Logger().Error("Error message!") app.Logger().Error( "Error message with attributes!", "id", 123, "error", err, )`
#####  With(attrs...) 
`With(atrs...)` creates a new local logger that will "inject" the specified attributes with each following log.
`l := app.Logger().With("total", 123) // results in log with data {"total": 123} l.Info("message A") // results in log with data {"total": 123, "name": "john"} l.Info("message B", "name", "john")`
#####  WithGroup(name) 
`WithGroup(name)` creates a new local logger that wraps all logs attributes under the specified group name.
`l := app.Logger().WithGroup("sub") // results in log with data {"sub": { "total": 123 }} l.Info("message A", "total", 123)`
###  Logs settings 
You can control various log settings like logs retention period, minimal log level, request IP logging, etc. from the logs settings panel:
![Logs settings screenshot](https://pocketbase.io/images/screenshots/logs.png)
###  Custom log queries 
The logs are usually meant to be filtered from the UI but if you want to programmatically retrieve and filter the stored logs you can make use of the `app.LogQuery()` query builder method. For example:
`logs := []*core.Log{} // see https://pocketbase.io/docs/go-database/#query-builder err := app.LogQuery(). // target only debug and info logs AndWhere(dbx.In("level", -4, 0). // the data column is serialized json object and could be anything AndWhere(dbx.NewExp("json_extract(data, '$.type') = 'request'")). OrderBy("created DESC"). Limit(100). All(&logs)`
Prev: Filesystem Next: Testing
