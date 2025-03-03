Skip to main content
On this page
Core behavior in Excalibur is implemented by Systems. Systems process all entities that have matching component types and perform some action.
Examples of systems are the GraphicsSystem, MotionSystem, CollisionSystem, and DebugSystem
## System​
Each Excalibur System loops through all entities in `System.priority` order. There are a list of built in system priorities SystemPriority that can be used to assign priority. Lower number means higher priority which runs first.
```

typescript
/**
 * Higher priorities run earlier than others in the system update
 */
exportconstSystemPriority= {
 Highest: -Infinity,
 Higher: -5,
 Average: 0,
 Lower: 5,
 Lowest: Infinity
} asconst;
Copy
```
```

typescript
/**
 * Higher priorities run earlier than others in the system update
 */
exportconstSystemPriority= {
 Highest: -Infinity,
 Higher: -5,
 Average: 0,
 Lower: 5,
 Lowest: Infinity
} asconst;
Copy
```

## System Types​
There are two system types update and draw.
SystemType.Update type systems all run before SystemType.Draw type systems.
## Lifecycle​
Systems execute in this order
  1. one-time `constructor(world: World)`
     * Initialize your query here
  2. one-time `initialize(world: World, scene: Scene)`
     * Initialize anything that relies on the scene/engine here
  3. every frame `preupdate(scene: Scene, elapsedMs: number)`
     * Run setup code for the update
  4. every frame `update(delta: number)`
     * Update all your entities here
  5. every frame `postupdate(scene: Scene, elapsedMs: number)`
     * Run cleanup code for the update


## Built in Systems​
Excalibur has a few built in systems that are used to enable the default behavior. These `Systems` are defined at Scene constructor time.
### MotionSystem​
The motion system implements motion on entities, like Actors moving with velocity and acceleration.
This system makes use of the TransformComponent and MotionComponent to implement motion.
If a BodyComponent is present that will be used to apply sleep or global acceleration Physics.acc to all CollisionType.Active bodies.
### CollisionSystem​
The collision system uses the TransformComponent, MotionComponent, and ColliderComponent to implement collision detection and resolution behavior.
### GraphicsSystem​
The Excalibur GraphicsSystem takes any entity with a TransformComponent and a GraphicsComponent and draws it to the screen using the ExcaliburGraphicsContext.
### DebugSystem​
The debug system is slightly odd, it operates on all entities with a TransformComponent to display debug information to the screen when Engine.showDebug is enabled.
Read more about the debug options here Debug
## Implementing your own Components & Systems​
To build your own component, extend the Excalibur Component abstract class and pick a unique type name (duplicate type names will cause problems).
For custom component types it is recommended you prefix your types, like `type = 'myCustomPrefixTransform'`
In this example, we create a "search" type component, that searches for a target position. Notice how this component implementation is mostly data.
```

typescript
classSearchComponentextendsex.Component {
constructor(publictarget:ex.Vector) {
super();
  }
}
classSearchSystemextendsex.System {
query:Query<typeof SearchComponent>;
constructor(world:World) {
this.query = world.query([TransformComponent, SearchComponent]);
 }
// Lower numbers mean higher priority
// 99 is low priority
publicpriority=99;
// Run this system in the "update" phase
publicsystemType= ex.SystemType.Update
private_searchSpeed=100// pixels/sec
publicupdate(delta:number) {
for (let entity ofthis.query.entities) {
consttarget= entity.get(SearchComponent).target;
consttransform= entity.get(ex.TransformComponent);
constdirection= target.sub(transform.pos);
constmotion= direction.normalize().scale(this._searchSpeed);
// Moves these entities towards the target at 10 pixels per second
    transform.pos = transform.pos.add(motion.scale(delta /1000))
  }
 }
}
constscene=new ex.Scene();
scene.world.add(SearchSystem);
// Actors come with batteries included built in features
constactor=new ex.Actor({
  pos: ex.vec(100, 100),
  width: 30,
  height: 30,
  color: ex.Color.Red
});
actor.addComponent(newSearchComponent(ex.vec(600, 400)));
Copy
```
```

typescript
classSearchComponentextendsex.Component {
constructor(publictarget:ex.Vector) {
super();
  }
}
classSearchSystemextendsex.System {
query:Query<typeof SearchComponent>;
constructor(world:World) {
this.query = world.query([TransformComponent, SearchComponent]);
 }
// Lower numbers mean higher priority
// 99 is low priority
publicpriority=99;
// Run this system in the "update" phase
publicsystemType= ex.SystemType.Update
private_searchSpeed=100// pixels/sec
publicupdate(delta:number) {
for (let entity ofthis.query.entities) {
consttarget= entity.get(SearchComponent).target;
consttransform= entity.get(ex.TransformComponent);
constdirection= target.sub(transform.pos);
constmotion= direction.normalize().scale(this._searchSpeed);
// Moves these entities towards the target at 10 pixels per second
    transform.pos = transform.pos.add(motion.scale(delta /1000))
  }
 }
}
constscene=new ex.Scene();
scene.world.add(SearchSystem);
// Actors come with batteries included built in features
constactor=new ex.Actor({
  pos: ex.vec(100, 100),
  width: 30,
  height: 30,
  color: ex.Color.Red
});
actor.addComponent(newSearchComponent(ex.vec(600, 400)));
Copy
```

Any entity that has the new component attached will be processed by the new system once added to the world!
  * System
  * System Types
  * Lifecycle
  * Built in Systems
    * [[MotionSystem]]
    * [[CollisionSystem]]
    * [[GraphicsSystem]]
    * [[DebugSystem]]
  * Implementing your own Components & Systems


