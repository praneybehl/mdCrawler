Skip to content
# SvelteKit
SvelteKit is a meta framework for Svelte. Learn more about SvelteKit at https://kit.svelte.dev/. This guide is accurate as of SvelteKit 2.5.7 / Svelte 4.2.15.
## Checklist
  * Use SSG and/or SPA via `static-adapter`. Tauri doesn’t support server-based solutions.
  * Use `build/` as `frontendDist` in `tauri.conf.json`.


## Example Configuration
  1. ##### Install `@sveltejs/adapter-static`
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npminstall--save-dev@sveltejs/adapter-static

```

```

yarnadd-D@sveltejs/adapter-static

```

```

pnpmadd-D@sveltejs/adapter-static

```

```

denoadd-Dnpm:@sveltejs/adapter-static

```

  2. ##### Update Tauri configuration
     * npm 
     * yarn 
     * pnpm 
     * deno 
tauri.conf.json```

{
"build": {
"beforeDevCommand": "npm run dev",
"beforeBuildCommand": "npm run build",
"devUrl": "http://localhost:5173",
"frontendDist": "../build"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn build",
"devUrl": "http://localhost:5173",
"frontendDist": "../build"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "pnpm dev",
"beforeBuildCommand": "pnpm build",
"devUrl": "http://localhost:5173",
"frontendDist": "../build"
}
}

```

tauri.conf.json```

{
"build": {
"beforeDevCommand": "deno task dev",
"beforeBuildCommand": "deno task build",
"devUrl": "http://localhost:5173",
"frontendDist": "../build"
}
}

```

  3. ##### Update SvelteKit configuration:
svelte.config.js```

import adapter from'@sveltejs/adapter-static';
import { vitePreprocess } from'@sveltejs/vite-plugin-svelte';
/** @type{import('@sveltejs/kit').Config} */
const config = {
// Consult https://kit.svelte.dev/docs/integrations#preprocessors
// for more information about preprocessors
preprocess: vitePreprocess(),
kit: {
adapter: adapter(),
},
};
exportdefaultconfig;

```

  4. ##### Disable SSR
Lastly, we need to disable SSR and enable prerendering by adding a root `+layout.ts` file (or `+layout.js` if you are not using TypeScript) with these contents:
src/routes/+layout.ts```

export const prerender = true;
export const ssr = false;

```

Note that `static-adapter` doesn’t require you to disable SSR for the whole app but it makes it possible to use APIs that depend on the global window object (like Tauri’s API) without Client-side checks.
Furthermore, if you prefer Single-Page Application (SPA) mode over SSG, you can change the adapter configurations and `+layout.ts` according to the adapter docs.


© 2025 Tauri Contributors. CC-BY / MIT
