# Validating builds and manifests

The [butler](https://itch.io/docs/butler) command-line tool can be used to validate build directories and manifests.

It's a good way to make sure your software will be opened correctly by the itch.io app before you even push a build to itch.io.

> The validate command returns a non-zero exit code if it detects serious problems.  
> It's a good idea to integrate it into your Continuous Deployment pipeline \(Travis CI, Gitlab CI etc.\)!

## Validating build folders

You can pass a folder to the validate command \(the same you'd pass to `butler push`\) to make a full analysis:

```
$ butler validate .

∙ Validating build directory .
For runtime 64-bit Windows (use --platform and --arch to simulate others)

∙ Validating 477 B manifest at (.itch.toml)

√ Validating 3 actions...

  → Action 'Default' (Sample Evil App{{EXT}})
    Requests API scope (profile:me)
    | (Sample Evil App.exe) (native)
    |-- 43 MiB Sample Evil App.exe windows-386 win(gui)
    |-- ↗ Will be launched as a native application

  → Action 'Sandbox opt-in' (Sample Evil App{{EXT}})
    Requests API scope (profile:me)
    Sandbox opt-in
    | (Sample Evil App.exe) (native)
    |-- 43 MiB Sample Evil App.exe windows-386 win(gui)
    |-- ↗ Will be launched as a native application

  → Action 'Args' (Sample Evil App{{EXT}})
    Passes arguments: being ::: john ::: malkovich
    | (Sample Evil App.exe) (native)
    |-- 43 MiB Sample Evil App.exe windows-386 win(gui)
    |-- ↗ Will be launched as a native application

√ Validating 5 prereqs...

  → Microsoft Visual C++ 2010 Redistributable (x86) (vcredist-2010-x86)
    Available on Windows for architecture 386

  → Microsoft Visual C++ 2010 Redistributable (x64) (vcredist-2010-x64)
    Available on Windows for architecture amd64

  → Microsoft Visual C++ 2015 Redistributable Update 3 (x86) (vcredist-2015-x86)
    Available on Windows for architecture 386

  → Microsoft Visual C++ 2015 Redistributable Update 3 (x64) (vcredist-2015-x64)
    Available on Windows for architecture amd64

  → OpenAL (openal-1.1)
    Available on Windows for architecture 386
```

## Validating for different platforms

Use the `--platform` and `--arch` options to validate for a platform other than the one you're currently running butler on. Here's butler being run on Windows 64-bit, validating for Linux 32-bit:

```
$ butler validate --platform linux --arch 386 Crosswords\ Arena/

∙ Validating build directory Crosswords Arena/
For runtime 32-bit Linux (use --platform and --arch to simulate others)

No manifest found (expected it to be at Crosswords Arena\.itch.toml)

Heuristics will be used to launch your project.
√ Configured in 500.2µs

√ Heuristic results (best first):

  → Implicit launch target 1
    | (Crosswords Arena\index.html) (html)
    |-- 280 B index.html html-
    |-- ☁ Will be opened as HTML5 app
```

## Validating manifests only

If you want to validate just the manifest \(maybe before the build directory is generated\), you can do that too.

Here's [Sample Evil App](https://github.com/fasterthanlime/sample-evil-app)'s manifest being validated:

```
$ butler validate .itch.toml

∙ Validating manifest only
For runtime 64-bit Windows (use --platform and --arch to simulate others)


================== Warning ==================
In manifest-only validation mode. Pass a valid build directory to perform further checks.
=============================================

∙ Validating 477 B manifest at (.itch.toml)

√ Validating 3 actions...

  → Action 'Default' (Sample Evil App{{EXT}})
    Requests API scope (profile:me)

  → Action 'Sandbox opt-in' (Sample Evil App{{EXT}})
    Requests API scope (profile:me)
    Sandbox opt-in

  → Action 'Args' (Sample Evil App{{EXT}})
    Passes arguments: being ::: john ::: malkovich

√ Validating 5 prereqs...

  → Microsoft Visual C++ 2010 Redistributable (x86) (vcredist-2010-x86)
    Available on Windows for architecture 386

  → Microsoft Visual C++ 2010 Redistributable (x64) (vcredist-2010-x64)
    Available on Windows for architecture amd64

  → Microsoft Visual C++ 2015 Redistributable Update 3 (x86) (vcredist-2015-x86)
    Available on Windows for architecture 386

  → Microsoft Visual C++ 2015 Redistributable Update 3 (x64) (vcredist-2015-x64)
    Available on Windows for architecture amd64

  → OpenAL (openal-1.1)
    Available on Windows for architecture 386
```

Validate will warn you against unknown or misspelled configuration keys:

```
================== Warning ==================
1 error(s) decoding:

* 'Actions[0]' has invalid keys: cope
=============================================
```

And it will return a non-zero exit code if a serious error is found, like a missing prerequisite:

```
================== Error ==================
Unknown prerequisite listed: openal-1.1x
=============================================

Found 1 errors.
```

Or invalid configuration:

```
error: Decoding error:
*mapstructure.Error 1 error(s) decoding:

* 'Actions[1].Sandbox' expected type 'bool', got unconvertible type 'int64'
```



