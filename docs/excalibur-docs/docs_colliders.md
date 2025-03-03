Skip to main content
On this page
Colliders are abstractions over geometry in Excalibur, they implement the Collider interface and know how to detect intersecions with other colliders, test ray casts, check point containment, etc. Related but not the same are bodies which are abstractions over the collision response
Colliders attached to an Entity will have a owner populated.
note
**Keep in mind** colliders are relative to the owner TransformComponent, they only represent geometry relative to an entity TransformComponent. Colliders can be shifted using the Collider.offset.
Colliders don't have a position in the world without an Actor/Entity with a position
### CircleCollider​
The CircleCollider defines a circular geometry and can be created and added to an actor
```

typescript
// Actors have a built in circle collider if radius is set
constactorWithCircleCollider=new ex.Actor({
 pos: ex.vec(5, 5),
 radius: 10
});
// Alternatively you can define and set a collider yourself
constcircle=new ex.CircleCollider({
 radius: 10// 10 pixel radius
});
// or
constcircle= ex.Shape.Circle(10); // 10 pixel radius
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: circle
});
// Change the collider afterwards
actor.collider.set(circle);
Copy
```
```

typescript
// Actors have a built in circle collider if radius is set
constactorWithCircleCollider=new ex.Actor({
 pos: ex.vec(5, 5),
 radius: 10
});
// Alternatively you can define and set a collider yourself
constcircle=new ex.CircleCollider({
 radius: 10// 10 pixel radius
});
// or
constcircle= ex.Shape.Circle(10); // 10 pixel radius
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: circle
});
// Change the collider afterwards
actor.collider.set(circle);
Copy
```

### Box and PolygonCollider​
The PolygonCollider allows the definition of arbitrary **convex** polygons. Convex meaning there are no dents in the shape, for example "Pac-Man" would be a non-convex shape.
A box collider is created using the PolygonCollider, there is a Shape.Box helper to build these.
```

typescript
// Actors have a built in box collider if width/height are set
constactorWithBoxCollider=new ex.Actor({
 pos: ex.vec(100, 100),
 width: 100,
 height: 10
});
// Alternatively you can define and set a collider yourself
constbox= ex.Shape.Box(100, 10);
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: box
});
Copy
```
```

typescript
// Actors have a built in box collider if width/height are set
constactorWithBoxCollider=new ex.Actor({
 pos: ex.vec(100, 100),
 width: 100,
 height: 10
});
// Alternatively you can define and set a collider yourself
constbox= ex.Shape.Box(100, 10);
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: box
});
Copy
```

A polygon collider can be defined using a set of points specified in clockwise order (also known as "winding").
```

typescript
consttriangle=new ex.PolygonCollider({
 points: [ex.vec(-100, 0), ex.vec(0, -50), ex.vec(100, 0)]
});
Copy
```
```

typescript
consttriangle=new ex.PolygonCollider({
 points: [ex.vec(-100, 0), ex.vec(0, -50), ex.vec(100, 0)]
});
Copy
```

### EdgeCollider​
An EdgeCollider can be used to define a single line collider.
They are useful for creating walls, barriers, or platforms in your game.
Edge points are relative to the Entity position, so begin of `(0, 0)` means it starts right on the top of the Entity TransformComponent
```

typescript
constedge=new ex.EdgeCollider({
 begin: ex.vec(0, 0),
 end: ex.vec(100, 0)
});
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: edge
});
Copy
```
```

typescript
constedge=new ex.EdgeCollider({
 begin: ex.vec(0, 0),
 end: ex.vec(100, 0)
});
constactor=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: edge
});
Copy
```

### CompositeCollider​
CompositeCollider can be used to attach multiple colliders to an entity at once. This can be useful when generating complex shapes, like for example a capsule collider for a player Actor.
```

typescript
// Capsule Collider
constcapsule=new ex.CompositeCollider([ex.Shape.Circle(10, ex.vec(0, -20)), ex.Shape.Box(20, 40), ex.Shape.Circle(10, ex.vec(0, 20))]);
constplayer=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: capsule
});
Copy
```
```

typescript
// Capsule Collider
constcapsule=new ex.CompositeCollider([ex.Shape.Circle(10, ex.vec(0, -20)), ex.Shape.Box(20, 40), ex.Shape.Circle(10, ex.vec(0, 20))]);
constplayer=new ex.Actor({
 pos: ex.vec(100, 100),
 collider: capsule
});
Copy
```

### Child Actor​
Another way of accomplishing complex collision logic is to add child actors with different colliders and handlers.
This is can be useful for implementing area of effect collisions or sensors when objects get close to each other.
For example:
```

typescript
constplayer=new ex.Actor({...});
constsensor=new ex.Actor({
 radius: 100
});
player.addChild(sensor);
sensor.on('collisionstart', (evt) => {
if (evt.other !== player) {
  console.log('something is within 100 pixels of player');
 }
})
Copy
```
```

typescript
constplayer=new ex.Actor({...});
constsensor=new ex.Actor({
 radius: 100
});
player.addChild(sensor);
sensor.on('collisionstart', (evt) => {
if (evt.other !== player) {
  console.log('something is within 100 pixels of player');
 }
})
Copy
```

  * CircleCollider
  * Box and PolygonCollider
  * EdgeCollider
  * CompositeCollider
  * Child Actor


