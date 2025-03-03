Skip to main content
On this page
Excalibur knows how to draw many types graphics to the screen by default comes with those pre-installed into the ExcaliburGraphicsContext. However, you may have a unique requirement to provide custom WebGL commands into excalibur, this can be done with a custom renderer plugin.
warning
This is an advanced API it is recommended you use built in graphics unless you are comfortable with building WebGL geometry and shaders.
## Registering a renderer plugin​
Registering a renderer with the graphics context will allow you to call it's draw method during your game.
```

typescript
constgame=new ex.Engine({...});
game.start().then(() => {
// register
  game.graphicsContext.register(newMyCustomRenderer());
});
// call from a graphics callback or event
constactor=new ex.Actor({...});
actor.graphics.onPostDraw= (graphicsContext) => {
  graphicsContext.draw<MyCustomRenderer>('myrenderer', ...);
}
Copy
```
```

typescript
constgame=new ex.Engine({...});
game.start().then(() => {
// register
  game.graphicsContext.register(newMyCustomRenderer());
});
// call from a graphics callback or event
constactor=new ex.Actor({...});
actor.graphics.onPostDraw= (graphicsContext) => {
  graphicsContext.draw<MyCustomRenderer>('myrenderer', ...);
}
Copy
```

## Writing a custom render plugin​
In order to build a custom renderer extend the RendererPlugin interface
```

typescript
exportclassMyCustomRendererextendsex.RendererPlugin {
/**
  * Unique type name for this renderer plugin
  */
readonlytype:string='myrenderer';
/**
  * Render priority tie breaker when drawings are at the same z index
  * @warning Not yet used by excalibur
  */
priority:number=0;
/**
  * Initialize your renderer
  *
  * @paramgl
  * @paramcontext
  */
initialize(gl:WebGLRenderingContext, context:ExcaliburGraphicsContextWebGL):void {
// initialize and compile shader
 }
/**
  * Issue a draw command to draw something to the screen
  * @paramargs
  */
draw(some:ex.Vector, args:ex.Color):void {
// update internal state with draw command with the args
 }
/**
  * @returns if there are any pending draws in the renderer
  */
hasPendingDraws():boolean {
// if there are any un-flushed drawings
returnfalse;
 }
/**
  * Flush any pending graphics draws to the screen
  */
flush():void {
// flush all pending draws to the screen
 }
}
Copy
```
```

typescript
exportclassMyCustomRendererextendsex.RendererPlugin {
/**
  * Unique type name for this renderer plugin
  */
readonlytype:string='myrenderer';
/**
  * Render priority tie breaker when drawings are at the same z index
  * @warning Not yet used by excalibur
  */
priority:number=0;
/**
  * Initialize your renderer
  *
  * @paramgl
  * @paramcontext
  */
initialize(gl:WebGLRenderingContext, context:ExcaliburGraphicsContextWebGL):void {
// initialize and compile shader
 }
/**
  * Issue a draw command to draw something to the screen
  * @paramargs
  */
draw(some:ex.Vector, args:ex.Color):void {
// update internal state with draw command with the args
 }
/**
  * @returns if there are any pending draws in the renderer
  */
hasPendingDraws():boolean {
// if there are any un-flushed drawings
returnfalse;
 }
/**
  * Flush any pending graphics draws to the screen
  */
flush():void {
// flush all pending draws to the screen
 }
}
Copy
```

