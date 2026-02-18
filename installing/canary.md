
# The canary version

If you're interested in helping us kill bugs before they even reach the stable
version, you can check out [the canary
channel](../developing/continuous-deployment.md#the-canary-channel).

It's a bleeding-edge, often-updated version of the app with *no guarantee of
stability* that you can install in parallel with the stable app.

## What's different

The canary version (`kitch`) runs as a fully separate application from the stable `itch` app:

* **Branding** -- blue instead of itch.io hot pink
* **Binary name** -- `kitch` instead of `itch`
* **URL protocols** -- `kitch://` and `kitchio://` instead of `itch://` and `itchio://`
* **Data folders** -- `%APPDATA%/kitch`, `~/.config/kitch`, `~/Library/Application Support/kitch`
* **No version pinning** -- canary always fetches the latest versions of components like butler and itch-setup, rather than pinning to specific versions

For a full technical breakdown, see the [canary channel](../developing/continuous-deployment.md#the-canary-channel) section in the developer docs.
