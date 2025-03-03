Skip to main content
## 📄️ Color
Colors
## 📄️ Graphics
Graphics are special object that abstract something that can be drawn to the screen. Examples include circles, polygons, and sprites.
## 📄️ Lines
The line graphic object can be used to draw lines using Excalibur. The Actor [GraphicsComponent]] centers graphics by default, so it might be desireable to set the [anchor to (0, 0);
## 📄️ Sprites
A sprite is a view into a ImageSource and a projection into a final destination size.
## 📄️ Spritesheets
SpriteSheet is really an ordered collection of sprites from the same base image.
## 📄️ Text & Fonts
You may want to display [[Text]] in your game, this can be achieved with the [[Text]], [[Font]], and [[SpriteFont]].
## 📄️ Animation
[[Animation|Animations]] are a series of graphics that take a specific duration in milliseconds. Each of these units is called a "Frame". There are a few playing strategies as well to consider
## 📄️ Canvas
For drawing hooks the ExcaliburGraphicsContext replaces the browser CanvasRenderingContext2D. However, if you need to do some custom drawing using the CanvasRenderingContext2D the new [[Canvas]] graphic has your back.
## 📄️ Graphics Component
There is a new component, ex.GraphicsComponent to work with these graphics with ex.Actor's and other ex.Entity's
## 📄️ Graphics Group
A graphics group is an new graphic that draws a graphics in some relation to one another. This can be useful when you want to compose graphics together into a single graphic. Graphics groups do support all types of graphics including animations
## 📄️ Materials (Custom Shaders)
Sometimes you need even more control about how your graphics render in your game! For example you might want a custom blend, a reflection effect, or a warping effect. With this api you can provide custom shaders to graphics.
## 📄️ Graphics Context
Why Graphics?
## 📄️ Parallax
The [[ParallaxComponent]] can be used for creating parallax effects on the graphics, entities with this component are drawn differently and a collider will not be where you expect. It is not recommended you use colliders with parallax entities.
## 📄️ Nine-Slice
🧪 Available in the v0.30.0 Alpha
## 📄️ Pixel Art
Pixel art is deceptively challenging to get right. There are a few rendering artifacts that can plague pixel art games in this guide hopefully we'll get you to the prettiest possible pixel art.
## 📄️ Custom Renderer Plugins
Excalibur knows how to draw many types graphics to the screen by default comes with those pre-installed into the [[ExcaliburGraphicsContext]]. However, you may have a unique requirement to provide custom WebGL commands into excalibur, this can be done with a custom renderer plugin.
