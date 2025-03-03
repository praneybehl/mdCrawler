Skip to main content
On this page
A graphics group is an new graphic that draws a graphics in some relation to one another. This can be useful when you want to compose graphics together into a single graphic. Graphics groups do support all types of graphics including animations
```

typescript
constgroup=new ex.GraphicsGroup({
 useAnchor: false, // position group from the top left
 members: [
  {
   graphic: newSprite,
   offset: ex.vec(0, 0),
  },
  {
   graphic: newSprite,
   offset: ex.vec(50, 0),
  },
  {
   graphic: newSprite,
   offset: ex.vec(0, 50),
  },
  {
   graphic: text,
   offset: ex.vec(100, 20),
  },
  {
   graphic: circle,
   offset: ex.vec(50, 50),
  },
  {
   graphic: anim,
   offset: ex.vec(200, 200),
  },
  {
   graphic: triangle,
   offset: ex.vec(0, 200),
  },
 ],
})
Copy
```
```

typescript
constgroup=new ex.GraphicsGroup({
 useAnchor: false, // position group from the top left
 members: [
  {
   graphic: newSprite,
   offset: ex.vec(0, 0),
  },
  {
   graphic: newSprite,
   offset: ex.vec(50, 0),
  },
  {
   graphic: newSprite,
   offset: ex.vec(0, 50),
  },
  {
   graphic: text,
   offset: ex.vec(100, 20),
  },
  {
   graphic: circle,
   offset: ex.vec(50, 50),
  },
  {
   graphic: anim,
   offset: ex.vec(200, 200),
  },
  {
   graphic: triangle,
   offset: ex.vec(0, 200),
  },
 ],
})
Copy
```

### Positioning GraphicsGroup and its Members​
There are a few options available to you when defining a grouping.
Setting `useAnchor: false` will tell the `GraphicsGroup` to completely ignore anchoring of any parent component and position from the top left.
```

typescript
constgroup=new ex.GraphicsGroup({
 useAnchor: false, // position group from the top left
 members: [
  {
   graphic: newSprite,
   offset: ex.vec(0, 0)
  },
  {
   graphic: newSprite,
   offset: ex.vec(50, 0)
  }
 ],
})
Copy
```
```

typescript
constgroup=new ex.GraphicsGroup({
 useAnchor: false, // position group from the top left
 members: [
  {
   graphic: newSprite,
   offset: ex.vec(0, 0)
  },
  {
   graphic: newSprite,
   offset: ex.vec(50, 0)
  }
 ],
})
Copy
```

Group members are added to the collection of graphics and their bounds are included as a default. You can disable the bounds inclusion into the `GraphicsGroup` on a per member basis, this is useful if you have large unpredictably sized graphics or dynamic text that can change the bounds. Excalibur default anchor centers graphics, these new bounds can cause `GraphicsGroup`s to shift when new members are added because bounds change.
```

typescript
exportinterfaceGraphicsGrouping {
offset:Vector;
graphic:Graphic;
/**
  * Optionally disable this graphics bounds as part of group calculation, default true
  * if unspecified
  *
  * You may want to do this if you're using text because their bounds will affect
  * the centering of the whole group
  */
useBounds?:boolean;
}
Copy
```
```

typescript
exportinterfaceGraphicsGrouping {
offset:Vector;
graphic:Graphic;
/**
  * Optionally disable this graphics bounds as part of group calculation, default true
  * if unspecified
  *
  * You may want to do this if you're using text because their bounds will affect
  * the centering of the whole group
  */
useBounds?:boolean;
}
Copy
```

note
`useAnchor: false` is the preferred option, turning off bounds can have some unexpected onscreen/offscreen effects like popping in or out unexpectedly.
  * Positioning GraphicsGroup and its Members


