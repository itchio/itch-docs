# Compatibility policy

This guide describes the _ideal way_ to publish software on itch.io, ie. **Platinum tier** level of support.

But it's cold out there in the real world, and on an open platform, life happens, and they stray from The Good Workflow. Nevertheless, the app tries its best to _get anything it can to run_, within certain rules.

**TL;DR: if you **_**cannot**_** use butler, **_**just upload a .zip**_**.**

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

### .zip archives \([Gold tier](#gold-tier)\)

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

### .rar archives \([Gold tier](#gold-tier)\)

There's a lot to dislike about the RAR file format - the licensing terms, the file structure, etc.[^6]

However, as of version 25.x of the application, they're gold tier, because 7-zip has great support for them.

> Note: Installs from .rar files have a significant warm-up time before progress is visible, because the entries are organized differently from .zip files.

### .tar, .tar.gz, .tar.bz2 archives \([Gold tier](#gold-tier)\)

TAR is a funny beast[^9]. It was designed for backing data on tapes, so it's a linear format. It doesn't specify compression, so the entire stream is compressed with something else.

For .tar \(uncompressed\), .tar.gz \(gzip, a variant of DEFLATE\), and .tar.bz2 \(bzip2, an odd format in itself[^8]\), the installation can be paused anywhere, because we have custom decompression engines for gzip and bzip2.

### .dmg \([Gold tier](#gold-tier)\)

Okay, all formats have some flavor of strange somewhere. But DMG files somehow take the cake, as they're:

* HFS+ \(or APFS\) partitions
* Stored in a file
  * without a stable magic number
  * usually compressed \(sometimes with bzip2, but not always\)
  * that typically contain multiple volumes, listed in an embedded XML file

And yet, 7-zip lets us extract any item we want easily, so they're gold tier.

> Note: if your DMG file contains a dialog with a EULA in it, it's not going to be shown during installation

### MojoSetup \([Gold tier](#gold-tier)\)

[MojoSetup](https://www.icculus.org/mojosetup/) installers are basically a Linux binary concatenated with a .zip archive.

Except when they're not, and they contain a .tar.xz data payload. We handle both cases \(uncompressed data, and .tar.xz data\).

However, **we do not support**:

* Specifying a removable installation medium \(DVD, etc.\) or a network installation source \(FTP, HTTP etc.\)
* Many other custom Mojosetup features.

### Self-extracting InstallShield archives \([Gold tier](#gold-tier)\)

Looks like an .exe, is actually a .cab. We identify those and extract them without storing them on disk first. We've only seen one in the wild so far, but hey, better safe than sorry.

Still, please use .zip instead of doing that.

## Silver tier

This tier is very similar to [gold tier](#gold-tier), but they have a separate **download** and **install** phase, and use temporary storage during installation.

> This sounds innocuous, but if you ship a 10GB game as a 4GB setup file, and the user only has 12GB disk space, they won't be able to install it.

### .7z archives \([Silver tier](#silver-tier)\)

The 7z format has wonderful properties, but no entry directory. It handles entries "as a whole" rather than invidiually \(what .zip does\) to achieve better compression, and as a result, it's not feasible to pause/resume compression without having to redownload and re-decompress large portions of the source file.

As a result, we force downloading .7z files to disk before extracting them, and it's silver tier. Sorry Igor[^10]

### tar.xz archives \([Silver tier](#silver-tier)\)

XZ is also a container format \(like .zip\), but in .tar.xz's case it's just used as an excuse to use LZMA2. We don't have a custom LZMA2 engine \(we use 7-zip for that\), so we download them to disk first.

## Bronze tier

This is a tier that really tests our commitment to supporting older builds of games and/or bad habits. On top of having a separate download and install phase and not allowing upgrades, those sometimes **require administrator access** to install.

They might install files outside the install folder, they might just plain old don't work, they make users wait because of their typically long install times, etc.

### .msi packages \([Bronze tier](#bronze-tier)\)

Most MSI files can be installed fine, as long as you don't do anything funky in the install scripts. So don't!

**Please **don't use those - bronze tier is not a good tier.

### InnoSetup installers \([Bronze tier](#bronze-tier)\)

Installation is performed silently and to the correct install folder. Uninstallation is handled properly as well.

Still, **please **don't use those - bronze tier is not a good tier.

### Nullsoft / NSIS installers \([Bronze tier](#bronze-tier)\)

Installation is performed silently and to the correct install folder. Uninstallation is handled properly as well.

Again, **please** don't use those - bronze tier is not a good tier.

## Oh no tier

These are outright rejected by the app. Don't upload those.

We don't plan to support these because of one or more of the following reasons:

* The format cannot be installed silently
* The format cannot be installed to a single folder in a portable manner
* The format is a sin

### .deb and .rpm packages \([Oh no tier](#oh-no-tier)\)

These are ignored when looking for uploads - it'll appear as if your app wasn't available on Linux at all.

**Do not use these.**

### .pkg packages \([Oh no tier](#oh-no-tier)\)

These are dialog-based, can have scripts, can ask for your password, don't let you specify install folders.

**Do not use these.**

### Literally any other installer type \([Oh no tier](#oh-no-tier)\)

Here's a non-exhaustive list of installer creators we don't support:

* IExpress \(Microsoft\)
* Install Creator \(Clickteam\)
* InstallShield \(Flexera\)
* Wise \(Wise Solutions, Inc.\)
* Makeself

**Do not use these**, and for the love of all that is holy, **do not make your own installer.**[^11]

[^1]: Extractors on Linux & macOS tend to forget about file permissions \(notably, the executable bit\), but that's 100% on them.

[^2]: It's not trivial - you have to read the end of the file first. But that's what HTTP range requests are for.

[^3]: There's a whole book to be written about our patching system - and it would be a good book, too! For now, let's stay humble and just mention that it routinely outperforms commercial patching solutions.

[^4]: Versions of the itch.io app up to 23.x used to take guesses as to non-butler-uploads updates. It caused more problems than it solved, so that's no longer the case.

[^5]: The actual sentiment is more along the lines of "everything else has significant drawbacks and no amount of GitHub comments would convince us otherwise at this point in time", but that doesn't roll off the tongue quite as easily.

[^6]: The fact that malware authors love it, the amount of password-protected archives out there, the fact that at least 3 major versions are in use in the wild \(Rar2, Rar3, Rar5\), and that it reminds one about the golden age of Rare, the one from Twycross Leicestershire.

[^7]: LZMA entries are indeed smaller, but if installation is paused in the middle of one of those, it'll have to start over at the beginning of the entry. As opposed to DEFLATE, which we support mid-entry checkpoints for.

[^8]: Only mainstream format to use [Burrows-Wheeler](https://en.wikipedia.org/wiki/Burrows–Wheeler_transform), typically has low compression \_and \_decompression speeds? The world was weird before LZMA.

[^9]: A quick note to .zip haters: TAR has also had [an eventful childhood](https://en.wikipedia.org/wiki/Tar_%28computing%29), and as a result, is just as messy. This is just another of those "ignorance is bliss" subjects, so maybe don't follow that link.

[^10]: Igor Pavlov is the driving force behind 7-zip. Reading the [release notes](https://www.7-zip.org/history.txt) is nothing short of awe-inspiring. I feel like we all have a collective debt towards Igor.

[^11]: This is not "don't become a standup comedian!" advice. This is "don't make it a career to repeatedly bang your head with multiple very large rocks over and over and over and over" advice. Still, this is just advice. Don't make your own desktop client for an open indie marketplace either but, hey, here we are.

