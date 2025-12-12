# Syncing Translations (i18n)

Translations for the itch app are managed in a separate repository and contributed via Weblate. To update the app with the latest translations, you need to sync from the external repo.

## How It Works

Translations are stored in the [itch-i18n](https://github.com/itchio/itch-i18n) repository. Community members contribute translations through [Weblate](https://weblate.itch.zone), which commits changes to that repo.

The locale files (JSON) are copied into the itch app at `src/static/locales/`.

## Syncing Translations

Ensure you have the itch-i18n repository checked out alongside itch:

```
parent/
├── itch/
└── itch-i18n/
```

Then run the import script:

```bash
node release/import-i18n-strings.js
```

This deletes the existing `src/static/locales/` directory and copies the latest translations from `../itch-i18n/locales/`.

## When to Sync

You should sync translations when:

- Preparing a new release
- New translations have been added via Weblate
- You want to test recent translation updates locally
