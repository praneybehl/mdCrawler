Skip to main content
On this page
Sprite Fusion is a new, exiting, and easy to use tile map editor based on the web! It's goal is to be lightweight and easy to use.
The current Excalibur plugin is designed to parse all data provided by the Sprite Fusion JSON export format and make it available to users. Not all features may be supported directly in Excalibur but the majority are.
![Use the JSON Export](https://excaliburjs.com/assets/images/dont-save-c05dc87b26203c42d36db47c49869c19.png)
warning
Export your map as JSON, IMPORTANT Do not use the "save" option in the current version of the plugin.
The plugin officially supports the latest version of Sprite Fusion that has been published and will warn if you are using an older version.
## Installation​
```

sh
npm install @excaliburjs/plugin-spritefusion
Copy
```
```

sh
npm install @excaliburjs/plugin-spritefusion
Copy
```

Create your resource, load it, then add it to your scene!
```

typescript
constgame=new ex.Engine({...});
constspriteFusionMap=newSpriteFusionResource({
  mapPath: './map/map.json',
  spritesheetPath: './map/spritesheet.png'
});
constloader=new ex.Loader([spriteFusionMap]);
game.start(loader).then(() => {
  spriteFusionMap.addToScene(game.currentScene);
});
Copy
```
```

typescript
constgame=new ex.Engine({...});
constspriteFusionMap=newSpriteFusionResource({
  mapPath: './map/map.json',
  spritesheetPath: './map/spritesheet.png'
});
constloader=new ex.Loader([spriteFusionMap]);
game.start(loader).then(() => {
  spriteFusionMap.addToScene(game.currentScene);
});
Copy
```

![Sprite Fusion example](https://excaliburjs.com/assets/images/sprite-fusion-example-abe33c915b1422a8ab2ef53819bd36b6.png)
## Solid Layers​
In order to create solid layers in Excalibur, use the Sprite Fusion collision layer check box. Any tiles in this layer will be treated as solid by Excalibur.
![solid layer example](https://excaliburjs.com/assets/images/solid-layer-bee117d032a94c10369aa08dd66e3466.png)
## Entity Factories​
Sometimes it is useful to supply a custom type to have the plugin construct when it runs across a particular entity, this might be the player, a collectable, or an enemy.
You can specify a factory to run and create your preferred type, once you've returned the Entity out of the factory it will automatically be added to the Scene. This is also a useful time to run any other custom code you want per Entity.
```

typescript
constspriteFusionMap=newSpriteFusionResource({
  mapPath: './map/map.json',
  spritesheetPath: './map/spritesheet.png',
  entityTileIdFactories: {
0 : (props) => {
returnnew ex.Actor({
        pos: props.worldPos,
        width: 16,
        height: 16,
        color: ex.Color.Red,
        z: props.layer.order +1
      });
    }
  }
});
Copy
```
```

typescript
constspriteFusionMap=newSpriteFusionResource({
  mapPath: './map/map.json',
  spritesheetPath: './map/spritesheet.png',
  entityTileIdFactories: {
0 : (props) => {
returnnew ex.Actor({
        pos: props.worldPos,
        width: 16,
        height: 16,
        color: ex.Color.Red,
        z: props.layer.order +1
      });
    }
  }
});
Copy
```

Currently you need to count the sprite id from the exported spritesheet.png.
![count tile id](https://excaliburjs.com/assets/images/tile-id-5afc5a92e98ae59645ea08852689dd89.png)
For example, now tile id `0` is replaced with a custom implementation that shows a red box.
![factory custom implementation](https://excaliburjs.com/assets/images/factory-result-1b62f011e70ca0dc4e56d868e3d0cd47.png)
  * Installation
  * Solid Layers
  * Entity Factories


