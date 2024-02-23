# Distributing macOS builds

macOS might just be the ideal platform to distribute third-party, proprietary apps.

**Just push your .app bundle with **[**butler**](https://itch.io/docs/butler)**.**

That's it.

If you need an [app manifest](/integrating/manifest.md), put your .app and the manifest in a folder, and push _that one_ with butler.

> If you really _really_ want to do something else, read the [Compatibility policy](/integrating/compatibility-policy.md) page.

## ...but I don't have an app bundle

App bundles are directories with a standardized structure and some metadata in an `Info.plist` file.

Here's a [good stackoverflow thread](http://stackoverflow.com/questions/1596945/building-osx-app-bundle) on how they're created. Good luck!

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

> If you don't use butler and upload an archive with wrong permissions, when players download and play your game without using the itch.io app, they'll encouter [Error -10810](http://www.thexlab.com/faqs/error-10810.html).

## Gatekeeper & other security measures

For players that are **not **using the itch.io app, you might get reports of your app being "Damaged and can't be opened" and that it should "be moved to the trash".

Player who do use the itch.io app do not encounter these issues, so you may want to encourage them to use it.
