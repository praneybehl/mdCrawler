Skip to content
# Window Menu
Native application menus can be attached to both to a window or system tray. Available on desktop.
## Creating a base-level menu
To create a base-level native window menu, and attach to a window:
  * JavaScript 
  * Rust 


Use the `Menu.new` static function to create a window menu:
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
// If a window was not created with an explicit menu or had one set explicitly,
// this menu will be assigned to it.
menu.setAsAppMenu().then((res)=> {
console.log('menu set success', res);
});

```

```

#![cfg_attr(not(debug_assertions), windows_subsystem ="windows")]
use tauri::menu::{Menu, MenuItem};
fnmain() {
tauri::Builder::default()
.setup(|app| {
letmenu= MenuBuilder::new(app)
.text("open", "Open")
.text("close", "Close")
.build()?;
app.set_menu(menu)?;
Ok(())
})
}

```

## Listening to events on custom menu items
Each custom menu item triggers an event when clicked. Use the `on_menu_event` API to handle them.
  * JavaScript 
  * Rust 


```

import { Menu } from'@tauri-apps/api/menu';
const menu = await Menu.new({
items: [
{
id: 'Open',
text: 'open',
action: ()=> {
console.log('open pressed');
},
},
{
id: 'Close',
text: 'close',
action: ()=> {
console.log('close pressed');
},
},
],
});
awaitmenu.setAsAppMenu();

```

```

#![cfg_attr(not(debug_assertions), windows_subsystem ="windows")]
use tauri::menu::{MenuBuilder};
fnmain() {
tauri::Builder::default()
.setup(|app| {
letmenu= MenuBuilder::new(app)
.text("open", "Open")
.text("close", "Close")
.build()?;
app.set_menu(menu)?;
app.on_menu_event(move|app_handle:&tauri::AppHandle, event| {
println!("menu event: {:?}", event.id());
matchevent.id().0.as_str() {
"open"=> {
println!("open event");
}
"close"=> {
println!("close event");
}
_=> {
println!("unexpected menu event");
}
}
});
Ok(())
})
}

```

## Creating a multi-level menu
To create a multi-level menu, you can add some submenus to the menu item:
  * JavaScript 
  * Rust 


```

