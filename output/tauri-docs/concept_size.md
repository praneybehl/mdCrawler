Skip to content
# App Size
While Tauri by default provides very small binaries it doesn’t hurt to push the limits a bit, so here are some tips and tricks for reaching optimal results.
## Cargo Configuration
One of the simplest frontend agnostic size improvements you can do to your project is adding a Cargo profile to it.
Dependent on whether you use the stable or nightly Rust toolchain the options available to you differ a bit. It’s recommended you stick to the stable toolchain unless you’re an advanced user.
  * Stable 
  * Nightly 


src-tauri/Cargo.toml```

[profile.dev]
incremental = true# Compile your binary in smaller steps.
[profile.release]
codegen-units = 1# Allows LLVM to perform better optimization.
lto = true# Enables link-time-optimizations.
opt-level = "s"# Prioritizes small binary size. Use `3` if you prefer speed.
panic = "abort"# Higher performance by disabling panic handlers.
strip = true# Ensures debug symbols are removed.

```

src-tauri/Cargo.toml```

[profile.dev]
incremental = true# Compile your binary in smaller steps.
rustflags = ["-Zthreads=8"] # Better compile performance.
[profile.release]
codegen-units = 1# Allows LLVM to perform better optimization.
lto = true# Enables link-time-optimizations.
opt-level = "s"# Prioritizes small binary size. Use `3` if you prefer speed.
panic = "abort"# Higher performance by disabling panic handlers.
strip = true# Ensures debug symbols are removed.
trim-paths = "all"# Removes potentially privileged information from your binaries.
rustflags = ["-Cdebuginfo=0", "-Zthreads=8"] # Better compile performance.

```

### References
  * incremental: Compile your binary in smaller steps.
  * codegen-units: Speeds up compile times at the cost of compile time optimizations.
  * lto: Enables link time optimizations.
  * opt-level: Determines the focus of the compiler. Use `3` to optimize performance, `z` to optimize for size, and `s` for something in-between.
  * panic: Reduce size by removing panic unwinding.
  * strip: Strip either symbols or debuginfo from a binary.
  * rpath: Assists in finding the dynamic libraries the binary requires by hard coding information into the binary.
  * trim-paths: Removes potentially privileged information from binaries.
  * rustflags: Sets Rust compiler flags on a profile by profile basis. 
    * `-Cdebuginfo=0`: Whether debuginfo symbols should be included in the build.
    * `-Zthreads=8`: Increases the number of threads used during compilation.


© 2025 Tauri Contributors. CC-BY / MIT
