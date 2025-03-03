Skip to main content
On this page
For drawing hooks the `ExcaliburGraphicsContext` replaces the browser `CanvasRenderingContext2D`. However, if you need to do some custom drawing using the `CanvasRenderingContext2D` the new Canvas graphic has your back.
The canvas is a special type of graphic that acts like a shim between direct CanvasRenderingContext2D drawing and the ExcaliburGraphicsContext.
This type of graphic is re-rendered every time the graphic is drawn, thus it should be used sparingly due to this inefficiency. It is recommended you use the `cache: true` property and call `flagDirty()` when there is something new to draw.
warning
It is recommended you specify your ex.Canvas width and height in the constructor.
Keep in mind that the underlying HTML canvas has a default size depending on your platform, this will be used for centering.
```

typescript
constcanvas=newCanvas({
draw: (ctx:CanvasRenderingContext2D) => {
...
 }
});
Copy
```
```

typescript
constcanvas=newCanvas({
draw: (ctx:CanvasRenderingContext2D) => {
...
 }
});
Copy
```

## Example​
```

ts
constcanvas=new ex.Canvas({
  width: 200,
  height: 200,
  cache: true, // If true draw once until flagged dirty again, otherwise draw to Canvas every frame
draw: (ctx) => {
    console.log('With cache=true I draw once');
    ctx.fillStyle ='red';
    ctx.fillRect(0, 0, 200, 200);
  }
})
constactor=new ex.Actor({
  pos: game.screen.center
});
actor.graphics.use(canvas);
Copy
```
```

ts
constcanvas=new ex.Canvas({
  width: 200,
  height: 200,
  cache: true, // If true draw once until flagged dirty again, otherwise draw to Canvas every frame
draw: (ctx) => {
    console.log('With cache=true I draw once');
    ctx.fillStyle ='red';
    ctx.fillRect(0, 0, 200, 200);
  }
})
constactor=new ex.Actor({
  pos: game.screen.center
});
actor.graphics.use(canvas);
Copy
```

  * Example


