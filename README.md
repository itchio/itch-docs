# The itch book

This book is a living documentation for [the itch.io app](https://itch.io/app).

Its intended audience includes:

* People using the app to install, manage and launch games and applications
* Game and application developers publishing to itch.io
* Contributors to the app \([it's open-source!](https://github.com/itchio/itch)\)

## Contributing to this book

If you find a typo, a factual inaccuracy, or an important caveat not covered in
this book, feel free to submit a pull request to the [GitHub
repository](https://github.com/itchio/itch-docs).


## Note to developers

This book is built using [Honkit](https://github.com/honkit/honkit).

Deployment happens automatically via GitHub Actions (`.github/workflows/docs.yml`) when pushed to the `master` branch. The docs are deployed to GitHub Pages.

The primary docs displayed at `https://itch.io/docs/itch/` are proxied from
the GitHub Pages deployment. To update, push to the `master` branch.

Create tags for substantial versions of the app and book to preserve older
versions for reference.

