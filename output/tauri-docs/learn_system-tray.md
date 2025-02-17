Skip to content
# System Tray
Tauri allows you to create and customize a system tray for your application. This can enhance the user experience by providing quick access to common actions.
## Configuration
First of all, update your `Cargo.toml` to include the necessary feature for the system tray.
src-tauri/Cargo.toml```

tauri = { version = "2.0.0", features = [ "tray-icon" ] }

```

## Usage
The tray API is available in both JavaScript and Rust.
### Create a Tray Icon
  * JavaScript 
  * Rust 


Use the `TrayIcon.new` static function to create a new tray icon:
```

import { TrayIcon } from'@tauri-apps/api/tray';
const options = {
// here you can add a tray menu, title, tooltip, event handler, etc
};
const tray = await TrayIcon.new(options);

```

See `TrayIconOptions` for more information on the customization options.
```

use tauri::tray::TrayIconBuilder;
tauri::Builder::default()
.setup(|app| {
lettray= TrayIconBuilder::new().build(app)?;
Ok(())
})

```

See `TrayIconBuilder` for more information on customization options.
### Change the Tray Icon
When creating the tray you can use the application icon as the tray icon:
  * JavaScript 
  * Rust 


```

import { TrayIcon } from'@tauri-apps/api/tray';
import { defaultWindowIcon } from'@tauri-apps/api/app';
const options = {
icon: await defaultWindowIcon(),
};
const tray = await TrayIcon.new(options);

```

```

lettray= TrayIconBuilder::new()
.icon(app.default_window_icon().unwrap().clone())
.build(app)?;

```

### Add a Menu
To attach a menu that is displayed when the tray is clicked, you can use the `menu` option.
  * JavaScript 
  * Rust 


```

import { TrayIcon } from'@tauri-apps/api/tray';
import { Menu } from'@tauri-apps/api/menu';
const menu = await Menu.new({
items: [
{
id: 'quit',
text: 'Quit',
},
],
});
const options = {
menu,
menuOnLeftClick: true,
};
const tray = await TrayIcon.new(options);

```

```

use tauri::{
menu::{Menu, MenuItem},
tray::TrayIconBuilder,
};
letquit_i= MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
letmenu= Menu::with_items(app, &[&quit_i])?;
lettray= TrayIconBuilder::new()
.menu(&menu)
.menu_on_left_click(true)
.build(app)?;

```

#### Listen to Menu Events
  * JavaScript 
  * Rust 


On JavaScript you can attach a menu click event listener directly to the menu item:
  * Using a shared menu click handler
```

import { Menu } from'@tauri-apps/api/menu';
functiononTrayMenuClick(itemId) {
// itemId === 'quit'
}
const menu = await Menu.new({
items: [
{
id: 'quit',
text: 'Quit',
action: onTrayMenuClick,
},
],
});

```

  * Using a dedicated menu click handler
```

import { Menu } from'@tauri-apps/api/menu';
const menu = await Menu.new({
items: [
{
id: 'quit',
text: 'Quit',
action: ()=> {
console.log('quit pressed');
},
},
],
});

```



Use the `TrayIconBuilder::on_menu_event` method to attach a tray menu click event listener:
```

use tauri::tray::TrayIconBuilder;
TrayIconBuilder::new()
.on_menu_event(|app, event|matchevent.id.as_ref() {
"quit"=> {
println!("quit menu item was clicked");
app.exit(0);
}
_=> {
println!("menu item {:?} not handled", event.id);
}
})

```

### Listen to Tray Events
The tray icon emits events for the following mouse events:
  * click: triggered when the cursor receives a single left, right or middle click, including information on whether the mouse press was released or not
  * Double click: triggered when the cursor receives a double left, right or middle click
  * Enter: triggered when the cursor enters the tray icon area
  * Move: triggered when the cursor moves around the tray icon area
  * Leave: triggered when the cursor leaves the tray icon area


  * JavaScript 
  * Rust 


```

import { TrayIcon } from'@tauri-apps/api/tray';
const options = {
action: (event) => {
switch (event.type) {
case 'Click':
console.log(
`mouse ${event.button} button pressed, state: ${event.buttonState}`
);
break;
case 'DoubleClick':
console.log(`mouse ${event.button} button pressed`);
break;
case 'Enter':
console.log(
`mouse hovered tray at ${event.rect.position.x}, ${event.rect.position.y}`
);
break;
case 'Move':
console.log(
`mouse moved on tray at ${event.rect.position.x}, ${event.rect.position.y}`
);
break;
case 'Leave':
console.log(
`mouse left tray at ${event.rect.position.x}, ${event.rect.position.y}`
);
break;
}
},
};
const tray = await TrayIcon.new(options);

```

See `TrayIconEvent` for more information on the event payload.
```

use tauri::{
Manager,
tray::{MouseButton, MouseButtonState, TrayIconBuilder, TrayIconEvent}
};
TrayIconBuilder::new()
.on_tray_icon_event(|tray, event|matchevent {
TrayIconEvent::Click {
button: MouseButton::Left,
button_state: MouseButtonState::Up,
..
} => {
println!("left click pressed and released");
// in this example, let's show and focus the main window when the tray is clicked
letapp=tray.app_handle();
iflet Some(window) =app.get_webview_window("main") {
let_=window.show();
let_=window.set_focus();
}
}
_=> {
println!("unhandled event {event:?}");
}
})

```

See `TrayIconEvent` for more information on the event type.
© 2025 Tauri Contributors. CC-BY / MIT
