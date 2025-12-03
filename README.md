# The itch book

This book is a living documentation for [the itch.io app](https://itch.io/app).

Its intended audience includes:

* People using the app to install, manage and launch games and applications
* Game and application developers publishing to itch.io
* Contributors to the app \([it's open-source!](https://github.com/itchio/itch)\)

## Contributing to this book

If you find a typo, a factual inaccuracy, or an important caveat not covered in  
this book, feel free to submit a pull request to the [GitHub repository](https://github.com/itchio/itch-docs).


## Note to developer

This book is built using [Honkit](https://github.com/honkit/honkit).

Deployment happens automatically via GitLab CI when pushed to the GitLab
mirror. Each ref (branch or tag) is deployed to Google Cloud Storage under
`https://docs.itch.zone/itch/REF`, e.g. `master` or `v0.14.0`. It's recommended
to push tags when there are significant changes to the book so that older
versions may be referenced.

The primary docs displayed at [`https://itch.io/docs/itch/` are proxied from
the `master` deployment on Google Cloud Storage. To update the these docs push
to GitLab's master branch.

The `master` branch is also deployed to GitHub Pages for preview. Create tags
for substantial versions of the app and book to preserve older versions for
reference.

