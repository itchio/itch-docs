# Distributing Web games

Web games have several advantages:

* They're easily accessible from web browsers
* They're less of a security threat than native games
* They work on all three platforms out of the box

However, they also tend to perform more poorly, and to have worse platform integration.

The itch.io app supports installing and launching web games. They'll behave as if they were running in Google Chrome.

Like the website, it will look for an `index.html` file \(or a top-level `.html` file with another name\).

You can use `Shift+F12` to open the developer toosl, see [Troubleshooting](/integrating/troubleshooting-guide.md) for more details.

## Fullscreen support

HTML5 games launched with the app can be switched to fullscreen and their window can be resized, so make sure your CSS handles that properly.

## Java applets

Java applets are not supported by the itch.io app.

## Flash games

Flash games are not supported by the itch.io app.

## Legacy Unity plug-in games

Legacy Unity plug-in games are not supported by the itch.io app. Use the **WebGL export** option instead.
