Skip to main content
## 📄️ Physics
Excalibur comes built in with two physics simulations.
## 📄️ Fixed Update
Using a fixed update time step can be useful when you need a very stable and consistent physics simulation, for example if you have a precision platformer or a physics game (think billiards or angry birds).
## 📄️ Bodies
[[BodyComponent|Bodies]] are an abstraction over the collision response, are manipulated by the physics simulation during the collision resolution phase. This is the component that receives the impulse to bounce off another object.
## 📄️ Colliders
Colliders are abstractions over geometry in Excalibur, they implement the [[Collider]] interface and know how
## 📄️ Collision Events
Collision Event Lifecycle
## 📄️ Collision Groups
Collision groups are useful when you want to filter the collision that are possible between colliders
## 📄️ Collision Types
Colliders have the default collision type of [[CollisionType.Passive]], this is so colliders don't accidentally opt into something computationally expensive. In order for colliders to participate in collisions and the global physics system, colliders must have a collision type of [[CollisionType.Active]] or [[CollisionType.Fixed]].
