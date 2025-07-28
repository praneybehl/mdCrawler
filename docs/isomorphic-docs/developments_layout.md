Skip to main content
Version: v7.0.0
On this page
## Layout​
Isomorphic, our versatile theme, empowers you to shape the visual identity of your website through a selection of six distinct layouts: `Hydrogen`, `Helium`, `Lithium`, `Beryllium`, `Boron` and `Carbon`.
## How to change default layout​
Isomorphic recognizes that not every project needs the `Hydrogen` layout as the default. If your project falls into this category and you prefer a different starting point, you're in the right place. Let's tailor your experience by changing the default layout.
Isomorphic provides a TypeScript enum called `LAYOUT_OPTIONS`, that encapsulates the available layout choices. A detailed documentation is available here.
Let's assume we want to turn the `Helium` layout into default layout.
Now, go to `apps/isomorphic/src/hooks/use-layout.ts` and replace `LAYOUT_OPTIONS.HYDROGEN` like following:
apps/isomorphic/src/hooks/use-layout.ts
```
const isomorphicLayoutAtom =atom(typeof window !=='undefined'? localStorage.getItem('isomorphic-layout')-:LAYOUT_OPTIONS.HYDROGEN+:LAYOUT_OPTIONS.HELIUM);
```

Finally, go to apps/isomorphic/src/hooks/use-layout.ts and replace like following:
apps/isomorphic/src/hooks/use-layout.ts
```
// 2. useLayout hook to check which layout is availableexportfunctionuseLayout(){const[layout, setLayout]=useAtom(isomorphicLayoutAtomWithPersistence);return{-  layout: layout ===null?LAYOUT_OPTIONS.HYDROGEN: layout,+  layout: layout ===null?LAYOUT_OPTIONS.HELIUM: layout,  setLayout,};}
```

#### Your are all set to use `HELIUM` layout as your default layout.​
note
If you want to change any of the layout to default, follow the same process.
  * Layout
  * How to change default layout


