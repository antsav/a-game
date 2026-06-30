# Market Snapshot — Hyper/Hybrid-Casual (iOS)

> **AS OF: 2026-06-29.** This is the refreshable state-of-the-market file. When the
> skill runs, treat anything here older than ~60 days as stale: re-verify the top
> charts, breakout games, and hot mechanics live, then rewrite this file and log the
> change in `../CHANGELOG.md`. Every claim below is dated — keep that discipline.

## The one-paragraph state of play

Pure hyper-casual (single mechanic, ad-only) is structurally broken post-IDFA for
anyone without massive UA scale. The market has consolidated around **hybrid-casual**:
an instantly-comprehensible casual hook + a retention/progression/IAP meta-layer.
Hybrid IAP revenue grew **~80% YoY in 2025** (AppMagic, Feb 6 2026) while hypercasual
downloads *fell* ~3.7% — the category now grows revenue by retaining and monetizing,
not by a download firehose. Total mobile gaming grew just **0.2% YoY in 2025**; hybrid
is taking share, not riding a tide. For a solo dev the viable path is a polished,
distinctively-themed **sort / block / jam puzzle hybrid**, distributed organically
(TikTok + ASO), not paid UA.

## What's winning right now (Q3 2025 → mid 2026)

**Top hybrid-casual titles, Q3 2025** (AppMagic / Gamigion, Oct 30 2025). Top-10
revenue grew **+114% YoY**:

| Game | Publisher | Core mechanic |
|---|---|---|
| Color Block Jam | Rollic (Zynga) | Block puzzle + parking-jam |
| Screwdom | iKame | 3D screw-sort |
| All in Hole | Homa | Eat & grow ("hole") |
| Pocket Champs | Madbox | Multiplayer idle racing |
| Hole People / Knit Out / Crowd Express | Rollic | Sort puzzles (+ parking) |
| Mob Control | Voodoo | Multiplying-gates PvP + card meta |
| Coin Sort | Lion Studios (AppLovin) | Coin sort + merge |

- **Block Blast!** was the download phenomenon — 368M installs in 2025 (+66%), still
  #1 globally in April 2026 (~23.8M installs that month).
- **Freshest mechanic (watch list):** "arrow puzzle" games broke out April 2026 —
  *Arrows: Puzzle Escape* (Miniclip, ~20.9M installs) and *Arrows GO!* (~16.1M) in one
  month (AppMagic, May 4 2026). Earliest-stage, highest-uncertainty opportunity.

## Hot vs saturated mechanics (2025-2026)

**Rising / working:**
- **Sort & organize puzzles** (color/block/screw/coin/yarn) — Sort Puzzle revenue
  **+116% YoY in 2025**. Hottest family; easy to reskin; viral on short-form video.
- **Block puzzle** — fastest-growing hypercasual subgenre.
- **"Jam" / spatial-shuffle** (parking jam, crowd/boarding).
- **Arrow puzzles** — brand-new April 2026 breakout.
- **Merge** — +50% rev YoY, but ~80% of revenue in top-10 titles (winner-take-most).
- **Hole / eat-and-grow**, **arcade-idle** — steady.
- **Action-roguelite + idle-RPG** (Habby lane) — proven, high LTV, high production bar.

**Saturated death-traps for a newcomer:**
- **Survivor-likes / Vampire-Survivors clones** — oversaturated; reviewers report
  burnout. Habby owns the mobile top.
- **Match-3** — flat revenue, capital-intensive LiveOps, owned by King/Playrix tier.
- **Pure ad-only single-mechanic hyper-casual** — broken without huge UA scale.
- **4X / survival-strategy** (Whiteout Survival, Last War) — huge revenue but midcore,
  top-10 hold ~64% of revenue. Not solo-viable.

## Publishers to watch (and study when cloning)

- **Rollic (Zynga/Take-Two)** — dominant in hybrid; held 4 of the Q3 2025 top 10.
  Industrialized puzzle/sort hybrids. **Study first for a puzzle hybrid.**
- **Voodoo** — pivoted hyper→hybrid; Mob Control (PvP + card meta).
- **Homa** — data-driven platform, "arcade idle" pioneer; All in Hole.
- **Supersonic (Unity)**, **Azur** (download volume, ad-heavy), **SayGames**,
  **Lion Studios** (AppLovin UA muscle), **CrazyLabs / Kwalee / Ketchapp** (factories).
- **Habby** — premium template for *deep* hybrid (Survivor.io, Archero 2 ~$27M/mo).
  Learn the template, don't try to match the production bar solo.

## Monetization reality (2026)

- Standard model = hybrid (ads + IAP). Puzzle/merge hybrids ~**45% IAP / 55% ads**;
  action/strategy hybrids skew ~82% IAP.
- **ARPDAU:** hybrid ~$0.15-0.50 blended vs pure hyper-casual ~$0.03-0.08 (4-7×).
- **Rewarded video is the workhorse** — top games get 50-70% of ad revenue from it;
  US eCPM ~$16-20. **Playables convert 2-4× video** and cut CPI ~20-30%.
- **Privacy fallout shapes design:** ATT opt-in ~12-18% for games; SKAN under-reports
  installs ~15-30% and is delayed/aggregated. This is *why* hybrid won — only
  higher-LTV designs (retention + IAP meta) make SKAN-era UA math work. Design
  implication: front-load progression + rewarded-ad economy in the first sessions.
- Side trends: D2C/web-shop revenue +26% YoY (US, external-purchase ruling);
  **AI-generated ad creatives ~56% of top-100 games' ads** (AppMagic 2026) — cheap
  creative production is now table stakes and a solo-dev advantage.

## Confidence & caveats

- **High confidence (primary, dated):** the hyper→hybrid shift, Q3 2025 top-10,
  named breakouts, Rollic dominance, April 2026 arrow-puzzle emergence, privacy/SKAN
  reality. Sources: AppMagic (Feb 6 2026), Sensor Tower, Deconstructor of Fun
  (Feb 2 & Jul 31 2025), Gamigion (Oct 30 2025).
- **Directional only (aggregator blogs, high variance):** all CPI/eCPM/ARPDAU/split
  numbers — see `validation-and-testing.md` for the full benchmark tables and their
  reliability flags. Cross-check against a paid AppMagic/Sensor Tower report before
  betting money.

## Key sources (refresh these first)

- AppMagic — Mobile Landscape Report 2026 (Feb 6 2026) + monthly top-games charts
  (via gamedevreports.substack.com mirror; AppMagic pages are JS-gated)
- Gamigion — Top 10 Hybridcasual quarterly reports
- Deconstructor of Fun — State of Mobile 2026 (Feb 2 2026); Habby deep-dive (Jul 2025)
- Sensor Tower — Top hybridcasual iOS US quarterly
- Naavik — hybridcasual deep-dives (mechanics/case studies; revenue figures age fast)
