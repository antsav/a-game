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
