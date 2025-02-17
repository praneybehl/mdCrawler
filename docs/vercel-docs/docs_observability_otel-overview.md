![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Observability
OpenTelemetry Collector
Tutorial
# Quickstart for using the Vercel OpenTelemetry Collector
Learn how to get started with OTEL on Vercel to send traces from your functions to application performance monitoring (APM) vendors.
Table of Contents
Vercel's OpenTelemetry collector is available in Beta on Pro and Enterprise plans
Vercel has an OpenTelemetry (OTEL) collector that allows you to send OTEL traces from your Serverless or Edge Functions to application performance monitoring (APM) vendors such as New Relic.
The use of the OTEL collector is recommended due to improved performance, but not strictly required. If desired, you can configure the OTEL SDK to use custom trace exporters.
Traces are a way to collect data about the performance and behavior of your application and help identify the cause of performance issues, errors, and other problems. Learn more about traces in the OpenTelemetry docs.
To start using OpenTelemetry on Vercel, follow the steps below. This guide gives examples using Next.js and other frameworks where you can use Serverless or Edge Functions.
### Prerequisites
  * You must be using an OTEL Integration: 
    * New Relic: Available in Beta to teams on Pro and Enterprise plans by following the steps below
    * DataDog: Available in Beta to teams on Pro and Enterprise plans by following the steps below


### Get started
  1. ### Install an OTEL integration to visualize traces
Select an integration from the Observability category in the Marketplace (such as DataDog or New Relic).
Click the Add Integration button to begin the installation and follow each step to add the correct Scope.
If you already have installed an OTEL integration, you can skip this step.
  2. ### Enable traces
To use OTEL, you must enable Traces for the Integration. You can do this either during initial setup, or if you already have the integration installed, select Manage next to the Integration in the Integrations tab and then select Configure.
  3. ### Initialize OTEL
Using `@vercel/otel` wrapperUsing OpenTelemetry SDK
For JavaScript and Typescript users on Vercel, you can use the `@vercel/otel` package to call the correct OpenTelemetry SDK for you.
Install the OpenTelemetry JavaScript SDK and `@vercel/otel`:
pnpmyarnnpm
```
pnpm i @opentelemetry/api @vercel/otel
```

Create an `instrumentation.ts` file in the root of your project, or, on Next.js it must be placed in the `src` directory if you are using one. Add the following code to initialize and configure OTEL using `@vercel/otel`.
instrumentation.ts
TypeScript
TypeScriptJavaScript
```
import { registerOTel } from'@vercel/otel';
exportfunctionregister() {
registerOTel({ serviceName:'your-project-name' });
}
// NOTE: You can replace `your-project-name` with the actual name of your project
```

Open inOpen in v0
Before receiving traces from an APM vendor (such as DataDog), it may be necessary to first create the service you intend to use as a `serviceName` within the service catalog. Refer to the APM vendor's documentation for specific requirements.
  4. ### Start tracing requests in your project
Next.js 13.4+Other frameworks
Next.js 13.4+ supports auto-instrumentation which means you no longer have to create a span for each request. To use this feature in Next.js 13 & 14, you must explicitly opt-in by adding `experimental.instrumentationHook = true` to your `next.config.js`. This is not required in Next.js 15+.
For more information, please refer to the Next.js docs for auto-instrumentation.
  5. ### Deploy your project to Vercel
If you have an existing project, you must trigger a redeployment to use traces.
You can either deploy your project through the dashboard or through the CLI.


### Custom OTEL exporters
The use of OTEL collector is recommended due to its performance benefits. However, if you need to export tracing to an unsupported APM vendor, you can do so using environment variables or configuration options in the `@vercel/otel` package.
Most of OpenTelemetry's SDK environment variables are supported by `@vercel/otel`, including OTLP exporter variables. You can configure these variables using Vercel's environment variables.
And you can supply completely custom exporter using the `traceExporter` or `spanProcessors` configuration options in the `registerOTel()` API.
instrumentation.ts
TypeScript
TypeScriptJavaScript
```
import { registerOTel } from'@vercel/otel';
import { MyCustomExporter } from'./my-custom-exporter';
exportfunctionregister() {
registerOTel({
  serviceName:'your-project-name',
  traceExporter:newMyCustomExporter(),
 });
}
```

Open inOpen in v0
### Using custom OpenTelemetry setup with Sentry
If you are using Sentry v8+, follow the Sentry documentation to learn how to use your existing custom OpenTelemetry setup.
Last updated on November 13, 2024
Previous
Log Drains Reference
Next
Checks
Was this helpful?
supported.
Send
AskAsk v0
OpenTelemetry CollectorAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
