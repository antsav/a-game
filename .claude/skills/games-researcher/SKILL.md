---
name: games-researcher
description: >-
  Research and validate hyper-casual / hybrid-casual mobile game opportunities for the
  iOS App Store, and recommend concrete game-concept candidates to build. Use this
  whenever the user wants to scout game trends, find an emerging mechanic, analyze what's
  topping the App Store, study competitors or publishers (Voodoo, Rollic, Homa, etc.),
  size a market, sanity-check a game idea, decide what game to build next, run the daily
  emerging-candidate scan / "what should I play tonight" tracker, or asks "what should my
  next game be" / "is this concept worth building" / "what's trending in mobile games."
  Runs a repeatable daily scan that persists a time series to data/ and surfaces a short
  ranked shortlist of games to download and play, plus (for deeper asks) a dated market
  report and scored candidate shortlist to DOCS/. Trigger it even when the user doesn't
  say the word "research" — any request about choosing, validating, finding, or daily
  tracking a mobile game concept to ship belongs here.
---

# Games Researcher

Find an **emerging hyper/hybrid-casual mechanic in its moderate-competition window**,
validate it against current market reality, and recommend a concrete "clone-plus"
candidate to build for iOS.

This skill runs in **two modes** that share one scoring model and one stance:

1. **Daily emerging-candidate tracker (the default recurring job).** A repeatable scan
   that **persists a time series** and surfaces a tight ranked shortlist — *"here are 4–5
   games to download and play tonight, and why."* This is a **means to playing games, not
   an analytics product**: if the pipeline ever gets more complex than the games it finds,
   it has failed.
2. **Deep concept research (the occasional big decision).** When the user is actually
   choosing what to build, the full funnel → a dated market report + scored candidate
   shortlist saved to `DOCS/`.

The market moves fast — **every run pulls fresh live data**, and the tracker's whole point
is that a single-day snapshot is weak; **velocity (day-over-day movement) is the signal.**
See "Keep this skill current" at the end; that self-update step is part of the job.

## Orientation (read the references a task needs)

- `references/mechanic-taxonomy.md` — the keyword groups for querying + classifying every
  charting app into mechanic **families** (Lane A). Mirrored in the scan script.
- `references/publisher-watchlist.md` — the publisher watchlist + alias-matching notes
  (Lane B). Backed by `data/aliases.json`.
- `references/discovery-techniques.md` — how to spot a trend before it peaks (ad
  intelligence, soft-launch watching, chart velocity, fresh-twist methods).
- `references/validation-and-testing.md` — CPI/retention/ROAS benchmarks, the stage-gate
  funnel, how to score a concept, solo-dev validation without a UA budget.
- `references/data-sources-and-apis.md` — the free→paid tooling stack and endpoints, and
  **when** paid data (AppMagic/AppFigures) would be worth it (it is NOT yet).
- `references/market-snapshot.md` — current leaders / hot vs saturated / publishers.
  **The refreshable one.** Check its "AS OF" date; if >~60 days old, re-verify live & rewrite.

Bundled scripts (free, no auth, **pure stdlib, no deps**) in `scripts/`:
- **`daily_scan.py`** — the tracker. Runs both lanes, writes the daily CSV + appends the
  master series; `--report` reads the series and prints the ranked shortlist.
- `apple_charts.py` / `app_lookup.py` — ad-hoc single chart / single app lookups.
- `youtube_trends.py` — secondary organic-interest proxy (content demand, NOT app data).

## Who this is for (calibrate every recommendation)

A strong engineer with **zero game-dev experience**, shipping **solo, iOS-first**, on a
tiny budget, applying "ship a polished better-version of an emerging thing, validate before
building" (he grew a $2.2k/mo Chrome extension that way). So:
- **Bias to mechanics a solo dev can build and ship** — low art burden, simple core loop,
  organic-shareable. Sort/block/jam/idle puzzles fit; 4X, match-3, Habby-scale roguelites do not.
- **Distribution must be organic** (ASO + short-form) — he can't win paid UA against the factories.
- **Calm-taste gate:** the target is a hot mechanic family that **nobody has shipped a
  genuinely calm / no-timer / meditative version of yet** (see `my-game-preference`). That
  gap is the differentiation we hunt — not novelty for its own sake.
- **Push back on scope creep and "invent a new genre."** Recommend clone-plus of a proven,
  still-rising mechanic. **For a first-timer the bigger risk is being TOO LATE, not too early.**

