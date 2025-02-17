Skip to content
# Qwik
This guide will walk you through creating your Tauri app using the Qwik web framework. Learn more about Qwik at https://qwik.dev.
## Checklist
  * Use SSG. Tauri doesn’t support server-based solutions.
  * Use `dist/` as `frontendDist` in `tauri.conf.json`.


## Example Configuration
  1. ##### Create a new Qwik app
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npmcreateqwik@latest
cd<PROJECT>

```

```

yarncreateqwik@latest
cd<PROJECT>

```

```

pnpmcreateqwik@latest
cd<PROJECT>

```

```

denorun-Anpm:create-qwik@latest
cd<PROJECT>

```

  2. ##### Install the `static adapter`
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npmrunqwikaddstatic

```

```

yarnqwikaddstatic

```

```

pnpmqwikaddstatic

```

```

denotaskqwikaddstatic

```

  3. ##### Add the Tauri CLI to your project
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npminstall-D@tauri-apps/cli@latest

```

```

yarnadd-D@tauri-apps/cli@latest

```

```

pnpmadd-D@tauri-apps/cli@latest

```

```

denoadd-Dnpm:@tauri-apps/cli@latest

```

  4. ##### Initiate a new Tauri project
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npmruntauriinit

```

```

yarntauriinit

```

```

pnpmtauriinit

```

```

denotasktauriinit

```

  5. ##### Tauri configuration
     * npm 
     * yarn 
     * pnpm 
     * deno 
tauri.conf.json```

{
"build": {
"devUrl": "http://localhost:5173"
"frontendDist":"../dist",
"beforeDevCommand": "npm run dev",
"beforeBuildCommand": "npm run build"
}
}

```

tauri.conf.json```

{
"build": {
"devUrl": "http://localhost:5173"
"frontendDist":"../dist",
"beforeDevCommand": "yarn dev",
"beforeBuildCommand": "yarn build"
}
}

```

tauri.conf.json```

{
"build": {
"devUrl": "http://localhost:5173"
"frontendDist":"../dist",
"beforeDevCommand": "pnpm dev",
"beforeBuildCommand": "pnpm build"
}
}

```

tauri.conf.json```

{
"build": {
"devUrl": "http://localhost:5173"
"frontendDist":"../dist",
"beforeDevCommand": "deno task dev",
"beforeBuildCommand": "deno task build"
}
}

```

  6. ##### Start your `tauri` app
     * npm 
     * yarn 
     * pnpm 
     * deno 
```

npmruntauridev

```

```

yarntauridev

```

```

pnpmtauridev

```

```

denotasktauridev

```



© 2025 Tauri Contributors. CC-BY / MIT
