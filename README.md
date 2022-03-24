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

This book is build using the opensource
[Gitbook](https://github.com/GitbookIO/gitbook-cli) tool. Sadly it's abandoned
so building this file currently involves a little patch. See
`release/ci-book.js`

If you about to change something about the build process, make a new tag and
push that first so we have a backup of the compiled output incase we need to
roll back quickly. Tagged releases are pushed to separate folder on the docs
bucket.

