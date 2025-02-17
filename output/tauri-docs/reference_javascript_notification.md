Skip to content
# @tauri-apps/plugin-notification
Send toast notifications (brief auto-expiring OS window element) to your user. Can also be used with the Notification Web API.
## Enumerations
### Importance
#### Enumeration Members
##### Default
```

Default: 3;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L287
##### High
```

High: 4;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L288
##### Low
```

Low: 2;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L286
##### Min
```

Min: 1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L285
##### None
```

None: 0;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L284
### ScheduleEvery
#### Enumeration Members
##### Day
```

Day: "day";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L159
##### Hour
```

Hour: "hour";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L160
##### Minute
```

Minute: "minute";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L161
##### Month
```

Month: "month";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L156
##### Second
```

Second: "second";

```

Not supported on iOS.
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L165
##### TwoWeeks
```

TwoWeeks: "twoWeeks";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L157
##### Week
```

Week: "week";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L158
##### Year
```

Year: "year";

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L155
### Visibility
#### Enumeration Members
##### Private
```

Private: 0;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L293
##### Public
```

Public: 1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L294
##### Secret
```

Secret: -1;

```

**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L292
## Classes
### Schedule
#### Constructors
##### new Schedule()
```

newSchedule(): Schedule

```

###### Returns
`Schedule`
#### Properties
Property| Type| Defined in  
---|---|---  
`at`| `undefined` | `object`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L169  
`every`| `undefined` | `object`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L184  
`interval`| `undefined` | `object`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L177  
#### Methods
##### at()
```

static at(
date,
repeating,
allowWhileIdle): Schedule

```

###### Parameters
Parameter| Type| Default value  
---|---|---  
`date`| `Date`| `undefined`  
`repeating`| `boolean`| `false`  
`allowWhileIdle`| `boolean`| `false`  
###### Returns
`Schedule`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L192
##### every()
```

static every(
kind,
count,
allowWhileIdle): Schedule

```

###### Parameters
Parameter| Type| Default value  
---|---|---  
`kind`| `ScheduleEvery`| `undefined`  
`count`| `number`| `undefined`  
`allowWhileIdle`| `boolean`| `false`  
###### Returns
`Schedule`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L211
##### interval()
```

static interval(interval, allowWhileIdle): Schedule

```

