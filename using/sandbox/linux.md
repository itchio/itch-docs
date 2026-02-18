# Linux sandboxing

The itch.io app supports multiple sandbox backends on Linux.

When the sandbox type is set to **Auto** (the default), the app selects a
backend in this order:

1. **Flatpak-spawn** — if running inside a Flatpak (detected by the presence of `/.flatpak-info`)
2. **Bubblewrap** — if `bwrap` is available
3. **Firejail** — will use system install of `firejail` if available, otherwise downloads and installs its own copy

## Sandbox types

### Bubblewrap

[Bubblewrap](https://github.com/containers/bubblewrap) (`bwrap`) is the preferred sandbox backend. It uses Linux namespaces (user, PID, UTS, and optionally network) to isolate games from the rest of the system.

Bubblewrap must be installed on your system. The app looks for `bwrap` in your `PATH`. Most Linux distributions provide it as a package (e.g. `bubblewrap` on Debian/Ubuntu, Fedora, Arch, etc.). If `bwrap` is not found and the sandbox type is set to Auto, the app will fall back to Firejail.

When a game launches under Bubblewrap:

- System directories (`/usr`, `/lib`, `/bin`, `/sbin`, `/etc`, `/sys`) are mounted **read-only**
- The game's install folder is mounted read-write
- A persistent per-game home directory is created at `{install_folder}/.itch/home` and mounted as the game's `$HOME`
- A temporary directory at `{install_folder}/.itch/temp` is provided (cleaned up after the game exits)
- The environment is cleared and only an allowlisted set of variables is passed through

Bubblewrap provides access to:

- **GPU** — `/dev/dri` and NVIDIA device nodes
- **Audio** — ALSA (`/dev/snd`), PulseAudio, and PipeWire sockets
- **Display** — X11 (`/tmp/.X11-unix`, `~/.Xauthority`) and Wayland sockets
- **D-Bus** — Session bus socket
- **Game controllers** — `/dev/input`

Each game gets its own isolated storage under the game's install folder:

```
{install_folder}/.itch/
├── home/    # Persistent home directory, mounted as the game's $HOME
└── temp/    # Temporary directory, cleaned up after the game exits
```

The `.itch/home` directory is mounted as the game's `$HOME`. Any save data, configuration files, or other files the game writes to `$HOME` will end up here, stored alongside the game's install folder rather than in your real home directory.

**Note:** Firejail does not redirect `$HOME`. Games running under Firejail write directly to your real home directory (with certain sensitive paths blacklisted). Because of this, **switching between sandbox types may cause games to lose access to previously created save data**. Games launched under Bubblewrap store their data in `{install_folder}/.itch/home`, while games launched under Firejail store data in your real home directory. If you switch sandbox types, you will need to manually copy save data between these locations.

### Firejail

[Firejail](https://github.com/netblue30/firejail) is an alternative sandbox that uses seccomp-bpf filtering. It generates a per-game profile at `{install_folder}/.itch/isolate-app.profile`.

The app will first look for a system-installed `firejail` in your `PATH`. If not found, the app will automatically download and install its own copy.

Firejail is generally **not recommended**. It was the only sandbox backend available for a long time, so its default allowlist is broad for backward compatibility. Unlike Bubblewrap, which starts from a minimal environment and explicitly mounts only what's needed, Firejail uses a blacklist approach: it allows access to most of the filesystem and selectively blocks known sensitive paths. This means its sandbox coverage is less comprehensive.

The profile blacklists access to sensitive directories, including:

- `~/.ssh`, `~/.gnupg`, `~/.aws`, `~/.kube`, `~/.pki`, `~/.local/share/keyrings`, etc.
- Browser profile directories (Chrome, Chromium, Firefox, etc.)
- The itch.io app's own configuration (except the game's data)

Firejail's binary needs to be SUID root to function. If you have a system-installed Firejail, this is typically already configured by your package manager. If the app is using its own downloaded copy, it will prompt for your password the first time to set the SUID bit. Sandboxed games do **not** run with root privileges.

Firejail also supports [local overrides](https://firejail.wordpress.com/documentation-2/building-custom-profiles/): you can place custom profiles at `/etc/firejail/itch_game_{name}.local` or `/etc/firejail/itch_games_globals.local`.

### Flatpak-spawn

When the itch.io app itself is running inside a [Flatpak](https://flatpak.org/), it automatically uses `flatpak-spawn --sandbox` to launch games in an isolated sub-sandbox. The `flatpak-spawn` binary is expected to be available in `PATH` as part of the Flatpak runtime. This backend is selected automatically and cannot be manually chosen. It is always used when the Flatpak environment is detected.


## Settings

The sandbox can be configured from the itch.io app's preferences:

- **Enable itch.io sandbox** — Master toggle to enable or disable sandboxing
- **Sandbox type** — Choose between **Auto**, **Bubblewrap**, or **Firejail**. Flatpak-spawn is used automatically when inside Flatpak and does not appear as a manual option.
- **Disable network access in sandbox** — When enabled, prevents all network access from sandboxed games. Bubblewrap achieves this by unsharing the network namespace; Firejail uses `--net=none`; Flatpak-spawn uses `--no-network`.
- **Allowed environment variable names** — A comma or whitespace-separated list of host environment variable names to pass into the sandbox (e.g. `LUA_CPATH LUA_PATH`). A base set of variables (display, audio, locale, and itch.io launch variables) is always passed through.

Games can detect that they are running inside the sandbox by checking for the `ITCHIO_SANDBOX=1` environment variable.

## Per-game storage

Each sandbox type handles game data storage differently:

- **Bubblewrap** — Redirects `$HOME` to `{install_folder}/.itch/home`, a persistent per-game directory stored alongside the game's install folder. Save data and configuration files written to `$HOME` are kept here, isolated from your real home directory.
- **Firejail** — Does not redirect `$HOME`. Games write directly to your real home directory, with certain sensitive paths blacklisted.
- **Flatpak-spawn** — Filesystem access is managed by Flatpak's own sandboxing. Games generally inherit the itch.io app's view of the home directory, as provided by the Flatpak sandbox.

Because each backend stores game data in a different location, **switching between sandbox types may cause games to lose access to previously created save data**. If you switch, you will need to manually copy save data between these locations.

## Limitations

The current sandbox profile is designed for **compatibility**: it shares the X11 display sockets, session D-Bus, and input devices (`/dev/input`) with the host so that games work out of the box.

On X11, this means a sandboxed game can still monitor keystrokes, capture screen contents, and send synthetic input to other windows. This is a limitation of the X11 protocol itself, which does not isolate clients from each other. Any application connected to the same X display can observe and interact with every other client.

If you run your desktop under **Wayland**, the display server enforces per-client isolation by default, so display-level protections are significantly stronger. If your desktop environment supports it, switching to a Wayland session is the simplest way to reduce this attack surface.

Even on X11, the sandbox still provides meaningful protection: filesystem isolation (Bubblewrap redirects `$HOME` and mounts system directories read-only), optional network isolation, and environment variable filtering prevent many classes of unwanted access.

## Troubleshooting

If a game is broken by the sandbox, try these steps:

1. **Check the app's output.** Exit the itch app and start it again from a terminal using the `itch` command. The sandbox backends print diagnostic messages when permissions are denied or errors occur.

2. **Review the Firejail profile.** If using Firejail, open `{install_folder}/.itch/isolate-app.profile` to see the policy being applied to your game. You can also add local overrides in `/etc/firejail/`.

3. **Try a different backend.** If one sandbox type causes issues, switch to another in the app's preferences.

4. **Report the issue.** If you can't resolve the problem, open an issue on our [issue tracker](https://github.com/itchio/itch/issues) with the terminal output.
