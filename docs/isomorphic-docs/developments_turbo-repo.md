Skip to main content
Version: v7.0.0
On this page
## Turbo Repo​
TurboRepo is a high-performance build system for JavaScript and TypeScript code-bases, designed to improve the developer experience and productivity by optimizing the build process. It's particularly beneficial for monorepos, where multiple packages or applications are managed within a single repository. **Learn More About Turborepo**
## Isomorphic Project Structure​
```
├── apps| ├── isomorphic      // Isomorphic Main Workspace|| └── ...| ├── isomorphic-intl   // Multi language and Next Auth supported starter pack workspace| └── ...| ├── isomorphic-starter  // Simple starter pack workspace| └── ...|├── packages| ├── isomorphic-core    // All the reusable components that are used across different workspaces are located here.|| ├── src|||  ├── components   // contains all the reusable common components here|||  └── ...|||  ├── hooks      // contains all the reusable custom hooks here|||  └── ...|||  ├── ui       // contains all the reusable common UI components here|||  └── ...|||  ├── utils      // contains all the reusable custom utility functions here|||  └── ...|| └── ...| └── ...└── ...
```

## Turbo json file structure​
This file is required for the turbo build system to work. It contains configuration for all of the tasks, dependencies, and environment variables. Learn more about **turbo.json** file from their **Official Documentation**
turbo.json
```
{"$schema":"https://turbo.build/schema.json","globalDependencies":["**/.env.*local"],"tasks":{"build":{"dependsOn":["^build"],"outputs":["dist/**",".next/**","!.next/cache/**"],"env":["NEXTAUTH_SECRET","NEXTAUTH_URL"]},"lint":{},"start":{"dependsOn":["^start"]},"dev":{"cache":false,"persistent":true},"clean":{"dependsOn":["^clean"]}},"ui":"stream"}
```

## Why used Turbo Repo?​
**1. Incremental Builds:**
  * TurboRepo supports incremental builds, meaning it only rebuilds parts of the project that have changed. This significantly reduces build times compared to traditional build systems that rebuild the entire project.


**2. Content-Based Caching:**
  * TurboRepo uses a content-based caching mechanism. It caches build outputs based on the content of files, ensuring that unchanged files are not rebuilt, further speeding up the build process.


**3. Task Scheduling:**
  * It optimizes task scheduling by running tasks in parallel when possible and respecting task dependencies. This ensures efficient utilization of system resources and faster completion of build tasks.


**4. Monorepo Support:**
  * TurboRepo is designed with monorepos in mind. It provides tools to manage multiple packages within a single repository, making it easier to share code and dependencies across different projects.


**5. Built-in Support for Popular Tools:**
  * It integrates seamlessly with popular JavaScript and TypeScript tools like Webpack, Rollup, Babel, Jest, and ESLint, allowing developers to use their preferred tools without significant configuration changes.


**6. Environment-Aware:**
  * TurboRepo can differentiate between development and production environments, optimizing builds accordingly. This ensures that development builds are fast while production builds are highly optimized.


  * Turbo Repo
  * Isomorphic Project Structure
  * Turbo json file structure
  * Why used Turbo Repo?


