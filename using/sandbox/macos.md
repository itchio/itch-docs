
# macOS sandboxing

The itch.io app uses macOS's built-in `sandbox-exec` facility to sandbox games. Each time a game launches, the app dynamically generates a sandbox policy written in Apple's Sandbox Profile Language (SBPL) and stores it at `{install_folder}/.itch/isolate-app.sb`.

The policy starts from a **deny-all** default and explicitly allows only the permissions a game needs to run.

Here's the policy template the itch app uses:

  * <https://github.com/itchio/smaug/blob/master/runner/policies/sandboxexec.go>

## How it works

When a game launches with the sandbox enabled:

1. The app generates an SBPL policy file tailored to the game's install location
2. The environment is filtered to an allowlist of safe variables (`HOME`, `USER`, `PATH`, locale settings, `TMPDIR`, and itch.io launch variables)
3. The game is launched through `sandbox-exec -f {policy_file}`

For **app bundles** (`.app` directories), the app creates a temporary shim bundle that wraps the original binary with a shell script invoking `sandbox-exec`. This allows app bundles to launch through the standard macOS app mechanism while still being sandboxed.

For **standalone executables**, `sandbox-exec` is invoked directly.

## Policy modes

The sandbox supports two policy modes:

- **Balanced** (default) — A hardened profile that limits device access to `/dev/null`, `/dev/random`, and `/dev/urandom` only.
- **Legacy** — A broader profile for compatibility with older games. Allows full `/dev` access and wider read access to `/private`.

The policy mode can be configured in the app's preferences. If a game fails to launch under the balanced profile, try switching to legacy mode before reporting an issue.

## What the sandbox allows

### Filesystem write access

- `~/Library` subpaths: Application Support, Preferences, Logs, Caches, KeyBindings, Saved Application State
- The game's own install folder (full read-write)
- `/var/folders` and `/private/var/folders` (macOS temp storage)

### Filesystem read access

- System libraries and binaries: `/usr/local`, `/usr/share`, `/usr/lib`, `/usr/bin`, `/bin`, `/System/Library`
- Rosetta 2 translation support: `/usr/libexec/rosetta`, `/Library/Apple/usr/libexec/oah` (for running x86_64 games on Apple Silicon)
- Java: `/Library/Java/JavaVirtualMachines`
- System preferences: `/etc`, `/private/etc`, `/Library/Preferences`
- Fonts and audio: `/Library/Audio`, `/Library/Fonts`, `~/Library/Fonts`
- Input methods and keyboard layouts: `~/Library/Keyboard Layouts`, `~/Library/Input Methods`
- `/Applications` (read-only)

### Explicitly denied

Even though `~/Library/Application Support` is writable, the following subpaths are explicitly blocked to prevent credential theft:

- `~/Library/Application Support/itch` and `~/Library/Application Support/kitch` (itch.io app config)
- `~/Library/Application Support/Google` (Chrome data)
- `~/Library/Application Support/Mozilla` (Firefox data)

### Network

Network access (`network-bind` and `network-outbound`) is allowed by default. It can be disabled with the **Disable network access in sandbox** preference.

### IPC and system access

The following are allowed for compatibility with game frameworks like SDL2 and Electron:

- Mach IPC (`mach-lookup`, `mach-register`)
- POSIX shared memory (`ipc-posix*`)
- System sockets (`system-socket`)
- IOKit device access (`iokit-open`)
- Process forking and execution (`process-fork`, `process-exec`)
- Hardware/OS limit probing (`sysctl-read`)

## Settings

The sandbox can be configured from the itch.io app's preferences:

- **Enable itch.io sandbox** — Master toggle to enable or disable sandboxing
- **Disable network access in sandbox** — Prevents all network access from sandboxed games
- **Policy mode** — Choose between **Balanced** (default) or **Legacy** for broader compatibility
- **Allowed environment variable names** — A comma or whitespace-separated list of extra host environment variable names to pass into the sandbox

Games can detect that they are running inside the sandbox by checking for the `ITCHIO_SANDBOX=1` environment variable.

## Troubleshooting

If a game is broken by the sandbox:

1. **Check Console.app.** Open the built-in Console.app and look for `sandboxd` messages to see which permissions are being denied. Shutting down other applications can help reduce noise in the logs.

2. **Try legacy mode.** If the game fails under the default balanced policy, switch the policy mode to legacy in the app's preferences and try again.

3. **Inspect the policy.** Open `{install_folder}/.itch/isolate-app.sb` to see the exact SBPL policy being applied to the game.

4. **Report the issue.** If you can't resolve the problem, open an issue on our [issue tracker](https://github.com/itchio/itch/issues) with the Console.app output and the contents of the `.sb` file.
