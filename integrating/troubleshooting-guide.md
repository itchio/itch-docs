# Troubleshooting

Here's a list of common situations and how to solve them.

### "Game is not available on this platform"

If you're seeing this, your uploads are not tagged properly.

For each upload, tick the appropriate checkbox so the app knows what to install for which platform:

![](tags.png)If you [push your builds using butler](https://itch.io/docs/butler), then just choosing a good channel name like `windows` or `linux-64` will tick the right box for you on first push.

> Using [butler](https://itchio/docs/butler) to push your builds is **strongly recommended**. Learn more about the benefits by reading the [Compatibility policy](/integrating/compatibility-policy.md) page.

### The wrong thing is launched

There's two ways to fix this.

The first is to **simplify your directory structure**. Your app might need other .exe files to be present when it works - but they don't all need to be in the top level directory. This is a good fix because it makes the install folder _more obvious to humans as well_.

The second is to [**ship an app manifest**](/integrating/manifest.md) that explicitly lists what needs to be launched. A manifest also lets you specify **prerequisites** \(VC++, DirectX, XNA, OpenAL etc.\) that your game needs, so even if you have a single launch target, read the docs anyway.[^1]

### The game / application crashes

As of itch 25.x, any crash will show you a modal with very useful info. Collapsed, it looks like:

![](/assets/universal-navigation.gif)

Expanding **View details**

### It says it's still running, but I closed the game / application!

On Windows 8 and up, the itch app will wait for the entire process tree to quit. If it says it's still running, _something_ hasn't exited yet. You can use force close to kill it, but with great power comes great responsibility.

[^1]: Speaking of, you're reading docs right now. Big up to you! We appreciate it a lot.

