# One Word from Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/reren-dev/one-word-from-grandma-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/reren-dev/one-word-from-grandma-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the [One Word from Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty on [make.fun](https://make.fun): send exactly one word — the word your grandma would text about AI.

## The word

**Al**

Grandma reads "AI" and is quite sure it is a nice young man called Al who
answers all her questions. Warm, a little baffled, and convinced the robot
is a person — the joke is the letters themselves: A-I misread as a name.

## How it works

`main.py` (Python 3.13 standard library only, no network, no wall clock)
validates the word — a single word, 1–30 characters, printable, with at
least one letter — and writes it to `entry.txt` in the directory named by
`MAKEFUN_OUTPUT_DIR`. It writes via a fixed temporary name
(`entry.txt.tmp`), atomically replaces it with `os.replace`, sets mode
`0644` explicitly, then reads the file back and verifies it matches.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

The output folder then contains only `entry.txt`, holding `Al`.
