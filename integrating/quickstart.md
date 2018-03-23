# Game developer quick start

Chances are, your software already works with [the itch.io app](https://itch.io/app).

But **keep reading!** This page also contains best practices.

## Push builds with butler

The single best way to upload your game to itch.io is [with our command-line tool butler](https://itch.io/docs/butler).

> No, really.

The butler tool:

* Lets you upload builds **up to 30GB** \(the web limit is 2GB\)
* **Uploads only changes** from the previous build which means
  * You upload faster
  * Users of [the itch.io app](https://itch.io/app) upgrade faster
* Uploads entire folders directly \(no need to create an archive first\)
* Lets all versions be associated to one upload per platform, giving you meaningful analytics
* Heals permissions for Linux & macOS executables, handles symbolic links properly
* Performs well even with poor network connectivity \(it will keep retrying for a long time\)
* Contains other useful commands for things like:
  * [Validating your builds and app manifests](/integrating/manifest/validating-your-manifest.md)
  * [Many other things](https://itch.io/docs/butler/utilities.html)

Save a cloud, use butler to push your builds. We spent way too much time making it lovable.

> If you're not using butler, your game will probably still work, but most importantly, **your users won't get upgrades**.
>
> To learn more about the workflows that the itch.io app plays well with, read the Compatibility policy page.

## Tag your uploads

For each upload, tick the appropriate checkbox so the app knows what to install for which platform:

![](tags.png)

## Keep it simple, or ship a manifest

The surest way to get your game working first try in the app is to  
ship an [app manifest](./manifest.md). It will tell the app how to launch  
your game, and will even let you specify secondary actions, and even integrate  
into the itch.io API.

**When no manifest is found**, the app tries to mimic a human when launching a game.  
The general rule is: the top-most executable wins. If you are also distributing  
a level editor, etc., you really should ship an [app manifest](./manifest.md)  
to let your players choose.

Additionally:

* The app can tell the difference between Linux, Mac OS, and Windows
  executables — which allows you to distribute all three in a single archive.
* The app will set the executable bit on every binary it can find before
  attempting to launch the game, salvaging badly-zipped archives.
* The app actively avoids files containing strings resembling `uninstall`
* The app will prefer shell scripts to binaries on Linux \(allowing you to
  set up the `LD_LIBRARY_PATH` correctly, for example\)

## Use simple archive formats

The ideal way is to let itch.io archive your game for you by directly  
uploading a folder using the [butler](https://itch.io/docs/butler) command-line upload tool.

As an added bonus, uploading with [butler](https://itch.io/docs/butler) lets  
your players update in a quick and easy way \(the app will download small patches  
instead of re-downloading the entire game\).

The app will also happily install archives uploaded directly from the itch.io  
web interface: .zip, .7z, .tar.gz, .tar.bz2, .dmg, even .rar.

Some installer formats are supported on Windows, but we [advise against using them](https://github.com/itchio/itch/issues/671),  
if you can help it. In time, [app manifests](./manifest.md) will let you do  
things like install prerequisites, which you would normally need an installer for.

**TL;DR: **[**butler**](https://itch.io/docs/butler)** &gt; archives &gt; installers &gt; nothing**  
\(where `>` means 'is better than'\)

## Test your games

The itch app will let you install all your own projects, whether they  
have a minimum price or not. If you need help testing your game, here are  
places you can look for testers:

* The [itch.io community forums](https://itch.io/community)
* The [itch.io chat](https://itch.io/chat)

## A note about page types

The [itch.io](https://itch.io) website lets you pick between several  
project types.

The app does platform filtering, configuration and launching  
for the types `game` and `tool`. All other types, including `assets`,  
`game_mod`, `physical_game`, `soundtrack`, `comic`, `book`, and `other`  
are just treated like a folder that it lets the user open.

If you're wondering why the app is giving you the choice to download  
something that isn't tagged for your platform, that's why.

