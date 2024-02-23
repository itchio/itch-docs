# Troubleshooting

Here's a list of common situations and how to solve them.

### "Game is not available on this platform"

If you're seeing this, your uploads are not tagged properly.

For each upload, tick the appropriate checkbox so the app knows what to install for which platform:

![](tags.png)

If you [push your builds using butler](https://itch.io/docs/butler), then just choosing a good channel name like `windows` or `linux-64` will tick the right box for you on first push.

> Using [butler](https://itchio/docs/butler) to push your builds is **strongly recommended**. Learn more about the benefits by reading the [Compatibility policy](/integrating/compatibility-policy.md) page.

### The wrong thing is launched

There's two ways to fix this.

The first is to **simplify your directory structure**. Your app might need other .exe files to be present when it works - but they don't all need to be in the top level directory. This is a good fix because it makes the install folder _more obvious to humans as well_.

The second is to [**ship an app manifest**](/integrating/manifest.md) that explicitly lists what needs to be launched. A manifest also lets you specify **prerequisites** \(VC++, DirectX, XNA, OpenAL etc.\) that your game needs, so even if you have a single launch target, read the docs anyway.[^1]

### The game / application crashes

As of itch 25.x, any crash will show you a modal with very useful info.

![](/assets/universal-navigation.gif)

This should let you evaluate whether it's more likely that:

* The computer / OS is at fault
  * In which case, fix it!
* The game / application is at fault
  * In which case you should contact them using the game page's comments section[^2]
* The itch.io app is at fault
  * In which case don't untick the checkbox, we'll take a look at your report!

### Something's wrong with my HTML5 game

Press `Shift+F12` to open up the Chrome Developer Tools, and see what went wrong.

Enter `navigator.appVersion` then press Enter in the Console to check what version of Chrome your itch.io app is shipping with.

![](/assets/html5-devtools.png)

### It says it's still running, but I closed the game / application!

On Windows 8 and up, the itch app will wait for the entire process tree to quit. If it says it's still running, _something_ hasn't exited yet. You can use force close to kill it, but with great power comes great responsibility.

[^1]: Speaking of, you're reading docs right now. Big up to you! We appreciate it a lot.

[^2]: If you happen to be developing the game/application in question, save valuable time by skipping the "contacting yourself" phase, going straight to "fixing the bug".