For example this is the PointRenderer implementation
```

typescript
exportclassPointRendererimplementsRendererPlugin {
publicreadonlytype='ex.point';
publicpriority:number=0;
private_shader:Shader;
private_maxPoints:number=10922;
private_buffer:VertexBuffer;
private_layout:VertexLayout;
private_gl:WebGLRenderingContext;
private_context:ExcaliburGraphicsContextWebGL;
private_pointCount:number=0;
private_vertexIndex:number=0;
initialize(gl:WebGLRenderingContext, context:ExcaliburGraphicsContextWebGL):void {
this._gl = gl;
this._context = context;
this._shader =newShader({
			graphicsContext: context,
   vertexSource: pointVertexSource,
   fragmentSource: pointFragmentSource
  });
this._shader.compile();
this._shader.use();
this._shader.setUniformMatrix('u_matrix', this._context.ortho);
this._buffer =newVertexBuffer({
   size: 7*this._maxPoints,
   type: 'dynamic'
  });
this._layout =newVertexLayout({
   shader: this._shader,
   vertexBuffer: this._buffer,
   attributes: [
    ['a_position', 2],
    ['a_color', 4],
    ['a_size', 1]
   ]
  });
 }
draw(point:Vector, color:Color, size:number):void {
// Force a render if the batch is full
if (this._isFull()) {
this.flush();
  }
this._pointCount++;
consttransform=this._context.getTransform();
constopacity=this._context.opacity;
constfinalPoint= transform.multv(point);
constvertexBuffer=this._buffer.bufferData;
  vertexBuffer[this._vertexIndex++] = finalPoint.x;
  vertexBuffer[this._vertexIndex++] = finalPoint.y;
  vertexBuffer[this._vertexIndex++] = color.r /255;
  vertexBuffer[this._vertexIndex++] = color.g /255;
  vertexBuffer[this._vertexIndex++] = color.b /255;
  vertexBuffer[this._vertexIndex++] = color.a * opacity;
  vertexBuffer[this._vertexIndex++] = size *Math.max(transform.getScaleX(), transform.getScaleY());
 }
private_isFull() {
if (this._pointCount >=this._maxPoints) {
returntrue;
  }
returnfalse;
 }
hasPendingDraws():boolean {
returnthis._pointCount !==0;
 }
flush():void {
// nothing to draw early exit
if (this._pointCount ===0) {
return;
  }
constgl=this._gl;
this._shader.use();
this._layout.use(true);
this._shader.setUniformMatrix('u_matrix', this._context.ortho);
  gl.drawArrays(gl.POINTS, 0, this._pointCount);
  GraphicsDiagnostics.DrawnImagesCount +=this._pointCount;
  GraphicsDiagnostics.DrawCallCount++;
this._pointCount =0;
this._vertexIndex =0;
 }
}
Copy
```
```

typescript
exportclassPointRendererimplementsRendererPlugin {
publicreadonlytype='ex.point';
publicpriority:number=0;
private_shader:Shader;
private_maxPoints:number=10922;
private_buffer:VertexBuffer;
private_layout:VertexLayout;
private_gl:WebGLRenderingContext;
private_context:ExcaliburGraphicsContextWebGL;
private_pointCount:number=0;
private_vertexIndex:number=0;
initialize(gl:WebGLRenderingContext, context:ExcaliburGraphicsContextWebGL):void {
this._gl = gl;
this._context = context;
this._shader =newShader({
			graphicsContext: context,
   vertexSource: pointVertexSource,
   fragmentSource: pointFragmentSource
  });
this._shader.compile();
this._shader.use();
this._shader.setUniformMatrix('u_matrix', this._context.ortho);
this._buffer =newVertexBuffer({
   size: 7*this._maxPoints,
   type: 'dynamic'
  });
this._layout =newVertexLayout({
   shader: this._shader,
   vertexBuffer: this._buffer,
   attributes: [
    ['a_position', 2],
    ['a_color', 4],
    ['a_size', 1]
   ]
  });
 }
draw(point:Vector, color:Color, size:number):void {
// Force a render if the batch is full
if (this._isFull()) {
this.flush();
  }
this._pointCount++;
consttransform=this._context.getTransform();
constopacity=this._context.opacity;
constfinalPoint= transform.multv(point);
constvertexBuffer=this._buffer.bufferData;
  vertexBuffer[this._vertexIndex++] = finalPoint.x;
  vertexBuffer[this._vertexIndex++] = finalPoint.y;
  vertexBuffer[this._vertexIndex++] = color.r /255;
  vertexBuffer[this._vertexIndex++] = color.g /255;
  vertexBuffer[this._vertexIndex++] = color.b /255;
  vertexBuffer[this._vertexIndex++] = color.a * opacity;
  vertexBuffer[this._vertexIndex++] = size *Math.max(transform.getScaleX(), transform.getScaleY());
 }
private_isFull() {
if (this._pointCount >=this._maxPoints) {
returntrue;
  }
returnfalse;
 }
hasPendingDraws():boolean {
returnthis._pointCount !==0;
 }
flush():void {
// nothing to draw early exit
if (this._pointCount ===0) {
return;
  }
constgl=this._gl;
this._shader.use();
this._layout.use(true);
this._shader.setUniformMatrix('u_matrix', this._context.ortho);
  gl.drawArrays(gl.POINTS, 0, this._pointCount);
  GraphicsDiagnostics.DrawnImagesCount +=this._pointCount;
  GraphicsDiagnostics.DrawCallCount++;
this._pointCount =0;
this._vertexIndex =0;
 }
}
Copy
```

  * Registering a renderer plugin
  * Writing a custom render plugin


