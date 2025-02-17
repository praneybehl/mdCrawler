Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Developers using React in their Capacitor app have access to a set of useful, community-maintained React Hooks to access Capacitor APIs in their React function components.
To install the hooks:
```
npminstall @capacitor-community/react-hooks
```

To use the hooks, import and use in a function component:
```
import{ useFilesystem, base64FromPath, availableFeatures }from'@capacitor-community/react-hooks/filesystem';constMyComponent=()=>(const{ readFile }=useFilesystem();useEffect(()=>{constreadMyFile=async()=>{const file =awaitreadFile({    path: filepath,    directory: FilesystemDirectory.Data});// ...}readMyFile();},[ readFile ]);
```

## More Reading​
See the @capacitor-community/react-hooks repo for documentation on all the available hooks.
## Contents
  * More Reading


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Freact-hooks&_biz_t=1739803076141&_biz_i=React%20Hooks%20%7C%20Capacitor%20Documentation&_biz_n=45&rnd=575048&cdn_o=a&_biz_z=1739803076141)
