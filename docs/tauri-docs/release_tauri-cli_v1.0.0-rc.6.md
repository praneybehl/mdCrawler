Skip to content
# tauri-cli@1.0.0-rc.6
ReturnView on GitHub
  * Improve “waiting for your dev server to start” message. 
    * 5999379f chore(cli): improve “waiting for dev server” message, closes #3491 (#3504) on 2022-02-18
  * Do not panic if the updater private key password is wrong. 
    * 17f17a80 fix(cli): do not panic if private key password is wrong, closes #3449 (#3495) on 2022-02-17
  * Check the current folder before checking the directories on the app and tauri dir path lookup function. 
    * a06de376 fix(cli): path lookup should not check subfolder before the current one (#3465) on 2022-02-15
  * Fixes the signature of the `signer sign` command to not have duplicated short flags. 
    * a9755514 fix(cli): duplicated short flag for `signer sign`, closes #3483 (#3492) on 2022-02-17


© 2025 Tauri Contributors. CC-BY / MIT
