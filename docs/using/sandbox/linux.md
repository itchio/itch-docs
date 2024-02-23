# Linux sandboxing

On Linux, the itch app uses [firejail](https://github.com/netblue30/firejail) to sandbox applications.

It's similar to macOS's `sandbox-exec`: applies a simple policy file, based on seccomp-bpf, will work on any Linux kernel &gt;3.x, doesn't rely on SELinux/AppArmor

Instead of running as a different user, firejail intercepts syscalls and even has advanced functionality like exposing a virtual filesystem so that changes can be recorded and later committed or discarded \(this way,  
the sandboxed application won't fail, the worst case scenario is: some things won't persist across app restarts\).

## One-time setup

Due to the way firejail works, its binary needs to be SUID root - which means that, when executed by any user, it'll be as if it was run by root. Sandboxed applications however do _NOT_ have root privilege.

That's why the itch.io app asks you for a password. To set the SUID bit on the firejail binary.

Feel free to [vet the code](https://github.com/itchio/butler/search?utf8=%E2%9C%93&q=EnsureSuidRoot&type=) responsible for making binaries executables and SUID root if needed.

## Troubleshooting

If your game is broken by the itch.io sandbox on Linux, we recommend taking a look at the app's output when launching a game. Simply exit the itch app, and start it again from a terminal, using the `itch` command.

firejail should print a message whenever a permission is denied, which should help you pinpoint what it is that your game is doing that isn't allowed by the sandbox.

To review the policy the itch.io app is applying to your game, open the `.itch/isolate-app.profile` placed in the game's install folder.

The default sandbox policy should be more than enough to get most games running, but if you run into an issue that you need help resolving, feel free to open an issue on our [Issue Tracker](https://github.com/itchio/itch/issues)

## Frequently Asked Questions

### Have you heard of \(other sandbox\)? It seems more secure.

Why yes! Yes we have! And when it'll do everything we need it to do, we'll switch to it.[^1]

[^1]: But not a second sooner.

