Skip to main content
The --max-turns flag limits the number of autonomous actions Claude Code can take during non-interactive sessions, providing precise control over automation scope and preventing runaway processes.
### How to Use It​
Use `--max-turns` with a number when using `--print` mode to limit how many autonomous actions Claude can perform in a single session.
```
claude -p "Fix linting errors" --max-turns 1claude --print "Generate documentation" --max-turns 3claude -p "Debug authentication" --max-turns 2 --verbose
```

### Why Use --max-turns​
The --max-turns flag prevents excessive resource usage and provides predictable automation behavior in scripts, CI/CD pipelines, and batch processing workflows.
**Benefits:**
  * **Automation Control** - Prevent runaway processes in automated workflows
  * **Cost Management** - Limit API usage and processing costs
  * **Resource Optimization** - Control computational resource consumption
  * **Predictable Behavior** - Ensure consistent automation scope
  * **CI/CD Safety** - Prevent pipeline failures from excessive processing


### Understanding Turns​
A turn is consumed each time Claude Code makes a tool call. Users may need to increase the number of turns to finish complex tasks that require multiple tool operations. The --max-turns limit helps prevent agents from getting stuck in infinite loops and burning tokens unnecessarily.
**Turn Planning:**
  * Simple tasks: 2-4 turns
  * Multi-file operations: 6-10 turns
  * Complex debugging: 10-20 turns
  * Sub-agent workflows: 40-200+ turns


##### Loop Prevention Control
--max-turns prevents infinite loops and token waste by limiting tool calls per session. Increase the limit if complex tasks don't complete within the turn budget.
![Custom image](https://www.claudelog.com/img/discovery/002.png)
**See Also** : Print Mode|Output Format|Configuration
  * How to Use It
  * Why Use --max-turns
  * Understanding Turns


