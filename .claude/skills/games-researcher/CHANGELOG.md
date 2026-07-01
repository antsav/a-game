# games-researcher — changelog

Append a dated one-line entry whenever the skill or its references change. This is how
the skill's evolution stays auditable. Newest on top.

## 2026-07-01 — capture reports for trace-and-improve + shape the daily "top 10 test/watch" job
- `--report` now **auto-saves** each run: `data/reports/<date>.md` (human snapshot of the
  shortlist we acted on) + `data/reports/<date>-shortlist.csv` (the FULL eligible set,
  machine-readable). Purpose: later join a past shortlist against the current candidates.csv
  to measure whether the games we flagged "emerging" actually rose — how the ranking earns
  trust or gets fixed. `--no-save` opts out. Report keyed by latest scan date; idempotent.
- Locked the recurring daily job in SKILL.md: scan → `--report` (saves trace) → deliver a
  **top 10 to test & watch**, each split TEST (download now + play brief) vs WATCH (the
  velocity move that would promote it). Kept the "confirm what a game actually is before
  classifying — don't trust the noisy tags" rule (learned the hard way this session).
- Docs: data/README.md documents the `reports/` trace layer.

## 2026-07-01 — fix: day-1 "emerging" was surfacing mature incumbents (and then newborns)
- Root cause: rating_count is CUMULATIVE, so a snapshot can't measure "emerging" (a velocity
  property); on a cold start `days_since_first_seen` is 0 for everything, so the whole chart
  was "eligible" and mature 500k-rating titles (Magic Sort!, My Perfect Hotel) leaked in.
