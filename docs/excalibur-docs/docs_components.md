Skip to main content
On this page
Components are a useful tool for storing data associated with an entity. Components can be used with Systems to implement complex behavior. Sometimes Components can be a better choice than using inheritance. Components provide reusable behavior that can be easier to maintain over complex inheritance hierarchies.
note
Excalibur is not a "pure" ECS, so building components with behavior is perfectly acceptable. Often this is really useful for sharing behavior.
## Custom Components​
To create a new component, you must extend the built in component class.
```

typescript
exportclassMyComponentextendsex.Component {
publicmyData:string='my custom data';
}
Copy
```
```

typescript
exportclassMyComponentextendsex.Component {
publicmyData:string='my custom data';
}
Copy
```

## Built in Excalibur Components​
### TransformComponent​
The Excalibur TransformComponent component primarily keeps track of the z-index position, rotation, and scale of an entity.
Additionally it keeps track of the coordinate plane which is whether it draws to the CoordPlane.Screen or part of the CoordPlane.World. The default is drawing in CoordPlane.World which shifts the entities in "world space" by the position of the current Camera If you are drawing in CoordPlane.Screen the entity is not influenced by the camera, for example an entity at (0, 0) will always be at the top left of the screen regardless of what happens to the current Camera.
### MotionComponent​
The MotionComponent keeps track of velocities, acceleration, torque, and inertia on an Entity. Motion component velocity units are in pixels per second.
### GraphicsComponent​
The GraphicsComponent holds an excalibur Graphic and draws it to the screen for an entity. The GraphicsComponent can only show 1 graphic at a time, to show more use a GraphicsGroup or child entities with graphics components.
  1. A GraphicsGroup, you can specify a list of graphics in painter order (first is draw first, then so on) ```

typescript
constactor=new ex.Actor({...});
constgraphicsGroup=new ex.GraphicsGroup({
 members: [
new ex.Rectangle({width: 100, height: 100, color: ex.Color.Red}),
  { offset: ex.vec(100, 100), graphic: new ex.Circle({radius: 100, color: ex.Color.Blue})}
 ]
});
actor.graphics.use(graphicsGroup);
Copy
```
```

typescript
constactor=new ex.Actor({...});
constgraphicsGroup=new ex.GraphicsGroup({
 members: [
new ex.Rectangle({width: 100, height: 100, color: ex.Color.Red}),
  { offset: ex.vec(100, 100), graphic: new ex.Circle({radius: 100, color: ex.Color.Blue})}
 ]
});
actor.graphics.use(graphicsGroup);
Copy
```

  2. Child actors if you need more control over graphic movement, transform, or behavior ```

typescript
constactor=new ex.Actor({...});
constchild=new ex.Actor({
 pos: ex.vec(100, 100),
 rotation: Math.PI/4,
 scale: ex.vec(3, 3)
});
actor.addChild(child);
actor.graphics.use(new ex.Rectangle({width: 100, height: 100, color: ex.Color.Red}));
child.graphics.use(new ex.Rectangle({width: 10, height: 10, color: ex.Color.Blue}));
Copy
```
```

typescript
constactor=new ex.Actor({...});
constchild=new ex.Actor({
 pos: ex.vec(100, 100),
 rotation: Math.PI/4,
 scale: ex.vec(3, 3)
});
actor.addChild(child);
actor.graphics.use(new ex.Rectangle({width: 100, height: 100, color: ex.Color.Red}));
child.graphics.use(new ex.Rectangle({width: 10, height: 10, color: ex.Color.Blue}));
Copy
```



### PointerComponent​
The PointerComponent configures pointer event behavior on entities. Entities only receive pointer events if they have the component.
### ActionsComponent​
The ActionsComponent is useful for producing scripted behavior on an entity. Read more here
For example:
```

typescript
constentity=new ex.Entity();
constactions=newActionsComponent();
entity.add(actions);
actions.repeatForever(ctx=> {
 ctx.moveTo(100, 100, 100); // moveTo (100, 100) at 100 pixels/sec
 ctx.moveTo(0, 0, 100); // moveTo (0, 0) at 100 pixels/sec
});
Copy
```
```

typescript
constentity=new ex.Entity();
constactions=newActionsComponent();
entity.add(actions);
actions.repeatForever(ctx=> {
 ctx.moveTo(100, 100, 100); // moveTo (100, 100) at 100 pixels/sec
 ctx.moveTo(0, 0, 100); // moveTo (0, 0) at 100 pixels/sec
});
Copy
```

  * Custom Components
  * Built in Excalibur Components
    * [[TransformComponent]]
    * [[MotionComponent]]
    * [[GraphicsComponent]]
    * [[PointerComponent]]
    * [[ActionsComponent]]


