# Known Issues

Here's a list of issues we know about, that you may be experiencing.

### Installer for macOS fails to launch the first time

When launching the installer on macOS for the first time, you'll get the
"This file has been downloaded from the internet" prompt.

Pressing "OK" is remembered, but the first launch doesn't do anything.
Opening "Install itch.app" a second time does work.

### Overriding the default directory in installer-based games causes issues on computers with multiple user accounts.

The details of this issue can be found at https://github.com/itchio/itch/issues/1279

In short: InnoSetup installers set up Start Menu and Desktop shortcuts. If a
game using an InnoSetup installer is installed via the itch app, on the same
computer, but with two different Windows accounts, one will override the other.

Note that you can work around this by having both itch installs use the same
install location.
