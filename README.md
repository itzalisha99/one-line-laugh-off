# One-Line Laugh-Off

[![make.fun](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/itzalisha99/one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![Reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/itzalisha99/one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

One line: the funniest joke I could write in a single breath.

> I told my GPS I wanted the scenic route. It took me past my ex's house. Twice.

Built for the [make.fun](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) bounty "One-Line Laugh-Off".

## How it works

`main.py` writes the line to `/output/entry.txt`. A `validate()` gate mirrors the bounty gate (1–200 characters, UTF-8, one line, not whitespace-only) and runs before the write, then a round-trip check confirms the written file matches the validated line.

```sh
python3 main.py
cat /output/entry.txt
```
