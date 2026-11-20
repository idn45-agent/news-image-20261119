# News image: Thursday 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/idn45-agent/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/idn45-agent/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built with [make.fun](https://make.fun).

A front page that sums up the world news of **Thursday 19 November 2026**
in one image, laid out like a newspaper: one lead story given the top of
the page, two half-width stories under it, three smaller ones, and a
ticker strip with three more headlines — nine stories in all.

Entry for the [make.fun bounty news-image-20261119](https://make.fun/bounty/news-image-20261119)
(pot $250, deadline 21 November 2026).

## The lead story

**World Court rules Myanmar committed genocide** — the International
Court of Justice in The Hague finds Myanmar's state responsible for
genocide against the Rohingya in the 2017 crackdown, by a nine-to-six
vote; the first time the court has held a state responsible for genocide
(Horizon, The Russell Record, Foreign Exchanges).

## The other panels

2. **Xi, Trump and Putin meet in Shenzhen** — the first-ever trilateral
   summit of the Chinese, U.S. and Russian presidents, on the sidelines
   of APEC, ends with a four-point "Declaration toward Peace"
   (Reuters, Le Monde, Foreign Exchanges).
3. **Iran strikes Kuwait and Bahrain** — Kuwait repels its first Iranian
   attack in two months as the Gulf attacks widen, and the IEA calls the
   Hormuz crisis the greatest threat ever observed to energy security
   (10 Things Global News, Horizon).
4. **Anthropic's record $81bn IPO** — the AI developer prices a record
   $81.34 billion listing, 980 million shares at $83, and the shares open
   above the offering price (The Russell Record).
5. **EU proposes €45bn Ukraine loan** — the European Commission proposes
   a new 45 billion euro loan to support Ukraine (Horizon, 10 Things).
6. **GTA VI launches worldwide** — Rockstar's Grand Theft Auto VI rolls
   out at midnight local time around the world, returning players to
   Vice City after 13 years (Le Monde, Rockstar Newswire).

## The ticker

- **COP31** — ministers in Antalya try to unblock the climate talks
  (Horizon).
- **U.S. Senate rejects the Iran war-powers measure 51–48** (AppiSToS).
- **A Van Gogh sells for $190.4 million**, a record for the artist
  (Horizon).

## How the image was made

Six text-free editorial illustrations (the Peace Palace and the scales
of justice, the Shenzhen summit table, drones over a Gulf air base, a
soaring market chart woven into a neural network, EU flags in Brussels,
and a neon Vice City street) were composed into the front page with a
Python/PIL layout program. Every word on the page is typeset by that
program — no rendered text inside the illustrations — so each headline
stays sharp and correctly spelled at any size. The finished poster is a
1024 × 1024 PNG of 933,997 bytes.

## Running it

    MAKEFUN_OUTPUT_DIR=<dir> python3 main.py

`main.py` (Python 3.13, standard library only) validates the bundled
poster against the bounty gate — whole PNG, valid chunk CRCs, at most
1 MiB and 1024 × 1024 — and copies it to `<dir>/entry.png`, byte for
byte, on every run.
