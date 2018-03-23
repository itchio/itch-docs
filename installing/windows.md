# Installing itch on Windows

* Download the latest version from [https://itch.io/app](https://itch.io/app)
* Double-click the installer executable
  * You should see a splash screen for a few seconds
* The app starts up, desktop & start menu shortcuts are created

If you encounter any problems installing the app, get in touch with [itch.io support](https://itch.io/support).

### Verifying the installer

All our installers, along with the application itself, are digitally signed with a certificate to the name of **itch corp**.

![](/assets/itchsetup-certs.png)

_Open this dialog by right-clicking the installer, and choosing 'Properties'._

> It's a good habit to verify the signatures of executables you download — if you encounter an installer that pretends to be the itch app, but doesn't have our digital signature on it, you should not use it.
>
> \(Even the [canary version](./canary.md) is digitally signed with the same certificate.\)

### Antivirus software

We often release new version of the itch.io app or the components it depends on.

You might encounter screens like these if you have a third-party antivirus installed:

![](/assets/avast.png)

We're working with Antivirus vendors to suppress these, but in the meantime, if you trust us, you can add the following locations to your whitelist:

* `%LOCALAPPDATA%\itch`
* `%APPDATA%\itch\broth`
* `%APPDATA%\itch\prereqs`

> "broth" contains components required for the itch app to run properly.
>
> Don't add the entire `%APPDATA%\itch` folder as it would prevent your Antivirus from scanning the games you're install.

## Updating

The app's behavior when it comes to updating \(itself\) is:

* Checking for updates every 6 hours
  * Or when manually asked to via the `Help -> Check for Updates` menu
* When it finds an update, will download and apply it
* At which point it'll prompt you to either:
  * Restart the app to take advantage of the new version right now, or
  * Snooze the update, and wait for the next time you restart the app yourself

![](update-dialog.png)

## Uninstalling

itch can be uninstalled from the **Apps & Features** section of the Windows 10 settings:

![](/assets/win10-uninstall.png)

For older Windows versions, use the Control Panel as usual.

> Note: uninstalling the itch.io app does not wipe the `%APPDATA%\itch` folder, which contains all your installed games, local database, web session data and cache, and so on.
>
> If you really want to delete it all, you'll need to take care of that folder too.



