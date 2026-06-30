# memory/ — lessons learned & discoveries (the skill's growing knowledge base)

This is the skill's **append-over-time memory**: dated lessons, discoveries, case
studies, and "this worked / this failed" notes that emerge from real work and ongoing
research. `references/` is the curated textbook; **`memory/` is the lab notebook.**

The user explicitly wants this skill **proactively updated when new discoveries emerge
and lessons are learned** — that update lands here (and, when it changes the textbook,
in `references/` too, logged in `../CHANGELOG.md`).

## How it works

- One lesson per file, dated, kebab-case (`2026-07-01-piggy-bank-converts-non-payers.md`).
- Add a one-line pointer to the index below (newest on top).
- Each entry: what was learned, the evidence/source, and how to apply it. Convert
  relative dates to absolute. Link related references/patterns.
- When a memory hardens into general guidance, fold it into the relevant `references/`
  file and keep the memory as the dated origin.

## Entry template

```markdown
---
date: YYYY-MM-DD
type: lesson | discovery | case-study | experiment-result
tags: [conversion, rewarded-ads, ...]
---

**Lesson:** one-line takeaway.

**Evidence:** what it's based on (live game + date, our own test, a cited source).

**How to apply:** concrete guidance for our game.

**Related:** [[references/...]] · [[patterns/...]]
```

## Index

- [2026-06-29 — ads-first for thin-meta puzzle](2026-06-29-ads-first-for-thin-meta-puzzle.md) — solo v1 money is in ads; defer IAP economy until a meta exists + D7 ≥ 15%
