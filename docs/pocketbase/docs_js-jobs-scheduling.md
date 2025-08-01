Jobs scheduling
If you have tasks that need to be performed periodically, you could setup crontab-like jobs with `cronAdd(id, expr, handler)`.
Each scheduled job runs in its own goroutine as part of the `serve` command process and must have:
  * **id** - identifier for the scheduled job; could be used to replace or remove an existing job
  * **cron expression** - e.g. `0 0 * * *` ( _supports numeric list, steps, ranges or macros _)
  * **handler** - the function that will be executed every time when the job runs


Here is an example:
`// prints "Hello!" every 2 minutes cronAdd("hello", "*/2 * * * *", () => {   console.log("Hello!") })`
To remove a single registered cron job you can call `cronRemove(id)`.
All registered app level cron jobs can be also previewed and triggered from the _Dashboard > Settings > Crons_ section.
Prev: Migrations Next: Sending emails