###### Parameters
Parameter| Type| Default value  
---|---|---  
`interval`| `ScheduleInterval`| `undefined`  
`allowWhileIdle`| `boolean`| `false`  
###### Returns
`Schedule`
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L200
## Interfaces
### Action
#### Properties
Property| Type| Defined in  
---|---|---  
`destructive?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L239  
`foreground?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L238  
`id`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L235  
`input?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L240  
`inputButtonTitle?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L241  
`inputPlaceholder?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L242  
`requiresAuthentication?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L237  
`title`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L236  
### ActionType
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`actions`| `Action`[]| The list of associated actions| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L253  
`allowInCarPlay?`| `boolean`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L256  
`customDismissAction?`| `boolean`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L255  
`hiddenPreviewsBodyPlaceholder?`| `string`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L254  
`hiddenPreviewsShowSubtitle?`| `boolean`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L258  
`hiddenPreviewsShowTitle?`| `boolean`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L257  
`id`| `string`| The identifier of this action type| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L249  
### ActiveNotification
#### Properties
Property| Type| Defined in  
---|---|---  
`actionTypeId?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L278  
`attachments`| `Attachment`[]| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L277  
`body?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L272  
`data`| `Record`<`string`, `string`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L275  
`extra`| `Record`<`string`, `unknown`>| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L276  
`group?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L273  
`groupSummary`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L274  
`id`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L269  
`schedule?`| `Schedule`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L279  
`sound?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L280  
`tag?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L270  
`title?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L271  
### Attachment
Attachment of a notification.
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`id`| `string`| Attachment identifier.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L229  
`url`| `string`| Attachment URL. Accepts the `asset` and `file` protocols.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L231  
### Channel
#### Properties
Property| Type| Defined in  
---|---|---  
`description?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L300  
`id`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L298  
`importance?`| `Importance`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L305  
`lightColor?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L303  
`lights?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L302  
`name`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L299  
`sound?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L301  
`vibration?`| `boolean`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L304  
`visibility?`| `Visibility`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L306  
### Options
Options to send a notification.
#### Since
2.0.0
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`actionTypeId?`| `string`| Defines an action type for this notification.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L62  
`attachments?`| `Attachment`[]| Notification attachments.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L104  
`autoCancel?`| `boolean`| Automatically cancel the notification when the user clicks on it.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L120  
`body?`| `string`| Optional notification body.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L44  
`channelId?`| `string`| Identifier of the Channel that deliveres this notification. If the channel does not exist, the notification won’t fire. Make sure the channel exists with listChannels and createChannel.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L36  
`extra?`| `Record`<`string`, `unknown`>| Extra payload to store in the notification.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L108  
`group?`| `string`| Identifier used to group multiple notifications. https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649872-threadidentifier| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L68  
`groupSummary?`| `boolean`| Instructs the system that this notification is the summary of a group on Android.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L72  
`icon?`| `string`| Notification icon. On Android the icon must be placed in the app’s `res/drawable` folder.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L90  
`iconColor?`| `string`| Icon color on Android.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L100  
`id?`| `number`| The notification identifier to reference this object later. Must be a 32-bit integer.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L29  
`inboxLines?`| `string`[]| List of lines to add to the notification. Changes the notification style to inbox. Cannot be used with `largeBody`. Only supports up to 5 lines.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L84  
`largeBody?`| `string`| Multiline text. Changes the notification style to big text. Cannot be used with `inboxLines`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L54  
`largeIcon?`| `string`| Notification large icon (Android). The icon must be placed in the app’s `res/drawable` folder.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L96  
`number?`| `number`| Sets the number of items this notification represents on Android.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L132  
`ongoing?`| `boolean`| If true, the notification cannot be dismissed by the user on Android. An application service must manage the dismissal of the notification. It is typically used to indicate a background task that is pending (e.g. a file download) or the user is engaged with (e.g. playing music).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L116  
`schedule?`| `Schedule`| Schedule this notification to fire on a later time or a fixed interval.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L48  
`silent?`| `boolean`| Changes the notification presentation to be silent on iOS (no badge, no sound, not listed).| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L124  
`sound?`| `string`| The sound resource name. Only available on mobile.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L76  
`summary?`| `string`| Detail text for the notification with `largeBody`, `inboxLines` or `groupSummary`.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L58  
`title`| `string`| Notification title.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L40  
`visibility?`| `Visibility`| Notification visibility.| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L128  
### PendingNotification
#### Properties
Property| Type| Defined in  
---|---|---  
`body?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L264  
`id`| `number`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L262  
`schedule`| `Schedule`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L265  
`title?`| `string`| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L263  
### ScheduleInterval
#### Properties
Property| Type| Description| Defined in  
---|---|---|---  
`day?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L138  
`hour?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L149  
`minute?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L150  
`month?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L137  
`second?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L151  
`weekday?`| `number`| 1 - Sunday 2 - Monday 3 - Tuesday 4 - Wednesday 5 - Thursday 6 - Friday 7 - Saturday| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L148  
`year?`| `number`| -| **Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L136  
## Type Aliases
### PermissionState
```

type PermissionState: "granted" | "denied" | "prompt" | "prompt-with-rationale";

```

**Source** : undefined
## Functions
### active()
```

functionactive():Promise<ActiveNotification[]>

```

Retrieves the list of active notifications.
#### Returns
`Promise`<`ActiveNotification`[]>
A promise resolving to the list of active notifications.
#### Example
```

import { active } from'@tauri-apps/plugin-notification';
const activeNotifications = await active();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L459
### cancel()
```

functioncancel(notifications):Promise<void>

```

Cancels the pending notifications with the given list of identifiers.
#### Parameters
Parameter| Type  
---|---  
`notifications`| `number`[]  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { cancel } from'@tauri-apps/plugin-notification';
awaitcancel([-34234, 23432, 4311]);

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L425
### cancelAll()
```

functioncancelAll():Promise<void>

```

Cancels all pending notifications.
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { cancelAll } from'@tauri-apps/plugin-notification';
awaitcancelAll();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L442
### channels()
```

functionchannels():Promise<Channel[]>

```

Retrieves the list of notification channels.
#### Returns
`Promise`<`Channel`[]>
A promise resolving to the list of notification channels.
#### Example
```

import { channels } from'@tauri-apps/plugin-notification';
const notificationChannels = await channels();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L553
### createChannel()
```

functioncreateChannel(channel):Promise<void>

```

