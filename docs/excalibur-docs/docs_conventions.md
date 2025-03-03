Skip to main content
There are a few things that Excalibur does that are good to know before you start building games!
  1. Excalibur uses a theater metaphor, for example: Scenes, Actors, and Actions.
  2. Excalibur uses Resources to load external files like images and sounds. They can also be used to load other things like data or config.
  3. The negative y direction is up, and the positive y direction is down.
  4. Distance units are in pixels, velocity in pixels per second, and acceleration in pixels per second per second.
  5. Rotation units are in radians.
  6. All elapsed times and durations in Excalibur are in milliseconds.
  7. Actor z-index's follow the browser way of doing things.
     * Things with larger positive numbers are on top of lower numbers.
  8. Coordinate Spaces
     * World space is the pixel position where Entities and Actors live by default.
     * Screen space is the pixels on the canvas element viewport according to the browser.
     * Page space is pixel offset from the top left of browser window
     * Local space is relative to a parent Entity or Actor
  9. Things are in "world" space unless specified with a `local` prefix or added as a child actor.
  10. Bounds are always an axis aligned bounding box, meaning a non-rotated box.
  11. Excalibur handles offscreen draw culling for you! No need to manage that!
  12. Excalibur uses pre-multiplied alphas when drawing which is important to know if you use Material


