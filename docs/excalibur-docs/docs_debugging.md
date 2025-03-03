Skip to main content
On this page
## Excalibur Dev Tool Browser Extension​
There are a couple gotchas that can bite new developers in excalibur. We recommend using the Excalibur Dev Tool Browser Extension
![excalibur dev tool extension](https://excaliburjs.com/assets/images/extension-e8d365522d2ddcb3716f4321f14c0a44.gif)
Install the extension in your favorite browser
  * Install in Chrome
  * Install in Firefox


tip
Check the browser console for warnings! These will often hint at something being wrong, so if you're game is behaving unexpectedly look there first!
## Why is my event not firing​
  1. Are you sure that's the right event name? For example `pointerdown` vs. `click`, Excalibur will let you listen to `click` event though it's not a supported event.


## Why is my Actor not showing up on screen?​
  1. Have you added it to a scene? Is it the current one?
  2. Do you have graphics assigned? `actor.graphics.use(graphic)`
  3. Give your actor a name `new ex.Actor({name: 'myCoolActor'})`, turn on names `game.debug.entity.showName = true` and toggle debug mode `game.toggleDebug()` to show debug drawing.
  4. Use the excalibur debug extension to help visualize https://github.com/excaliburjs/excalibur-extension


### Issue: My game only shows a white screen​
  * Did you remember to call `game.start()`?


### Issue: Poor/laggy game performance​
  * Consult our performance guide


### Issue: My images show up as black rectangles on mobile or other platforms​
  * Ensure your images are less than 4k pixels in width or height, this is usually the limit for mobile devices in WebGL.


## How do I visualize values for debugging​
Use the Debug static drawing helpers! They can be called from anywhere without a graphics context and can be very useful for debugging your game. You will need to `game.toggleDebug()` to see them.
```

typescript
constgame=new ex.Engine({...})
game.toggleDebug();
constplayer=new ex.Actor({...});
player.onPostUpdate= () => {
 ex.Debug.drawLine(
  player.pos,
  player.pos.add(ex.Vector.Down.scale(100)), {
   color: ex.Color.Red
  });
 ex.Debug.drawPoint(player.pos, {
  size: 1,
  color: ex.Color.Violet
 });
 ex.Debug.drawCircle(player.pos, 100, {
  color: ex.Color.Transparent,
  strokeColor: ex.Color.Black,
  width: 1
 });
 ex.Debug.drawBounds(player.collider.bounds, { color: ex.Color.Yellow });
}
Copy
```
```

typescript
constgame=new ex.Engine({...})
game.toggleDebug();
constplayer=new ex.Actor({...});
player.onPostUpdate= () => {
 ex.Debug.drawLine(
  player.pos,
  player.pos.add(ex.Vector.Down.scale(100)), {
   color: ex.Color.Red
  });
 ex.Debug.drawPoint(player.pos, {
  size: 1,
  color: ex.Color.Violet
 });
 ex.Debug.drawCircle(player.pos, 100, {
  color: ex.Color.Transparent,
  strokeColor: ex.Color.Black,
  width: 1
 });
 ex.Debug.drawBounds(player.collider.bounds, { color: ex.Color.Yellow });
}
Copy
```

  * Excalibur Dev Tool Browser Extension
  * Why is my event not firing
  * Why is my Actor not showing up on screen?
    * Issue: My game only shows a white screen
    * Issue: Poor/laggy game performance
    * Issue: My images show up as black rectangles on mobile or other platforms
  * How do I visualize values for debugging


