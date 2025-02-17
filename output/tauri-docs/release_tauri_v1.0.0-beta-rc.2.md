Skip to content
# tauri@1.0.0-beta-rc.2
ReturnView on GitHub
  * Prevent “once” events from being able to be called multiple times.
  * `Window::trigger(/*...*/)` is now properly `pub` instead of `pub(crate)`.
  * `Manager::once_global(/*...*/)` now returns an `EventHandler`.
  * `Window::once(/*...*/)` now returns an `EventHandler`.
  * (internal) `event::Listeners::trigger(/*...*/)` now handles removing “once” events.
  * ece243d don’t remove once listener on new thread (#1506) on 2021-04-14
  * Window and global events can now be nested inside event handlers. They will run as soon as the event handler closure is finished in the order they were called. Previously, calling events inside an event handler would produce a deadlock.


Note: The order that event handlers are called when triggered is still non-deterministic.
  * e447b8e allow event listeners to be nested (#1513) on 2021-04-15


© 2025 Tauri Contributors. CC-BY / MIT
