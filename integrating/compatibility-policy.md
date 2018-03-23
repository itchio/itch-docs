# Compatibility policy

This guide describes the _ideal way_ to publish software on itch.io, ie. **Platinum tier** level of support.

But it's cold out there in the real world, and on an open platform, life happens, and they stray from The Good Workflow. Nevertheless, the app tries its best to _get anything it can to run_, within certain rules.

## Platinum tier

Builds pushed with [butler](https://itch.io/docs/butler) are **Platinum tier**, which enables the following features:

* Installing or uninstalling games **does not require administrator privileges**.
* Installing games **does not require temporary disk space** \(the downloads folder is almost empty\)
* Installing games **can be paused and resumed** \(again, without using extra disk space\).
* An **integrity check** can be performed on installed games with minimal network usage.
* **Corrupted files can be healed** with minimal network usage.
* Upgrading an installation uses **binary patch files** which are small, beautiful, and efficient.[^3]
* Uninstalls are near-instantaneous.

Platinum tier is the, uh, gold standard we strive for, and all you have to do for it to work is simply to **use **[**butler**](https://itch.io/docs/butler)** to push your builds**.

## Gold tier

All tiers below platinum have the following inconvenients:

* **No automatic upgrades**. With different uploads, there's no way for the itch app to tell _for sure_ what needs to be upgraded to what, so it just doesn't update at all.[^4]
* **No integrity check** - it's reinstall or nothing.

However, installs still don't require additional disk space, or administrator privileges, and uninstalls are instant.

The itch.io app achieves this level of support by:

* Using either custom decompression engines or 7-zip under the hood
* Having those engines operate on "remote files" by
  * transparently making HTTP range requests
  * with opportunistic caching \(in memory\)

Install pause/resume support is poorer for some of these: resuming might restart from the beginning of an entry rather than where it left off.

### .zip archives \(Gold tier\)

Everyone loves to hate the .zip file format, sometimes with reason. Folks prefer .rar, or .7z, or maybe .xz because they compress smaller. They prefer custom formats, because .zip files have been around for a _long_ time and there's a lot of cruft in the [spec](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT).

We however, like[^5] the .zip file format because it:

* Can be decompressed out-of-the-box on Windows, macOS and reasonable Linux distributions[^1]
* Allows extracting individual items without reading the whole file[^2]
* Includes checksums \(CRC32\) mandated by the spec
* Has a smaller, beautiful version [standardized by ISO](https://www.iso.org/standard/60101.html)

In fact, we like it so much it's the de-facto storage format for builds pushed with butler.

We support everything in ISO/IEC 21320-1:2015, along with some extensions:

* LZMA-compressed entries[^7]
* Shift-JIS filenames \(typically Japanese games\)

### .rar archives \(Gold tier\)

There's a lot to dislike about the RAR file format - the licensing terms, the file structure, etc.[^6]

However, as of version 25.x of the application, they're gold tier, because 7-zip has great support for them.

> Note: Installs from .rar files have a significant warm-up time before progress is visible, because the entries are organized differently from .zip files.

### .tar, .tar.gz, .tar.bz2 archives \(Gold tier\)

TAR is a funny beast[^9]. It was designed for backing data on tapes, so it's a linear format. It doesn't specify compression, so the entire stream is compressed with something else.

For .tar \(uncompressed\), .tar.gz \(gzip, a variant of DEFLATE\), and .tar.bz2 \(bzip2, an odd format in itself[^8]\), the installation can be paused anywhere.

### tar.xz archives \(Silver tier\)

[^1]: Extractors on Linux & macOS tend to forget about file permissions \(notably, the executable bit\), but that's 100% on them.

[^2]: It's not trivial - you have to read the end of the file first. But that's what HTTP range requests are for.

[^3]: There's a whole book to be written about our patching system - and it would be a good book, too! For now, let's stay humble and just mention that it routinely outperforms commercial patching solutions.

[^4]: Versions of the itch.io app up to 23.x used to take guesses as to non-butler-uploads updates. It caused more problems than it solved, so that's no longer the case.

[^5]: The actual sentiment is more along the lines of "everything else has significant drawbacks and no amount of GitHub comments would convince us otherwise at this point in time", but that doesn't roll off the tongue quite as easily.

[^6]: The fact that malware authors love it, the amount of password-protected archives out there, the fact that at least 3 major versions are in use in the wild \(Rar2, Rar3, Rar5\), and that it reminds one about the golden age of Rare, the one from Twycross Leicestershire.

[^7]: LZMA entries are indeed smaller, but if installation is paused in the middle of one of those, it'll have to start over at the beginning of the entry. As opposed to DEFLATE, which we support mid-entry checkpoints for.

[^8]: Only mainstream format to use [Burrows-Wheeler](https://en.wikipedia.org/wiki/Burrows–Wheeler_transform), typically has low compression \_and \_decompression speeds? The world was weird before LZMA.

[^9]: A quick note to .zip haters: TAR has also had [an eventful childhood](https://en.wikipedia.org/wiki/Tar_(computing)), and as a result, is just as messy. This is just another of those "ignorance is bliss" subjects, so maybe don't follow that link.
