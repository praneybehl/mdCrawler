Skip to main content
On this page
Nearly everything in Excalibur has a way to listen to events! This is useful when you want to know exactly when things happen in Excalibur and respond to them with game logic. Actors, Scenes, Engines, Actions, Animations, and various components have events you can hook into just look for the `.events` member!
info
Excalibur events are handled synchronously, which is great for debugging and reducing timing bugs.
## Strongly-typed Events​
Excalibur has types on all it's event listeners, you can check these types with Intellisense in VS Code or by following the Typescript definition.
![event auto complete](https://excaliburjs.com/assets/images/events-a199b6327bc581f84c7034e10a7d4436.png)
## Pub/Sub or Signal-based Event Bus​
Excalibur also allows you to listen/send any event you want to as well, but you'll need to provide your own types for that. At its core, the EventEmitter is a pub/sub mechanism (also called "Signals" in other engines), which means you can create an emitter as a way to pass messages between entities, components, or systems. This is how much of Excalibur works internally.
### Example: Health Depletion​
Here is an example of emitting a custom `healthdepleted` event that is strongly-typed:
```

ts
typePlayerEvents= {
healthdepleted:PlayerHealthDepletedEvent;
}
exportclassPlayerHealthDepletedEventextendsex.GameEvent<Player> {
constructor(publictarget:Player) {
super();
 }
}
exportconstPlayerEvents= {
 Healthdepleted: 'healthdepleted'
} asconst;
exportclassPlayerextendsex.Actor {
publicevents=new ex.EventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit(PlayerEvents.Healthdepleted, newPlayerHealthDepletedEvent(this));
  }
 }
}
Copy
```
```

ts
typePlayerEvents= {
healthdepleted:PlayerHealthDepletedEvent;
}
exportclassPlayerHealthDepletedEventextendsex.GameEvent<Player> {
constructor(publictarget:Player) {
super();
 }
}
exportconstPlayerEvents= {
 Healthdepleted: 'healthdepleted'
} asconst;
exportclassPlayerextendsex.Actor {
publicevents=new ex.EventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit(PlayerEvents.Healthdepleted, newPlayerHealthDepletedEvent(this));
  }
 }
}
Copy
```

There are three main parts to this example:
  1. The `type` declaration holds the mapping of event name to event class.
  2. A `class` representing the custom event which can extend GameEvent
  3. A `const` declaration to provide a public way to pass the event name without using strings _(optional)_


tip
The third is optional but recommended to avoid "magic strings" especially for events used all over your codebase.
Finally, you can expose an EventEmitter on your entity for other entities to subscribe/publish to. In this case, Actor.events is already provided by Excalibur, so you need to intersect your custom events with the existing events.
note
You don't _have to_ override the existing Actor.events property. You could also export a static emitter, or use a different property name. This example emitter lifecycle is tied to the `Player` and maintains a consistent way to emit other events but its just to illustrate a way to accomplish pub/sub.
### Example: Strict Event Names​
By default, EventEmitter is flexible to allow _any_ `string` event name and _any_ event.
If you want more strictness with TypeScript, you can do it by deriving a custom event emitter that overrides the various overloaded methods to only allow strict event key names.
In this example, there's a typo, and a compiler error is thrown:
```

ts
typeStrictEventKey<TEventMap> =keyofTEventMap;
classStrictEventEmitter<TEventMapextendsex.EventMap> extendsex.EventEmitter<TEventMap> {
emit<TEventNameextendsStrictEventKey<TEventMap>>(eventName:TEventName, event:TEventMap[TEventName]):void;
emit<TEventNameextendsStrictEventKey<TEventMap> |string>(eventName:TEventName, event?:TEventMap[TEventName]):void {
super.emit(eventName asany, event asany);
 }
}
exportclassPlayerextendsex.Actor {
publicevents=newStrictEventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit("healthdpleted", newPlayerHealthDepletedEvent(this));
Argument of type '"healthdpleted"' is not assignable to parameter of type '"healthdepleted" | keyof EntityEvents | "collisionstart" | "collisionend" | "precollision" | "postcollision" | "prekill" | "postkill" | "predraw" | "postdraw" | ... 19 more ... | "actioncomplete"'.2345Argument of type '"healthdpleted"' is not assignable to parameter of type '"healthdepleted" | keyof EntityEvents | "collisionstart" | "collisionend" | "precollision" | "postcollision" | "prekill" | "postkill" | "predraw" | "postdraw" | ... 19 more ... | "actioncomplete"'.
  }
 }
}
Copy
```
```

ts
typeStrictEventKey<TEventMap> =keyofTEventMap;
classStrictEventEmitter<TEventMapextendsex.EventMap> extendsex.EventEmitter<TEventMap> {
emit<TEventNameextendsStrictEventKey<TEventMap>>(eventName:TEventName, event:TEventMap[TEventName]):void;
emit<TEventNameextendsStrictEventKey<TEventMap> |string>(eventName:TEventName, event?:TEventMap[TEventName]):void {
super.emit(eventName asany, event asany);
 }
}
exportclassPlayerextendsex.Actor {
publicevents=newStrictEventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit("healthdpleted", newPlayerHealthDepletedEvent(this));
Argument of type '"healthdpleted"' is not assignable to parameter of type '"healthdepleted" | keyof EntityEvents | "collisionstart" | "collisionend" | "precollision" | "postcollision" | "prekill" | "postkill" | "predraw" | "postdraw" | ... 19 more ... | "actioncomplete"'.2345Argument of type '"healthdpleted"' is not assignable to parameter of type '"healthdepleted" | keyof EntityEvents | "collisionstart" | "collisionend" | "precollision" | "postcollision" | "prekill" | "postkill" | "predraw" | "postdraw" | ... 19 more ... | "actioncomplete"'.
  }
 }
}
Copy
```

But when passing the appropriate constant, the error is gone:
```

ts
exportclassPlayerextendsex.Actor {
publicevents=newStrictEventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit(PlayerEvents.Healthdepleted, newPlayerHealthDepletedEvent(this));
  }
 }
}
Copy
```
```

ts
exportclassPlayerextendsex.Actor {
publicevents=newStrictEventEmitter<ex.ActorEvents&PlayerEvents>();
privatehealth:number=100;
publiconPostUpdate() {
if (this.health <=0) {
this.events.emit(PlayerEvents.Healthdepleted, newPlayerHealthDepletedEvent(this));
  }
 }
}
Copy
```

note
This example is intentionally only showing the `emit` method, but you can override all the methods in the same way.
  * Strongly-typed Events
  * Pub/Sub or Signal-based Event Bus
    * Example: Health Depletion
    * Example: Strict Event Names


