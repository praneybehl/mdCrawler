Skip to main content
On this page
Excalibur offers several modes of input for your games.
The Engine.input property can be inspected during Actor.update or other areas of the game. This allows you to respond to any type of user input without writing complex input event code yourself.
Learn more about Keyboard, Mouse and Touch, and Gamepads support.
### Inspecting engine input​
Access Engine.input to see if any input is being tracked during the current update frame.
```

ts
classPlayerextendsex.Actor {
publicupdate(engine, delta) {
if (
   engine.input.keyboard.isHeld(ex.Keys.W) ||
   engine.input.gamepads.at(0).getAxes(ex.Axes.LeftStickY) >0.5
  ) {
// implement the code to move the player forward
  }
 }
}
Copy
```
```

ts
classPlayerextendsex.Actor {
publicupdate(engine, delta) {
if (
   engine.input.keyboard.isHeld(ex.Keys.W) ||
   engine.input.gamepads.at(0).getAxes(ex.Axes.LeftStickY) >0.5
  ) {
// implement the code to move the player forward
  }
 }
}
Copy
```

  * Inspecting engine input


