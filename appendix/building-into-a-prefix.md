# Building Linux software into a prefix

If, instead of using a pre-made game engine package like Unity, you prefer picking a few libraries and mixing them in your own way, you might reach a point where you want to build your own versions of those libraries so that you can bundle them with your game.

_See the _[_Distributing Linux builds_](../integrating/platforms/linux.md)_ page of this book_

## What is a prefix?

When you install software on Linux, files are placed into a directory hierarchy called the prefix. The default prefix is usually `/usr` or `/usr/local`, which means:

* Binaries are installed in `/usr/bin/`
* Libraries are installed in `/usr/lib/`
* Data files are installed in `/usr/share/`
* ...and so on

By specifying your own prefix, you can install a library into an unprivileged, user-owned directory, ready for bundling with your game. Building each library into its own prefix makes it clear which files belong to which library.

For the purpose of [bundling your libraries](../integrating/platforms/linux.md), you would copy the files from your prefix's `lib/` directory into your game's bundled library folder.

## CMake

CMake is the most common build system for open-source C/C++ libraries. The recommended build process uses an out-of-tree build directory:

```bash
$ cmake -B build -DCMAKE_INSTALL_PREFIX=$HOME/myprefix/chipmunk2d
$ cmake --build build
$ cmake --install build
```

## Meson

[Meson](https://mesonbuild.com/) is used by many Linux libraries, particularly in the freedesktop/GNOME ecosystem. It always uses out-of-tree builds:

```bash
$ meson setup build --prefix=$HOME/myprefix/my-library
$ meson compile -C build
$ meson install -C build
```

## autotools \(./configure && make\)

Some older libraries still use autotools. The build process is:

```bash
$ ./configure --prefix=$HOME/myprefix/sdl2
$ make
$ make install
```

_Note: _`--prefix`_ usually has to be an absolute path._

For a cleaner setup, you can do an out-of-tree build by running configure from a separate directory:

```bash
$ mkdir build && cd build
$ ../my-library-source/configure --prefix=$HOME/myprefix/my-library
$ make
$ make install
```

This keeps the source directory untouched.

## Why build your own libraries?

Copying libraries straight out of `/usr/lib` and into your game's bundle is not always the best idea. Distribution-packaged libraries may have patches or configuration specific to that distribution that cause them to behave differently elsewhere.

Building from source also gives you flexibility: if you find a bug in a library you depend on, you can apply a fix and ship it yourself without waiting for the upstream maintainer and distribution packagers to catch up.
