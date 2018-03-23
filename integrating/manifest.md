# App manifests

There are several good reasons to include an app manifest with your game:

* You want to provide a choice between multiple launch targets
  * Examples: game, level editor, etc.
* Your app needs access to [the itch.io API](https://itch.io/docs/api/overview), for authentication or more

"It launches the wrong thing" is usually a bad reason to ship a manifest, see [Troubleshooting](/integrating/troubleshooting-guide.md).

> This documentation is more of a Guide than a Reference.
>
> If you just want the details, skip over to the [type definitions](http://docs.itch.ovh/buse/master/#/?id=manifest).

## Basics

A manifest is a file named `.itch.toml` placed at the top level of your game directory.

For example, the Windows build of a Unity game might be structured like this:

```
FooBar-windows/
  FooBar.exe
  FooBar_Data/
  .itch.toml
```

The same application for macOS could have this structure:

```
FooBar-macOS/
  FooBar.app/
  .itch.toml
```

The contents of the file must be valid [TOML markup](https://github.com/toml-lang/toml).

## Validating your manifest

Before you push a build with your manifest file, you can validate with the [butler](https://itch.io/docs/butler) `validate` command.

Read the [Validating your manifest](#validating-your-manifest) section for more information.

## Prerequisites

The itch.io app can ensure that certain libraries are installed before your app is launched.

These typically include Microsoft Visual C++ Redistributables, DirectX, XNA, etc.

This minimal manifest can be used for a 32-bit windows build that requires Visual C++ 2010:

```toml
[[prereqs]]
name = "vcredist-2010-x86"
```

Read the [prerequisites documentation](./prereqs/README.md) to learn more.

> If you're a command-line person, use the `butler test-prereqs` command to list known prerequisites.
>
> You'll need [butler](https://itch.io/docs/butler) for that. Obviously.

## Actions

Manifests can contain between zero and "a few" options[^1]

```toml
[[actions]]
name = "play"
path = "FooBar.exe"

[[actions]]
name = "editor"
path = "FooBar.exe"
args = ["--editor"]
```

Read the [manifest actions](/integrating/manifest-actions.md) page to learn more about what you can do with those.

### 

[^1]: Keep it simple, you don't want players to have to scroll all the way down to pick the right action.

