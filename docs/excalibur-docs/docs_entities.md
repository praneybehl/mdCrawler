Skip to main content
On this page
An Entity in is an empty container for Components which store data, alone an Entity has little behavior.
They are useful for defining bare bones game objects with custom behavior.
If you want a batteries included prebuilt Entity use an Actor, read more here. Remember an Excalibur Actor is just an Entity with a list of prebuilt components and some useful apis built over them.
## Entity​
Entities have no behavior by default, only a few lifecycle hooks `onInitialize`, and a concept of parent/children.
Building and adding an entity to a game is pretty straightforward.
```

typescript
constgame=new ex.Engine({...});
constentity=new ex.Entity();
constentityWithName=new ex.Entity({name: 'Named Entity'});
game.currentScene.add(entity);
Copy
```
```

typescript
constgame=new ex.Engine({...});
constentity=new ex.Entity();
constentityWithName=new ex.Entity({name: 'Named Entity'});
game.currentScene.add(entity);
Copy
```

## Child Entities​
Entities can be added as children of other entities, once added child entities move relative to their parents.
  * `Entity.parent` - Returns the parent of this entity, if one exists otherwise returns `null`
  * `Entity.children` - Returns the list of child entities, otherwise returns an empty list
  * `Entity.unparent()` - Removes this entity from its parent this entity
  * `Entity.addChild(entity)` - Add a child to this entity
  * `Entity.removeChild(entity)` - Remove a child
  * `Entity.removeAllChildren()` - Removal all children


## Lifecycle​
  * `onInitialize` happens before first update
  * `onPreUpdate` happens at the beginning of update
  * `onPostUpdate` happens at the end of the update


## Components​
Components can be added and removed from an entity. Only 1 instance of a component type can be part of an entity at at time.
When removing components removal is deferred until the end of the update, unless forced. Deferred removal is useful to prevent bugs where an entity is only partially processed by all applicable systems.
```

typescript
constentity=new ex.Entity()
entity.addComponent(new ex.TransformComponent())
// Remove by type or instances
entity.removeComponent(ex.TransformComponent)
// Force removal
entity.removeComponent(ex.TransformComponent, true)
Copy
```
```

typescript
constentity=new ex.Entity()
entity.addComponent(new ex.TransformComponent())
// Remove by type or instances
entity.removeComponent(ex.TransformComponent)
// Force removal
entity.removeComponent(ex.TransformComponent, true)
Copy
```

Components can be retrieved by type name, however if the component doesn't exist undefined will be returned.
```

typescript
constentity=new ex.Entity()
constmaybeTransform= entity.get(ex.TransformComponent)
if (maybeTransform) {
 console.log(maybeTransform.pos)
}
Copy
```
```

typescript
constentity=new ex.Entity()
constmaybeTransform= entity.get(ex.TransformComponent)
if (maybeTransform) {
 console.log(maybeTransform.pos)
}
Copy
```

Entities can be checked for components as well
```

typescript
constentity=new ex.Entity()
if (entity.has(ex.TransformComponent)) {
 console.log('Entity has a transform component')
}
Copy
```
```

typescript
constentity=new ex.Entity()
if (entity.has(ex.TransformComponent)) {
 console.log('Entity has a transform component')
}
Copy
```

All the components can be retrieved at once
```

typescript
constcomponents:Component[] = entity.getComponents()
Copy
```
```

typescript
constcomponents:Component[] = entity.getComponents()
Copy
```

## Tags​
Tags are special components that are only types. Useful when the presence of a component is all that is needed.
  * `Entity.addTag("someTag")` - Add a tag to an entity
  * `Entity.removeTag("someTag")` - Remove a tag on an entity
  * `Entity.hasTag("someTag")` - Check if a tag exists


## Templates aka Prefab​
  * Entity.addTemplate(TemplateEntity)


## EntityManager​
  * EntityManager.getById(entityId)
  * EntityManager.getByName(entityName)


  * Entity
  * Child Entities
  * Lifecycle
  * Components
  * Tags
  * Templates aka Prefab
  * EntityManager


