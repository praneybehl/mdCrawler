Skip to main content
On this page
Excalibur can render the screen in various different display modes by default.
## Managing display modes​
Excalibur supports multiple display modes for a game. Pass in a displayMode option when creating a game to customize the viewport.
### Fixed Display Mode​
DisplayMode.Fixed is the default, use a specified resolution for the game. Like 600x400 pixels for example.
```

ts
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.Fixed // fixed is the default so this is optional
});
Copy
```
```

ts
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.Fixed // fixed is the default so this is optional
});
Copy
```

### Fit Screen Display Mode​
DisplayMode.FitScreen Fit to screen using as much space as possible while maintaining aspect ratio and resolution.
This is not the same as Screen.enterFullscreen, which uses the fullscreen api, but behaves in a similar way maintaining aspect ratio.
You may want to center your game and fit to the screen here is an example:
```

css
html, body {
height: 100%;
}
body {
display: flex;
height: 100vh;
justify-content: center;
align-items: center;
}
Copy
```
```

css
html, body {
height: 100%;
}
body {
display: flex;
height: 100vh;
justify-content: center;
align-items: center;
}
Copy
```
```

ts
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitScreen
});
Copy
```
```

ts
constgame=new ex.Engine({
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitScreen
});
Copy
```

Click and drag right corner to resize!
### Fill Screen Display Mode​
DisplayMode.FillScreen Fill the entire screen's css width/height for the game resolution dynamically. This means the resolution of the game will change dynamically as the window is resized. This is not the same as Screen.enterFullscreen
```

ts
constgame=new ex.Engine({
  displayMode: ex.DisplayMode.FillScreen
});
Copy
```
```

ts
constgame=new ex.Engine({
  displayMode: ex.DisplayMode.FillScreen
});
Copy
```

Click and drag right corner to resize!
### Fit Container Display Mode​
DisplayMode.FitContainer Fit to parent element width/height using as much space as possible while maintaining aspect ratio and resolution.
```

css
.container {
/* Flexbox used to center game */
display: flex;
justify-content: center;
align-items: center;
/* Container size with border */
border: red4pxdashed;
width: 50%;
height: 300px;
}
.snippet-resizer { display:flex; margin:0; padding:0; resize:both; overflow:hidden }
.snippet-resizer>.snippet-resized { flex-grow:1; margin:0; padding:0; border:0 }
Copy
```
```

css
.container {
/* Flexbox used to center game */
display: flex;
justify-content: center;
align-items: center;
/* Container size with border */
border: red4pxdashed;
width: 50%;
height: 300px;
}
.snippet-resizer { display:flex; margin:0; padding:0; resize:both; overflow:hidden }
.snippet-resizer>.snippet-resized { flex-grow:1; margin:0; padding:0; border:0 }
Copy
```
```

html
<divclass="container snippet-resizer">
  <canvasid="game"></canvas>
</div>
Copy
```
```

html
<divclass="container snippet-resizer">
  <canvasid="game"></canvas>
</div>
Copy
```
```

ts
constgame=new ex.Engine({
  canvasElementId: 'game',
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitContainer
});
Copy
```
```

ts
constgame=new ex.Engine({
  canvasElementId: 'game',
  width: 600,
  height: 400,
  displayMode: ex.DisplayMode.FitContainer
});
Copy
```

Click and drag right corner to resize!
### Fill Container Display Mode​
DisplayMode.FillContainer will fill the entire screen's css width/height for the game resolution dynamically. This means the resolution of the game will change dynamically as the window is resized. This is not the same as Screen.enterFullscreen
```

css
.container {
border: red4pxdashed;
width: 50%;
height: 300px;
}
.snippet-resizer { display:flex; margin:0; padding:0; resize:both; overflow:hidden }
.snippet-resizer>.snippet-resized { flex-grow:1; margin:0; padding:0; border:0 }
Copy
```
```

css
.container {
border: red4pxdashed;
width: 50%;
height: 300px;
}
.snippet-resizer { display:flex; margin:0; padding:0; resize:both; overflow:hidden }
.snippet-resizer>.snippet-resized { flex-grow:1; margin:0; padding:0; border:0 }
Copy
```
```

html
<divclass="container snippet-resizer">
  <canvasid="game"></canvas>
</div>
Copy
```
```

html
<divclass="container snippet-resizer">
  <canvasid="game"></canvas>
</div>
Copy
```
```

ts
constgame=new ex.Engine({
  canvasElementId: 'game',
  displayMode: ex.DisplayMode.FillContainer
});
Copy
```
```

ts
constgame=new ex.Engine({
  canvasElementId: 'game',
  displayMode: ex.DisplayMode.FillContainer
});
Copy
```

Click and drag right corner to resize!
### Fit Screen And Fill Display Mode​
DisplayMode.FitScreenAndFill is similar to DisplayMode.FitScreen and will fit the game in the screen while preserving the original aspect ratio, but allow the excess gaps to be drawn to drawn to. This ensures there is no "letterboxing" and the entire screen is covered by canvas. You can use the Screen.contentArea to return a screen space bounding box of area of the screen guaranteed to be visible to the user.
![Content area](https://excaliburjs.com/assets/images/content-area-41dfe8a40aae4101c8d69afb7ff2ce54.png)
Click and drag right corner to resize!
### Fit Container And Fill Display Mode​
DisplayMode.FitContainerAndFill is similar to DisplayMode.FitContainer and will fit the game to the the current container preserving the original aspect ratio, but allow the excess gaps in the container to be drawn to. You can use the Screen.contentArea to return a screen space bounding box of area of the screen guaranteed to be visible to the user.
![Content area](https://excaliburjs.com/assets/images/content-area-41dfe8a40aae4101c8d69afb7ff2ce54.png)
Click and drag right corner to resize!
## Fullscreen API​
warning
Currently Apple does not support fullscreen API on iPhones, it does however work on later model iPads.
The screen abstraction now supports the browser fullscreen api. This will cause the game to be displayed fullscreen until the user exits (usually with the escape key or by gesturing to the exit button at the top of the browser window).
Click and drag right corner to resize!
note
This requires an explicit user gesture due to browser security, so wiring it into a native HTML button click is the easiest way to do this.
```

typescript
document.getElementById('go-fullscreen')!.addEventListener('click', () => {
  game.screen.enterFullscreen();
});
Copy
```
```

typescript
document.getElementById('go-fullscreen')!.addEventListener('click', () => {
  game.screen.enterFullscreen();
});
Copy
```
```

typescript
await game.screen.enterFullscreen();
await game.screen.exitFullscreen();
Copy
```
```

typescript
await game.screen.enterFullscreen();
await game.screen.exitFullscreen();
Copy
```

By default `enterFullscreen()` will use the canvas element as the root of full screen mode. If your game uses HTML based UI, the HTML UI will not be included because it is not a child of the canvas element.
To include both the HTML based game UI as well as the game canvas, pass an id of an element that is the parent of both the canvas and UI. For example `enterFullscreen('root')`
  * Managing display modes
    * Fixed Display Mode
    * Fit Screen Display Mode
    * Fill Screen Display Mode
    * Fit Container Display Mode
    * Fill Container Display Mode
    * Fit Screen And Fill Display Mode
    * Fit Container And Fill Display Mode
  * Fullscreen API


