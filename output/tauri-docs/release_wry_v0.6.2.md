Skip to content
# wry@0.6.2
ReturnView on GitHub
  * Add pipe back to version check for covector config. This prevents the CI failure on publish if it exists already. The issue was patched in covector (and tests in place so it doesn’t break in the future). 
    * a32829c chore: add pipe for publish check back in (#131) on 2021-03-28
  * Fix messages to the webview from the backend being delayed on Linux/GTK when the user is not actively engaged with the UI. 
    * d2a2a9f fix: spawn async event loop on gtk to prevent delayed messages (#135) on 2021-03-31
  * Add draggable regions, just add `drag-region` class to the html element. 
    * b2a0bfc feat/ draggable-region (#92) on 2021-03-25
  * Add event listener in application proxy 
    * c49846c feat: event listener (#129) on 2021-03-26
  * Better result error handling 
    * 485035f chore: better result error handling (#124) on 2021-03-21
  * Fix visibility on webview2 when window was invisible previously and then shown. 
    * 6d31706 Fix visibility on webview2 when window was invisible previously (#128) on 2021-03-24


© 2025 Tauri Contributors. CC-BY / MIT
