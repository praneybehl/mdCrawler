Skip to main content
Version: v7.0.0
On this page
## Site Config​
Open up `apps/isomorphic/src/config/site.config.tsx` to make quick changes to your site's title, description, logo and the color preset.
apps/isomorphic/src/config/site.config.tsx
```
importlogoImgfrom'@public/logo.svg';importlogoIconImgfrom'@public/logo-short.svg';enumMODE{DARK='dark',LIGHT='light',}exportconst siteConfig ={ title:'Isomorphic - React Typescript Admin Dashboard Template', description:`Isomorphic the ultimate React TypeScript Admin Template. Streamline your admin dashboard development with our feature-rich, responsive, and highly customizable solution. Boost productivity and create stunning admin interfaces effortlessly.`, logo: logoImg, icon: logoIconImg, mode:MODE.LIGHT, layout:LAYOUT_OPTIONS.HYDROGEN,};
```

  * Site Config


