# games-researcher — Concept scouting & validation

**Purpose:** find an emerging hyper/hybrid-casual mechanic **in its moderate-competition
window**, validate it against current market reality, and recommend a concrete "clone-plus"
candidate to build for iOS. Deliverable in the repo is a dated market report + a scored
candidate shortlist.

**Use this lens for:** "what's trending," "is this concept worth building," "what should my
next game be," analyzing publishers (Voodoo, Rollic, Homa, Grand Games…), sizing a market,
sanity-checking an idea, or planning a cheap validation test.

## Calibration (who it's for)

Strong engineer, **zero gamedev experience**, **solo**, **iOS-first**, tiny budget, organic
distribution only (no paid UA war chest). So:
- Bias to mechanics a solo dev can build & ship: **low art burden, simple core loop,
  organic-shareable (TikTok/ASMR-friendly)**. Sort/block/jam/arrow puzzles fit; 4X, match-3,
  Habby-scale roguelites do **not**.
- Distribution must be **organic** (ASO + short-form video) — can't out-spend the factories.
- Push back on scope creep and "invent a new genre" ideas — they break the validate-first
  thesis. Recommend **clone-plus of a proven, still-rising mechanic.**
- The bigger risk for a first-timer is being **TOO LATE**, not too early.

## The workflow it runs

1. **Frame the question** (whole-market scan vs. validate one concept vs. study one publisher).
   Date-stamp everything.
2. **Pull fresh live data** (never skip — references age): Apple Top Free/Grossing/New charts
   (US + an emerging geo like br/in/ph/id); ad intelligence (Meta Ad Library, TikTok Creative
   Center) for target publishers; soft-launch pipeline (mobilegamer.biz); recent (~60 day)
   market reports. Risers in **Top Free but NOT yet Top Grossing** = fresh hooks still scaling
   — the window to study.
3. **Identify candidate mechanics** via the convergence rule: showing up across **3+
   publishers/creatives in ~4–8 weeks, CPI not spiked, no polished version dominating** = a
   real window. For each, name the **fresh-twist angle** (mix-two-loops / swap-the-meta /
   re-theme) and confirm a **hybrid meta path** exists (no meta headroom = dead on arrival).
4. **Score 1–5 on six axes:** trend timing · solo-buildability · organic-distribution fit ·
   monetization headroom · competition (moderate vs winner-take-most) · differentiation.
   Be honest, surface risks, bias toward fast/cheap kill signals (pros kill ~99% of concepts).
5. **Recommend + a kill-fast validation plan:** a CTR/CPI test on a concept video, which geos,
   the metric gates for go/kill — sized for a no-UA-budget solo dev (organic soft-launch, ASO).

## Current findings (2026-06-30 refresh — verify before acting)

- The market is **hybrid-casual, not pure hyper-casual.** Pure ad-only single-mechanic games
  are dead for a no-UA solo dev — design a light progression + rewarded-ad + modest IAP from
  day one.
- **Leading candidate: a calm "arrow puzzle"** (broke out ~Apr 2026) — earliest-stage window,
  matches my taste exactly. **Color/block sort** is the safer sibling (hottest rising family,
  reportedly +116% YoY 2025) but more crowded; a small sort game is a fine feel warm-up.
- **06-30 delta:** the arrow window is now *openly contested* — multiple new clones launched
  the same week — while the two leaders (Arrows – Puzzle Escape ~277k ratings; Block Out! –
  Color Sort past 100k) keep compounding and are **not in Top Grossing yet** (still scaling).
- **The one risk (sharper now):** being **TOO LATE.** Differentiation = the *calm* lane the
  bright/juicy incumbents don't occupy + a gentle growing-world meta. **Speed beats polish.**
  Start the cheap CTR/CPI concept test soon.
- **Avoid:** match-3, survivor-likes, 4X/strategy, anything needing paid UA.

## Data & tooling behind the research (what's real vs a proxy)
- **Free, wired up:** Apple iTunes RSS charts + Search/Lookup (rank/metadata/rating counts) —
  the backbone. Plus a **YouTube view-velocity** script — treat this as a *secondary
  organic-interest proxy* (content demand, useful for TikTok distribution), **NOT** app
  downloads/revenue/retention.
- **Manual (no usable API):** Meta Ad Library (US game ads are UI-only) + TikTok Creative
  Center — for competitor ad-creative longevity.
- **Paid app-intelligence API (hold until the validation gate):** **AppMagic** (Sensor
  Tower's SMB tier, ~$400–1k/mo — 500+ mechanic tags, retention estimates, soft-launch
  detector = best game-scouting fit) or **AppFigures** ($7.99–599.99/mo, cheaper but
  competitor data needs its Partner API add-on). Buy one only to *automate* scanning or
  *size* a serious concept — not before.

> Numbers (CPI/eCPM/ARPDAU/revenue growth, ratings, prices) vary 2–10× by source and drift
> fast. Treat as directional; verify live and cite source + date before betting on them.
