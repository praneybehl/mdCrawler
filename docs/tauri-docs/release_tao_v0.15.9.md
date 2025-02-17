Skip to content
# tao@0.15.9
ReturnView on GitHub
  * On Linux, Fix mnemonics for submenus. 
    * 77569c89 fix(linux): fix mnemonics for submenus (#650) on 2022-12-20
    * e313ef69 publish new versions (#651) on 2023-01-09
    * 3cd851d1 Revert “Publish New Versions” (#663) on 2023-01-09
  * On iOS, add Sync trait to `EventLoopProxy` when `T` has Send trait. 
    * 651137ce On iOS, add Sync trait on `EventLoopProxy` when `T` has Send trait (#658) on 2023-01-04
    * e313ef69 publish new versions (#651) on 2023-01-09
    * 3cd851d1 Revert “Publish New Versions” (#663) on 2023-01-09
  * On Linux, fix setting min/max size clears the other. 
    * 9927c3a5 fix(linux): fix setting min/max size, clears the other (#669) on 2023-01-11
  * Fix resize event emits before fullscreen actually exit. 
    * 3867e7b7 On macOS, fix resize event emits before fullscreen actually exit (#662) on 2023-01-09
    * e313ef69 publish new versions (#651) on 2023-01-09
    * 3cd851d1 Revert “Publish New Versions” (#663) on 2023-01-09
  * Add `WindowBuilder::with_visible_on_all_workspaces` and `Window::set_visible_on_all_workspaces`. 
    * 0aa2176c feat: add `set_visible_on_all_workspaces`, closes #185 (#666) on 2023-01-11
  * Add `WindowExtWindows::set_undecorated_shadow` and `WindowBuilderExtWindows::with_undecorated_shadow` to draw the drop shadow behind a borderless window. 
    * f832ca99 feat(Windows): undecorated shadows (#664) on 2023-01-10


© 2025 Tauri Contributors. CC-BY / MIT
