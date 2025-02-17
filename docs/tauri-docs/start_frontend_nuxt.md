Skip to content
# Nuxt
Nuxt is a meta framework for Vue. Learn more about Nuxt at https://nuxt.com. This guide is accurate as of Nuxt 3.11.
## Checklist
  * Use SSG by setting `ssr: false`. Tauri doesn’t support server based solutions.
  * Use `process.env.TAURI_DEV_HOST` as the development server host IP when set to run on iOS physical devices.
  * Use `dist/` as `frontendDist` in `tauri.conf.json`.
  * Compile using `nuxi generate`.
  * (Optional): Disable telemetry by setting `telemetry: false` in `nuxt.config.ts`.


## Example Configuration
  1. ##### Update Tauri configuration
     * npm 
     * yarn 
     * pnpm 
     * deno 
tauri.conf.json```

{
"build": {
"beforeDevCommand": "npm run dev",
"beforeBuildCommand": "npm run generate",
"devUrl": "http://localhost:3000",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn generate",
"devUrl": "http://localhost:3000",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "pnpm dev",
"beforeBuildCommand": "pnpm generate",
"devUrl": "http://localhost:3000",
"frontendDist": "../dist"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "deno task dev",
"beforeBuildCommand": "deno task generate",
"devUrl": "http://localhost:3000",
"frontendDist": "../dist"
}
}

```

  2. ##### Update Nuxt configuration
```

exportdefaultdefineNuxtConfig({
// (optional) Enable the Nuxt devtools
devtools: { enabled: true },
// Enable SSG
ssr: false,
// Enables the development server to be discoverable by other devices when running on iOS physical devices
devServer: { host: process.env.TAURI_DEV_HOST||'localhost' },
vite: {
// Better support for Tauri CLI output
clearScreen: false,
// Enable environment variables
// Additional environment variables can be found at
// https://v2.tauri.app/reference/environment-variables/
envPrefix: ['VITE_', 'TAURI_'],
server: {
// Tauri requires a consistent port
strictPort: true,
},
},
});

```



© 2025 Tauri Contributors. CC-BY / MIT
