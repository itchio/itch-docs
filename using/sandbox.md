# The itch.io sandbox

The itch.io sandbox tries to prevent several typical attacks a malicious game could run on a computer.

For example, the sandbox will:

* Limit what files a process can read
* Limit what files a process can write to
  * On Linux, give games a persistent per-game home directory and restrict access to sensitive host files
* On Windows, run games as a different, less-privileged user

## Scope

Attacks that the itch.io sandbox try to prevent include:

### Stealing your itch.io credentials

This is especially important if you're a developer. Someone stealing your butler API key could push a malicious build of your game to all your players.

### Stealing your browser cookies / saved passwords

This affects everyone. See [pycookiecheat](https://github.com/n8henrie/pycookiecheat) for an example of how easy it is to decrypt Chrome's cookies.

Stealing saved passwords is especially scary as it can happen no matter how secure the servers are in 2016, millions of hwitter credentials were leaked due to malware harvesting saved passwords from browsers, highlighting how vulnerable locally-stored credentials can be.

### Additional notes

It shouldn't be possible to escape the sandbox by forking/spawning/execing.

The sandbox makes no attempts to protect against:

* The user collaborating in being attacked \(giving out their password, running untrusted software, etc.\)
* Vulnerabilities in graphics drivers \(see WebGL security history\)

It's not the answer to everything, but running games via the sandbox safer than not doing so.

## Save game access

Some sandbox modes create isolated or simulated user directories for each game. For example, on Linux, each sandboxed game may get its own `$HOME` directory. This means:

* Games running inside the sandbox won't see save files stored in your real home directory
* Save files created inside the sandbox won't appear in your real home directory either

**No data is deleted** when you change sandbox settings. Your save files still exist on disk, but the game may not be able to find them under the new configuration.

If you switch between sandbox modes (or turn the sandbox on or off), you may need to manually copy or move save files between your real home directory and the sandboxed location. See the platform-specific pages below for details on where each sandbox type stores its data.

### Implementation

For implementation details, please refer to the following platform-specific pages:

* [Windows sandboxing](sandbox/windows.md)
* [macOS sandboxing](sandbox/macos.md)
* [Linux sandboxing](sandbox/linux.md)



