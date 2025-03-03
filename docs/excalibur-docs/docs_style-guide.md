Skip to main content
On this page
This is a test page.
## API Links​
  * Class: Actor
  * Class method: Actor.onInitialize
  * Class property: Actor.pos
  * Interface: Action
  * Namespaces: Events
  * Enum: CollisionType
  * Function: canonicalizeAngle
  * Reference: Events.ActivateEvent
  * Type Alias: AnimationEvents
  * Variable: EX_VERSION


## Code Snippets​
### TypeScript (inline)​
```

Player.ts
ts
import { Actor, Sprite } from"excalibur";
classPlayerextendsActor {
onInitialize() {
this.graphics.use(newSprite());
 }
}
Copy
```
```

Player.ts
ts
import { Actor, Sprite } from"excalibur";
classPlayerextendsActor {
onInitialize() {
this.graphics.use(newSprite());
 }
}
Copy
```

### Live Code (compiled)​
tbd
### Iframe Embedding​
```

mdx
<IFrameEmbedsrc={url} />
Copy
```
```

mdx
<IFrameEmbedsrc={url} />
Copy
```

### CodeSandbox Embedding​
```

mdx
<CodeSandboxEmbedsrc={url} title={title} {...props} />
Copy
```
```

mdx
<CodeSandboxEmbedsrc={url} title={title} {...props} />
Copy
```

## Storybook​
```

mdx
<Examplestory="name_of_storybook_story" />
Copy
```
```

mdx
<Examplestory="name_of_storybook_story" />
Copy
```

## Diagrams​
tbd
## Markdown Features​
Docusaurus supports **Markdown** and a few **additional features**.
### Front Matter​
Markdown documents have metadata at the top called Front Matter:
```

my-doc.md
text
// highlight-start
---
id: my-doc-id
title: My document title
description: My document description
slug: /my-custom-url
---
// highlight-end
## Markdown heading
Markdown text with [links](./hello.md)
Copy
```
```

my-doc.md
text
// highlight-start
---
id: my-doc-id
title: My document title
description: My document description
slug: /my-custom-url
---
// highlight-end
## Markdown heading
Markdown text with [links](./hello.md)
Copy
```

### Links​
Regular Markdown links are supported, using url paths or relative file paths.
```

md
Let's see how to [Create a page](/create-a-page).
Copy
```
```

md
Let's see how to [Create a page](/create-a-page).
Copy
```
```

md
Let's see how to [Create a page](./create-a-page.md).
Copy
```
```

md
Let's see how to [Create a page](./create-a-page.md).
Copy
```

**Result:** Let's see how to Create a page.
### Images​
Regular Markdown images are supported.
You can use absolute paths to reference images in the static directory (`static/img/docusaurus.png`):
```

md
![Docusaurus logo](/img/docusaurus.png)
Copy
```
```

md
![Docusaurus logo](/img/docusaurus.png)
Copy
```

![Docusaurus logo](https://excaliburjs.com/docs/style-guide)
You can reference images relative to the current file as well. This is particularly useful to colocate images close to the Markdown files using them:
```

md
![Docusaurus logo](./img/docusaurus.png)
Copy
```
```

md
![Docusaurus logo](./img/docusaurus.png)
Copy
```

### Code Blocks​
Markdown code blocks are supported with Syntax highlighting.
```

src/components/HelloDocusaurus.js
jsx
functionHelloDocusaurus() {
return (
    <h1>Hello, Docusaurus!</h1>
  )
}
Copy
```
```

src/components/HelloDocusaurus.js
jsx
functionHelloDocusaurus() {
return (
    <h1>Hello, Docusaurus!</h1>
  )
}
Copy
```
```

src/components/HelloDocusaurus.js
jsx
functionHelloDocusaurus() {
return <h1>Hello, Docusaurus!</h1>;
}
Copy
```
```

src/components/HelloDocusaurus.js
jsx
functionHelloDocusaurus() {
return <h1>Hello, Docusaurus!</h1>;
}
Copy
```

### Admonitions​
Docusaurus has a special syntax to create admonitions and callouts:
My tip
Use this awesome feature option
:::
Take care
This action is dangerous
My tip
Use this awesome feature option
Take care
This action is dangerous
### MDX and React Components​
MDX can make your documentation more **interactive** and allows using any **React components inside Markdown** :
```

jsx
exportconstHighlight= ({children, color}) => (
 <span
style={{
   backgroundColor: color,
   borderRadius: '20px',
   color: '#fff',
   padding: '10px',
   cursor: 'pointer',
  }}
onClick={() => {
alert(`You clicked the color ${color} with label ${children}`)
  }}>
  {children}
 </span>
);
This is <Highlight color="#25c2a0">Docusaurus green</Highlight>!
This is <Highlight color="#1877F2">Facebook blue</Highlight>!
Copy
```
```

jsx
exportconstHighlight= ({children, color}) => (
 <span
style={{
   backgroundColor: color,
   borderRadius: '20px',
   color: '#fff',
   padding: '10px',
   cursor: 'pointer',
  }}
onClick={() => {
alert(`You clicked the color ${color} with label ${children}`)
  }}>
  {children}
 </span>
);
This is <Highlight color="#25c2a0">Docusaurus green</Highlight>!
This is <Highlight color="#1877F2">Facebook blue</Highlight>!
Copy
```

This is Docusaurus green !
This is Facebook blue !
  * API Links
  * Code Snippets
    * TypeScript (inline)
    * Live Code (compiled)
    * Iframe Embedding
    * CodeSandbox Embedding
  * Storybook
  * Diagrams
  * Markdown Features
    * Front Matter
    * Links
    * Images
    * Code Blocks
    * Admonitions
    * MDX and React Components


