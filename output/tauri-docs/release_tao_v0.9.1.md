Skip to content
# tao@0.9.1
ReturnView on GitHub
  * Fix the size of the slice passed to `DragQueryFileW` by passing `std::mem::transmute(path_buf.spare_capacity_mut())` instead of `&amp;mut path_buf`. 
    * d0dbfa1a Fix drag drop on Windows (#401) on 2022-05-23


© 2025 Tauri Contributors. CC-BY / MIT
