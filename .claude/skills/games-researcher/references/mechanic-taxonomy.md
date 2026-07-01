# Mechanic Taxonomy — Keyword Groups for Querying + Classifying

The taxonomy does two jobs:
1. **Query nets** — the keyword groups to cast across the charts (broad recall, Lane A).
2. **Classification** — tag every charting app with the mechanic **family** it belongs to,
   by matching its title + description against these groups.

`scripts/daily_scan.py` reads this taxonomy (mirrored in the script's `TAXONOMY` dict —
keep the two in sync) to auto-tag each app's `mechanic_tags`. An app can carry **multiple**
tags (e.g. a "color sort" idle game → `sort` + `idle`); that's expected and useful — it's
how we spot cross-family blends.

> **This list is a starting point — extend it as we learn.** When a new mechanic word shows
> up repeatedly in charting titles/descriptions, add it to the right family (or open a new
> family) here AND in the script's `TAXONOMY`, and log it in `CHANGELOG.md`.

## Families (keyword groups)

| Family key | Keywords (match on title + description, case-insensitive, word-ish) |
|---|---|
| **sort** | color sort, water sort, ball sort, pin sort, block sort, nuts & bolts, nuts and bolts, screw, unscrew, bolt, tidy, declutter, organize, organise, sort |
| **unblock** | unblock, untangle, tangle, knot, rope, escape, jam, traffic, parking, pull the pin, pull pin, get them out, get out, extract |
| **merge** | merge, combine, fusion, evolve, 2048 |
| **stack** | stack, fill, fit, block blast, wood block, woodoku, pack, tangram, packing |
| **idle** | idle, tycoon, manager, empire, incremental, prestige, offline, tap, clicker |
| **physics** | pachinko, plinko, aim, ricochet, bounce, drop, brick breaker, breakout, ball, physics |
| **draw** | draw, paint, color, colour, fill, coloring, colouring, line, sketch |
| **crowd** | run, runner, crowd, count, counting, army, gate, multiplier, horde |
| **dig** | dig, excavate, mine, mining, reveal, scratch, sand, wash, clean, power wash, powerwash |

Notes on matching:
- Match is **substring, case-insensitive**, on the concatenation of `title` + `description`.
  Keep keywords specific enough to avoid junk (e.g. `tap` and `ball` and `line` and `run`
  are noisy — they'll over-tag; that's tolerated because a human reads the shortlist, but
  prefer the more specific multi-word keys when extending).
- A single strong multi-word hit (e.g. "water sort") is worth more than a lone noisy word;
  the script currently treats any hit as a tag — the human prunes at read time.
- `mechanic_tags` is stored **pipe-joined** in the CSV (e.g. `sort|idle`) because comma is
  the field delimiter.

## The two-lane synthesis this feeds

- **Lane A (this taxonomy)** classifies the whole charting field into families and tracks
  **rating-count velocity within each family** — catching self-published sleepers early.
- **Lane B** (`publisher-watchlist.md`) flags brand-new app IDs from known publishers.
- **Score higher when both point at the same family:** Lane B says a mechanic family is hot
  (a publisher just bet on it); Lane A tells us whether the window inside that family is
  still open (a self-published riser no publisher has grabbed yet).

## The calm-taste filter (don't lose this in the data)

The tags are mechanical, but Anton's taste is not. When a family lights up, ask whether it
has a **calm / no-timer / meditative** expression (see `my-game-preference`). `sort`,
`stack`, `idle`, `draw`, `dig/reveal` lend themselves to the calm lane; `crowd`/`runner`
and timer-driven `physics` usually don't. The differentiation gap we're hunting is a hot
mechanic family that nobody has shipped a genuinely *calm* version of yet.

## Category note (Apple genre IDs)

The legacy iTunes RSS filters by genre ID. We scan: **Games-all (6014)**, **Puzzle (7012)**,
**Arcade (7003)**, **Simulation (7015)** — idle/tycoon lives in Simulation. **"Casual" has
no dedicated legacy-RSS genre ID**, so Casual titles are captured via the Games-all (6014)
chart and then separated by mechanic tag, not by an Apple category filter.
