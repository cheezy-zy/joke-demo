# AGENTS.md

Project instructions for this repository.

## What this is

A single-file entry for the make.fun competition
`the-joke-about-the-demo-20261121-0551`. The deliverable is one line of text
about working beside AI coding agents.

## Rules for changes

- `main.py` stays standard library only, Python 3.13, no network access.
- The entry text is 1 to 280 Unicode code points, UTF-8, and must be
  byte-identical across runs; never introduce randomness, time, or locale
  dependent output.
- Write the output file with an explicit LF newline so Windows does not turn
  it into CRLF.
- The joke is written here, not fetched from anywhere.

## Verify before committing

```bash
python main.py
python -c "s=open('output/entry.txt',encoding='utf-8').read(); print(len(s)); print(repr(s))"
```
