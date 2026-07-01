# `data/` — the daily-scan time series

This is the whole datastore for the daily emerging-candidate tracker. It is **flat CSV +
one JSON alias map, on purpose.**

## Why CSV and nothing else (the "no Postgres yet" decision)

This is a **means to playing games, not an analytics product.** The output is "here are 4–5
games to try tonight and why." If the pipeline ever gets more complex than the games it
finds, it has failed.

- **No Postgres, no SQLite, no dashboard, no web app, no ORM.** Appended CSV is the datastore.
- **No paid API.** Free Apple endpoints only (iTunes RSS charts + Lookup).
- Derived metrics (velocity, deltas, recency) are **computed at read time** from the series,
  never stored — so there's no schema migration to do when we change how we score.

**When to revisit this decision (not before):** once we have **2–3 weeks** of daily data
*and* a concrete thing CSV can't do — e.g. we're querying the history so often that
`--report` is too slow, or we want to join against a second data source. Then, and only
then, consider SQLite (still a single file, still no server). Upgrading to a paid data API
(AppMagic / AppFigures) is a **separate** decision, triggered only when a specific concept
is serious enough to need download/revenue *estimates* to size its market — see
`references/data-sources-and-apis.md`.

## Layout

```
data/
  scans/YYYY-MM-DD.csv   one file per scan day (full snapshot of that day's rows)
  candidates.csv         appended master series (all days) — the file --report reads
  aliases.json           publisher-name alias map for Lane B matching
  README.md              this file
```

`scans/*.csv` and `candidates.csv` are **generated data** — regenerable by re-running the
scan, but the point is to *accumulate* them over time (that's the velocity signal), so they
are committed to the repo, not gitignored. A day's scan file is overwritten if the scan is
re-run that day; the master is de-duplicated on `(scan_date, geo, chart, category, app_id)`.

## Schema — one row per app, per geo, per chart, per scan day

| Column | Source | Notes |
|---|---|---|
| `scan_date` | run date | `YYYY-MM-DD` (local date the scan ran) |
| `geo` | run config | `us` + one rotating emerging geo (br/in/ph/id) |
| `chart` | RSS feed | `free` \| `grossing` \| `new` |
| `category` | RSS genre | `games` (6014) \| `puzzle` (7012) \| `arcade` (7003) \| `simulation` (7015) |
| `rank` | RSS position | 1-based within that geo/chart/category |
| `app_id` | RSS `im:id` | Apple track ID — the stable join key |
| `title` | Lookup `trackName` | |
| `seller_name` | Lookup `sellerName` | legal entity (used for Lane B match) |
| `price` | Lookup `price` | 0.0 for free |
| `avg_rating` | Lookup `averageUserRating` | score, NOT a scaling signal — barely moves |
| `rating_count` | Lookup `userRatingCount` | **the primary signal** — best free download proxy; storefront-specific |
| `version_release_date` | Lookup `currentVersionReleaseDate` | ⚠️ latest *update*, NOT first launch |
| `first_seen_date` | our own | first `scan_date` this `app_id` ever appeared in our data — the real recency signal |
| `mechanic_tags` | classifier | pipe-joined families, e.g. `sort|idle` (see `references/mechanic-taxonomy.md`) |
| `is_watchlist_publisher` | classifier | `true`/`false` — Lane B (see `references/publisher-watchlist.md`) |
| `notes` | scan | free-text flags (e.g. `open-window`) |

### Derived at read time (computed by `--report`, never stored)
`rating_count_delta_1d`, `rating_count_delta_7d`, `rank_delta_7d`, `days_since_first_seen`,
`open_window` (in `free` but absent from `grossing` for that geo/day).

> **Why `first_seen_date` is our own field, not `version_release_date`:** Apple's
> `currentVersionReleaseDate` is the date of the *latest update*, so a 3-year-old game that
> shipped a patch yesterday looks brand-new. The only trustworthy recency signal we have is
> the first day *we* saw the app ID. That's why the scan must run daily and accumulate.

## Regenerating / reading

```bash
# Run the daily scan (writes scans/<today>.csv, appends candidates.csv):
python ../scripts/daily_scan.py

# Read the series and print the ranked candidate shortlist (no network):
python ../scripts/daily_scan.py --report
```

`rating_count` is **storefront-specific** (a US lookup and a BR lookup return different
counts for the same app), so velocity is computed per `(app_id, geo)`, not globally.
