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

To learn more about the workflows that the itch.io app plays well with, read the [Compatibility policy](/integrating/compatibility-policy.md) page.

## Tag your uploads

For each upload, tick the appropriate checkbox so the app knows what to install for which platform:

![](tags.png)

## Keep it simple, or ship a manifest

If you have a single top-level executable \(Windows\), or .app file \(macOS\), or binary or shell script \(Linux\), then things should **Just Work**.

If your game:

* Requires libraries like Visual C++ Redistributable, DirectX, XNA, etc.
* Has multiple launch targets \(Game, Editor, Manual, etc.\)
* Integrates with the [itch.io API](https://itch.io/docs/api/overview).

Then **you'll need an **[**app manifest**](/integrating/manifest.md).

> Don't be scared. There's examples and a validation tool. You'll see, it's nice.

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

