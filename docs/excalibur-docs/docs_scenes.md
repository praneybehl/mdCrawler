Skip to main content
On this page
## Adding actors to the scene​
For an Actor to be drawn and updated, it needs to be part of the "scene graph". The Engine provides several easy ways to quickly add/remove actors from the current scene.
```

js
constgame=new ex.Engine(...);
constplayer=new ex.Actor();
constenemy=new ex.Actor();
// add them to the "root" scene
game.add(player);
game.add(enemy);
// start game
game.start();
Copy
```
```

js
constgame=new ex.Engine(...);
constplayer=new ex.Actor();
constenemy=new ex.Actor();
// add them to the "root" scene
game.add(player);
game.add(enemy);
// start game
game.start();
Copy
```

You can also add actors to a scene instance specifically using Scene.add:
```

js
constgame=new ex.Engine();
constlevel1=new ex.Scene();
constplayer=new ex.Actor();
constenemy=new ex.Actor();
// add actors to level1
level1.add(player);
level1.add(enemy);
// add level1 to the game
game.add('level1', level1);
// start the game
game.start().then(() => {
// after player clicks start game, for example
 game.goToScene('level1');
});
Copy
```
```

js
constgame=new ex.Engine();
constlevel1=new ex.Scene();
constplayer=new ex.Actor();
constenemy=new ex.Actor();
// add actors to level1
level1.add(player);
level1.add(enemy);
// add level1 to the game
game.add('level1', level1);
// start the game
game.start().then(() => {
// after player clicks start game, for example
 game.goToScene('level1');
});
Copy
```

