# BornHack 2023 Badge Fediverse Association Interrogator

**Work-in-progress** Python3 program which will search a Mastodon instance of
the fediverse for accounts which mention the NFC tag ID read from a [BornHack
2023 NFC badge][badge].

[badge]: https://github.com/bornhack/badge2023

This requires the badge's initial program for dumping the ID on the serial port
(available from the [`cp-init` branch][cpinit] and this program running on the
computer to which the badge is attached.

[cpinit]: https://github.com/bornhack/badge2023/tree/cp-init

# Concept

The idea is to associate a badge with a fediverse account by mentioning the ID
of the badge in the bio of the account. This will enable anyone who meets up
with the owner carrying the badge to pair this physical person/badge with a
fediverse presence by scanning the badge and let this program search for the
account associated with the ID.

# Status

* Anonymous search seems to not return account bio results: even though my
[fediverse account @mikini@fosstodon.org][mikini-foss] has the ID in both
the bio and [a post][foss-post] no results are returned, my hunch is that
authentication is needed to do a proper match.

[foss-bio]: https://fosstodon.org/@mikini
[foss-post]: https://fosstodon.org/@mikini/110839840685439057

* The ID needs to be without semicolon: if formatted with a semicolon between
each bytes hexadecimal numbers the Mastodon API returns unrelated accounts,
probably because each byte is searched as a separate entity.

* Attached computer needed: at the moment the badge needs to be connected to a
computer with internet connected to do the search immediately at badge scan.
But this can potentially be improved so that the badge will store a list of IDs
it has met while being offline in its 16 MiB W25Q128JV flash and then later
perform the fediverse association asynchronously.

# Dependencies

Install Python's `serial` and `requests` module by fx. doing this on a Debian
derived distribuion.

```
$ sudo apt install python3-serial python3-requests
```

# License: GPL-3.0-or-later

Copyright (C) 2023 Mikkel Kirkgaard Nielsen

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

See LICENSE file included in this repository for a copy of the full license, or
alternatively visit https://www.gnu.org/licenses/.
