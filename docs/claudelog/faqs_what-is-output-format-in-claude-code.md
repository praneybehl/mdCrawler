Skip to main content
The --output-format flag controls how Claude Code structures its responses in non-interactive mode, enabling JSON output for programmatic processing or formatted text for human consumption.
### How to Use It​
Use `--output-format` with `--print` mode to specify response structure: text for human reading, json for programmatic processing, or stream-json for real-time data handling.
```
claude -p "Analyze code quality" --output-format jsonclaude -p "Generate documentation" --output-format textclaude -p "Large analysis" --output-format stream-json
```

### Why Use --output-format​
The --output-format flag enables Claude Code integration with data processing pipelines, automation scripts, and tools requiring structured data input.
**Benefits:**
  * **Programmatic Processing** - JSON output for scripts and automation workflows
  * **Data Integration** - Structured responses for database storage and API integration
  * **Pipeline Compatibility** - Stream processing for large responses and real-time handling
  * **Parsing Efficiency** - Machine-readable formats for complex data extraction
  * **Tool Interoperability** - Compatible with jq, Python scripts, and CI/CD systems


### Format Options​
**Text** - Human-readable plain text (default format).
**JSON** - Structured data with metadata, analysis results, and processing information.
**Stream-JSON** - Real-time streaming JSON for large responses and progressive processing.
### Common Use Cases​
**CI/CD Integration** - Extract specific metrics from Claude Code analysis for build pipelines.
**Script Automation** - Process JSON responses with jq, Python, or other data processing tools.
**Data Analysis** - Store structured Claude Code outputs in databases or generate reports.
Automation Essential
--output-format json is crucial for CI/CD integration and automation workflows. It enables precise data extraction and programmatic processing of Claude Code analysis.
##### Data Pipeline Ready
--output-format transforms Claude Code into a data source for automation and integration workflows. JSON format enables seamless tool interoperability and complex data processing.
![Custom image](https://www.claudelog.com/img/discovery/003.png)
**See Also** : Print Mode|Max Turns|Configuration
  * How to Use It
  * Why Use --output-format
  * Format Options
  * Common Use Cases


