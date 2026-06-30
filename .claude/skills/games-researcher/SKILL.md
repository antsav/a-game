---
name: games-researcher
description: >-
  Research and validate hyper-casual / hybrid-casual mobile game opportunities for the
  iOS App Store, and recommend concrete game-concept candidates to build. Use this
  whenever the user wants to scout game trends, find an emerging mechanic, analyze what's
  topping the App Store, study competitors or publishers (Voodoo, Rollic, Homa, etc.),
  size a market, sanity-check a game idea, decide what game to build next, or asks
  "what should my next game be" / "is this concept worth building" / "what's trending in
  mobile games." Produces a dated market report plus a scored shortlist of candidates
  saved to DOCS/. Trigger it even when the user doesn't say the word "research" — any
  request about choosing, validating, or finding a mobile game concept to ship belongs
  here.
---

# Games Researcher

Find an **emerging hyper/hybrid-casual mechanic in its moderate-competition window**,
validate it against current market reality, and recommend a concrete "clone-plus"
candidate to build for iOS. The deliverable is a dated report **and** a scored
candidate shortlist saved to `DOCS/`.

This skill encodes a methodology and a starting market snapshot. **The market moves
fast — every run must pull fresh live data, not just recite the references.** See
"Keep this skill current" at the end; that self-update step is part of the job, not optional.

## Orientation (read the references)

Four reference files hold the domain knowledge. Read the ones a task needs — don't
recite them blindly; use them to interpret live data.

- `references/market-snapshot.md` — current leaders, hot vs saturated mechanics,
  publishers. **The refreshable one.** Check its "AS OF" date first; if >~60 days old,
  treat it as a hypothesis to re-verify live, then rewrite it.
- `references/discovery-techniques.md` — how to spot a trend before it peaks (ad
  intelligence, soft-launch watching, chart velocity, the fresh-twist methods).
- `references/validation-and-testing.md` — CPI/retention/ROAS benchmarks, the
  stage-gate funnel, how to score a concept, solo-dev validation without a UA budget.
- `references/data-sources-and-apis.md` — the free→$100/mo tooling stack and endpoints.

Bundled scripts (free, no auth, no deps) in `scripts/`:
- `apple_charts.py` — Apple Top Free/Grossing/New for Games (any country/subgenre).
- `app_lookup.py` — App Store metadata for any title (publisher, ratings, dates).

## Who this is for (calibrate every recommendation)

The user is a strong engineer with **zero game-dev experience**, shipping **solo**,
**iOS-first**, on a tiny budget, applying a "ship a polished better-version of an
emerging thing, validate before building" philosophy (he previously grew a $2.2k/mo
Chrome extension that way). So:
- **Bias to mechanics a solo dev can actually build and ship** — low art burden, simple
  core loop, organic-shareable (TikTok/ASMR-friendly). Sort/block/jam puzzles fit; 4X,
  match-3, and Habby-scale roguelites do not.
- **Distribution must be organic** (ASO + short-form), because he can't win paid UA
  against the factories. Score candidates on that, not on a UA war chest.
- **Push back on scope creep and "invent a new genre" ideas** — they contradict the
  validate-first thesis. Recommend clone-plus of a proven, still-rising mechanic.
- **The bigger risk for a first-timer is being TOO LATE**, not too early.

## The research workflow

Scale depth to the request — a quick "what's trending?" needs steps 1-2; "what should I
build next?" warrants the full funnel through step 5. Default to the full run unless the
user clearly wants a quick read.

### 1. Frame the question
Clarify scope if ambiguous (whole-market scan vs. validating one specific concept vs.
studying one publisher). Note the date; convert "current" to an absolute date so the
report is self-dating.

### 2. Pull fresh live data (never skip — the references age)
Gather the leading signals (see `discovery-techniques.md` for the why and the weekly
routine):
- **Charts:** run `apple_charts.py` for US Top Free + Top Grossing (Games), and at least
  one emerging market (br/in/ph/id). Note risers in Top Free **not yet in Top Grossing**
  — fresh hooks still scaling. Use `app_lookup.py` to profile the interesting ones.