Creates a notification channel.
#### Parameters
Parameter| Type  
---|---  
`channel`| `Channel`  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { createChannel, Importance, Visibility } from'@tauri-apps/plugin-notification';
awaitcreateChannel({
id: 'new-messages',
name: 'New Messages',
lights: true,
vibration: true,
importance: Importance.Default,
visibility: Visibility.Private
});

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L519
### isPermissionGranted()
```

functionisPermissionGranted():Promise<boolean>

```

Checks if the permission to send notifications is granted.
#### Returns
`Promise`<`boolean`>
#### Example
```

import { isPermissionGranted } from'@tauri-apps/plugin-notification';
const permissionGranted = await isPermissionGranted();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L319
### onAction()
```

functiononAction(cb):Promise<PluginListener>

```

#### Parameters
Parameter| Type  
---|---  
`cb`| (`notification`) => `void`  
#### Returns
`Promise`<`PluginListener`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L563
### onNotificationReceived()
```

functiononNotificationReceived(cb):Promise<PluginListener>

```

#### Parameters
Parameter| Type  
---|---  
`cb`| (`notification`) => `void`  
#### Returns
`Promise`<`PluginListener`>
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L557
### pending()
```

functionpending():Promise<PendingNotification[]>

```

Retrieves the list of pending notifications.
#### Returns
`Promise`<`PendingNotification`[]>
A promise resolving to the list of pending notifications.
#### Example
```

import { pending } from'@tauri-apps/plugin-notification';
const pendingNotifications = await pending();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L408
### registerActionTypes()
```

functionregisterActionTypes(types):Promise<void>

```

Register actions that are performed when the user clicks on the notification.
#### Parameters
Parameter| Type  
---|---  
`types`| `ActionType`[]  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { registerActionTypes } from'@tauri-apps/plugin-notification';
awaitregisterActionTypes([{
id: 'tauri',
actions: [{
id: 'my-action',
title: 'Settings'
}]
}])

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L391
### removeActive()
```

functionremoveActive(notifications):Promise<void>

```

Removes the active notifications with the given list of identifiers.
#### Parameters
Parameter| Type  
---|---  
`notifications`| `object`[]  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { cancel } from'@tauri-apps/plugin-notification';
awaitcancel([-34234, 23432, 4311])

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L476
### removeAllActive()
```

functionremoveAllActive():Promise<void>

```

Removes all active notifications.
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { removeAllActive } from'@tauri-apps/plugin-notification';
awaitremoveAllActive()

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L495
### removeChannel()
```

functionremoveChannel(id):Promise<void>

```

Removes the channel with the given identifier.
#### Parameters
Parameter| Type  
---|---  
`id`| `string`  
#### Returns
`Promise`<`void`>
A promise indicating the success or failure of the operation.
#### Example
```

import { removeChannel } from'@tauri-apps/plugin-notification';
awaitremoveChannel();

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L536
### requestPermission()
```

functionrequestPermission():Promise<NotificationPermission>

```

Requests the permission to send notifications.
#### Returns
`Promise`<`NotificationPermission`>
A promise resolving to whether the user granted the permission or not.
#### Example
```

import { isPermissionGranted, requestPermission } from'@tauri-apps/plugin-notification';
let permissionGranted = await isPermissionGranted();
if (!permissionGranted) {
const permission = await requestPermission();
permissionGranted = permission ==='granted';
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L342
### sendNotification()
```

functionsendNotification(options):void

```

Sends a notification to the user.
#### Parameters
Parameter| Type  
---|---  
`options`| `string` | `Options`  
#### Returns
`void`
#### Example
```

import { isPermissionGranted, requestPermission, sendNotification } from'@tauri-apps/plugin-notification';
let permissionGranted = await isPermissionGranted();
if (!permissionGranted) {
const permission = await requestPermission();
permissionGranted = permission ==='granted';
}
if (permissionGranted) {
sendNotification('Tauri is awesome!');
sendNotification({ title: 'TAURI', body: 'Tauri is awesome!' });
}

```

#### Since
2.0.0
**Source** : https://github.com/tauri-apps/plugins-workspace/blob/v2/plugins/notification/guest-js/index.ts#L364
© 2025 Tauri Contributors. CC-BY / MIT
