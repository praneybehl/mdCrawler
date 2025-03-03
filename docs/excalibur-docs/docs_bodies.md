Skip to main content
On this page
Bodies are an abstraction over the collision response, are manipulated by the physics simulation during the collision resolution phase. This is the component that receives the impulse to bounce off another object.
## Physical properties​
The physics body modules
  * Mass
  * Inertia
  * Bounciness
  * Friction


## Degrees of Freedom​
In the realistic simulation, bodies in 2D have 3 degrees of freedom, X axis, Y axis, and rotation, which can be limited using the following
```

typescript
constactor=new ex.Actor({...});
actor.body.limitDegreeOfFreedom.push(ex.DegreeOfFreedom.Rotation);
Copy
```
```

typescript
constactor=new ex.Actor({...});
actor.body.limitDegreeOfFreedom.push(ex.DegreeOfFreedom.Rotation);
Copy
```

## Gravity​
Bodies can be subject to the global acceleration (commonly used for gravity), the body must also be an CollisionType.Active
```

typescript
ex.Physics.gravity = ex.vec(0, 800); // accelerate 800 pixels down per second per second
constactor=new ex.Actor({...});
actor.body.collisionType = ex.CollisionType.Active;
actor.body.useGravity =true;
Copy
```
```

typescript
ex.Physics.gravity = ex.vec(0, 800); // accelerate 800 pixels down per second per second
constactor=new ex.Actor({...});
actor.body.collisionType = ex.CollisionType.Active;
actor.body.useGravity =true;
Copy
```

## Sleep​
In the realistic simulation, bodies can fall asleep, which is a common performance enhancement to avoid recalculating collisions for objects that aren't moving much. To adjust the threshold where objects fall asleep use the `ex.Physics.sleepEpsilon`.
This can be configured globally setting the `ex.Physics.bodiesCanSleepByDefault`, note this should be done before engine construction.
You can also wake or put a body to sleep with the `setSleeping(true)` or `setSleeping(false)`.
  * Physical properties
  * Degrees of Freedom
  * Gravity
  * Sleep


