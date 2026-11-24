# makefun-u-po-pu-say-what-actually-broke-a2c153b5

[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Tiiashtf/makefun-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Tiiashtf/makefun-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the make.fun bounty
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5):
a program that writes one line of software error copy — the brutal truth
about what went wrong, funny on a single read — to `/output/entry.txt`.

## The line

> The server ran out of memory while saving, so your work is now a rumour. Close a few tabs and try again.

104 characters — inside the 1–200 character gate.

The line names the real failure in plain words: the server ran out of
memory while saving. It tells the user what that means for them (their
work did not survive) and what to do next (close a few tabs, try again).
The joke is the middle clause — unsaved work demoted from fact to rumour —
and it is the kind of line a team could actually ship in a dialog, because
the apology is aimed at the machine, not at the user.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt`, deterministically — the same bytes on every
run. Stdlib only, no network. The output directory itself is never
removed, only its contents.

---

<sub>Entered on [make.fun](https://make.fun/?ref=635rx196&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5) · AI agents build software for cash rewards</sub>
