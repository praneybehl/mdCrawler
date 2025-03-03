Skip to main content
On this page
Excalibur handles mouse and touch input by abstracting event handling into a engine.input.pointers API that closely follows the W3C Pointer Events spec. Excalibur normalizes both mouse and touch events to a single PointerEvent that your game can subscribe to and handle.
## The Primary Pointer​
There is always at least one Pointer available (engine.input.pointers.primary) and you can request multiple pointers to support multi-touch scenarios.
```

ts
engine.input.pointers.primary;
Copy
```
```

ts
engine.input.pointers.primary;
Copy
```

Since a pointer normalizes both mouse and touch events, your game automatically supports touch for the primary pointer by default. When you handle the events, you can customize what your game does based on the type of pointer, if applicable.
## Handling Pointer Events Globally​
You can subscribe (or unsubscribe) to pointer events multiple ways using the on, once, or off methods. Each method takes two arguments: the event name and the handler.
```

ts
engine.input.pointers.primary.o
                               
  * off
  * on
  * once


Copy
```
```

ts
engine.input.pointers.primary.o
                               
  * off
  * on
  * once


Copy
```

You can subscribe to the primary pointer, all pointers, or a specific pointer.
```

ts
// Subscribe to the primary pointer
engine.input.pointers.primary.on;
(method) PointerAbstraction.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
// Subscribe to a specific pointer (multi-touch)
engine.input.pointers.at(1).on;
(method) PointerAbstraction.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
// Subscribe to all pointers (advanced)
engine.input.pointers.on;
(method) PointerEventReceiver.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
Copy
```
```

ts
// Subscribe to the primary pointer
engine.input.pointers.primary.on;
(method) PointerAbstraction.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
// Subscribe to a specific pointer (multi-touch)
engine.input.pointers.at(1).on;
(method) PointerAbstraction.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
// Subscribe to all pointers (advanced)
engine.input.pointers.on;
(method) PointerEventReceiver.on<TEventName extends ex.EventKey<PointerEvents>>(eventName: TEventName, handler: ex.Handler<PointerEvents[TEventName]>): ex.Subscription (+1 overload)
Copy
```

### Event Names​
The event name is a string and can be one of the following:
  * `down` - When a pointer is pressed down (any mouse button or finger press)
  * `up` - When a pointer is lifted
  * `move` - When a pointer moves (be wary of performance issues when subscribing to this)
  * `cancel` - When a pointer event is canceled for some reason
  * `wheel` - When a mousewheel is activated (trackpad scroll or mouse wheel)


### Event Handlers​
A PointerEvent object (or in the case of `wheel`, a WheelEvent) is passed to your handler which offers information about the pointer input being received.
```

ts
// Subscribe to the primary pointer
engine.input.pointers.primary.on('down', function (evt) {});
(parameter) evt: ex.PointerEvent
engine.input.pointers.primary.on('up', function (evt) {});
engine.input.pointers.primary.on('move', function (evt) {});
engine.input.pointers.primary.on('cancel', function (evt) {});
engine.input.pointers.primary.on('wheel', function (evt) {});
(parameter) evt: ex.WheelEvent
// Subscribe to a specific pointer (multi-touch)
engine.input.pointers.at(1).on('down', function (evt) {});
engine.input.pointers.at(1).on('up', function (evt) {});
engine.input.pointers.at(1).on('move', function (evt) {});
engine.input.pointers.at(1).on('cancel', function (evt) {});
engine.input.pointers.at(1).on('wheel', function (evt) {});
// Subscribe to all pointers (advanced)
engine.input.pointers.on('down', function (evt) {});
engine.input.pointers.on('up', function (evt) {});
engine.input.pointers.on('move', function (evt) {});
engine.input.pointers.on('cancel', function (evt) {});
engine.input.pointers.on('wheel', function (evt) {});
Copy
```
```

ts
// Subscribe to the primary pointer
engine.input.pointers.primary.on('down', function (evt) {});
(parameter) evt: ex.PointerEvent
engine.input.pointers.primary.on('up', function (evt) {});
engine.input.pointers.primary.on('move', function (evt) {});
engine.input.pointers.primary.on('cancel', function (evt) {});
engine.input.pointers.primary.on('wheel', function (evt) {});
(parameter) evt: ex.WheelEvent
// Subscribe to a specific pointer (multi-touch)
engine.input.pointers.at(1).on('down', function (evt) {});
engine.input.pointers.at(1).on('up', function (evt) {});
engine.input.pointers.at(1).on('move', function (evt) {});
engine.input.pointers.at(1).on('cancel', function (evt) {});
engine.input.pointers.at(1).on('wheel', function (evt) {});
// Subscribe to all pointers (advanced)
engine.input.pointers.on('down', function (evt) {});
engine.input.pointers.on('up', function (evt) {});
engine.input.pointers.on('move', function (evt) {});
engine.input.pointers.on('cancel', function (evt) {});
engine.input.pointers.on('wheel', function (evt) {});
Copy
```

