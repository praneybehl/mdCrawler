Skip to content
# @tauri-apps/cli@1.0.0-rc.1
ReturnView on GitHub
  * Fix `init` command prompting for values even if the argument has been provided on the command line. 
    * def76840 fix(cli.rs): do not prompt for `init` values if arg set (#3400) on 2022-02-11
    * 41052dee fix(covector): add cli.js to change files on 2022-02-11
  * Fixes CLI freezing when running `light.exe` on Windows without the `--verbose` flag. 
    * 8beab636 fix(cli): build freezing on Windows, closes #3399 (#3402) on 2022-02-11
  * Respect `.gitignore` configuration when looking for the folder with the `tauri.conf.json` file. 
    * 9c6c5a8c perf(cli.rs): improve performance of tauri dir lookup reading .gitignore (#3405) on 2022-02-11
    * 41052dee fix(covector): add cli.js to change files on 2022-02-11


© 2025 Tauri Contributors. CC-BY / MIT
