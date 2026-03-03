# Scanning for games

The itch app can scan your install locations to find games that are installed on disk but not currently showing up in your library. This is useful if the app's database was reset, you restored game files from a backup, or you're sharing an install folder between machines.

## How it works

The scan looks through every folder in your registered [install locations](install-locations.md) for game folders that contain an `.itch` metadata folder. This metadata is created by the app when it installs a game, and contains information about which game and upload the folder belongs to. When the scan finds a game folder with valid metadata that isn't already in your library, it offers to re-import it.

## When it runs

- **On startup** - the app automatically scans in the background each time it launches. Any games it finds are imported silently.
- **When you add a new install location** - the app scans the new location automatically.
- **Manually** - you can trigger a scan from the install locations preferences. This opens a window that shows you which games were found and asks you to confirm the import.

## What it can't do

The scan can only find games that were **previously installed by the itch app**. It cannot detect games that were downloaded through the itch.io website and placed into an install location manually, because those downloads don't have the `.itch` metadata folder that the app creates during installation.

If you want a game in your app library, you'll need to install it through the app directly.
