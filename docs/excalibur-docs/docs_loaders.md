Skip to main content
On this page
Games typically will have assets like image files, sound files, level data, etc. that you want to make available to your code. Excalibur has built in types to help you load assets. Excalibur loaders can load anything that implement the Loadable interface.
To build a custom designed loader check out the custom loaders docs.
## Loader​
Excalibur has a built in type Loader with the Excalibur.js logo, progress bar and a play button.
![loader](https://excaliburjs.com/assets/images/loader-1ad5f28886fd6d5da28c542569321c04.gif)
warning
You can suppress the play button with EngineOptions.suppressPlayButton, but user input is required by the browser to unlock the audio context.
To unlock the audio context as part of a user action handler (clicking for example) call WebAudio.unlock
## DefaultLoader & Customizing Loaders​
DefaultLoader is the new base loader type that all excalibur loaders must derive from, in fact the built in Loader derives from this type.
It comes built in with a really simple logo-less loader that can be overridden.
![default loader example](https://excaliburjs.com/assets/images/default-loader-50ed344eed7380706f89b8e743ab12a0.gif)
```

typescript
// my-loader.ts
import*as ex from'excalibur';
exportclassMyLoaderextendsex.DefaultLoader {
overrideonUpdate(engine:Engine, elapsedMilliseconds:number):void {
// Perform something every tick, for example collect time elapsed or check 
// what file names have been loaded for drawing!
 }
overrideonDraw(ctx:CanvasRenderingContext2D) {
// Returns the progress of the loader as a number between [0, 1] inclusive.
  console.log(this.progress);
 }
overrideasynconUserAction():Promise<void> {
// Return a promise that resolves when the user interacts with the loading screen in some way,
// usually a click.
//
// It's important to implement this in order to unlock the audio context in the browser.
// Browsers automatically prevent audio from playing until the user performs an action.
 }
overrideasynconBeforeLoad():Promise<void> {
// Overrideable lifecycle method, called directly before loading starts
// Useful if you need to do anything to the screen/viewport
 }
overrideasynconAfterLoad():Promise<void> {
// Overrideable lifecycle method, called after loading has completed
// Useful if you need to do anything to the screen/viewport
 }
}
Copy
```
```

typescript
// my-loader.ts
import*as ex from'excalibur';
exportclassMyLoaderextendsex.DefaultLoader {
overrideonUpdate(engine:Engine, elapsedMilliseconds:number):void {
// Perform something every tick, for example collect time elapsed or check 
// what file names have been loaded for drawing!
 }
overrideonDraw(ctx:CanvasRenderingContext2D) {
// Returns the progress of the loader as a number between [0, 1] inclusive.
  console.log(this.progress);
 }
overrideasynconUserAction():Promise<void> {
// Return a promise that resolves when the user interacts with the loading screen in some way,
// usually a click.
//
// It's important to implement this in order to unlock the audio context in the browser.
// Browsers automatically prevent audio from playing until the user performs an action.
 }
overrideasynconBeforeLoad():Promise<void> {
// Overrideable lifecycle method, called directly before loading starts
// Useful if you need to do anything to the screen/viewport
 }
overrideasynconAfterLoad():Promise<void> {
// Overrideable lifecycle method, called after loading has completed
// Useful if you need to do anything to the screen/viewport
 }
}
Copy
```

warning
DefaultLoader needs to have DefaultLoader.onUserAction implemented to unlock the audio context as part of a user interaction.
Present a button or something else for the user to interact, resolve `onUserAction` after the user interacts.
## Scene Loading​
Excalibur can now load resources specific to a scene instead of all up front!
In your scene extend the Scene.onPreLoad method and you'll be passed any configured loader. Scene.onPreLoad will be called only once before Scene.onInitialize;
```

typescript
import*as ex from'excalibur';
classLevelOneextendsex.Scene {
spriteFont!:ex.ImageSource;
playerSpriteSheet!:ex.ImageSource;
overrideonPreLoad(loader:DefaultLoader) {
this.spriteFont =new ex.ImageSource('./res/spritefont.png');
this.playerSpriteSheet =new ex.ImageSource('./res/player-sheet.png');
  loader.addResource(this.spriteFont);
  loader.addResource(this.playerSpriteSheet);
 }
}
Copy
```
```

typescript
import*as ex from'excalibur';
classLevelOneextendsex.Scene {
spriteFont!:ex.ImageSource;
playerSpriteSheet!:ex.ImageSource;
overrideonPreLoad(loader:DefaultLoader) {
this.spriteFont =new ex.ImageSource('./res/spritefont.png');
this.playerSpriteSheet =new ex.ImageSource('./res/player-sheet.png');
  loader.addResource(this.spriteFont);
  loader.addResource(this.playerSpriteSheet);
 }
}
Copy
```

To customize the loader you are passed during Scene.onPreLoad update you scene config like so
```

typescript
import*as ex from'excalibur';
import { MyLoader } from'./my-loader'
constgame=new ex.Engine({
 scenes: {
  scene1: {
   scene: MyScene,
   loader: MyLoader
  }
 }
});
game.goToScene('scene1');
Copy
```
```

typescript
import*as ex from'excalibur';
import { MyLoader } from'./my-loader'
constgame=new ex.Engine({
 scenes: {
  scene1: {
   scene: MyScene,
   loader: MyLoader
  }
 }
});
game.goToScene('scene1');
Copy
```

## Common Patterns​
We recommend creating a `resource.ts` to house all your loadable resources in a strongly typed way. This also has the advantage of not cluttering up your main entrypoint. See an example of production game's resources file
```

typescript
// resources.ts
import*as ex from'excalibur';
exportconstResources= {
  TitleImage: new ex.ImageSource('./path/to/some/image.png'),
  KnightSpriteSheet: new ex.ImageSource('./path/to/some/other/image.png'),
  TitleMusic: new ex.Sound('.path/to/first-preference.wav', '.path/to/second-preference.wav'),
} asconst; // < -- as const is important to get strong typing!
exportconstloader=new ex.Loader();
for (let res ofObject.values(Resources)) {
  loader.addResource(res);
}
Copy
```
```

typescript
// resources.ts
import*as ex from'excalibur';
exportconstResources= {
  TitleImage: new ex.ImageSource('./path/to/some/image.png'),
  KnightSpriteSheet: new ex.ImageSource('./path/to/some/other/image.png'),
  TitleMusic: new ex.Sound('.path/to/first-preference.wav', '.path/to/second-preference.wav'),
} asconst; // < -- as const is important to get strong typing!
exportconstloader=new ex.Loader();
for (let res ofObject.values(Resources)) {
  loader.addResource(res);
}
Copy
```

Inside your `main.ts` entry
```

typescript
// main.ts
import*as ex from'excalibur';
import { loader } from'./resources';
constgame=new ex.Engine({...});
game.start(loader);
Copy
```
```

typescript
// main.ts
import*as ex from'excalibur';
import { loader } from'./resources';
constgame=new ex.Engine({...});
game.start(loader);
Copy
```

Also you can reference your `Resources` in your game code
```

typescript
// my-actor.ts
import*as ex from'excalibur';
import { Resources } from'./resources';
exportclassMyActorextendsex.Actor {
overrideonInitialize() {
constknightSpriteSheet= ex.SpriteSheet.fromImageSource({
   image: Resources.KnightSpriteSheet,
   grid: {
     rows: 1,
     columns: 4,
     spriteHeight: 32,
     spriteWidth: 32
   }
  });
constidle= ex.Animation.fromSpriteSheetCoordinates({
    spriteSheet: knightSpriteSheet,
    strategy: ex.AnimationStrategy.Loop,
    frameCoordinates: [
      {x: 0, y: 0, duration: 200},
      {x: 1, y: 0, duration: 200},
      {x: 2, y: 0, duration: 200},
      {x: 3, y: 0, duration: 200}
    ]
  });
this.graphics.use(idle);
 }
}
Copy
```
```

typescript
// my-actor.ts
import*as ex from'excalibur';
import { Resources } from'./resources';
exportclassMyActorextendsex.Actor {
overrideonInitialize() {
constknightSpriteSheet= ex.SpriteSheet.fromImageSource({
   image: Resources.KnightSpriteSheet,
   grid: {
     rows: 1,
     columns: 4,
     spriteHeight: 32,
     spriteWidth: 32
   }
  });
constidle= ex.Animation.fromSpriteSheetCoordinates({
    spriteSheet: knightSpriteSheet,
    strategy: ex.AnimationStrategy.Loop,
    frameCoordinates: [
      {x: 0, y: 0, duration: 200},
      {x: 1, y: 0, duration: 200},
      {x: 2, y: 0, duration: 200},
      {x: 3, y: 0, duration: 200}
    ]
  });
this.graphics.use(idle);
 }
}
Copy
```

  * Loader
  * DefaultLoader & Customizing Loaders
  * Scene Loading
  * Common Patterns


