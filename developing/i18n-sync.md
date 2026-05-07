# Syncing Translations (i18n)

Translations for the itch app are managed in a separate repository and contributed via Weblate. Syncing is bidirectional: the itch repo pushes new English keys out, and pulls every locale back in.

## How It Works

* **English** \(`src/static/locales/en.json`\) is the source of truth and lives in the itch repo. Add new strings here.
* **All other locales** are translator output, edited via [Weblate](https://weblate.itch.zone/projects/itchio/), which commits to the [itch-i18n](https://github.com/itchio/itch-i18n) repo.
* The sync script copies `en.json` into itch-i18n \(so Weblate picks up the new keys\), then wipes `src/static/locales/` and copies every locale back wholesale.

> **Don't edit `af.json`, `ar.json`, etc. in either repo.** They're Weblate output and will be overwritten on the next sync.

## Syncing

Check out itch-i18n alongside itch:

```
parent/
├── itch/
└── itch-i18n/
```

Then run:

```bash
node release/sync-i18n-strings.js
```

This is **destructive**: it deletes `src/static/locales/` and writes to `../itch-i18n`. Don't run it casually. The conventional commit message after a sync is `sync translations`.

## When to Sync

Run a sync when:

* You've added new English keys to `en.json` and want translators to see them
* You're preparing a release and want to pull in the latest translator work

Adding a new English string to `en.json` doesn't require an immediate sync. It'll be pushed out the next time someone runs the script, typically alongside a release.
