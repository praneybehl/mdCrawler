Skip to main content
On this page
When building UIs in order to prevent a flash of unstyled content (a moment of default font/styling before the font loads) Excalibur has a built in resource type to help with that.
## Using FontSource​
Using a FontSource will ensure the font is loaded and the font face is ready before the game starts!
```

typescript
constfontSource=new ex.FontSource('/my-font.ttf', 'My Font')
loader.addResource(fontSource)
game.start(loader).then(() => {
constfont= fontSource.toFont() // returns ex.Font
})
Copy
```
```

typescript
constfontSource=new ex.FontSource('/my-font.ttf', 'My Font')
loader.addResource(fontSource)
game.start(loader).then(() => {
constfont= fontSource.toFont() // returns ex.Font
})
Copy
```

Font options can be defined either at the source or at the `toFont()` call. If defined in both, `toFont(options)` will override the options in the FontSource.
```

typescript
constfontSource=new ex.FontSource('/my-font.ttf', 'My Font', { 
 filtering: ex.ImageFiltering.Pixel,
 size: 16, // set a default size
})
constfont= fontSource.toFont({
// override just the size
 size: 20,
})
Copy
```
```

typescript
constfontSource=new ex.FontSource('/my-font.ttf', 'My Font', { 
 filtering: ex.ImageFiltering.Pixel,
 size: 16, // set a default size
})
constfont= fontSource.toFont({
// override just the size
 size: 20,
})
Copy
```

  * Using FontSource


