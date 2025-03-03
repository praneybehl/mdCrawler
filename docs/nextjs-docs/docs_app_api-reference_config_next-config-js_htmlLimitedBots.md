Menu
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
Configurationnext.config.jshtmlLimitedBots
# htmlLimitedBots
The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of streaming metadata.
next.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { NextConfig } from'next'
constconfig:NextConfig= {
 htmlLimitedBots:'MySpecialBot|MyAnotherSpecialBot|SimpleCrawler',
}
exportdefault config
```

## Default list
Next.js includes a default list of HTML limited bots.
Specifying a `htmlLimitedBots` config will override the Next.js' default list, allowing you full control over what user agents should opt into this behavior. However, this is advanced behavior, and the default should be sufficient for most cases.
## Version History
Version| Changes  
---|---  
15.2.0| `htmlLimitedBots` option introduced.  
Was this helpful?
supported.
Send
