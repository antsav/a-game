# Data Sources & APIs

The tooling stack for this skill, organized free → paid for a solo dev on ~$0-100/mo.
Bundled scripts in `../scripts/` already wrap the free Apple endpoints.

> **2026 tooling consolidation — re-check old tutorials.** **Sensor Tower acquired
> AppMagic (~May 12 2026)**, keeping AppMagic as its affordable SMB tier; Sensor Tower
> already owned **data.ai / App Annie**, so data.ai as an independent option is gone.
> AppMagic also began **moving free features behind premium from Jan 1 2026**.
> **Supersonic's ironSource ad network shut down Apr 30 2026.** Verify any tool's
> current state and log changes in `../CHANGELOG.md`.

## The recommended ~$0-100/mo stack

1. **Free, wire up first:** Apple iTunes RSS charts + Search/Lookup (bundled scripts),
   Meta Ad Library (UI + API), TikTok Creative Center, Google Trends (pytrends),
   AppFigures free tier, AppMagic/Sensor Tower free public charts.
2. **One affordable paid tool if a concept gets serious** (pick ONE, not all):
   - **AppMagic** (now Sensor Tower SMB tier) — best value for download estimates +
     soft-launch detector. Check current pricing post-acquisition.
   - or **AppGrowing Global** (~$57/mo) — if you need Asia ad-network creative coverage.
   - or **Foreplay** (~$59/mo, has an API) — if you want a programmatic ad swipe-file.
3. **Skip** the enterprise tiers (Sensor Tower full, SocialPeta, Apptica, GameRefinery
   — $11k-150k/yr). Know they exist; the free stack covers ~80% of scouting.

---

## Free Apple App Store endpoints (no auth, no deps)

**These are the backbone — bundled in `../scripts/`.**

### iTunes RSS top charts (supports Games genre filtering)
Format:
```
https://itunes.apple.com/{country}/rss/{feed}/limit={N}/genre={genreId}/json
```
- `{feed}`: `topfreeapplications`, `toppaidapplications`, `topgrossingapplications`,
  `newapplications`, `newfreeapplications`
- `{genreId}`: **6014 = Games (all)**; subgenres incl. 7001 Action, 7003 Arcade,
  7012 Puzzle, 7015 Simulation, 7017 Strategy, 7005 Card, 7006 Casino, 7004 Board.
- `{country}`: `us`, `br`, `in`, `ph`, `id`, … (watch emerging markets — HC breaks
  there first).
