Skip to main content
On this page
This extension adds support for Aseprite SpriteSheets and Animations exported to json AND the `.aseprite` native format.
```

> npm install @excaliburjs/plugin-aseprite
Copy
```
```

> npm install @excaliburjs/plugin-aseprite
Copy
```

  1. Optionally export JSON using the aseprite cli or through the UI


![Export as JSON in Aseprite](https://github.com/excaliburjs/excalibur-aseprite/raw/main/export.gif)
  1. Load the Aseprite resource via the json and voila ✨


  * Use `AsepriteResource.getAnimation(name)` to retrieve animations by the name in aseprite
  * Use `AsepriteResource.getSpriteSheet()` to get the equivalent Excalibur SpriteSheet
  * Use `Aseprite.rawAseprite` to access the raw data structure from Aseprite
  * Use `Aseprite.image` to access the source image for the SpriteSheet


## Example:​
```

typescript
import { AsepriteResource } from'@excaliburjs/plugin-aseprite'
constgame=newEngine({
 width: 600,
 height: 400,
 displayMode: DisplayMode.FitScreen,
})
constasepriteSpriteSheet=newAsepriteResource('./beetle.aseprite')
// or json
// const asepriteSpriteSheet = new AsepriteResource('./beetle.json')
constloader=newLoader([asepriteSpriteSheet])
game.start(loader).then(() => {
constanim= asepriteSpriteSheet.getAnimation('Loop')
constactor=newActor({ pos: vec(100, 100) })
 actor.graphics.use(anim)
 game.currentScene.add(actor)
})
Copy
```
```

typescript
import { AsepriteResource } from'@excaliburjs/plugin-aseprite'
constgame=newEngine({
 width: 600,
 height: 400,
 displayMode: DisplayMode.FitScreen,
})
constasepriteSpriteSheet=newAsepriteResource('./beetle.aseprite')
// or json
// const asepriteSpriteSheet = new AsepriteResource('./beetle.json')
constloader=newLoader([asepriteSpriteSheet])
game.start(loader).then(() => {
constanim= asepriteSpriteSheet.getAnimation('Loop')
constactor=newActor({ pos: vec(100, 100) })
 actor.graphics.use(anim)
 game.currentScene.add(actor)
})
Copy
```

![Example running](https://github.com/excaliburjs/excalibur-aseprite/raw/main/example.gif)
  * Example:


