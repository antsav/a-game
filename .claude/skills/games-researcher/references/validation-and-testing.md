# Validation & Testing Methodology

How studios decide whether a hyper/hybrid-casual concept is worth building — and the
2025-2026 benchmark numbers to judge against. Use this to score candidates and to
design a cheap kill-fast validation plan.

> **Reliability warning, read once:** Almost every absolute number below comes from
> aggregator blogs and varies **2-10× by genre, platform, geo, UA source, and report
> methodology.** Most "2025" reports run on 2024 impression data. iOS-vs-Android and
> tier-1-vs-emerging swings dwarf genre differences — **always segment by platform +
> geo before judging a number.** Treat these as calibration ranges, not pass/fail
> gates. Publishers (Voodoo, Kwalee, SayGames) deliberately do **not** publish hard
> thresholds; the named numbers are industry benchmarks, not any one publisher's cutoff.

## Table of contents
1. The stage-gate funnel
2. CPI test (the core greenlight gate)
3. Marketability / creative (CTR + IPM) testing
4. Retention & engagement gates
5. Hybrid-casual economics — why validation changed
6. Benchmark tables (CPI, CTR/IPM, retention, ARPDAU, eCPM, ROAS)
7. Solo-dev validation without a UA budget
8. Publisher funnels & how the pros gate

---

## 1. The stage-gate funnel

The industry funnel, kill-fast at each gate:

**Idea → CTR pre-test → CPI / marketability test → prototype (retention) test → soft launch → scale**

- **CTR pre-test** (cheapest): run a fake/concept ad on Meta link-click traffic before
  building anything. Aim **CTR ≥ 4%**. Kills bad concepts for ~$50.
- **CPI / marketability test:** 1-2 polished levels + ad creative (no ads/IAP in the
  build), Android-first (iOS far costlier). Read CPI + IPM. **First real kill gate.**
- **Prototype / retention test:** fuller build. Modern bar (Kwalee, 2024) is a
  **30-60 min / 20-30 level** playable measuring **D1 and D3** retention —
  "a low CPI alone is no longer sufficient." **Second kill gate.**
- **Soft launch:** limited geos, monitored at **D3 / D7 / D30**. Decide scale vs kill.
- **Scale:** only once retention + monetization are stable; iterate 10-15 fresh ad
  creatives/week and step budget up while watching ROAS.

Gates are **traded against each other**, not independent: strong retention rescues a
borderline CPI (SayGames' *Draw the Line* launched at CPI $0.38, above target, but 51%
D1 → validated and scaled).

---

## 2. CPI test (the core greenlight gate)

You cut an ad creative for a concept (sometimes before the game is fully built), run a
small paid campaign, and read the install economics.

- **Classic hyper-casual greenlight:** CPI **< $0.30** (Supersonic, 2021). Still
  parroted in 2025-2026 but **stale and HC-era** — use with care.
- **Voodoo competition bar:** Android CPI **< $0.20** + D1 > 30%; iOS CPI **< $0.30**.
- **The trap:** that $0.30 is a *test-campaign target on cheap early traffic*, NOT what
  you pay at scale. 2025-2026 **market-average** casual CPI is 3-8× higher (see table).
  Keep "test CPI" and "scaled-UA CPI" separate or you'll mis-judge.
- **Test mechanics (industry norm):** ~**$50/day for 4-6 days** per concept; Meta's
  learning phase eats the first 3-4 days before CPI stabilizes. Android-first.
- **Companion metric — APPU** (Average Playtime Per User, cumulative): D7 target
  **> 2,000 sec (~33 min)**, used as a pre-monetization LTV proxy.

---

## 3. Marketability / creative (CTR + IPM) testing

Test the **ad creative** before committing to the full game — Supersonic, Voodoo, and
Kwalee all run a named "marketability test" that *precedes* heavy build.

- **CTR:** cheap early gate ≥ **4%** on Meta link-click. Feed-CTR benchmarks: TikTok
  in-feed 0.8-2.5% (good > 2.5%), Meta feed 0.5-1.5% (good > 1.5%). Apple Search Ads
  CTR is structurally higher (5-15%, search intent) — not comparable to feed CTR.
- **IPM (Installs Per Mille):** the headline marketability metric — higher IPM = stronger
  marketability. Useful rule: `eCPM ≈ IPM × CPI`. HC survival signal is high IPM
  (~15-30+). **Weak metric** — few public absolute numbers; use as a *relative*
  creative-testing signal, and note Android IPM > iOS universally.
- **Creative format edge:** **playables convert 2-4× video** on IAP-heavy hybrids and
  cut CPI ~20-30%. AI-generated creatives are now ~56% of top-100 games' ads — cheap
  creative production is a solo-dev advantage.

---

## 4. Retention & engagement gates

Two different retention regimes — **don't mix them:**
- **All-installs medians** (GameAnalytics, 2024 data, includes organic/low-quality):
  D1 median ~22%, top-25% 26-33% (iOS higher), top-10% ~40%; D7 median ~3.4-4%,
  top-25% 7-8%, top-10% ~12%.
- **Paid-UA cohorts** (Admiral): D7 avg 15-20%, top-quartile 25%+, < 10% below average.

**Practical go/no-go gates:**

| Gate | Hyper-casual | Hybrid-casual |
|---|---|---|
| D1 retention | ≥ 38% (Android) / 30%+ | 35-45% |
| D7 retention | ≥ 10-12% | 15-22% (< 10% = core loop broken, do not scale) |
| D30 retention | ~3-5% | ~8-12% |
| D7 APPU (playtime) | > 2,000 sec | > 2,000 sec |
| Viability rule of thumb | — | D1 > 30% **and** D30 > 4% → unit economics likely viable |

Engagement context (GameAnalytics 2024): median daily playtime ~22 min, session 5-6
min (top-25% 8-9 min), ~4 sessions/day (midcore 6-7).

---

## 5. Hybrid-casual economics — why validation changed

**Why pure hyper-casual broke (post-IDFA/ATT, 2021+):** HC was an ad-arbitrage machine
— buy cheap precisely-targeted installs, show interstitials, pocket the spread. ATT
broke all three legs: attribution became guesswork, CPIs rose, CPMs fell. Pure HC is
projected **< 5% of casual revenue by 2027** (down from ~12% in 2022).

**Why hybrid won:** higher retention → longer monetization window → tolerates higher
CPI; IAP adds a high-value long tail ads can't reach (~28% higher ARPU than ad-only;
+25% D90 ARPU on iOS midcore). Hybrid IAP grew +67% YoY (Q1 2025) → ~100% (Q2 2025).

**The validation shift — single-number test → multi-horizon unit economics:**

| Hyper-casual (old) | Hybrid-casual (now) |
|---|---|
| CPI vs same-session ad RPI | **LTV** (blended ad+IAP, projected to D90+) vs **CAC** |
| Day-0/1 arbitrage spread | **ROAS by horizon** (D7 / D30 / D90) |
| "Did it go viral cheaply?" | **Payback window** (cumulative revenue = CPI when?) |
| Single revenue stream (ads) | **Blended** (model ad + IAP curves separately) |
| Kill/keep in days | Soft-launch over weeks; judge curve + early ARPDAU + payer conv. |

**The trap:** a D7 snapshot lies. IAA-only games show up to 40% higher D7 ROAS but
lose that lead by D30 as IAP keeps accruing. **Measure the window that matches your
monetization.** Break-even ROAS = 1 ÷ profit margin (25% margin → need 400% ROAS).
Payback: ad-driven ~30 days; IAP-heavy 90-180 days; hybrid in between.

---

## 6. Benchmark tables (2025-2026, US/tier-1 unless noted)

### CPI by genre/platform
| Genre | iOS CPI | Android CPI | Source |
|---|---|---|---|
| Hyper-casual | $0.50-1.50 | $0.25-0.80 (raw bid $0.10-0.30) | Admiral/Udonis 2025 |
| Casual (Singular avg) | $1.41 | $0.14 | Liftoff 2025 (Feb24-Feb25) |
| Casual / Puzzle | $1.50-3.50 | $0.80-2.00 | Admiral 2025 |
| Hybrid-casual puzzle | $2.00-3.50 | ~$0.95+ | Game Growth Advisor 2026 |
| Match-3 | $2.00-5.74 | $1.00-2.50 | Admiral/GGA |
| Midcore RPG | $4.00-12.00 | $2.50-6.00 | Admiral 2025 |
| US/tier-1 overall 2026 | ~$4.22 avg (NA ~$5) | ~$2.97 avg | GGA Mar 2026 |

CPIs rose **15-20% YoY** on Meta/TikTok; iOS often >4× Android. **Sources conflict
3-10×** (e.g. Udonis casual $2.23 iOS vs Liftoff $1.41) — trust Liftoff's primary
dataset over single blogs.

### Retention — see §4 table.

### ARPDAU by genre
| Genre | ARPDAU |
|---|---|
| Hyper-casual (ad-only) | $0.03-0.08 |
| Hybrid-casual (blended) | **$0.15-0.50** (non-payers $0.08-0.15 ads + payers +$0.30 IAP) |
| Casual / Puzzle | $0.03-0.10 |
| Midcore / RPG | $0.08-0.20 |
| Strategy / 4X | $0.10-0.35 |
| Social casino | $0.20-0.80+ |

