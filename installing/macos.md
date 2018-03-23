# Installing itch on OSX

* Download the latest version from [https://itch.io/app](https://itch.io/app)
* Open the DMG image, a window pops up:

![](/assets/itch-dmg.png)

* Drag the app to the `Applications` folder
* Close & eject the DMG image
* Launch the app by searching for **itch** in Spotlight

### Verifying the app

All our OSX binaries are signed by a Developer ID certificate to the name of [Amos Wenger](https://github.com/fasterthanlime), and you can verify them by running the following command in a terminal:

```bash
spctl -a -vvvv /Applications/itch.app
```

...where `/Applications/itch.app` is the full path to the .app. If the app is correctly signed, you should see the following terminal output:

```
/Applications/itch.app: accepted
source=Developer ID
origin=Developer ID Application: Amos Wenger (B2N6FSRTPV)
```

## Updating

The app is self-updating on OSX, just like on Windows. Refer to the [Windows](./windows.md#updating) page for details.

## Uninstalling

You can uninstall the app by dragging `itch.app` out of your `/Applications`folder and into the Trash.

> This won't remove your library, which resides at `~/Library/Application Support/itch`,  
> along with any additional install locations you have added from the app.
>
> If you really want to uninstall everything, you'll need to delete that folder as well.



