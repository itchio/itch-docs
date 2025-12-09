# Distributing macOS builds

macOS might just be the ideal platform to distribute third-party, proprietary apps.

**Just push your .app bundle with **[**butler**](https://itch.io/docs/butler)**.**

That's it.

If you need an [app manifest](/integrating/manifest.md), put your .app and the manifest in a folder, and push _that one_ with butler.

> If you really _really_ want to do something else, read the [Compatibility policy](/integrating/compatibility-policy.md) page.

### ...but I don't have an app bundle

App bundles are directories with a standardized structure and some metadata in an `Info.plist` file.

A minimal app bundle structure looks like this:

```
MyGame.app/
├── Contents/
│   ├── Info.plist        # Required metadata (bundle ID, version, executable name)
│   ├── MacOS/
│   │   └── MyGame        # Your main executable
│   └── Resources/
│       └── MyGame.icns   # Your app icon (optional)
```

The `Info.plist` file is an XML file containing at minimum:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>MyGame</string>
    <key>CFBundleIdentifier</key>
    <string>com.yourcompany.mygame</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
</dict>
</plist>
```

Most game engines and frameworks will generate this structure for you automatically.

> Please don't push naked macOS binaries.
>
> Support for them is disappearing a little more every macOS release.

## Symbolic links and permissions

App bundles typically have symbolic links \(for frameworks\) and need some file permissions to be set properly.

We've taken several measures to ensure this works properly:

* At upload time
  * butler handles symlinks, and fixes file permissions if they're wrong
* At launch time
  * the itch.io app fixes permissions if they're wrong.

> If you don't use butler and upload an archive with wrong permissions, when players download and play your game without using the itch.io app, they'll encounter **Error -10810**. This error means macOS cannot find or execute the application's main binary, typically because the executable permission bit was lost during archiving. To fix this, ensure your build process preserves Unix permissions, or use butler which handles this automatically.

## Gatekeeper & other security measures

For players that are **not **using the itch.io app, you might get reports of your app being "Damaged and can't be opened" and that it should "be moved to the trash".

Player who do use the itch.io app do not encounter these issues, so you may want to encourage them to use it.

