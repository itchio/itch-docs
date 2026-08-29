# Linking an existing folder

Some downloads are hosted outside itch.io (on Google Drive, Mega, and so
on), so the app can't install them for you. If you downloaded and extracted
such a game yourself, you can link its folder to your library entry: the
game then shows up as installed and launches through the app like any
other.

This is a power-user feature. The app takes your word that the folder
contains the right files, and once linked, it manages the folder as its
own.

## Linking a folder

1. Move the game's folder inside your [install
   location](install-locations.md). The app only manages folders that live
   there.
2. Open the game's install dialog, then the menu in the top right of the
   cover image, and choose **Link existing folder...**. The install dialog
   also points you there when a download can't be installed automatically.
3. Drop the folder on the dialog or pick it with **Choose folder...**.
4. Pick which of the game's downloads the folder contains, then press
   **Link folder**.

No files are copied or moved. The app records the folder as an install of
the selected download, detects its executables, and writes an install
receipt inside it.

## Caveats

* **Uninstalling deletes the folder.** From the moment it's linked, the
  folder belongs to the app: uninstalling the game later removes the
  folder and everything in it.
* **The contents aren't verified.** The app can't check that the folder
  actually matches the download you picked. If it doesn't, launching may
  not work, and anything that relies on the download's metadata will be
  wrong.
* **Externally hosted downloads still can't update automatically.** To
  move to a new version, download and extract it yourself, uninstall the
  linked install (this deletes the old folder), and link the new folder.
* A download that is already installed, or currently downloading, can't be
  linked again.
* A folder that already contains an install receipt was installed by the
  app; use [Scanning for games](scan-install-locations.md) to import it
  instead of linking it.
