Skip to main content
On this page
Animations are a series of graphics that take a specific duration in milliseconds. Each of these units is called a "Frame". There are a few playing strategies as well to consider
```

ts
exportenumAnimationStrategy {
/**
  * Animation ends without displaying anything
  */
 End ='end',
/**
  * Animation loops to the first frame after the last frame
  */
 Loop ='loop',
/**
  * Animation plays to the last frame, then backwards to the first frame, then repeats
  */
 PingPong ='pingpong',
/**
  * Animation ends stopping on the last frame
  */
 Freeze ='freeze',
}
Copy
```
```

ts
exportenumAnimationStrategy {
/**
  * Animation ends without displaying anything
  */
 End ='end',
/**
  * Animation loops to the first frame after the last frame
  */
 Loop ='loop',
/**
  * Animation plays to the last frame, then backwards to the first frame, then repeats
  */
 PingPong ='pingpong',
/**
  * Animation ends stopping on the last frame
  */
 Freeze ='freeze',
}
Copy
```
```

ts
constanimation=new ex.Animation({
 frames: [
  {
   graphic: newSprite,
   duration: 500,
  },
  {
   graphic: circle,
   duration: 1000,
  },
  {
   graphic: rect,
   duration: 1500,
  },
  {
   graphic: triangle,
   duration: 2000,
  },
 ],
});
Copy
```
```

ts
constanimation=new ex.Animation({
 frames: [
  {
   graphic: newSprite,
   duration: 500,
  },
  {
   graphic: circle,
   duration: 1000,
  },
  {
   graphic: rect,
   duration: 1500,
  },
  {
   graphic: triangle,
   duration: 2000,
  },
 ],
});
Copy
```

## Animation From SpriteSheet​
Animations can also be constructed quickly from `ex.SpriteSheets`.
Animation frames can be created by hand in the following example by specifying the sprite sheet indices from the top left, top to bottom (row major order).
![Character running sprite sheet](https://excaliburjs.com/assets/images/player-run-43f110652c0efed153e43ba4126a14a2.png)
Additionally you can specify the (x, y) positions of sprites in the SpriteSheet of each frame, for example (0, 0) is the the top left sprite, (0, 1) is the sprite directly below that, and so on.
## Events​
Animations also emit events per frame, per loop, and per end (if it completes).
```

ts
animation.events.on('loop', (a) => {
 console.log('loop')
})
animation.events.on('frame', (f) => {
 console.log('frame')
})
animation.events.on('end', (a) => {
 console.log('ended')
})
Copy
```
```

ts
animation.events.on('loop', (a) => {
 console.log('loop')
})
animation.events.on('frame', (f) => {
 console.log('frame')
})
animation.events.on('end', (a) => {
 console.log('ended')
})
Copy
```

  * Animation From SpriteSheet
  * Events