iOS ARPDAU runs up to ~5× Android in the same genre.

### eCPM by format (US, 2024-25 data — ±20% noise, charts often image-gated)
| Format | US iOS | US Android | Tier-1 range |
|---|---|---|---|
| Banner | $0.45 | $0.68 | $0.50-1.50 |
| Interstitial | $14.32 | $14.08 | $5-8 (some sources higher) |
| Rewarded video | $19.63 | $16.49 | $15-30 |

Rewarded = ~62% of mobile-game ad revenue; top titles 50-70% from rewarded.

### ROAS / payback
| Genre | D7 ROAS | D30 ROAS | D90 ROAS |
|---|---|---|---|
| Hyper-casual | 60-80% | 80-100% | 100-120% |
| Casual (IAP+ads) | 20-30% | 50-70% | 90-120% |
| Midcore | 10-20% | 30-50% | 70-100% |

Liftoff paid casual cohorts: **D30 ROAS 47% iOS / 15% Android.** Rule of thumb:
HC must hit ~100% ROAS by D30-D90 (shallow LTV, fast payback); hybrid tolerates a
longer tail. LTV:CAC sanity floor 3:1, but pros gate on ROAS-by-horizon + payback.

---

## 7. Solo-dev validation without a UA budget

**Honest take:** hybrid-casual *economics* are attractive, but its *standard growth
model is paid-UA-driven and hostile to no-budget solos.* You can build a hybrid game
solo; you mostly cannot *scale* one the way Voodoo/Rollic do. Your route to scale is
**organic virality or a publishing deal — not out-spending the factories.**

What's realistic without a UA war chest:
- **Validation doesn't require buying installs.** A small soft-launch (even a few
  hundred organic/cheap-geo installs) reveals the signals that matter: D1/D7 retention
  curve, early ARPDAU, rewarded-ad engagement, early payer conversion.
- **Cheap-geo soft launch** (Canada/Australia/UK/Nordics mirror US behavior at lower
  CPI; avoid India/Brazil for retention reads — cheap installs skew the data).
- **Organic distribution** is the only affordable channel: TikTok/Reels/Shorts (~7-14
  clips/week), ASO (download *velocity* > total installs; big publishers neglect ASO,
  leaving keyword gaps), "oddly-satisfying"/ASMR creative that doubles as ad + organic.
- **Validate "fun" in 2-4 weeks with placeholder art** before committing — standard HC
  discipline and a direct guard against over-building.
- **Use a publisher's public rubric as a free kill-test** even if you never sign:
  Kwalee's stated requirements (4:5 1080×1350 video, 1-2 levels for a CPI read, 20-30
  levels for a retention read, Android-first) + the ~$0.30-0.40 Android CPI and ~38%
  D1 targets let you kill bad concepts cheaply.

---

## 8. Publisher funnels & how the pros gate

- **Voodoo (best-documented proxy):** ~**1,000 prototypes tested/year → ~4 full
  launches (~0.4%) → ~1 hit.** Roughly **1 in 250 tested becomes a real hit**; ~100
  prototypes in progress at any time.
- **Kwalee:** 2022 — 258 concepts tested → 12 launches (~4.7% concept-to-launch; hits
  far rarer). Portal is now **Hitseeker**. Submit a store link / playable; CPI test =
  4:5 1080×1350 video or 1-2 levels; retention test = 20-30 levels + analytics SDK;
  Android-first. Rev-share undisclosed.
- **SayGames:** funnel = Request → SayGreenlight (≤2 weeks, "greenlights studios not
  games") → SayKit SDK + soft launch → global → growth ($30M investment program).
  Explicitly **refuses fixed numeric gates** ("we focus on the big picture"); 2025
  pivot to "fewer projects, deeper partnerships" → wants deeper prototypes closer to
  the real game. Rev-share negotiated per deal.

**Takeaway for scoring candidates:** the pros kill ~99% of concepts. Bias toward
*fast, cheap kill signals* (CTR pre-test, then CPI, then retention) and toward
mechanics with a proven retention ceiling, not novelty for its own sake.

---

## Primary sources (verify on refresh)
Liftoff 2025 Casual Gaming Apps Report · GameAnalytics 2025/2026 benchmarks ·
Tenjin Ad Monetization Benchmark 2025/2026 · Gamigion hybridcasual reports ·
Deconstructor of Fun (Voodoo secret sauce Jun 2024, Habby Jul 2025, State of Mobile
2026) · Game Growth Advisor 2026 · Admiral Media 2025 · Supersonic KPI guide (2021,
stale) · Kwalee & SayGames developer portals · Naavik hybridcasual deep-dive.
