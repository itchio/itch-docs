# Protocol URLs and automation

The app registers the `itch://` URL scheme (and `itchio://`, which is
treated the same way). Opening one of these URLs from a web page, another
program or the command line brings the app to the front and performs an
action or opens a page. This page lists the URLs and command-line entry
points the app supports for automating it from outside.

*Note: the canary build of the app uses `kitch://` and `kitchio://`
instead, and `--appname kitch` for itch-setup. Everything below applies
with those substitutions.*

If you are building your own launcher rather than driving the itch app,
see [Building a launcher with
butlerd](https://itch.io/docs/butler/launcher-integration.html) in the
butler documentation instead.

No URL performs an action on its own: each one either opens a page, or
opens a dialog that the user confirms. Unattended operations are
available through the command line flags described further down.

## Action URLs

These URLs open a dialog for the user to confirm. If the user isn't
logged in yet, the URL is kept until login completes and then processed.

### Install a game

```
itch://install?game_id=<game id>
itch://install?game_id=<game id>&upload_id=<upload id>
```

Opens the install dialog for the game, letting the user choose the upload
and install location. When `upload_id` is given, that upload is
pre-selected. Nothing is downloaded without the user confirming.

The game id is the numeric id of the game, which you can find on the
game's edit page on itch.io, or through the [API](api/README.md). An
upload id refers to one of the game's files, and is only needed when a
game has several uploads for the same platform.

### Launch a game

```
itch://install?game_id=<game id>&launch
itch://install?game_id=<game id>&upload_id=<upload id>&launch
```

The bare `launch` parameter asks the app to launch the game rather than
just install it:

* When the game is already installed, the app asks the user to confirm and
  then launches it.
* When the game isn't installed, the install dialog opens instead, and the
  game launches once the install finishes.

Launchers that want to start a game without a prompt should use
`itch-setup --run-game` instead, described below.

### Add a game to Steam

```
itch://steam-shortcuts
itch://steam-shortcuts?game_id=<game id>
itch://steam-shortcuts?game_id=<game id>&mode=direct
```

Opens the app's [Steam shortcuts](../using/steam-shortcuts.md) dialog,
which creates entries in the user's Steam library for games installed
through the app. With `game_id`,
that game is checked in advance. `mode` picks how the shortcut launches
the game: `itch` (the default) runs it through the app, `direct` points
Steam at the game's own executable. A `direct` request is ignored for
games without a suitable executable. Nothing is written to Steam until the
user saves, and Steam has to be closed at that point.

## Navigation URLs

Any other `itch://` URL opens the matching page inside the app. The useful
ones to link to are:

| URL | Opens |
| --- | --- |
| `itch://library` | The user's library |
| `itch://library/owned` | Owned games |
| `itch://library/installed` | Installed games |
| `itch://library/bundles/<bundle id>` | The games in a bundle the user owns |
| `itch://collections` | The user's collections |
| `itch://collections/<collection id>` | One collection |
| `itch://games/<game id>` | A game's page |
| `itch://caves/<cave id>` | One install of a game (a "cave" in the app's terms) |
| `itch://featured` | The explore page |
| `itch://dashboard` | The user's creator dashboard |
| `itch://upload` | The upload page for creators |
| `itch://downloads` | The downloads page |
| `itch://preferences` | Preferences |
| `itch://locations` | Install locations |
| `itch://locations/<install location id>` | One install location |
| `itch://applog` | The app's log, useful for support |

Plain itch.io web addresses work as well: opening
`https://someone.itch.io/some-game` through the app shows that game's
page in the app's browser.

The app uses this scheme for its own internal pages too, so other paths
exist. Only the ones above are meant for outside use; the rest can change
between versions.

## Opening a URL from the command line

The operating system routes `itch://` URLs to the app the same way it
does for a browser, so the usual tools work whether or not the app is
already running:

```sh
# Linux
xdg-open "itch://install?game_id=12345&launch"

# macOS
open "itch://install?game_id=12345&launch"

# Windows
start "" "itch://install?game_id=12345&launch"
```

Passing the URL directly as an argument to the app's executable also
works on Linux and Windows.

## itch-setup

`itch-setup` is the native program that installs and updates the app. A
copy of it stays at a fixed path after installation, which doesn't change
when the app updates:

| Platform | Path |
| --- | --- |
| Linux | `~/.itch/itch-setup` |
| Windows | `%LOCALAPPDATA%\itch\itch-setup.exe` |

On macOS there is no launcher copy; use the `open` command with a URL
instead.

Always pass `--appname itch` (or `--appname kitch` for canary) so
itch-setup knows which app it is working with.

### Launching a game headlessly

```sh
~/.itch/itch-setup --appname itch --run-game <game id>
~/.itch/itch-setup --appname itch --run-game <game id> --profile-id <user id>
```

`--run-game` starts an installed game without opening the app. itch-setup
runs the game through the app's copy of butler, applying the same launch
configuration the app would (the selected launch target, sandbox settings,
environment from the app manifest) and stays running until the game
exits. Steam shortcuts created by the app use it.

`--profile-id` is the itch.io user id of the account whose play sessions
the launch should be recorded under. Without it, an account that has
access to the game is picked from those logged into the app.

Some launches can't be done headlessly: browser games, games that need a
login first, or a game that isn't installed. In those cases itch-setup
hands the launch to the app, which opens the corresponding
`itch://install?...&launch` URL, installing the app first if it is missing.

### Launching the app with arguments

```sh
~/.itch/itch-setup --appname itch --prefer-launch "itch://library"
```

`--prefer-launch` starts the installed app if there is a valid version,
and runs the installer otherwise. Any further arguments are passed on to
the app, so a protocol URL given here is handled as described above. This
is supported on Linux and Windows.

### Other flags

| Flag | Effect |
| --- | --- |
| `--shutdown` | Ask the running app to quit; does nothing when the app isn't installed |
| `--upgrade` | Update the app to the latest version without launching it |
| `--info` | Print information about the installed app and exit |
| `--silent` | Install without showing the installer window |
| `--uninstall` | Remove the app |
| `--log-file <path>` | Also write itch-setup's JSON log lines to this file |

Only one of the action flags may be given at a time.

## App command-line flags

The app executable itself understands these flags:

* `--hidden` starts the app minimized to the system tray. The "open at
  login" preference uses this.
* `--shutdown` asks the running app to quit, the same way as choosing
  Quit in the app: if a game is running, the user is asked whether to
  close it. When no app is running, the command exits immediately.
  `itch-setup --shutdown` invokes this without needing the app's path.
* Any `itch://` URL argument is processed as described above. When the
  app is already running, the argument is forwarded to the running
  instance.
