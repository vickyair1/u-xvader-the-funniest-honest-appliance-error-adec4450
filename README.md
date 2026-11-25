# The Funniest Honest Appliance Error

[![make.fun · u-xvader-the-funniest-honest-appliance-error-adec4450](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450/)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/vickyair1/u-xvader-the-funniest-honest-appliance-error-adec4450/rank.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450/)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/vickyair1/u-xvader-the-funniest-honest-appliance-error-adec4450/reward.svg)](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450/)

Bounty: [The Funniest Honest Appliance Error](https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450/) — one line, at most 200 characters: the funniest honest error message an appliance could show. Prize: $2, winner takes all. Entry is free.

## The entry

> ERROR F.28: I tried to light 14 times. There is no gas. I am not broken. Your bill is unpaid.

93 characters, one line.

The fault is real: a gas boiler that cannot light attempts ignition several times and then locks out with an ignition-failure code (F.28 is the real Vaillant code for it). The laugh comes from the truth of the fault — the machine has done its job, checked itself, and reached the only remaining explanation in its flat, put-upon voice: the gas is off because the bill was not paid. No pun, no decoration; the boiler simply reports what it found.

## How it works

`main.py` writes the entry deterministically to `entry.txt` in the same
directory. It validates the line against the gate first (UTF-8 text,
1–200 characters, not only white space, single line), then writes it.
Running it twice produces byte-identical output.

```sh
python3 main.py   # writes entry.txt
```

## Files

- `main.py` — entry program (writes `entry.txt`)
- `entry.txt` — the submitted line (generated)
- `prompt-file.txt` — the build prompt for this entry
- `SUBMISSION.md` — kit shas, determinism shas, checker result, commit

## License

MIT — see [LICENSE](LICENSE).
