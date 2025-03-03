Skip to main content
On this page
Please consider html based first but if the UI makes more sense in-canvas look to screen elements.
## Screen Elements​
In Excalibur, if you want to display something like a HUD element or UI element inside the Excalibur canvas, you can create an instance of ScreenElement. A screen element has the following semantics that differ from a regular actor:
  * They automatically capture pointer events
  * They do not participate in collisions
  * They appear above all "normal" actors in a scene
  * Invoking ScreenElement.contains will check against screen coordinates by default.


Other than that, they are the same as normal actors where you can assign drawings, perform actions, etc.
```

ts
import*as ex from'excalibur'
import Resources from'./resources'
classStartButtonextendsex.ScreenElement {
constructor() {
super({
   x: 50,
   y: 50,
  })
 }
onInitialize() {
this.graphics.add('idle', Resources.StartButtonBackground)
this.graphics.add('hover', Resources.StartButtonHovered)
this.on('pointerup', () => {
alert("I've been clicked")
  })
this.on('pointerenter', () => {
this.graphics.show('hover')
  })
this.on('pointerleave', () => {
this.graphics.show('idle')
  })
 }
}
game.add(newStartButton())
game.start()
Copy
```
```

ts
import*as ex from'excalibur'
import Resources from'./resources'
classStartButtonextendsex.ScreenElement {
constructor() {
super({
   x: 50,
   y: 50,
  })
 }
onInitialize() {
this.graphics.add('idle', Resources.StartButtonBackground)
this.graphics.add('hover', Resources.StartButtonHovered)
this.on('pointerup', () => {
alert("I've been clicked")
  })
this.on('pointerenter', () => {
this.graphics.show('hover')
  })
this.on('pointerleave', () => {
this.graphics.show('idle')
  })
 }
}
game.add(newStartButton())
game.start()
Copy
```

  * Screen Elements


