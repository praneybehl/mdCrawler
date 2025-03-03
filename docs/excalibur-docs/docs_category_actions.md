Skip to main content
## 📄️ Actions
Actions
## 📄️ Blink
Blinking is useful for showing that damage has been taken
## 📄️ CallMethod
This method allows you to call an arbitrary method as the next action in the action queue. This is useful if you want to execute code in after a specific action, i.e An actor arrives at a destination after traversing a path
## 📄️ Parallel Actions
Sometimes it's useful to run actions in parallel to produce scripted behavior.
## 📄️ Delay
Delays are useful when you need to wait a certain amount of time between actions.
## 📄️ EaseTo
The easing action is a lot like the moveTo except you can specify an [[EasingFunction]]. With built in easing functions like [[EasingFunctions.EaseInOutCubic]] you can make things look really smooth.
## 📄️ MoveTo/MoveBy
Moving actions are super useful for creating patrolling behavior, and are often paired with repeat or repeatForever
## 📄️ Fade
Fade
## 📄️ RotateTo/RotateBy
Rotation actions are useful for creating spinning objects in your game.
## 📄️ Repeat
It is sometimes useful to repeat a sequence of action for your games. For example if you want an enemy to patrol back and forth, or for a platform to repeat a certain pattern.
## 📄️ Die
[[ActionContext.die|Die]] is a quick wrapper around [[Entity.kill]] to remove something from a scene.
## 📄️ Follow
[[ActionsContext.follow|Follow]] can be useful for building things that need to follow behind another actor.
## 📄️ Meet
[[ActionsContext.meet|Meet]] can be useful for building tracking projectiles that always reach their target.
## 📄️ ScaleTo/ScaleBy
ScaleTo
