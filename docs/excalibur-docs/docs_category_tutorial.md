Skip to main content
## 📄️ Building Breakout
Be sure to check out our new tutorial, building a flappy bird clone
## 📄️ Building Flappy Bird
Introduction
## 📄️ Step 0 - Setting up Your TypeScript Environment
You can skip this step if you have a preferred environment setup
## 📄️ Step 1 - Start Your Engines
First in main.ts we can import all of Excalibur as ex, this makes it clear in this example what types are coming from Excalibur.
## 📄️ Step 2 - Adding a Bird Actor
Next let's making our first Actor for the Bird and .add() it to the default Excalibur Scene which can be accessed off the Engine.
## 📄️ Step 3 - The Bird and the Grounds
Let's create some ground for the Bird to collide with, make a new ground.ts file.
## 📄️ Step 4 - Flying the Bird
We can take user input in Excalibur from keyboard, pointers (mouse, touch), and gamepads!
## 📄️ Step 5 - Plumbing the Pipes
Now we want to make those classic "mario" style pipe obstacles you see in Flappy Bird.
## 📄️ Step 6 - Refactor to a Scene
Up to this point we've been using the default scene, which is great for small prototypes. However we want to keep main.ts clean so we'll move our game composition and initialization logic into a ex.Scene.
## 📄️ Step 7 - Refactor to Config Constants
Using magic numbers in your code can start to get tricky as your code base grows. We recommend creating a config.ts file to hold these numbers with names that mean something to you and your game.
## 📄️ Step 8 - Periodic Pipes
We want pipe to appear after a certain amount of time and for them to be in random positions. To accomplish this we'll use the ex.Timer which is a handy type for firing a callback periodically according to the excalibur Clock and ex.Random which provides a way of doing seeded random.
## 📄️ Step 9 - Scoring Points
Any good game needs points, so let's add some!
## 📄️ Step 10 - Game Over
For our game, when the bird collides with the ground, pipe, or goes offscreen we want to trigger a game over. To accomplish this we'll setup a start(), stop() and reset() on the various components of our game so that we can "freeze" things in place on a game over.
## 📄️ Step 11 - Images and Graphics
It would be nice to have some graphics for our Bird actor, we can load images to use in in actors using the ex.ImageSource and a ex.Loader. The loader will show a loading bar while our images and other resources are loading. Generally we do this in a new resources.ts file.
## 📄️ Step 12 - Bird Graphics
We have a lovely Excalibur themed bird we created especially for this sample, feel free to use and remix. You'll notice that we have a sprite sheet for various frames.
## 📄️ Step 13 - Pipe Graphics
We also created a pipe especially for this sample, feel free to use and remix.
## 📄️ Step 14 - Ground Graphics
Finally the ground graphics, feel free to use and remix.
## 📄️ Step 15 - Sounds and Music
Finally to really add depth to a game let's add some sound! ex.Sound needs to be loaded much like ex.ImageSource.
## 📄️ Step 16 - Voila 🎉
Celebrate! You've made a game in Excalibur! Go forth and celebrate to all your friends!