## Scene lifecycle​
A scene has a basic lifecycle that dictates how it is initialized, updated, and drawn. Once a scene is added to the engine it will follow this lifecycle:
![Scene Lifecycle](https://excaliburjs.com/assets/images/SceneLifecycle-f54c57011352c478c15937d5180f5643.png)
SystemECS WorldCurrent SceneSystemECS WorldCurrent Scenealt[Update][Draw]loop[EntityQuery]loop[Every tick Engine.mainloop()]Update SystemsDraw SystemsUpdateEntity QueryQuery ChangedUpdate
For more complex games, you might want more control over a scene in which case you can extend Scene. This is useful for menus, custom loaders, and levels.
### Adding a scene Dynamically​
Use Engine.add to add a new scene to the game. Each scene has a `string` key you can assign. You can then use Engine.goToScene to switch scenes which runs the scene lifecycle hooks.
```

ts
classMainMenuextendsex.Scene {}
// add to game and activate it
game.add('mainmenu', newMainMenu());
game.goToScene('mainmenu');
Copy
```
```

ts
classMainMenuextendsex.Scene {}
// add to game and activate it
game.add('mainmenu', newMainMenu());
game.goToScene('mainmenu');
Copy
```

## Static Scene Collection​
You may also add scenes up front as part of your Engine construction. In the `scenes:` map you can specify a Scene constructor, a Scene instance, or a Scene Custom Configuration.
  * Scene Constructors may extend `export class StartScreen extends ex.Scene`
  * Scene Custom Configurations, like the one named `sceneWithCustomTransitionAndLoader:` can also take a scene constructor or an instances


One advantage of using Scene constructors is Excalibur will only construct your Scene when needed to present. This can save a lot of memory on the bigger games.
```

typescript
constgame=newEngine({
 width: 800,
 height: 600,
 scenes: {
  startScreen: StartScreen,
  levelSelect: LevelSelect,
  tutorial: Tutorial,
  introLevel: newLevel(Config.startingPuzzle),
  endScreen: EndScreen,
  sceneWithCustomTransitionAndLoader: {
   scene: scene2,
   loader: MyLoader,
   transitions: {
    out: new ex.FadeInOut({ duration: 500, direction: 'out' }),
    in: new ex.CrossFade({ duration: 2500, direction: 'in', blockInput: true })
   }
  },
 },
});
Copy
```
```

typescript
constgame=newEngine({
 width: 800,
 height: 600,
 scenes: {
  startScreen: StartScreen,
  levelSelect: LevelSelect,
  tutorial: Tutorial,
  introLevel: newLevel(Config.startingPuzzle),
  endScreen: EndScreen,
  sceneWithCustomTransitionAndLoader: {
   scene: scene2,
   loader: MyLoader,
   transitions: {
    out: new ex.FadeInOut({ duration: 500, direction: 'out' }),
    in: new ex.CrossFade({ duration: 2500, direction: 'in', blockInput: true })
   }
  },
 },
});
Copy
```

### Initialization​
note
This is the recommended hook for setting up scene state
Scene.onInitialize is called **once** when the scene is created for use in the game. It is called _before_ Scene.onActivate and can be used to set up the scene state. This is typically where you'd add any actors to the scene, set up initial state, and other startup tasks.
```

ts
classMainMenuextendsScene {
private_startButton:StartButton;
/**
  * Start-up logic, called once
  */
publiconInitialize(engine:Engine) {
// initialize scene actors
this._startButton =newStartButton();
this.add(this._startButton);
 }
}
Copy
```
```

ts
classMainMenuextendsScene {
private_startButton:StartButton;
/**
  * Start-up logic, called once
  */
publiconInitialize(engine:Engine) {
// initialize scene actors
this._startButton =newStartButton();
this.add(this._startButton);
 }
}
Copy
```

You can even call Engine.start to preload assets for your scene, to avoid having to load them at game initialization time:
```

ts
classMainMenuextendsScene {
private_loaded:boolean=false;
/**
  * Start-up logic, called once
  */
publiconInitialize(engine:Engine) {
// load scene-specific assets
  engine.start(sceneLoader).then(() => {
this._loaded =true;
  });
 }
}
Copy
```
```

ts
classMainMenuextendsScene {
private_loaded:boolean=false;
/**
  * Start-up logic, called once
  */
publiconInitialize(engine:Engine) {
// load scene-specific assets
  engine.start(sceneLoader).then(() => {
this._loaded =true;
  });
 }
}
Copy
```

### Activation​
Scene.onActivate is called when the engine switches to the scene. It may be called more than once during the lifetime of a game, if you switch back and forth between scenes. It is useful for taking action before showing the scene. You may use this hook over `onInitialize` for anything specific to the context in which the scene was activated.
Data can be passed to a scene during activation via the `goToScene('sceneKey', { some: 'data' })`.
```

ts
interfaceMyLevelData {
spawnLocation:Vector;
}
classMainMenuextendsScene<MyLevelData> {
privatestartButton:StartButton;
/**
  * Each time the scene is entered (Engine.goToScene)
  */
publiconActivate(ctx:SceneActivationContext<MyLevelData>) {
const { spawnLocation } = ctx.data;
  console.log(spawnLocation);
if (ctx.previousScene instanceofLevel) {
this.startButton.text ='Resume game';
  } else {
this.startButton.text ='Start game';
  }
 }
}
Copy
```
```

ts
interfaceMyLevelData {
spawnLocation:Vector;
}
classMainMenuextendsScene<MyLevelData> {
privatestartButton:StartButton;
/**
  * Each time the scene is entered (Engine.goToScene)
  */
publiconActivate(ctx:SceneActivationContext<MyLevelData>) {
const { spawnLocation } = ctx.data;
  console.log(spawnLocation);
if (ctx.previousScene instanceofLevel) {
this.startButton.text ='Resume game';
  } else {
this.startButton.text ='Start game';
  }
 }
}
Copy
```

### Deactivation​
Scene.onDeactivate is called when the engine exits a scene and is typically used for cleanup, exit tasks, and garbage collection.
```

ts
classLevelextendsScene {
/**
  * Each time the scene is exited (Engine.goToScene)
  */
publiconDeactivate(ctx:SceneActivationContext) {
this.saveState();
 }
}
Copy
```
```

ts
classLevelextendsScene {
/**
  * Each time the scene is exited (Engine.goToScene)
  */
publiconDeactivate(ctx:SceneActivationContext) {
this.saveState();
 }
}
Copy
```

## Loading​
Scenes can now load resources specific to them by implementing the Scene.onPreLoad.
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

Read more in the loaders documentation;
  * Adding actors to the scene
  * Scene lifecycle
    * Adding a scene Dynamically
  * Static Scene Collection
    * Initialization
    * Activation
    * Deactivation
  * Loading