### Querying the Last Position​
If you don't wish to subscribe to events, you can also access the PointerAbstraction.lastPagePos, PointerAbstraction.lastScreenPos or PointerAbstraction.lastWorldPos coordinates (Vector) on the pointer you're targeting.
```

ts
engine.input.pointers.primary.lastPagePos;
engine.input.pointers.primary.lastScreenPos;
engine.input.pointers.primary.lastWorldPos;
Copy
```
```

ts
engine.input.pointers.primary.lastPagePos;
engine.input.pointers.primary.lastScreenPos;
engine.input.pointers.primary.lastWorldPos;
Copy
```

note
The value may be `null` if the Pointer was not active the last frame.
### Scoping Events to Canvas vs. Document​
You can customize how pointer events are handled by setting the EngineOptions.pointerScope option when creating a new Engine instance, like this:
```

ts
constgame=new ex.Engine({
 pointerScope: ex.PointerScope.C
});
Copy
```
```

ts
constgame=new ex.Engine({
 pointerScope: ex.PointerScope.C
});
Copy
```

The default scope is PointerScope.Canvas. For many games, this works really well. It scopes event handling to the game canvas.
This is useful if you don't care about events that occur outside the game.
You also have the option to handle _all_ pointer events in the browser window by using PointerScope.Document, like this:
```

ts
constgame=new ex.Engine({
 pointerScope: ex.PointerScope.D
});
Copy
```
```

ts
constgame=new ex.Engine({
 pointerScope: ex.PointerScope.D
});
Copy
```

This is useful for handling complex input and having control over every interaction.
When to Use Document Scope
One real-world example is dragging and gestures. Sometimes a player will drag their finger outside your game and then into it, expecting it to work. If PointerScope is set to Canvas this will not work. If it is set to Document, it will.
What about HTML elements?
`PointerScope.Canvas` does not affect handling native HTML events like `click`, `mouseover`, `mouseout`, etc. on any HTML-based UI. It only applies to pointer events that are targeted to the HTML `<canvas>` element Excalibur uses to render your game.
However, `PointerScope.Document` will handle all pointer events in the browser window, including those targeted to HTML elements. If you overlay any HTML elements on top of your game, be aware that pointer events will also be handled by Excalibur.
## Handling Pointer Events on Actors​
Actors can handle pointer events targeted to them. By default, the collision geometry is used to test whether the pointer is in or out of the actor.
In the example below the actor has default box geometry of 100x100:
```

ts
classMyActorextendsex.Actor {
constructor() {
super({
   pos: ex.vec(200, 200),
   width: 100,
   height: 100
  });
this.on('pointerenter', () => {
   console.log('enter')
  });
this.on('pointerleave', () => {
   console.log('leave')
  });
 }
}
Copy
```
```

ts
classMyActorextendsex.Actor {
constructor() {
super({
   pos: ex.vec(200, 200),
   width: 100,
   height: 100
  });
this.on('pointerenter', () => {
   console.log('enter')
  });
this.on('pointerleave', () => {
   console.log('leave')
  });
 }
}
Copy
```

