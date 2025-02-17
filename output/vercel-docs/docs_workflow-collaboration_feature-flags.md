![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Workflow
Feature Flags
Reference
# Feature Flags
Learn how to use feature flags with Vercel's DX platform.
Table of Contents
Feature flags are a powerful tool that allows you to control the visibility of features in your application, enabling you to ship, test, and experiment with confidence. Vercel offers various options to integrate feature flags into your application.
## Choose how you work with flags
Vercel provides a flexible approach to working with flags, allowing you to tailor the process to your team's workflow at any stage of the lifecycle. The options can be used independently or in combination, depending on the project's needs. You can:
  * Implement flags as code, using the Flags SDK in Next.js or SvelteKit, or use an SDK from your existing feature flag provider.
  * Manage feature flags through the Vercel Toolbar to view, override, and share your application's feature flags.
  * Observe your flags using Vercel's observability features.
  * Optimize your feature flags by using an Edge Config integration.


### Implementing Feature Flags in your codebase
If you're using Next.js or SvelteKit for your application, you can implement feature flags directly in your codebase. In Next.js, this includes using feature flags for static pages by generating multiple variants and routing between them with middleware.
  * Vercel is compatible with any feature flag provider including LaunchDarkly, Optimizely, Statsig, Hypertune, Split, and custom feature flag setups.
  * Flags SDK: A free open-source library that gives you the tools you need to use feature flags in Next.js and SvelteKit applications


### Managing Feature Flags from the Toolbar
Flags Explorer is available in Beta on all plans
Using the Vercel Toolbar, you're able to view, override, and share feature flags for your application without leaving your browser tab.
You can manage feature flags from the toolbar in any development environment that your team has enabled the toolbar for. This includes local development, preview deployments, and production deployments.
  * Using Feature Flags in the Vercel Toolbar: Learn how to view and override your application's feature flags from the Vercel Toolbar.
  * Implementing Feature Flags in the Vercel Toolbar: Learn how to set up the Vercel Toolbar so you can see and override your application's feature flags.


### Observing your flags
Web Analytics are available on all plans
Feature flags play a crucial role in the software development lifecycle, enabling safe feature rollouts, experimentation, and A/B testing. When you integrate your feature flags with the Vercel platform, you can improve your application by using Vercel's observability features.
  * Integrate Feature Flags with Runtime Logs: Learn how to send feature flag data to Vercel logs.
  * Integrate Feature Flags with Web Analytics: Learn how to tag your page views and custom events with feature flags.


### Optimizing your feature flags
Edge Config is available on all plans
An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers. With Vercel Integrations, you can connect with external providers to synchronize their flags into your Edge Config.
With Vercel's optimizations, you can read Edge Config data at negligible latency. The vast majority of your reads will complete within 15ms at P99, or as low as 0ms in some scenarios.
  * Vercel Edge Config: Experiment with A/B testing by storing feature flags in your Edge Config.
  * Vercel Edge Config Quickstart: Get started with reading data from Edge Config.


Last updated on August 7, 2024
Previous
Accessibility Audit Tool
Next
Flags SDK
Was this helpful?
supported.
Send
AskAsk v0
Feature FlagsAskAsk v0
