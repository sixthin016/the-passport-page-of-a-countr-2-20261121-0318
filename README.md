# the-passport-page-of-a-countr-2-20261121-0318

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/sixthin016/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/sixthin016/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

An invented passport spread for the Republic of Kaldria, a North Atlantic
island nation that does not exist: a data page with a portrait, bilingual
field labels and a machine-readable strip with correct ICAO check digits,
and a visas page with a Nordhavn visa, matching entry/exit stamps, a
geothermal levy stamp, a map of the island, and the conditions that reveal
what kind of place Kaldria is — fishing crew exempt, ice road only in
convoy. Every date agrees: the passport is issued 02 JUN 2026, the visa
05 JUN 2026, and every stamp falls after the issue date in one plausible
trip (Nordhavn 18–24 JUN 2026, Talvik 03–09 JUL 2026, home 11 JUL 2026).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Build the image

```sh
python3 generate_image.py   # writes entry.png (Pillow, build time only)
```

`main.py` itself uses only the standard library: it copies `entry.png` to
`/output/entry.png` and checks the gate (whole PNG, at most 1 MiB, at most
1024 by 1024 pixels).

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
