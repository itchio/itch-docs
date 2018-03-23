# Manifest actions

Actions are options players can pick from when launching your game / opening your application.

Valid actions contain at least:

* A name: this will affect the label shown to users
* A path: this specifies what to run when the action is picked

For executables, give the path of the `.exe` on Windows, of the binary or launcher script on Linux, and of the `FooBar.app` app bundle on macOS.

Here's a minimal manifest with a single action:

```toml
[[actions]]
name = "play"
path = "Overland.exe"
```

### 

### Names

A few well-known names are supported:

* `play`: shows up as `Play Now` in english, is highlighted
* `editor`: shows up as `Editor` in english
* `manual`: shows up as `User Manual` in english
* `forums`: shows up as `Forums` in english

Well-known names are localized as well as the rest of the itch app via our translation platform, and have a corresponding icon.

Custom names are supported too, but you'll need to provide your own localizations.

For example:

```toml
[[actions]]
name = "Let's go already!"
path = "FooBar.exe"

[[actions.locales.fr]]
name = "Allons-y!"

[[actions.locales.de]]
name = "Gehen wir bereits!"
```

_Note: the example manifest above describes just a single action, in three languages._

### Paths

Paths can either be:

* A file path, relative to the manifest's location \(ie. the game folder\)
* An URL

If you're unsure how an action will be opened by the itch app, use [butler](https://itch.io/docs/butler)'s `validate` command on your build folder to run a simulation. See [Validating builds and manifests](/integrating/manifest/validating-your-manifest.md) for more info.

Sample manifest:

```toml
[[actions]]
name = "play"
path = "game.exe"

[[actions]]
name = "editor"
path = "tools/editor.exe"

[[actions]]
name = "Open mods folder"
path = "mods/"

[[actions]]
name = "Discussion forum"
path = "https://foo.itch.io/bar/community"
```

### Arguments

The `args` field can be used to specify an array of arguments to pass to native executables.

Sample manifest:

```toml
[[actions]]
name = "A lot of arguments"
path = "sample.exe"
args = ["--that", "--is", "--a", "lot=of-arguments"]
```

For HTML5 games, arguments are available as `Itch.args` \(`Itch` being added to the global scope, usually `window` \).

### API key & scoping

Games can ask for an itch.io API key by setting the `scope` parameter.

Sample manifest:

```toml
[[actions]]
name = "play"
path = "DokiDokiOnline.exe"
scope = "profile:me"
```

Valid values for `scope`:

* `profile:me`: grants access to `https://itch.io/api/1/jwt/me`
* \(This is the only valid scope for now\)

When the `scope` parameter is set, the itch.io app sets the following **environment variables**:

* `ITCHIO_API_KEY :`a game-specific, session-specific API key
* `ITCHIO_API_KEY_EXPIRES_AT` the expiration date of the key, in iso-8601 format.

#### Making requests with the API key

The itch.io API key provided to the game should be the value of an HTTP  
header named `Authorization`.

For example, using the JavaScript library `needle`, one would do:

```javascript
const apiKey = process.env.ITCHIO_API_KEY

const opts = {
  headers: { 'Authorization': apiKey }
}
needle.get('https://itch.io/api/1/jwt/me', opts, function (error, response) {
  // deal with error, if any & process response
})
```

#### Accessing the API key in HTML5 games

The HTML5 environment doesn't grant access to environment variables by design,  
so the itch app injects a global object named `Itch` into the JavaScript runtime.

Here's the proper way to check that it's there:

```javascript
if (typeof Itch === 'undefined') {
  // not launched by itch app (regular web browser, missing manifest, etc.)
} else {
  // launched by itch app
  makeRequestWithKey(Itch.env.ITCHIO_API_KEY)
}
```

XHR requests are normally limited to the host that served the javascript: in the case of the itch.io app, HTML5 games are served from a custom protocol, and _the same-origin policy is disabled_ so that your HTML5 game can make requests to the itch.io server or to your own server somewhere else.

### Sandbox opt-in

Adding `sandbox = true` to an action opts into [the itch.io sandbox](../using/sandbox.md).

This means that, no matter what the user's settings are, the game will always be launched within the sandbox.

Game developers are encouraged to opt into the sandbox as early as they can afford to, to have plenty of time to adapt to it. In the future, the sandbox might become mandatory \(for app users\).

Sample manifest:

```toml
[[actions]]
name = "play"
path = "ProceduralChaos.exe"
sandbox = true
```

### Console / text-mode applications

By default, the itch app redirects the standard output and standard error to  
a log file on disk, which helps debugging when reports are sent.

For console applications, this might not be desirable. You can opt out from  
redirection by setting the `console` attribute of the relevant action to `true`:

```
[[actions]]
name = "play"
path = "TheWillowEffect.exe"
console = true
```

On Windows, it'll also open a new command line window to display the game into.

> `console` is not yet supported on Linux and macOS





