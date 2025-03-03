Skip to main content
On this page
You may want to display Text in your game, this can be achieved with the Text, Font, and SpriteFont.
## Text​
Text is a raster graphic that can be used to draw text to the screen, all of the normal things that can be done with rasters and graphics can be done with text.
Text supports both normal OS/web fonts and Sprite fonts.
Example
```

typescript
var text =new ex.Text({
 text: 'This is raster text ❤️',
 font: new ex.Font({ size: 30 }),
})
Copy
```
```

typescript
var text =new ex.Text({
 text: 'This is raster text ❤️',
 font: new ex.Font({ size: 30 }),
})
Copy
```

Text is a prebuilt Graphic that can be used to draw text to the screen. Multiple lines of text are supported.
```

typescript
constgame=new ex.Engine({...});
consttext=new ex.Text({
  text: 'Some Text Drawn Here\nNext line'
});
constactor=new ex.Actor({
  pos: ex.vec(100, 100)
});
actor.graphics.use(text);
game.currentScene.add(actor);
Copy
```
```

typescript
constgame=new ex.Engine({...});
consttext=new ex.Text({
  text: 'Some Text Drawn Here\nNext line'
});
constactor=new ex.Actor({
  pos: ex.vec(100, 100)
});
actor.graphics.use(text);
game.currentScene.add(actor);
Copy
```

## Labels​
Labels are a batteries included Actors with Text built and font built in.
```

typescript
constlabel=new ex.Label({
  text: 'Some text',
  pos: ex.vec(100, 100),
  font: new ex.Font({
    family: 'impact',
    size: 24,
    unit: ex.FontUnit.Px
  })
});
Copy
```
```

typescript
constlabel=new ex.Label({
  text: 'Some text',
  pos: ex.vec(100, 100),
  font: new ex.Font({
    family: 'impact',
    size: 24,
    unit: ex.FontUnit.Px
  })
});
Copy
```

## Font​
A Font is a traditional system or loaded web font.
Possible font options
```

typescript
exportinterfaceFontOptions {
size?:number
unit?:FontUnit
family?:string
style?:FontStyle
bold?:boolean
textAlign?:TextAlign
baseAlign?:BaseAlign
direction?:Direction
shadow?: {
blur?:number
offset?:Vector
color?:Color
 }
}
Copy
```
```

typescript
exportinterfaceFontOptions {
size?:number
unit?:FontUnit
family?:string
style?:FontStyle
bold?:boolean
textAlign?:TextAlign
baseAlign?:BaseAlign
direction?:Direction
shadow?: {
blur?:number
offset?:Vector
color?:Color
 }
}
Copy
```
```

typescript
var text =new ex.Text({
 text: 'This is raster text ❤️',
 font: new ex.Font({
  size: 30,
  unit: FontUnit.Px,
  family: 'sans-serif',
  style: FontStyle.Normal,
  bold: false,
  textAlign: TextAlign.Left,
  baseAlign: BaseAlign.Alphabetic,
  direction: Direction.LeftToRight,
  shadow: {
   blur: 2,
   offset: ex.Vec(2, 2),
   color: ex.Color.Black,
  };
 })
});
Copy
```
```

typescript
var text =new ex.Text({
 text: 'This is raster text ❤️',
 font: new ex.Font({
  size: 30,
  unit: FontUnit.Px,
  family: 'sans-serif',
  style: FontStyle.Normal,
  bold: false,
  textAlign: TextAlign.Left,
  baseAlign: BaseAlign.Alphabetic,
  direction: Direction.LeftToRight,
  shadow: {
   blur: 2,
   offset: ex.Vec(2, 2),
   color: ex.Color.Black,
  };
 })
});
Copy
```

It is recommended you load any font important to your game and not rely on any pre-installed system fonts, those will be different from computer to computer.
For example the google fonts loader is a common way to do this.
```

html
<linkrel="preconnect"href="https://fonts.googleapis.com" />
<linkrel="preconnect"href="https://fonts.gstatic.com"crossorigin />
<link
href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap"
rel="stylesheet"
/>
Copy
```
```

html
<linkrel="preconnect"href="https://fonts.googleapis.com" />
<linkrel="preconnect"href="https://fonts.gstatic.com"crossorigin />
<link
href="https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap"
rel="stylesheet"
/>
Copy
```
```

typescript
constfont=new ex.Font({
 family: 'Roboto',
 size: 24,
 unit: ex.FontUnit.Px,
})
Copy
```
```

typescript
constfont=new ex.Font({
 family: 'Roboto',
 size: 24,
 unit: ex.FontUnit.Px,
})
Copy
```

One potential issue with using web fonts is they won't render correctly until loaded see article for details.
```

typescript
asyncfunctionwaitForFontLoad(font, timeout=2000, interval=100) {
returnnewPromise((resolve, reject) => {
// repeatedly poll check
constpoller=setInterval(async () => {
try {
await document.fonts.load(font);
   } catch (err) {
reject(err);
   }
if (document.fonts.check(font)) {
clearInterval(poller);
resolve(true);
   }
  }, interval);
setTimeout(() =>clearInterval(poller), timeout);
 });
}
// Load font before game start
awaitwaitForFontLoad('24px Roboto');
constgame=new ex.Engine({...})
await game.start();
Copy
```
```

typescript
asyncfunctionwaitForFontLoad(font, timeout=2000, interval=100) {
returnnewPromise((resolve, reject) => {
// repeatedly poll check
constpoller=setInterval(async () => {
try {
await document.fonts.load(font);
   } catch (err) {
reject(err);
   }
if (document.fonts.check(font)) {
clearInterval(poller);
resolve(true);
   }
  }, interval);
setTimeout(() =>clearInterval(poller), timeout);
 });
}
// Load font before game start
awaitwaitForFontLoad('24px Roboto');
constgame=new ex.Engine({...})
await game.start();
Copy
```

## SpriteFont​
Sometimes you want to use a custom font based on your spritesheet of character glyphs
Example `sprite-font.png` file:
![Custom pixel art glyphs](https://excaliburjs.com/docs/text)
```

typescript
constspriteFontImage=new ex.ImageSource('./path/to/sprite-font.png')
constspriteFontSheet= ex.SpriteSheet.fromImageSource({
 image: spriteFontImage,
 grid: {
  rows: 3,
  columns: 16,
  spriteWidth: 16,
  spriteHeight: 16
 }
});
constspriteFont=new ex.SpriteFont({
  alphabet: '0123456789abcdefghijklmnopqrstuvwxyz,!\'&."?- ',
  caseInsensitive: true,
  spriteSheet: spriteFontSheet
 });
});
consttext=new ex.Text({
 text: 'This is sprite font text!!',
 font: spriteFont
});
Copy
```
```

typescript
constspriteFontImage=new ex.ImageSource('./path/to/sprite-font.png')
constspriteFontSheet= ex.SpriteSheet.fromImageSource({
 image: spriteFontImage,
 grid: {
  rows: 3,
  columns: 16,
  spriteWidth: 16,
  spriteHeight: 16
 }
});
constspriteFont=new ex.SpriteFont({
  alphabet: '0123456789abcdefghijklmnopqrstuvwxyz,!\'&."?- ',
  caseInsensitive: true,
  spriteSheet: spriteFontSheet
 });
});
consttext=new ex.Text({
 text: 'This is sprite font text!!',
 font: spriteFont
});
Copy
```

  * Text
  * Labels
  * Font
  * SpriteFont