---

## The two scanning lanes (the tracker runs both — they catch different things)

**Lane A — Category / keyword scan (broad recall).** Cast a wide net across the mechanic
taxonomy, classify **every** charting app by matching title + description against the
keyword groups, and track **rating-count velocity within each family**. This catches
**self-published sleepers** before any publisher grabs them — the truly early signal.

**Lane B — Publisher-release watch (high precision, pre-validated).** When a **new app ID
from a watchlist publisher** first appears, flag it high-priority. A publisher only launches
a title that already cleared its internal soft-launch gates (D1/D7 retention, CPI) — so it's
**pre-validated proof the mechanic has legs.**

**The synthesis (the important part):** Lane B tells us which mechanic *families* are hot
right now; Lane A tells us where inside those families the window is still *open* (a
self-published game showing rating-count velocity that no publisher has picked up yet).
**Score a candidate higher when both lanes point at the same family** — the scan labels
these `A+B`.

## Metrics — what matters, in order

1. **Rating-count velocity** — daily and 7-day delta in *rating count* (NOT rating score).
   Rating count is the best free proxy for download volume; score barely moves and doesn't
   signal scaling. **This is the primary signal.**
2. **The open-window flag** — present in **Top Free but absent from Top Grossing** = still
   scaling, monetization not yet locked = the window to study.
3. **Recency** — `days_since_first_seen ≤ 45`. We track our **own `first_seen` date**
   (first day an app ID appears in our data) because Apple's `version_release_date` is the
   *latest update*, not first launch — an old game that patched yesterday looks new.
4. **Rank movement** — 7-day rank delta (secondary; noisy and lagging vs rating velocity).
5. **New-from-watchlist-publisher** — binary high-priority flag (Lane B).

---

## Mode 1 — the daily tracker procedure

Run this when the user wants the daily scan, "what should I play tonight," a velocity
read, or just periodically to keep the series alive. **Scan daily** — the value is the
accumulating time series, not any single day.

1. **Scan (writes data, hits the network):**
   ```bash
   python .claude/skills/games-researcher/scripts/daily_scan.py
   ```
   Scans US + one rotating emerging geo (br/in/ph/id, weekly), categories Games/Puzzle/
   Arcade/Simulation, charts Free/Grossing/New. Appends one row per app/geo/chart to
   `data/scans/<date>.csv` and the `data/candidates.csv` master. Idempotent per day.

2. **Report (reads the series, no network):**
   ```bash
   python .claude/skills/games-researcher/scripts/daily_scan.py --report
   ```
   Prints a pre-ranked table with the derived velocity metrics (Δ1d, Δ7d rating count,
   rank move, open-window, days-since-first-seen, lane A/B/A+B) plus a "faded" list of
   candidates whose velocity died or that dropped off the charts.

