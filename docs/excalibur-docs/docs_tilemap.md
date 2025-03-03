Skip to main content
On this page
TileMaps can be useful tools to build levels for platformers or top down games.
Excalibur supports building tile based games, often referred to as "TileMaps." Excalibur has a Tiled plugin to support the popular Tiled editor map files.
## Tilemap​
Tilemaps consist of a uniform grid of cells that can be solid or not. Each cell can have it's own graphics.
Tile maps are made up of Tiles which can draw Graphics. Tile maps support multiple layers of Graphics and work well for building tile-based games such as RPGs, adventure games, strategy games, and others. Tiles can be solid so that Actors can't pass through them.
```

typescript
// Load your favorite tileset (maybe from Kenney.nl)
constkenneyRougeLikePack=new ex.ImageSource(rougeLikeImageSrc);
// Create a sprite sheet
constrougeLikeSpriteSheet= ex.SpriteSheet.fromImageSource({
  image: kenneyRougeLikePack,
  grid: {
    rows: 31,
    columns: 51,
    spriteHeight: 16,
    spriteWidth: 16
  },
  spacing: {
    margin: {
      x: 1,
      y: 1
    }
  }
});
// Create a tilemap
consttilemap=new ex.TileMap({
  rows: 10,
  columns: 10,
  tileWidth: 16,
  tileHeight: 16,
});
// loop through tilemap cells
for (let tile of tilemap.tiles) {
constsprite= rougeLikeSpriteSheet.getSprite(0, 0);
if (sprite) {
    tile.addGraphic(sprite);
  }
}
Copy
```
```

typescript
// Load your favorite tileset (maybe from Kenney.nl)
constkenneyRougeLikePack=new ex.ImageSource(rougeLikeImageSrc);
// Create a sprite sheet
constrougeLikeSpriteSheet= ex.SpriteSheet.fromImageSource({
  image: kenneyRougeLikePack,
  grid: {
    rows: 31,
    columns: 51,
    spriteHeight: 16,
    spriteWidth: 16
  },
  spacing: {
    margin: {
      x: 1,
      y: 1
    }
  }
});
// Create a tilemap
consttilemap=new ex.TileMap({
  rows: 10,
  columns: 10,
  tileWidth: 16,
  tileHeight: 16,
});
// loop through tilemap cells
for (let tile of tilemap.tiles) {
constsprite= rougeLikeSpriteSheet.getSprite(0, 0);
if (sprite) {
    tile.addGraphic(sprite);
  }
}
Copy
```

## Tiled plugin​
Excalibur has a Tiled map plugin https://github.com/excaliburjs/excalibur-tiled/ for loading `.tmx` maps.
We recommend using the Tiled map editor to build your maps and export them to JSON. You can then load them using a Generic Resource and process them to create your levels. A TileMap can then be used as part of a level or map class that adds enemies and builds game objects from the Tiled map.
Read more here!
```

typescript
import*as ex from'excalibur'
import*as tiled from'@excaliburjs/plugin-tiled';
import exampleCityUrl from'./example-city.tmx';
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitScreen
});
consttiledMapResource=new tiled.TiledResource(exampleCityUrl);
constloader=new ex.Loader([tiledMapResource])
game.start(loader).then(() => {
  tiledMapResource.addToScene(game.currentScene);
  game.currentScene.camera.zoom =2;
});
Copy
```
```

typescript
import*as ex from'excalibur'
import*as tiled from'@excaliburjs/plugin-tiled';
import exampleCityUrl from'./example-city.tmx';
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitScreen
});
consttiledMapResource=new tiled.TiledResource(exampleCityUrl);
constloader=new ex.Loader([tiledMapResource])
game.start(loader).then(() => {
  tiledMapResource.addToScene(game.currentScene);
  game.currentScene.camera.zoom =2;
});
Copy
```

## Currently unsupported​
Hexagonal and Staggered TileMaps are not yet supported out of the box (but they are in our plans).
We recommend reading some of the material on Red Blob Games for algorithms around Hexagonal.
  * Tilemap
  * Tiled plugin
  * Currently unsupported


