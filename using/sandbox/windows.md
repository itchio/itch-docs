# Windows sandboxing

## One-time setup

For sandboxing to work, the itch app creates a separate local account whose
name starts with `itch-player-`.

The account is assigned a randomly generated password and removed from the
`Users` group so that it does not appear on the login screen. The app asks for
Administrator approval when this one-time setup is required. Sandboxed games do
not run with Administrator privileges.

The sandbox account has its own folder under `C:\Users`, and that is where most
game saves and configuration files will go.

## Troubleshooting

If your game is broken by the itch.io sandbox on Windows, we recommend using
[Microsoft Process Monitor](https://learn.microsoft.com/sysinternals/downloads/procmon)
to see what the game is trying to access that it does not have permission to.

You may need to filter by executable name for the logs to be readable.

You can disable the sandbox for a specific game from **Manage →
[Launch settings](../launch-settings.md)**. If you run into an issue that you need help resolving, feel free to
open an issue on our [Issue Tracker](https://github.com/itchio/itch/issues).

## Frequently Asked Questions

### I have a new folder in C:\\Users\\, what gives?

This is necessary for the sandbox to function properly, since it runs games as
another user. It allows itch to protect personal files that the sandbox account
does not have permission to access.

### I lost my saves when enabling the sandbox

They are still present, but the game is looking in the sandbox account's profile
instead of your regular profile. For example:

   * Original location: `C:\Users\leaf\AppData\Roaming\com.unity.game`
   * Sandboxed location: `C:\Users\itch-player-…\AppData\Roaming\com.unity.game`

You can switch the sandbox off for that game to use the original save location,
or copy the save files between the two profiles. Windows may ask for
Administrator permission when you open the sandbox account's profile.
