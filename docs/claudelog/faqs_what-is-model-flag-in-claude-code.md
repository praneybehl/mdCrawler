Skip to main content
The --model flag selects which Claude AI model to use for your session, enabling you to choose between Claude 4 Sonnet, Opus, and Claude 3.5 Haiku based on task complexity, speed requirements, and cost considerations.
### How to Use It​
Use `--model` when launching Claude Code with simple aliases like `sonnet`, `opus`, or `haiku`, or specify the full model name for precise version control.
```
claude --model claude-sonnet-4-20250514claude --model claude-opus-4-20250514claude --model claude-3-5-haiku-20241022
```

### Why Use Different Models​
Different models offer distinct advantages for specific development scenarios. Sonnet provides balanced performance for most coding tasks, Opus delivers maximum reasoning for complex problems, and Haiku offers fast responses for simple operations.
**Strategic Usage:**
  * **Sonnet** : Regular development, file operations, routine coding (most tasks)
  * **Opus** : Complex debugging, architecture decisions, security analysis (premium tasks)
  * **Haiku** : Simple edits, quick questions, basic formatting (fast tasks)


I use Sonnet for daily development work, escalate to Opus for complex architectural decisions, and switch to Haiku for quick text edits.
### Model Access by Plan​
**Claude Pro ($17/month annually, $20/month monthly)** - Access to Sonnet model with 5x usage limits compared to free tier.
**Claude Max 5x ($100/month)** - Access to Sonnet with 5x higher usage limits than Pro, plus limited Opus access.
**Claude Max 20x ($200/month)** - Full access to all models including unrestricted Opus with 20x higher usage limits than Pro.
**API Usage** - Pay-per-token pricing with access to all models based on API tier.
##### Smart Model Selection
Strategic model selection balances performance, cost, and development speed in Claude Code workflows. Plan with Opus, implement with Sonnet, edit with Haiku for optimal efficiency.
![Custom image](https://www.claudelog.com/img/discovery/000.png)
**See Also** : Model Comparison|Pricing|Configuration
  * How to Use It
  * Why Use Different Models
  * Model Access by Plan


