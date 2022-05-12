---
title: Tools for working with ELFs
---

Here I collect a list of tools which I found useful for working with ELFs (incl. executables and shared libraries):

- [**`objdump`**](https://en.wikipedia.org/wiki/Objdump): `objdump --TC xxx.so`
  - The `-C` flag enables demangling.
- [**`ldd`**](https://man7.org/linux/man-pages/man1/ldd.1.html): `ldd xxx.so`
  - Print shared object dependencies, which allows you to find out which shared library is missing.
- **`ld`**: `ld xxx.so`
- **`nm`**: `nm xxx.so`
  - The `-C` flag enables demangling.
- **`readelf`**: `readelf --dyn-syms xxx.so`
  - The `--demangle` flag enables demangling.
- [**`patchelf`**](https://github.com/NixOS/patchelf):
  - Particularly useful when you bring your own GLIBC and want to link to the updated one.