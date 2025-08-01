Jobs scheduling
If you have tasks that need to be performed periodically, you could setup crontab-like jobs with the builtin `app.Cron()` _(it returns an app scoped`cron.Cron` value)_ .
The jobs scheduler is started automatically on app `serve`, so all you have to do is register a handler with `app.Cron().Add(id, cronExpr, handler)` or `app.Cron().MustAdd(id, cronExpr, handler)` (_the latter panic if the cron expression is not valid_).
Each scheduled job runs in its own goroutine and must have:
  * **id** - identifier for the scheduled job; could be used to replace or remove an existing job
  * **cron expression** - e.g. `0 0 * * *` ( _supports numeric list, steps, ranges or macros _)
  * **handler** - the function that will be executed everytime when the job runs


Here is one minimal example:
`// main.go package main import ( "log" "github.com/pocketbase/pocketbase" ) func main() {   app := pocketbase.New() // prints "Hello!" every 2 minutes   app.Cron().MustAdd("hello", "*/2 * * * *", func() {     log.Println("Hello!") }) if err := app.Start(); err != nil {     log.Fatal(err) } }`
To remove already registered cron job you can call `app.Cron().Remove(id)`
All registered app level cron jobs can be also previewed and triggered from the _Dashboard > Settings > Crons_ section.
Keep in mind that the `app.Cron()` is also used for running the system scheduled jobs like the logs cleanup or auto backups (the jobs id is in the format `__pb*__`) and replacing these system jobs or calling `RemoveAll()`/`Stop()` could have unintended side-effects.
If you want more advanced control you can initialize your own cron instance independent from the application via `cron.New()`.
Prev: Migrations Next: Sending emails