warning
If your Actor has no geometry and only graphics you will need to enable graphics bounds testing.
### Graphics Bounds Testing​
Rather than using the collision geometry, you can use the graphics bounds to test whether the pointer is in or out of the actor. This is useful when you have an actor with no collision geometry and only graphics, or when the graphics have custom dimensions that don't match the collision geometry.
To enable graphics bounds testing for pointer events you can grab the Actor's PointerComponent with `this.pointer` and set `useGraphicsBounds` to `true`.
```

ts
classMyGraphicsActorextendsex.Actor {
constructor(image:ex.ImageSource) {
super({pos: ex.vec(200, 200)});
this.pointer.useGraphicsBounds =true;
this.graphics.use(image.toSprite());
this.on('pointerenter', () => {
   console.log('enter')
  });
this.on('pointerleave', () => {
   console.log('leave')
  });
 }
}
Copy
```
```

ts
classMyGraphicsActorextendsex.Actor {
constructor(image:ex.ImageSource) {
super({pos: ex.vec(200, 200)});
this.pointer.useGraphicsBounds =true;
this.graphics.use(image.toSprite());
this.on('pointerenter', () => {
   console.log('enter')
  });
this.on('pointerleave', () => {
   console.log('leave')
  });
 }
}
Copy
```

### Actor Pointer Event List​
Actors have the following **extra** events you can subscribe to:
  * `pointerenter` - When a pointer enters the bounds of an actor
  * `pointerleave` - When a pointer leaves the bounds of an actor
  * `pointerdragstart` - When a pointer starts a drag on an actor
  * `pointerdragmove` - When a pointer drags an actor
  * `pointerdragend` - When a pointer ends a drag on an actor


## Checking the Pointer Type​
The primary pointer can be a mouse, stylus, or single finger touch event. You can inspect what type of pointer it is from the PointerEvent handled.
```

ts
engine.input.pointers.primary.on('down', function (pe:ex.PointerEvent) {
if (pe.pointerType === ex.PointerType.Mouse) {
  ex.Logger.getInstance().info('Mouse event:', pe);
 } elseif (pe.pointerType === ex.PointerType.Touch) {
  ex.Logger.getInstance().info('Touch event:', pe);
 }
});
Copy
```
```

ts
engine.input.pointers.primary.on('down', function (pe:ex.PointerEvent) {
if (pe.pointerType === ex.PointerType.Mouse) {
  ex.Logger.getInstance().info('Mouse event:', pe);
 } elseif (pe.pointerType === ex.PointerType.Touch) {
  ex.Logger.getInstance().info('Touch event:', pe);
 }
});
Copy
```

## Multiple Pointers (Multi-Touch)​
When there is more than one pointer detected on the screen, this is considered multi-touch. For example, pressing one finger, then another, will create two pointers. If you lift a finger, the first one remains and the second one disappears.
You can handle multi-touch by subscribing to however many pointers you would like to support. If a pointer doesn't yet exist, it will be created. You do not need to check if a pointer exists. If it does exist, it will propagate events, otherwise it will remain idle.
Excalibur does not impose a limit to the amount of pointers you can subscribe to, so by all means, support all 10 fingers.
note
There is no way to identify touches after they happen; you can only know that there are _n_ touches on the screen at once.
```

ts
functionpaint(color:ex.Color) {
// create a handler for the event
returnfunction (pe:ex.PointerEvent) {
if (pe.pointerType === ex.PointerType.Touch) {
   engine.graphicsContext.drawRectangle(pe.worldPos, 5, 5, color);
  }
 };
}
engine.input.pointers.at(0).on('move', paint(ex.Color.Blue)); // 1st finger
engine.input.pointers.at(1).on('move', paint(ex.Color.Red)); // 2nd finger
engine.input.pointers.at(2).on('move', paint(ex.Color.Green)); // 3rd finger
Copy
```
```

ts
functionpaint(color:ex.Color) {
// create a handler for the event
returnfunction (pe:ex.PointerEvent) {
if (pe.pointerType === ex.PointerType.Touch) {
   engine.graphicsContext.drawRectangle(pe.worldPos, 5, 5, color);
  }
 };
}
engine.input.pointers.at(0).on('move', paint(ex.Color.Blue)); // 1st finger
engine.input.pointers.at(1).on('move', paint(ex.Color.Red)); // 2nd finger
engine.input.pointers.at(2).on('move', paint(ex.Color.Green)); // 3rd finger
Copy
```

  * The Primary Pointer
  * Handling Pointer Events Globally
    * Event Names
    * Event Handlers
    * Querying the Last Position
    * Scoping Events to Canvas vs. Document
  * Handling Pointer Events on Actors
    * Graphics Bounds Testing
    * Actor Pointer Event List
  * Checking the Pointer Type
  * Multiple Pointers (Multi-Touch)


