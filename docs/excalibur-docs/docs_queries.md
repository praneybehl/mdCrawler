Skip to main content
On this page
Queries can be used to identify Entities that match a certain type. This is useful if you need to maintain a list of entities that match a list of component types or tags. Queries update automatically as part of the World update.
## Component Query​
Component queries are the heart and soul of Systems, these allow you to find all the entities that have a list of desired components.
```

typescript
constgame=new ex.Engine({...});
constentityA=new ex.Entity();
entityA.addComponent(new ex.TransformComponent());
constentityB=new ex.Entity();
entityB.addComponent(new ex.MotionComponent());
game.currentScene.add(entityA);
game.currentScene.add(entityB);
constqueryA= game.currentScene.world.query([ex.TransformComponent]);
constqueryB= game.currentScene.world.query([ex.MotionComponent]);
console.log(entityA === queryA.entities[0]); // true
console.log(entityB === queryB.entities[0]); // true
Copy
```
```

typescript
constgame=new ex.Engine({...});
constentityA=new ex.Entity();
entityA.addComponent(new ex.TransformComponent());
constentityB=new ex.Entity();
entityB.addComponent(new ex.MotionComponent());
game.currentScene.add(entityA);
game.currentScene.add(entityB);
constqueryA= game.currentScene.world.query([ex.TransformComponent]);
constqueryB= game.currentScene.world.query([ex.MotionComponent]);
console.log(entityA === queryA.entities[0]); // true
console.log(entityB === queryB.entities[0]); // true
Copy
```

## Tag Query​
It is possible query all entities by their tags! This can be useful for flagging entities as dead, hostile, aggressive, having some status effect, etc.
```

typescript
constgame=new ex.Engine({...});
constentityA=new ex.Entity();
entityA.addTag("tagA");
constentityB=new ex.Entity();
entityB.addTag("tagB");
game.currentScene.add(entityA);
game.currentScene.add(entityB);
constqueryA= game.currentScene.world.queryTags(["tagA"]);
constqueryB= game.currentScene.world.queryTags(["tagB"]);
constentityA= queryA.entities[0];
constentityB= queryB.entities[0];
Copy
```
```

typescript
constgame=new ex.Engine({...});
constentityA=new ex.Entity();
entityA.addTag("tagA");
constentityB=new ex.Entity();
entityB.addTag("tagB");
game.currentScene.add(entityA);
game.currentScene.add(entityB);
constqueryA= game.currentScene.world.queryTags(["tagA"]);
constqueryB= game.currentScene.world.queryTags(["tagB"]);
constentityA= queryA.entities[0];
constentityB= queryB.entities[0];
Copy
```

  * Component Query
  * Tag Query


