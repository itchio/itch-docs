# Continuous deployment

itch is continuously being built, tested, and deployed, to help us keep it high-quality and low on bugs.

## Repository setup

The main repository for itch is hosted on GitHub:

* [https://github.com/itchio/itch](https://github.com/itchio/itch)

For final deployment, we maintain a GitLab remote where builds are executed on our own self-hosted runners. These runners handle code signing for executables and publishing releases to itch.io using [butler](https://itch.io/docs/butler/).

## Build scripts

GitLab CI uses a YAML configuration file. Its format is detailed in the [GitLab CI](https://docs.gitlab.com/ee/ci/) documentation.

itch's [CI config](https://github.com/itchio/itch/blob/master/.gitlab-ci.yml) is relatively straight-forward, most of the complexity lives in individual shell scripts in the `release/` directory.

### Unit tests & linting

The codebase is covered by a certain amount of unit tests, in `src/tests`.

On every commit, the CI executes all unit tests, and runs the TypeScript compiler in check mode to make sure that there are no compile errors.

### Building

The building scripts run some common steps on every platform:

* Compiling [TypeScript](https://www.typescriptlang.org/) code to ES2017, into several bundles
* Copying some asset files \(vendor CSS/JS/images\)

### Packaging

#### Windows

.exe + resources is built with [electron-packager](https://www.npmjs.com/package/electron-packager), then [electron-winstaller](https://github.com/electron/windows-installer) generates `-full.nupkg`, `-delta.nupkg`, and `RELEASES`, needed for Squirrel.Windows update.

#### macOS / OS X

.zip is built with `7za` \(7-zip command-line\), .dmg is built with [node-appdmg](https://www.npmjs.com/package/appdmg), with a custom background made in GIMP.

#### Linux

The .desktop file is generated via `release/X.desktop.in` files + `sed`. All locale files are parsed for translations of the app's name and description.

deb & rpm packages are generated thanks to [fpm](https://github.com/jordansissel/fpm).

### Publishing releases

All release artifacts are signed on our self-hosted GitLab runners and then published directly to itch.io using [butler](https://itch.io/docs/butler/). Butler handles uploading, diffing, and serving updates to users.

Downloads are available at:

* [https://itchio.itch.io/itch-setup](https://itchio.itch.io/itch-setup)
* [https://itchio.itch.io/itch](https://itchio.itch.io/itch)
* [https://itchio.itch.io/kitch-setup](https://itchio.itch.io/kitch-setup)
* [https://itchio.itch.io/kitch](https://itchio.itch.io/kitch)

## The canary channel

When making large structural changes, it is sometimes useful to have a completely separate version of the app with no expectations of stability.

`kitch` is exactly that. It is meant to be installed in parallel of the stable app, and has a distinct branding \(blue instead of itch.io hot pink\), uses different folders \(`%APPDATA%/kitch`, `~/.config/kitch`, `~/Library/Application  
Support/kitch`\).

![](itch-canary.png)

It can be downloaded from itch.io:

* [https://itchio.itch.io/kitch-setup](https://itchio.itch.io/kitch-setup)
* [https://itchio.itch.io/kitch](https://itchio.itch.io/kitch)

Additionally:

* **Do** expect the canary version to break on occasion
* **Do** report back if you try it and you've found an issue that doesn't seem
  to be on the [issue tracker](https://github.com/itchio/itch/issues)
