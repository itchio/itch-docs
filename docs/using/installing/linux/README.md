# Installing on Linux

```{toctree}
:hidden:

ubuntu-and-debian
fedora
archlinux
gentoo
```

These instructions apply to itch v25 and up.

> If you have an older version of the app installed, uninstall it before
> following those instructions.

Simply head to [https://itch.io/app](https://itch.io/app) and grab the Linux installer.

## Installing

Run `chmod +x itch-setup && ./itch-setup` (or use your file manager
to set the executable bit and double-click it).

You'll need GTK3 installed (`libgtk-3-0` package on most Debians).

The latest version of itch downloads and installs to `~/.itch`. After
a successful installation, itch starts up.

## Updating

When a new version of the app becomes available, "A new version is available"
shows up in the top right corner.

Clicking it allows you to restart into the new version.

> The APT and YUM repositories are no longer officially supported.
>
> [the itch installer](https://github.com/itchio/itch-setup) is open-source, and purpose-built on top of the same technology as [butler](https://github.com/itchio/butler), our diffing and patching solution.
>
> Please open issues directly on the itch-setup repository if you
> encounter issues or if it doesn't cater to your use-case!

## Uninstalling

Run `~/.itch/itch-setup --uninstall` to uninstall itch from your system.

> Note that this won't remove your library, which resides at `$HOME/.config/itch`,  
> along with any additional install locations you have added from the app.
>
> If you really want to uninstall everything, you'll have to take care of that folder as well.
