# Dependencies

itch uses a few external tools to download & manage content.

It installs and keeps them up-to-date automatically, which means you should never have to worry about them. However, in the interest of you knowing what runs on your computer, they're documented here.

Third-party programs are built from source. Home-grown programs are continuously built on our CI servers.

## Directories

All dependencies are downloaded and extracted into the following folders:

* `%APPDATA%\itch\broth` on Windows
* `~/Library/Application Support/itch/broth` on OSX
* `~/.config/itch/broth` on Linux

## Packages

### butler

butler is a homemade command-line tool written in Go, distributed under the MIT license.

It runs as a daemon process (butlerd) that communicates with the itch app via JSON-RPC 2.0 over TCP. butler handles downloading, installing, updating, and launching games, and maintains a SQLite database to track installation data.

Its source code is available for you to audit, debug, and improve at will:

* [https://github.com/itchio/butler](https://github.com/itchio/butler)

### itch-setup

itch-setup is a Go program that handles the initial installation of the itch app on all platforms. It also manages self-update checks and restarts the app when a new version is available.

Its source code is available here:

* [https://github.com/itchio/itch-setup](https://github.com/itchio/itch-setup)

## Implementation

The logic for downloading, extracting and installing itch dependencies can be found in the `broth` directory.

The authors are aware of the irony of having an ad-hoc, half-baked Implementation of a package manager inside a package managing application, itself installed by various other package managers, and there is no need to point it out!