- **Ad intelligence:** check Meta Ad Library (UI) and TikTok Creative Center for the
  target publishers — flag creatives 30+ days old / in high impression buckets
  (validated winners) and the same mechanic across multiple advertisers.
- **Soft-launch / pipeline:** check mobilegamer.biz's soft-launch column and target
  publishers' newest releases / test geos.
- **Web search** for the latest (last ~60 days) market reports, breakout stories, and
  any tooling/market structure changes. Always verify time-sensitive claims live.
- Cross-reference live findings against `market-snapshot.md`; note what changed.

### 3. Identify candidate mechanics
Apply the convergence rule: a mechanic showing up across **3+ publishers/creatives in
~4-8 weeks, CPI not yet spiked, no polished version dominating the charts** = a real
window. For each, identify the **fresh-twist angle** (mix-two-loops / swap-the-meta /
re-theme) and confirm a **hybrid meta path** exists (no meta headroom = dead on arrival).

### 4. Score each candidate
Score 1-5 on each axis (see `validation-and-testing.md` for the benchmarks behind these):
- **Trend timing** — emerging vs saturated (CPI not spiked, charts still moving).
- **Solo-buildability** — art/engineering burden for a first-time solo iOS dev.
- **Organic distribution fit** — ASO + short-form shareability (no paid UA needed).
- **Monetization headroom** — clear hybrid meta + IAP/rewarded path; realistic ARPDAU.
- **Competition** — moderate (beatable incumbents) vs winner-take-most.
- **Differentiation** — is the clone-plus angle real and defensible?
Surface the honest risks per candidate; don't inflate scores. The pros kill ~99% of
concepts — bias toward fast, cheap kill signals.

### 5. Recommend + define a cheap validation plan
For the top candidate(s), propose the **kill-fast validation** before any heavy build:
a CTR/CPI test on a concept video (see the stage-gate funnel and current benchmark
bars), the geos to test in, and the metric gates that mean go vs kill. Make the
validation match a no-UA-budget solo dev (organic soft-launch in a cheap geo, ASO).

## Output format

Save two artifacts to `DOCS/` (create `DOCS/research/` if needed), and give the user a
tight summary in chat. Use the date in the filename: `DOCS/research/YYYY-MM-DD-<topic>.md`.

**Report structure (always this skeleton):**
```
# Game Research — <topic> — <YYYY-MM-DD>
## TL;DR            (3-5 bullets: the call, top candidate, the one risk)
## Market snapshot  (live state: leaders, what's hot/saturated, what changed since last run)
## Candidate shortlist  (the scored table, ranked)
## Top pick(s)      (the clone-plus angle, why it fits a solo iOS dev, the meta path)
## Validation plan  (cheap kill-fast test: gates, geos, budget, go/kill criteria)
## Sources & confidence  (URLs + dates; flag estimates vs verified; note staleness)
```

**Candidate shortlist table:** one row per candidate, columns = the 6 scoring axes +
total + one-line verdict (pursue / park / kill).

Keep numbers honest: label estimates vs verified, cite source + date, and flag where
data is stale or sources conflict (CPI/eCPM/ARPDAU numbers vary 2-10× by source — see
the reliability warnings in `validation-and-testing.md`).

## Keep this skill current (do this every run — it's part of the job)

The user explicitly wants this skill to improve itself over time. On each run, if you
discover anything new, **update the skill, don't just use it:**
- **New leaders / mechanics / market shifts** → rewrite `references/market-snapshot.md`
  and bump its "AS OF" date.
- **New technique, source, or a better way to spot/validate trends** → fold it into the
  relevant reference file.
- **Tooling changes** (new API, pricing change, a tool acquired/shut down — this space
  restructures constantly) → update `references/data-sources-and-apis.md` and, if
  useful, add/upgrade a script in `scripts/`.
- **Always** append a dated one-line entry to `CHANGELOG.md` describing what changed and
  why, so the skill's evolution is auditable.
Treat a reference that names a specific game, publisher, tool, or threshold as
**possibly stale** — verify before relying on it, and fix it when it's wrong.