- **Use the bundled `apple_charts.py` instead of curl** — it parses to clean rows.
- Feed types also include `topfreeipadapplications`, `newpaidapplications`.
- ⚠️ The newer **v2 feed** (`https://rss.marketingtools.apple.com/api/v2/{cc}/apps/{top-free|top-paid|top-grossing}/{N}/apps.json`; note `rss.applemarketingtools.com`
  301-redirects here) has cleaner JSON but **does NOT support a Games genre filter**
  (`.../games.json` → HTTP 404, verified). **For game-specific charts you must use the
  legacy iTunes RSS above.** Build v2 URLs at [rss.marketingtools.apple.com](https://rss.marketingtools.apple.com/).

### iTunes Search & Lookup (app metadata)
```
https://itunes.apple.com/search?term={q}&country=us&entity=software&limit={N}
https://itunes.apple.com/lookup?id={trackId}&country=us
https://itunes.apple.com/lookup?bundleId={bundleId}&country=us
```
Returns publisher, genres, **userRatingCount** (rough popularity proxy), release &
current-version dates, price, description. **Use the bundled `app_lookup.py`.**
No documented hard rate limit, but it throttles ~20 req/min — batch politely.

### App Store Connect API & Apple Search Ads API
Both require your own Apple account + auth (JWT). App Store Connect exposes *your own*
app's data, not competitors'. Apple Search Ads API gives keyword popularity/bid data
useful for ASO once you have an account. Not needed for cold trend scouting.

---

## Ad creative intelligence

### Meta Ad Library — FREE, the #1 free ad tool
- **UI:** [facebook.com/ads/library](https://www.facebook.com/ads/library) — all ads
  incl. game ads, search by advertiser page, sort oldest-first (longevity), filter by
  the new **impression-range buckets** (Jan 2026). No login.
- **API** (`ads_archive` Graph endpoint): free to call but **gated** — needs a Meta
  app, a token with `ads_read`, AND government-ID verification (~1-2 days).
- **⚠️ CRITICAL SCOPE LIMIT (verified from Meta docs):** for **non-EU** ads the API
  returns **only** social-issue/election/political ads. Commercial/game ads are
  retrievable via API **only if the ad reached an EU location**. **US/non-EU game
  creatives are NOT available via the API** — for those, the free option is the **UI,
  used manually**. Don't build an automated US-game-ad pull on the Meta API; it won't work.

### TikTok Creative Center — FREE
- [ads.tiktok.com/business/creativecenter](https://ads.tiktok.com/business/creativecenter/pc/en)
  → **Top Ads** filterable by Industry=Gaming, region, time period; plus trending
  hashtags/songs/keywords. No login for most of it. **No public API** for this data
  (the Commercial Content API is EU-only; Research API is academic-only). Use manually.

### Paid ad-spy (if you want programmatic creatives)
- **Foreplay.co** — Basic $59/mo; documented **public API** (1 ad = 1 credit, 10k free
  credits/mo). Best self-serve + API pick. Covers Meta + TikTok.
- **AdSpy** $149/mo flat (FB/IG only). **SocialPeta** custom/enterprise (most game
  coverage, gated API). **BigSpy** free tier + ~$99/mo Pro.

---

## Market intelligence platforms

| Tool | Free tier | Paid | API |
|---|---|---|---|
| **AppMagic** | **Genuine free tier** (limited daily credits) + 1-week full trial | ~$400/mo entry (contact-sales; up to ~$1k/seat) | **Yes — public JSON REST API, 50+ endpoints, but paid add-on** |
| **GameRefinery (Liftoff)** | **Genuinely useful: free downloads/revenue for 100k+ games across 33 markets** + best free feature-taxonomy reports | Full taxonomy enterprise | Enterprise only (no self-serve docs) |
| **Sensor Tower** | Public Top Charts page + free "State of Mobile" reports | Enterprise (~$30k-150k/yr, est.) | Enterprise-gated |
| **AppFigures** | Connect tier: Top Charts + free monthly "most downloaded/earning" reports; independent | from ~$/mo | Yes |
| **data.ai / App Annie** | **GONE** — acquired by Sensor Tower (Mar 18 2024), brand retired | — | — |
| **Apptopia** | none usable | ~$15k-50k/yr (est.) | Real API w/ public docs (dev.apptopia.com) but paid creds |
| **SocialPeta / Apptica** | blog only | Enterprise | Gated |

All download/revenue figures from these are **modeled estimates** — downloads more
reliable than revenue. Cross-check before betting money. **Best practical picks for a
solo dev: AppMagic free tier + 1-week trial, and GameRefinery's free tier** (the most
useful free game-specific taxonomy + performance data).

---

## Trend-signal sources with APIs (cheap automation)

- **YouTube Data API v3** — free, API key only (no OAuth), **10,000 units/day**.
  `search.list` = 100 units (~100 searches/day); `videos.list` = 1 unit per ≤50 IDs.
  Pattern: few targeted searches → batch-hydrate view counts cheaply. Detect rising
  game interest via video view-velocity on a keyword watchlist. Solid.
- **Reddit API via PRAW** — free non-commercial: **100 QPM with OAuth** (app
  registration + 2025 pre-approval). Monitor r/incremental_games, r/iosgaming for demand
  signals; watch r/gamedev for "how do I clone X" (saturation warning). Solid.
- **Google Trends** via **pytrends** — ⚠️ **repo ARCHIVED Apr 17 2025**, unofficial
  scraper, heavy 429 throttling. Fine for occasional *manual* pulls (rising/breakout
  related queries are a key emerging signal), **unreliable for automated pipelines.**
  Paid alternatives: SerpApi (~$75/mo→5k) or DataForSEO Google Trends.
- **Google Play** — **no official chart/ranking API.** Best scraper:
  **google-play-scraper (Node, facundoolano)** — active, has `list()`/charts; warns it
  breaks on Play layout changes + IP-bans at volume. The Python `google-play-scraper`
  (JoMingyu) is effectively unmaintained (no charts). For reliable Play charts/Trends,
  **SerpApi** ($25→1k / $75→5k searches/mo, real `chart` param) or **DataForSEO**
  ($50 min top-up, ~$0.0006/app) are the cheap paid paths.
- **iOS scraper libs** (all wrap the same free Apple endpoints our scripts use; risk =
  Apple's ~20/min throttle): best-maintained are **`@perttu/app-store-scraper`**
  (Node/TS, v2.0.0 Dec 2025, full charts/similar/search) and **`itunes-app-scraper-dmi`**
  (Python, v0.9.6 Nov 2024). Pair with **`app-store-web-scraper`** (Python) for reviews.
  The original `app-store-scraper` (facundoolano, Node) and `cowboy-bebug` (Python) are
  stale — prefer the maintained forks.

---

## Practical notes

- **Wire up the free Apple scripts + Meta Ad Library UI + TikTok Creative Center
  first** — that covers leading signals (ad creative), chart velocity, and metadata at
  $0.
- **Pay for exactly one tool** only when a specific concept needs download/revenue
  estimates to size the market — and prefer AppMagic's SMB tier.
- **Everything time-sensitive (pricing, API scope, tool ownership) drifts fast** —
  re-verify at decision time and record changes in `../CHANGELOG.md`.
