Realtime messaging
By default PocketBase sends realtime events only for Record create/update/delete operations (_and for the OAuth2 auth redirect_), but you are free to send custom realtime messages to the connected clients via the `$app.subscriptionsBroker()` instance.
`$app.subscriptionsBroker().clients()` returns all connected `subscriptions.Client` indexed by their unique connection id.
The current auth record associated with a client could be accessed through `client.get("auth")`
Note that a single authenticated user could have more than one active realtime connection (aka. multiple clients). This could happen for example when opening the same app in different tabs, browsers, devices, etc.
Below you can find a minimal code sample that sends a JSON payload to all clients subscribed to the "example" topic:
`const message = new SubscriptionMessage({ name: "example", data: JSON.stringify({ ... }), }); // retrieve all clients (clients id indexed map) const clients = $app.subscriptionsBroker().clients() for (let clientId in clients) { if (clients[clientId].hasSubscription("example")) {     clients[clientId].send(message) } }`
From the client-side, users can listen to the custom subscription topic by doing something like:
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.realtime.subscribe('example', (e) => {   console.log(e) })`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.realtime.subscribe('example', (e) { print(e) })`
Prev: Sending HTTP requests Next: Filesystem