3. **Turn the table into the play shortlist (your judgment, not the script's).** The
   `--report` heuristic is a pre-sort, **not** the six-axis score. Take its top rows,
   **apply the calm-taste gate and the six-axis model**, drop giant incumbents and
   over-tagged noise (the taxonomy over-tags on purpose — a human prunes here), and pick
   **4–5 games max** to actually download and play. Cross-check anything ambiguous with
   `app_lookup.py` or the store page.

4. **Write the play shortlist** (chat, and optionally `DOCS/research/`): see "Daily output".

> **Day 1 caveat:** with one day of data, velocity is null and ranking is weak — that's
> expected. The tracker earns its keep after ~3–7 daily runs. Don't over-interpret a cold start.

## Mode 2 — deep concept research (the full funnel)

When the user is choosing what to build (not just tracking), run the whole funnel and save
a dated report to `DOCS/`. Scale depth to the request; default to the full run for "what
should I build next?"

1. **Frame the question** — whole-market scan vs validating one concept vs studying one
   publisher. Note the absolute date so the report self-dates.
2. **Pull fresh live data** — run the tracker (both lanes) for the chart/velocity layer,
   AND the leading signals the scripts can't get: **Meta Ad Library** (UI) + **TikTok
   Creative Center** for creative longevity/concentration, **mobilegamer.biz** soft-launch
   column, and a web search for the last ~60 days of breakout stories / tooling changes.
   Cross-reference against `market-snapshot.md`; note what changed.
3. **Identify candidate mechanics** — convergence rule: a mechanic across **3+ publishers/
   creatives in ~4–8 weeks, CPI not spiked, no polished version dominating** = a real
   window. For each, name the **fresh-twist angle** and confirm a **hybrid meta path**.
4. **Score each candidate** (the six-axis model, below).
5. **Recommend + a cheap kill-fast validation** — CTR/CPI test on a concept video, the
   geos, the go/kill gates, sized for a no-UA-budget solo dev (see `validation-and-testing.md`).

## The six-axis scoring model (used by BOTH modes — unchanged)

Score 1–5 on each axis (benchmarks in `validation-and-testing.md`):
- **Trend timing** — emerging vs saturated (CPI not spiked, charts still moving; the
  tracker's velocity + open-window flags feed this directly).
- **Solo-buildability** — art/engineering burden for a first-time solo iOS dev.
- **Single-input core** — can the whole core loop be played with *one* repeated gesture (all
  tap **or** all slide, never mixed, no 3D-object manipulation)? Mixed input is a kill
  signal; see `game-designer/patterns/single-input-modality.md`.
- **Organic distribution fit** — ASO + short-form shareability (no paid UA needed).
- **Monetization headroom** — clear hybrid meta + IAP/rewarded path; realistic ARPDAU.
- **Competition** — moderate (beatable incumbents) vs winner-take-most.
- **Differentiation** — is the clone-plus / calm-lane angle real and defensible?

Surface honest risks per candidate; don't inflate. The pros kill ~99% of concepts — bias
toward fast, cheap kill signals.

---

## Daily output (Mode 1 — what the tracker produces)

A tight ranked shortlist — **4–5 candidates max** — each with:
- Title, publisher, mechanic family, `first_seen` / days tracked.
- The velocity read (rating-count 7-day delta, rank move, open-window yes/no).
- **Why it's flagged** — Lane A riser / Lane B new publisher launch / both (`A+B`).
- A **one-line play brief:** what to look for when testing it — the core verb, the one
  thing that makes you want to replay, and where the **calm-lane differentiation gap**
  might be.

Plus a one-line note on any candidate that **dropped off** (velocity died) so we prune the
watchlist. Keep it terminal-tight; this feeds tonight's play session, not a slide deck.

## Report output (Mode 2 — deep research)

Save to `DOCS/research/YYYY-MM-DD-<topic>.md` and give a tight chat summary. Skeleton:
```
# Game Research — <topic> — <YYYY-MM-DD>
## TL;DR            (3-5 bullets: the call, top candidate, the one risk)
## Market snapshot  (live state: leaders, what's hot/saturated, what changed since last run)
## Candidate shortlist  (the six-axis scored table, ranked)
## Top pick(s)      (the clone-plus angle, why it fits a solo iOS dev, the meta path)
## Validation plan  (cheap kill-fast test: gates, geos, budget, go/kill criteria)
## Sources & confidence  (URLs + dates; flag estimates vs verified; note staleness)
```
Keep numbers honest: label estimates vs verified, cite source + date, flag staleness/
conflicts (CPI/eCPM/ARPDAU vary 2–10× by source — see `validation-and-testing.md`).

## The datastore (CSV, and it stops there)

`data/` is the whole datastore — **flat CSV + one JSON alias map, on purpose.** No
Postgres, no SQLite, no dashboard, no web app, no paid API. Derived metrics are computed at
read time, never stored. **Revisit only** after 2–3 weeks of data AND a concrete thing CSV
can't do; a paid data API is a separate decision, triggered only when a specific concept is
serious enough to need download/revenue *estimates*. See `data/README.md` for the schema
and this decision in full.

## Keep this skill current (do this every run — it's part of the job)

- **New mechanic word** recurring in charting titles → add it to a family in
  `references/mechanic-taxonomy.md` **and** the script's `TAXONOMY` (keep them in sync).
- **Watchlist publisher charting under a name the matcher missed** → add the alias to
  `data/aliases.json` and note it in `references/publisher-watchlist.md`.
- **New leaders / market shifts** → rewrite `references/market-snapshot.md`, bump "AS OF".
- **New technique / source / tooling change** (this space restructures constantly) → fold
  into the relevant reference; update `references/data-sources-and-apis.md` and scripts.
- **Always** append a dated one-line entry to `CHANGELOG.md`.
Treat a reference that names a specific game, publisher, tool, or threshold as **possibly
stale** — verify before relying on it, and fix it when it's wrong.
