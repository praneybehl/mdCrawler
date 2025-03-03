Skip to main content
On this page
warning
The dev tool plugin is no longer supported in later versions, use the browser extension instead.
This is a dev tool to help you debug your game written in excalibur.
This tool allows you to see information about the engine, currentScene, camera, clock, entities, and more!
## Using the Dev Tool​
  1. Install using npm

```

> npm install @excaliburjs/dev-tools
Copy
```
```

> npm install @excaliburjs/dev-tools
Copy
```

  1. Inside your game code pass your game to the devtool

```

typescript
constgame=new ex.Engine({...});
constdevtool=newDevTool(game);
Copy
```
```

typescript
constgame=new ex.Engine({...});
constdevtool=newDevTool(game);
Copy
```

  1. Voila!


![](https://user-images.githubusercontent.com/612071/150462738-433536d9-28b0-486c-b5bb-8e8b4e2526fc.png)
  * Using the Dev Tool


