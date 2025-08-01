Realtime messaging
By default PocketBase sends realtime events only for Record create/update/delete operations (_and for the OAuth2 auth redirect_), but you are free to send custom realtime messages to the connected clients via the `app.SubscriptionsBroker()` instance.
`app.SubscriptionsBroker().Clients()` returns all connected `subscriptions.Client` indexed by their unique connection id.
`app.SubscriptionsBroker().ChunkedClients(size)` is similar but return the result as a chunked slice allowing you to split the iteration across several goroutines (usually combined with `errgroup` ).
The current auth record associated with a client could be accessed through `client.Get(apis.RealtimeClientAuthKey)`
Note that a single authenticated user could have more than one active realtime connection (aka. multiple clients). This could happen for example when opening the same app in different tabs, browsers, devices, etc.
Below you can find a minimal code sample that sends a JSON payload to all clients subscribed to the "example" topic:
`func notify(app core.App, subscription string, data any) error {   rawData, err := json.Marshal(data) if err != nil { return err   }   message := subscriptions.Message{     Name: subscription,     Data: rawData, }   group := new(errgroup.Group)   chunks := app.SubscriptionsBroker().ChunkedClients(300) for _, chunk := range chunks {     group.Go(func() error { for _, client := range chunk { if !client.HasSubscription(subscription) { continue }         client.Send(message) } return nil }) } return group.Wait() } err := notify(app, "example", map[string]any{"test": 123}) if err != nil { return err }`
From the client-side, users can listen to the custom subscription topic by doing something like:
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.realtime.subscribe('example', (e) => {   console.log(e) })`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.realtime.subscribe('example', (e) { print(e) })`
Prev: Console commands Next: Filesystem
