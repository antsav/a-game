# games-researcher — changelog

Append a dated one-line entry whenever the skill or its references change. This is how
the skill's evolution stays auditable. Newest on top.

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
