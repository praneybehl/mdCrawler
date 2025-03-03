Skip to main content
On this page
Often you want external images loaded into your game, this is accomplished with ImageSource. In some other engines/frameworks this can be known as a Texture.
ImageSource represents the source bitmap and contains the logic for loading that image from a file. You can think of this as the file representation in Excalibur for the image. Use Sprites to draw them to the screen.
## Loading Images with the ImageSource Resource​
Excalibur supports `.png`, `.jpg`, `.gif`, and `.bmp` image sources with partial support for `.svg`
  * `.png` and `.svg` will be completely lossless formats. For pixel art type games we recommend `.png`
  * `.jpg` and `.gif` are lossy formats, useful to optimize for download size.
  * `.bmp` are the biggest
  * `base64` useful if you don't want to pay the loading time cost of your images at the expense of larger source download 
    * `data:image/png;base64,BASE64DATA...`

```

typescript
constgame=newEngine({...});
constspriteSheetImage=newImageSource('./my/spritesheet.png');
constloader=newLoader([spriteSheetImage]);
await game.start(loader);
constspriteSheet= SpriteSheet.fromImageSource({
 image: spriteFontImage,
 grid: {
  rows: 5,
  columns: 2,
  spriteWidth: 32, // pixels
  spriteHeight: 32// pixels
 }
});
Copy
```
```

typescript
constgame=newEngine({...});
constspriteSheetImage=newImageSource('./my/spritesheet.png');
constloader=newLoader([spriteSheetImage]);
await game.start(loader);
constspriteSheet= SpriteSheet.fromImageSource({
 image: spriteFontImage,
 grid: {
  rows: 5,
  columns: 2,
  spriteWidth: 32, // pixels
  spriteHeight: 32// pixels
 }
});
Copy
```

These images can be presented to the loader at the start of an Excalibur game
```

typescript
constgame=new ex.Engine({ width: 800, height: 600 })
constimage=new ex.ImageSource('./img/myimg.png')
constloader=new ex.Loader()
loader.addResource(image)
game.start(loader).then(() => {
// resources like ImageSource loaded before game started
})
Copy
```
```

typescript
constgame=new ex.Engine({ width: 800, height: 600 })
constimage=new ex.ImageSource('./img/myimg.png')
constloader=new ex.Loader()
loader.addResource(image)
game.start(loader).then(() => {
// resources like ImageSource loaded before game started
})
Copy
```

Or they can be loaded out of band **Note: it is important to check that a ImageSource has been loaded before using it at runtime to avoid errors and visual bugs if your game is loading images this way.**
```

typescript
constimage=new ex.ImageSource('./img/myimg.png')
image.load().then(() => {
// image loaded
// good for use in sprites inside this function
})
if (image.isLoaded()) {
// image.data is good for use in sprites
constmySprite= image.toSprite()
}
Copy
```
```

typescript
constimage=new ex.ImageSource('./img/myimg.png')
image.load().then(() => {
// image loaded
// good for use in sprites inside this function
})
if (image.isLoaded()) {
// image.data is good for use in sprites
constmySprite= image.toSprite()
}
Copy
```

  * Loading Images with the [[ImageSource]] Resource


