# Launch settings

Every installed game has its own launch settings. To find them, open the game's
**Manage** dialog (from the game's page, or from its right-click menu in your
library) and look for the **Launch settings** section.

## Launch options

The **Launch options** field lets you pass extra arguments to the game, or run
it through another program.

Plain text is passed to the game as extra arguments:

```
--fullscreen
```

To run the game through a wrapper, such as a compatibility layer or a debugging
tool, write `%command%` where the game's command should go. It expands to the
game's executable along with all of its arguments:

```
mangohud %command%
```

Leading `NAME=value` pairs set environment variables for the game:

```
MANGOHUD=1 %command%
```

The field is parsed with shell-style quoting, so quote arguments that contain
spaces. `%command%` must be a standalone word and can appear at most once.

Launch options only apply to games that run as native executables. They have no
effect on web games.

## Sandbox

The rest of the section overrides your global [sandbox](sandbox.md) preferences
for this game. Every setting defaults to **Default**, which inherits the
corresponding global preference.

* **Sandbox** turns the sandbox on or off for this game.

On Linux, a few more settings control how the sandbox behaves:

* **Sandbox type** picks the backend: **Auto**, **Bubblewrap**, or
  **Firejail**. See [Linux sandboxing](sandbox/linux.md) for the differences.
* **Network access in sandbox** allows or blocks network access for the game.
* **Allowed environment variable names** is a comma or whitespace separated
  list of host environment variables to pass into the sandbox.

These extra settings are shown dimmed when the sandbox isn't going to be used.
They still take effect if the game's [manifest](../integrating/manifest.md)
asks to be sandboxed.
