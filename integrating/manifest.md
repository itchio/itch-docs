# App manifests

App manifests are optional `.itch.toml` files placed at the top level of a build.

Use an app manifest when you want more control over how the itch app launches and prepares your software.

A manifest can:

* Define one or more launch actions (play, editor, docs, links, platform-specific actions, arguments, sandbox opt-in)
* Request API scope so your app can receive a temporary itch.io API key
* Declare prerequisites the app should install before launch (VC++, .NET, XNA, DirectX, etc.)

"It launches the wrong thing" is usually a bad reason to ship a manifest. Read [Troubleshooting](/integrating/troubleshooting-guide.md) first.

## Learn more

* [Manifest actions](/integrating/manifest-actions.md)
* [Prerequisites](/integrating/prereqs/README.md)
* [Validating builds and manifests](/integrating/manifest/validating-your-manifest.md)

> This documentation is a guide, not a full schema reference.
>
> If you want raw field definitions, see [butlerd manifest type definitions](http://docs.itch.zone/butlerd/master/#/?id=manifest).

## Minimal example

This minimal manifest defines one action and one prerequisite:

```toml
[[actions]]
name = "play"
path = "FooBar.exe"

[[prereqs]]
name = "vcredist-2010-x86"
```
