# Installing itch on OSX

  * Download the latest version from [https://itch.io/app](https://itch.io/app)
  * Open `Install itch.app`

> If it doesn't launch the first time - try a second time. We're looking
> into that particular issue.

Note: before v25, itch used to install in `/Applications/itch.app`. It now installs
per-user, in `~/Applications/itch.app`. You might want to remove the former before
(or after) installing itch v25.

## Verifying the app

All our OSX binaries are signed by a Developer ID certificate to the name of [Amos Wenger](https://github.com/fasterthanlime), and you can verify them by running the following command in a terminal:

```bash
spctl -a -vvvv ~/Applications/itch.app
```

...where `~/Applications/itch.app` is the full path to the .app. If the app is correctly signed, you should see the following terminal output:

```
/Applications/itch.app: accepted
source=Developer ID
origin=Developer ID Application: Amos Wenger (B2N6FSRTPV)
```

## Updating

When a new version of the app becomes available, "A new version is available"
shows up in the top right corner.

Clicking it allows you to restart into the new version.

## Uninstalling

You can uninstall the app by dragging `itch.app` out of your `~/Applications` folder and into the Trash.

> This won't remove your library, which resides at `~/Library/Application Support/itch`,  
> along with any additional install locations you have added from the app.
>
> If you really want to uninstall everything, you'll need to delete that folder as well.



