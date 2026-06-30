# Game Research — Hyper/Hybrid-Casual Opening Scan — 2026-06-29

*First run of the `games-researcher` skill. Scope: broad market scan + initial candidate
shortlist for a solo, iOS-first, organic-distribution build. Live data pulled
2026-06-29 via bundled scripts + web research.*

## TL;DR

- **The market is hybrid-casual, not pure hyper-casual.** Build a simple hook with a
  light progression + rewarded-ad + modest IAP layer designed in from day one. Pure
  ad-only single-mechanic games are dead for a no-UA-budget solo dev.
- **Top pick: a sort/organize puzzle ("color/block sort") with a fresh theme + meta.**
  It's the hottest, still-rising family (Sort Puzzle revenue +116% YoY 2025), low art
  burden, organic-shareable, and live data shows it breaking cross-geo *right now*.
- **Freshest window: "arrow puzzle"** (broke out Apr 2026) — earliest-stage, highest
  upside, highest uncertainty. Worth a fast concept test.
- **The one risk:** sort puzzles are heating fast and factory publishers (Rollic,
  Grand Games) are already converging — for a first-timer the real danger is being
  **too late**. Differentiation (theme + a meta twist) and speed matter more than polish.
- **Avoid:** match-3, survivor-likes, 4X/strategy, and anything needing paid UA.

## Market snapshot (live, 2026-06-29)

**Live US Top Free (Games)** is dominated by sort/puzzle hooks: Meowdoku, Smash Fest!,
**Block Out! – Color Sort** (#3), Magic Sort!, **Arrows – Puzzle Escape** (#8). **US Top
Grossing** is the incumbent wall (Monopoly GO!, Royal Match, Candy Crush, Gossip Harbor,
Kingshot) — note **none of the Top-Free sort risers appear in Top Grossing yet**: fresh
hooks still in their UA-scaling phase, exactly the window to study.

**Cross-geo convergence signal:** Grand Games A.Ş. (Turkish publisher) has **Block Out!
– Color Sort at #3 in both US and Brazil**, plus Magic Sort! charting in both (#6 US /
#10 BR). One publisher pushing two sort titles into multiple geos = a mechanic with
proven, scaling CPI economics — and a sign the window is mid-stage, not wide open.

**What changed vs. the skill's snapshot:** consistent with `market-snapshot.md` (sort
puzzles hot, Rollic/Grand Games active, arrow-puzzle fresh). Block Out! released
2025-10-31 and is still climbing — confirms the "windows are quarters not weeks" thesis.

| Game | Publisher | Released | Ratings | Signal |
|---|---|---|---|---|
| Block Out! – Color Sort | Grand Games (TR) | 2025-10-31 | ~99k | #3 US **and** BR top free; not yet grossing |
| Arrows – Puzzle Escape | Lessmore (DE) | 2025-08-09 | ~275k | Arrow-puzzle breakout; #8 US top free |
| Magic Sort! | Grand Games (TR) | — | — | Charting US + BR; same-publisher convergence |
| Block Blast! | Hungry Studio | 2022-04-03 | ~2.56M | The block-puzzle giant; saturation reference |

## Candidate shortlist (scored 1-5; higher = better)

| Candidate | Timing | Solo-build | Organic fit | Monetiz. headroom | Competition* | Differentiation | Total | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Color/block sort puzzle** | 4 | 5 | 5 | 4 | 3 | 3 | **24/30** | **Pursue** |
| **Arrow puzzle** | 5 | 5 | 4 | 3 | 4 | 3 | **24/30** | **Pursue (fast test)** |
| Screw-sort puzzle | 3 | 4 | 4 | 4 | 2 | 2 | 19/30 | Park (crowding) |
| Hole / eat-and-grow | 3 | 3 | 4 | 3 | 3 | 3 | 19/30 | Park |
| Merge-2 (standalone) | 2 | 3 | 3 | 4 | 1 | 2 | 15/30 | Kill (winner-take-most) |

*Competition scored inverted: 5 = wide-open, 1 = saturated/winner-take-most.

## Top picks

**1. Color/block sort puzzle (clone-plus).** Proven rising core, lowest art burden
(flat shapes/colors, juicy satisfying feedback), inherently TikTok/ASMR-shareable, and
the meta path is clear (level progression + soft currency + rewarded "undo/extra moves"
+ a couple of starter IAPs → hybrid, ~45% IAP / 55% ads). **The clone-plus angle must be
a distinctive theme + a meta twist**, not a reskin — Grand Games and Rollic already own
the generic version. Lean on "swap-the-meta" or a fresh oddly-satisfying visual identity.

**2. Arrow puzzle (fast concept test).** Freshest breakout (Apr 2026) → earliest window,
least clone competition *today*. Same solo-buildability profile. Higher uncertainty on
whether it has hybrid monetization headroom — test the concept's marketability before
committing, and verify a meta layer is viable.

## Validation plan (kill-fast, before any heavy build)

Match the no-UA-budget reality — validate "fun" and marketability cheaply first:
1. **Concept video → CTR/CPI test** on Meta (US, ~$15-20/day × ~5-6 days, ~$200-300).
   Gate: **CTR > ~4%** and a CPI in the test band (current hybrid-casual iOS target
   ~< $1.80 is a strong signal; > ~$3.50 = kill). No game needed yet — just the ad.
2. **If it passes → thin playable prototype** (~20-30 levels) measuring retention.
   Gates: **D1 ≥ ~38-40%, D7 ≥ ~12-15%** (hybrid target D7 ~20%); **D7 < 10% = core
   loop broken, do not scale.**
3. **Organic soft-launch** in a cheap US-like geo (Canada/Australia/NZ) + ASO + 7-14
   short-form clips/week. Watch retention curve + early rewarded-ad engagement + any
   payer conversion. Only invest further if retention holds for 3-4 weeks.

Don't fall in love with one concept — the pros kill ~99%. Kill fast on a bad CTR/CPI.

## Sources & confidence

- **Live (high confidence, 2026-06-29):** Apple iTunes RSS charts (US + BR top
  free/grossing) and iTunes Search/Lookup metadata, via bundled `apple_charts.py` /
  `app_lookup.py`. Chart positions and app metadata are factual as of pull time.
- **Directional (aggregator-sourced):** all CPI/CTR/retention/ARPDAU benchmark numbers —
  vary 2-10× by source/geo/platform; see `references/validation-and-testing.md` for the
  reliability flags. Cross-check against a paid AppMagic/Sensor Tower report before
  committing money.
- **Market structure (mid-2026):** hyper→hybrid shift, hot/saturated mechanics, publisher
  landscape — from the skill's research references (dated, with sources). Re-verify
  anything time-sensitive at decision time.

*Next run: refresh `market-snapshot.md` if >60 days old; deepen the top candidate with
ad-creative analysis (Meta Ad Library longevity + TikTok Creative Center) and an
AppMagic download estimate.*
