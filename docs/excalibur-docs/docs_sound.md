Skip to main content
On this page
Plenty of times you'll want sound effects in your game. The Sound resource will help you load files in order of preference in case the browser doesn't support them.
## Audio with the Sound Resource​
Excalibur supports any audio the browser supports like `.wav`, `.mp3`, and `.ogg`. Due to mixed browser support you may wish to specify a list of source files and codecs, the order of the files specifies order of preference (we recommend mp3, wav).
Major Browser support table documented on MDN
Pass an instance of Sound to a Loader to preload it. Once a sound is loaded, you can play it. You can pass an argument from 0.0 - 1.0 into play in order to play the sound at that volume.
```

typescript
constgame=newEngine({...});
constsound=newSound('./path/to/my.mp3', './path/to/fallback.wav');
constloader=newLoader([sound]);
await game.start(loader);
sound.play(0.5);
Copy
```
```

typescript
constgame=newEngine({...});
constsound=newSound('./path/to/my.mp3', './path/to/fallback.wav');
constloader=newLoader([sound]);
await game.start(loader);
sound.play(0.5);
Copy
```

See the examples or API documentation for Sound for additional features available such as looping, volume setting, and more.
  * Audio with the Sound Resource


