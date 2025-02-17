Skip to content
# Content Security Policy (CSP)
Tauri restricts the Content Security Policy (CSP) of your HTML pages. This can be used to reduce or prevent impact of common web based vulnerabilities like cross-site-scripting (XSS).
Local scripts are hashed, styles and external scripts are referenced using a cryptographic nonce, which prevents unallowed content from being loaded.
The CSP protection is only enabled if set on the Tauri configuration file. You should make it as restricted as possible, only allowing the webview to load assets from hosts you trust, and preferably own. At compile time, Tauri appends its nonces and hashes to the relevant CSP attributes automatically to bundled code and assets, so you only need to worry about what is unique to your application.
This is an example CSP configuration taken from the `api` example of Tauri, but every application developer needs to tailor this to their own application needs.
tauri/examples/api/src-tauri/tauri.conf.json```

"csp": {
"default-src": "'self' customprotocol: asset:",
"connect-src": "ipc: http://ipc.localhost",
"font-src": ["https://fonts.gstatic.com"],
"img-src": "'self' asset: http://asset.localhost blob: data:",
"style-src": "'unsafe-inline' 'self' https://fonts.googleapis.com"
},

```

See `script-src`, `style-src` and CSP Sources for more information about this protection.
© 2025 Tauri Contributors. CC-BY / MIT
