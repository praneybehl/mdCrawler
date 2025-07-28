Open Source backend
**in 1 file**
Realtime database
Authentication
File storage
Admin dashboard
![Gopher](https://pocketbase.io/)
![PocketBase dashboard preview](https://pocketbase.io/)
Live demo Read the documentation
## Ready to use out of the box
JavaScript Dart
`// JavaScript SDK import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... // list and search for 'example' collection records const list = await pb.collection('example').getList(1, 100, { filter: 'title != "" && created > "2022-08-01"', sort: '-created,title', }); // or fetch a single 'example' collection record const record = await pb.collection('example').getOne('RECORD_ID'); // delete a single 'example' collection record await pb.collection('example').delete('RECORD_ID'); // create a new 'example' collection record const newRecord = await pb.collection('example').create({ title: 'Lorem ipsum dolor sit amet', }); // subscribe to changes in any record from the 'example' collection pb.collection('example').subscribe('*', function (e) {   console.log(e.record); }); // stop listening for changes in the 'example' collection pb.collection('example').unsubscribe();`
## Integrate nicely with your favorite frontend stack
![Flutter logo](https://pocketbase.io/images/flutter_logo.svg?v2) ![Svelte logo](https://pocketbase.io/images/svelte_logo.svg?v2) ![Vue logo](https://pocketbase.io/images/vue_logo.svg?v2) ![React logo](https://pocketbase.io/images/react_logo.svg?v2) ![Angular logo](https://pocketbase.io/images/angular_logo.svg?v2)