- Added `release_date` (Apple's true first-launch date) to the schema + scan — the only
  recency signal available before we accrue our own velocity. Re-scanned 07-01 to populate.
- `--report` now has an explicit **cold-start mode** (single scan day): eligibility =
  **`emerging`** = launched ≤180d AND rating_count in [1,000–50,000) (real-but-unscaled
  traction — a floor to kill 0-rating `new`-feed newborns, a ceiling to kill arrived giants),
  ranked by current chart traction. Once ≥2 scan days exist, velocity takes over automatically.
- Also gated the "new-from-watchlist" flag behind `multi_day` (on day 1 every watchlist app
  is trivially "new" → meaningless). Added `days_since_launch` + `emg` columns to the report.
- Docs: data/README.md schema + "emerging is a velocity property" note; this is why the tool
  is a *daily* tracker, not a one-shot.

## 2026-07-01 — review pass: harden scan against silent feed-deprecation
- Audited the 07-01 scan: data confirmed authentic (live Lookup `userRatingCount` matches
  the CSV exactly — Meowdoku! 46,964; Block Out! 101,362), pipeline + `--report` working.
- **Hardened `daily_scan.py` to fail LOUD, not silent:** if every chart for a geo returns
  0 entries (the signature of Apple retiring/changing the legacy iTunes RSS feed), the scan
  now `sys.exit`s with a diagnostic instead of writing an empty snapshot that would read as
  a calm market. Added a second guard for the chart-ok-but-Lookup-empty case (0 total rows).
- Considered a rating_count tie-break for day-1 report ranking; rejected/reverted — it
  foregrounded giant incumbents (aquapark.io/Paper.io), fighting the sleeper-hunting goal.

## 2026-07-01 — daily emerging-candidate tracker (time-series pipeline + two lanes)
- Reframed the skill into **two modes** sharing the six-axis model + stance: (1) a
  repeatable **daily tracker** that persists a time series and outputs 4–5 games to play
  tonight, and (2) the existing deep-research report to DOCS/. SKILL.md rewritten; scoring
  model left intact (this feeds it, doesn't replace it).
- **Verified live (2026-07-01) before building:** legacy iTunes RSS charts (genre filter
  still the only game-chart feed), Lookup fields (`sellerName`/`artistName`/`userRatingCount`/
  `genres`/`currentVersionReleaseDate`), and **batch Lookup** (comma-separated IDs → N
  results) — the key to staying under Apple's ~20/min throttle. Endpoints unchanged since
  the 06-30 verification. Noted: `sellerName` is the legal entity (e.g. "GRAND GAMES OYUN
  VE YAZILIM ANONIM SIRKETI"), so Lane B must normalized-substring match both name fields.
- **New:** `scripts/daily_scan.py` (pure stdlib, no deps) — runs Lane A (classify every
  charting app by mechanic family, track rating-count velocity) + Lane B (flag new app IDs
  from watchlist publishers); writes `data/scans/<date>.csv` + appends `data/candidates.csv`;
  `--report` computes velocity/open-window/recency at read time and prints the ranked
  shortlist. Tracks our own `first_seen` date (Apple's version date = latest update, not launch).
- **New references:** `mechanic-taxonomy.md` (keyword families, mirrored in the script) and
  `publisher-watchlist.md` (watchlist + alias matching). **New data scaffolding:**
  `data/aliases.json`, `data/README.md` (schema + the explicit "no Postgres/SQLite/dashboard/
  paid-API yet — revisit after 2–3 weeks + a concrete need" decision).
- Design choices (noted, anti-over-engineering): `data/` lives **inside the skill** (self-
  contained; avoids a lowercase top-level dir clashing with DOCS/); **stdlib not requests**
  (zero deps, consistent with existing scripts); geo rotation is **weekly not daily** (so an
  emerging geo gets consecutive days to compute velocity). Seeded day 1: US + Indonesia.

## 2026-06-29 — data-sources hardening (firsthand-verified API catalog)
- Corrected `data-sources-and-apis.md` from live endpoint testing: v2 RSS lives at
  `rss.marketingtools.apple.com` and has **no Games genre filter** (404) → legacy iTunes
  RSS confirmed as the only game-chart feed. data.ai acquired by Sensor Tower Mar 2024.
- Added: AppMagic has a paid public REST API + genuine free tier; GameRefinery free tier
  (downloads/revenue for 100k+ games, 33 markets) is the best free game taxonomy source.
- Trend-signal APIs made precise: YouTube Data API (10k units/day), Reddit PRAW (100 QPM),
  **pytrends archived Apr 2025** (manual-only); SerpApi/DataForSEO as cheap Google Play
  chart + Trends paths; maintained scraper libs (`@perttu/app-store-scraper`,
  `itunes-app-scraper-dmi`) over the stale originals.

## 2026-06-29 — initial version
- Created the skill: SKILL.md workflow (frame → pull live data → identify → score →
  recommend + validation plan), output = dated report + scored candidate shortlist to DOCS/.
- References from deep research (mid-2026): `market-snapshot.md`,
  `discovery-techniques.md`, `validation-and-testing.md`, `data-sources-and-apis.md`.
- Scripts: `apple_charts.py`, `app_lookup.py` (free iTunes RSS + Search/Lookup, no auth).
- Key market facts baked in (verify on next run): hyper-casual → hybrid-casual shift;
  sort/block/jam puzzles the hottest family; Rollic #1 publisher; arrow-puzzle the
  freshest breakout (Apr 2026); Sensor Tower acquired AppMagic + owns data.ai;
  Supersonic/ironSource shutting down (Apr 2026); Meta Ad Library impression buckets;
  Apple Games app split. Benchmark numbers are aggregator-sourced — flagged as directional.

## 2026-06-30 — 1-day refresh run (arrow/sort delta)
- Live pull (US free/grossing/new + puzzle 7012, BR/PH): market structure unchanged vs
  06-29. New grain — 4 same-day new entrants (Arrow Stack!, Traffic Sort!, Pack Flow,
  Café Sort), confirming arrow+sort windows now openly contested.
- Leader rating velocity: Arrows – Puzzle Escape 277.5k (#8 free/#4 puzzle);
  Block Out! – Color Sort crossed 100k (#2 free). Neither in Top Grossing → still scaling.
- Action: dropped Competition score for arrow (4→3) and sort (3→2); sharpened the
  "ship fast / being-late is the risk" call. Report: DOCS/research/2026-06-30-refresh.md.
- market-snapshot.md left as-is (only 1 day old; still fresh).
- Tooling: added `scripts/youtube_trends.py` — wires up the free YouTube Data API v3
  (view-velocity trend detector on a keyword watchlist). Reads YOUTUBE_API_KEY from
  env/.keys.local. Registered in references/data-sources-and-apis.md. Also created a
  root .keys.local.example (was missing) documenting GEMINI_API_KEY + YOUTUBE_API_KEY.
- Data sources: verified live (2026-06-30) and folded into data-sources-and-apis.md the
  paid-API landscape for "search/sort/filter apps by criteria": AppMagic (SMB tier, 14M
  apps, 500+ mechanic tags, D1-D360 retention, soft-launch detector; real API as paid
  add-on ~$400-1000/mo/seat = best game-scouting fit) vs AppFigures ($7.99-599.99/mo,
  real API but competitor/market data gated behind the Partner API add-on). Added a
  "which paid API" decision block. Clarified youtube_trends.py is a secondary
  organic-interest proxy, NOT app-performance data — hold paid API spend until validation.