#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
use tauri::{image::Image, menu::{CheckMenuItemBuilder, IconMenuItemBuilder, MenuBuilder, SubmenuBuilder}};
fnmain() {
tauri::Builder::default()
.setup(|app| {
let text_menu=SubmenuBuilder::new(app, "File")
.text("open", "Open")
.text("quit", "Quit")
.build()?;
let lang_str = "en";
let check_sub_item_1 = CheckMenuItemBuilder::new("English")
.id("en")
.checked(lang_str=="en")
.build(app)?;
letcheck_sub_item_2=CheckMenuItemBuilder::new("Chinese")
.id("en")
.checked(lang_str=="en")
.enabled(false)
.build(app)?;
leticon_image=Image::from_bytes(include_bytes!("../icons/icon.png")).unwrap();
leticon_item=IconMenuItemBuilder::new("icon")
.icon(icon_image)
.build(app)?;
letcheck_menus=SubmenuBuilder::new(app, "language")
.item(&check_sub_item_1)
.item(&check_sub_item_2)
.build()?;
letmenu=MenuBuilder::new(app)
.items(&[&text_menu, &check_menus, &icon_item])
.build()?;
app.set_menu(menu)?;
print!("Hello from setup");
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

```

use tauri::menu::{CheckMenuItemBuilder, MenuBuilder, SubmenuBuilder};
fnmain() {
tauri::Builder::default()
.setup(|app| {
letfile_menu= SubmenuBuilder::new(app, "File")
.text("open", "Open")
.text("quit", "Quit")
.build()?;
letlang_str="en";
letcheck_sub_item_1= CheckMenuItemBuilder::new("English")
.id("en")
.checked(lang_str=="en")
.build(app)?;
letcheck_sub_item_2= CheckMenuItemBuilder::new("Chinese")
.id("en")
.checked(lang_str=="en")
.enabled(false)
.build(app)?;
// Load icon from path
leticon_image= Image::from_bytes(include_bytes!("../icons/icon.png")).unwrap();
leticon_item= IconMenuItemBuilder::new("icon")
.icon(icon_image)
.build(app)?;
letother_item= SubmenuBuilder::new(app, "language")
.item(&check_sub_item_1)
.item(&check_sub_item_2)
.build()?;
letmenu= MenuBuilder::new(app)
.items(&[&file_menu, &other_item,&icon_item])
.build()?;
app.set_menu(menu)?;
Ok(())
})
}

```

Note that you need to enable `image-ico` or `image-png` feature to use this API:
src-tauri/Cargo.toml```

[dependencies]
tauri = { version = "...", features = ["...", "image-png"] }

```

## Creating predefined menu
To use built-in (native) menu items that has predefined behavior by the operating system or Tauri:
  * JavaScript 
  * Rust 


```

import { Menu, PredefinedMenuItem } from'@tauri-apps/api/menu';
const copy = await PredefinedMenuItem.new({
text: 'copy-text',
item: 'Copy',
});
const separator = await PredefinedMenuItem.new({
text: 'separator-text',
item: 'Separator',
});
const undo = await PredefinedMenuItem.new({
text: 'undo-text',
item: 'Undo',
});
const redo = await PredefinedMenuItem.new({
text: 'redo-text',
item: 'Redo',
});
const cut = await PredefinedMenuItem.new({
text: 'cut-text',
item: 'Cut',
});
const paste = await PredefinedMenuItem.new({
text: 'paste-text',
item: 'Paste',
});
const select_all = await PredefinedMenuItem.new({
text: 'select_all-text',
item: 'SelectAll',
});
const menu = await Menu.new({
items: [copy, separator, undo, redo, cut, paste, select_all],
});
awaitmenu.setAsAppMenu();

```

```

#![cfg_attr(not(debug_assertions), windows_subsystem ="windows")]
use tauri::menu::{MenuBuilder, PredefinedMenuItem};
fnmain() {
tauri::Builder::default()
.setup(|app| {
letmenu= MenuBuilder::new(app)
.copy()
.separator()
.undo()
.redo()
.cut()
.paste()
.select_all()
.item(&PredefinedMenuItem::copy(app, Some("custom text"))?)
.build()?;
app.set_menu(menu)?;
Ok(())
})
}

```

For more preset capabilities, please refer to the documentation `PredefinedMenuItem`.
## Change menu status
If you want to change the status of the menu, such as text, icon, or check status, you can `set_menu` again:
  * JavaScript 
  * Rust 


```

import {
Menu,
CheckMenuItem,
IconMenuItem,
MenuItem,
} from'@tauri-apps/api/menu';
import { Image } from'@tauri-apps/api/image';
let currentLanguage = 'en';
const check_sub_item_en = await CheckMenuItem.new({
id: 'en',
text: 'English',
checked: currentLanguage === 'en',
action: () => {
currentLanguage = 'en';
check_sub_item_en.setChecked(currentLanguage === 'en');
check_sub_item_zh.setChecked(currentLanguage === 'cn');
console.log('English pressed');
},
});
const check_sub_item_zh = await CheckMenuItem.new({
id: 'zh',
text: 'Chinese',
checked: currentLanguage === 'zh',
action: () => {
currentLanguage = 'zh';
check_sub_item_en.setChecked(currentLanguage === 'en');
check_sub_item_zh.setChecked(currentLanguage === 'zh');
check_sub_item_zh.setAccelerator('Ctrl+L');
console.log('Chinese pressed');
},
});
// Load icon from path
const icon = await Image.fromPath('../src/icon.png');
const icon2 = await Image.fromPath('../src/icon-2.png');
const icon_item = await IconMenuItem.new({
id: 'icon_item',
text: 'Icon Item',
icon: icon,
action: () => {
icon_item.setIcon(icon2);
console.log('icon pressed');
},
});
const text_item = await MenuItem.new({
id: 'text_item',
text: 'Text Item',
action: () => {
text_item.setText('Text Item Changed');
console.log('text pressed');
},
});
const menu = await Menu.new({
items: [
{
id: 'change menu',
text: 'change_menu',
items: [text_item, check_sub_item_en, check_sub_item_zh, icon_item],
},
],
});
awaitmenu.setAsAppMenu();

```

```

// change-menu-status
#![cfg_attr(not(debug_assertions), windows_subsystem ="windows")]
use tauri::{
image::Image,
menu::{CheckMenuItemBuilder, IconMenuItem, MenuBuilder, MenuItem, SubmenuBuilder},
};
fnmain() {
tauri::Builder::default()
.setup(|app| {
letcheck_sub_item_en= CheckMenuItemBuilder::with_id("en", "EN")
.checked(true)
.build(app)?;
letcheck_sub_item_zh= CheckMenuItemBuilder::with_id("zh", "ZH")
.checked(false)
.build(app)?;
lettext_menu= MenuItem::with_id(
app,
"change_text",
&"Change menu".to_string(),
true,
Some("Ctrl+Z"),
)
.unwrap();
leticon_menu= IconMenuItem::with_id(
app,
"change_icon",
&"Change icon menu",
true,
Some(Image::from_bytes(include_bytes!("../icons/icon.png")).unwrap()),
Some("Ctrl+F"),
)
.unwrap();
letmenu_item= SubmenuBuilder::new(app, "Change menu")
.item(&text_menu)
.item(&icon_menu)
.items(&[&check_sub_item_en, &check_sub_item_zh])
.build()?;
letmenu= MenuBuilder::new(app).items(&[&menu_item]).build()?;
app.set_menu(menu)?;
app.on_menu_event(move|_app_handle:&tauri::AppHandle, event| {
matchevent.id().0.as_str() {
"change_text"=> {
text_menu
.set_text("changed menu text")
.expect("Change text error");
text_menu
.set_text("changed menu text")
.expect("Change text error");
}
"change_icon"=> {
icon_menu
.set_text("changed menu-icon text")
.expect("Change text error");
icon_menu
.set_icon(Some(
Image::from_bytes(include_bytes!("../icons/icon-2.png")).unwrap(),
))
.expect("Change icon error");
}
"en"|"zh"=> {
check_sub_item_en
.set_checked(event.id().0.as_str() =="en")
.expect("Change check error");
check_sub_item_zh
.set_checked(event.id().0.as_str() =="zh")
.expect("Change check error");
check_sub_item_zh.set_accelerator(Some("Ctrl+L"))
.expect("Change accelerator error");
}
_=> {
println!("unexpected menu event");
}
}
});
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

© 2025 Tauri Contributors. CC-BY / MIT
