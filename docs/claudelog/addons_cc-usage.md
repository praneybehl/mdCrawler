Skip to main content
On this page
**Monitor your Claude Code API usage and costs with detailed analytics**
**Author** : @ryoppippi | GitHub Repo | 5065 Stars|152 Forks|MIT License|Updated Jul 23, 2025
### Overview​
CC Usage is a command-line tool that helps you track and analyze your Claude Code API consumption. Get detailed insights into your usage patterns, costs, and optimize your Claude Code workflows.
![CC Usage command line interface showing daily usage report with token counts, costs, and colorful table formatting](https://www.claudelog.com/assets/images/claude-code-cc-usage-addon-dashboard-screenshot-712f336e404a6afd9a79a0ea71190441.png)
### Features​
  * **Daily & Monthly Reports** - View token usage and costs aggregated by date or month
  * **5-Hour Block Monitoring** - Track usage within Claude's billing windows with active block monitoring
  * **Live Dashboard** - Real-time monitoring showing active session progress and token burn rate
  * **Model Tracking** - See which Claude models you're using with per-model cost breakdown
  * **Date Filtering** - Filter reports by date range and export data in JSON format
  * **MCP Integration** - Built-in Model Context Protocol server for integration with other tools


### Installation​
**Quick Start (Recommended)**
```
npx ccusage@latest # or: bunx ccusage # or: pnpm dlx ccusage
```

**Global Installation**
```
npm install -g ccusage && ccusage daily
```

### Usage​
**Daily Usage Report**
```
# View daily token usage and costsccusage daily
```

**Monthly Reports**
```
# Monthly usage summaryccusage monthly
```

For additional options and advanced usage, read the official documentation.
##### Community Need
Developers on Claude Pro and Max subscriptions frequently express frustration about hitting usage limits without understanding consumption patterns. CC Usage provides visibility into subscription usage, helping optimize workflows and track value.
![Custom image](https://www.claudelog.com/img/discovery/013.png)
### Integration with Claude Code​
CC Usage works alongside your existing Claude Code setup to provide transparency into your API consumption patterns.
**Workflow Integration**
  * Track usage during development sessions
  * Optimize prompt efficiency based on usage data
  * See how much money you saved with Claude Max or Pro


_CC Usage is an independent community project. For technical support and updates, please refer to the official GitHub repository._
  * Overview
  * Features
  * Installation
  * Usage
  * Integration with Claude Code


