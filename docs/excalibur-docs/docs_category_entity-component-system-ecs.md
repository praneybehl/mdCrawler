Skip to main content
## 📄️ ECS
Excalibur has a built in Entity Component System (ECS for short), which is a popular software technique in the video game industry
## 📄️ Entities
An [[Entity]] in is an empty container for [[Component|Components]] which store data, alone an Entity has little behavior.
## 📄️ Components
[[Component|Components]] are a useful tool for storing data associated with an entity. Components can be used with [[System|Systems]] to implement complex behavior. Sometimes [[Component|Components]] can be a better choice than using inheritance. Components provide reusable behavior that can be easier to maintain over complex inheritance hierarchies.
## 📄️ Systems
Core behavior in Excalibur is implemented by Systems. Systems process all entities that have matching component types and perform some action.
## 📄️ Queries
[[Query|Queries]] can be used to identify Entities that match a certain type. This is useful if you need to maintain a list of entities that match
