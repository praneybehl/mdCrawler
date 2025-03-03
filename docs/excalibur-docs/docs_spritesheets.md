Skip to main content
On this page
SpriteSheet is really an ordered collection of sprites from the same base image.
```

typescript
constspriteSheet=new ex.SpriteSheet({
 image: imageRun,
 sprites: [...]
})
Copy
```
```

typescript
constspriteSheet=new ex.SpriteSheet({
 image: imageRun,
 sprites: [...]
})
Copy
```

## Uniform Grid Based Spritesheet​
If you spritesheet is a neat grid there is a static builder for you to slice up that image source. Most sprite sheets are tightly packed like so.
Some source spritesheets may have margin between sprites and an offset, like these playing cards from Kenny.nl
![Kenney.nl pixel art playing cards](https://excaliburjs.com/docs/spritesheets)
```

typescript
constkennyCardsImage=new ex.ImageSource(kennyCardsImageSrc);
constspriteSheet= ex.SpriteSheet.fromImageSource({
  image: kennyCardsImage,
  grid: {
    rows: 4,
    columns: 14,
    spriteWidth: 42,
    spriteHeight: 60
  },
  spacing: {
// Optionally specify the offset from the top left of sheet to start parsing
    originOffset: { x: 11, y: 2 }, // you can now also use a Vector here i.e. vec(11,2), or new Vector(11,2),
// Optionally specify the margin between each sprite
    margin: { x: 23, y: 5} // you can now also use a Vector here i.e. vec(23,5), or new Vector(23,5),
  }
});
Copy
```
```

typescript
constkennyCardsImage=new ex.ImageSource(kennyCardsImageSrc);
constspriteSheet= ex.SpriteSheet.fromImageSource({
  image: kennyCardsImage,
  grid: {
    rows: 4,
    columns: 14,
    spriteWidth: 42,
    spriteHeight: 60
  },
  spacing: {
// Optionally specify the offset from the top left of sheet to start parsing
    originOffset: { x: 11, y: 2 }, // you can now also use a Vector here i.e. vec(11,2), or new Vector(11,2),
// Optionally specify the margin between each sprite
    margin: { x: 23, y: 5} // you can now also use a Vector here i.e. vec(23,5), or new Vector(23,5),
  }
});
Copy
```

## Sparse Spritesheet​
You can also build a spritesheet from a list of different sized source views using SpriteSheet.fromImageSourceWithSourceViews method
```

typescript
constss= ex.SpriteSheet.fromImageSourceWithSourceViews({
 image,
 sourceViews: [
  { x: 0, y: 0, width: 20, height: 30 },
  { x: 20, y: 0, width: 40, height: 50 },
 ],
})
Copy
```
```

typescript
constss= ex.SpriteSheet.fromImageSourceWithSourceViews({
 image,
 sourceViews: [
  { x: 0, y: 0, width: 20, height: 30 },
  { x: 20, y: 0, width: 40, height: 50 },
 ],
})
Copy
```

  * Uniform Grid Based Spritesheet
  * Sparse Spritesheet


