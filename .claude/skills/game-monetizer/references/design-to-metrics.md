# Design → Metrics

The monetization metrics and the **concrete design lever that moves each one.** Use this to
diagnose ("ARPDAU is low — what do I change?") and to predict the effect of a design
choice. Pair with `ad-monetization.md` and `pricing-and-offers.md`.

> **Benchmarks vary 2-3× by source** (blended vs payer-only, geo, platform). Treat as
> ranges, not precision. Most "whale = X%" stats trace to a 2014 figure — directional only.

## The metrics and their levers

**ARPDAU** (avg revenue per daily active user) = ad-ARPDAU + IAP-ARPDAU. Hybrid-casual
**$0.15-0.50**; pure puzzle ~$0.08; hypercasual $0.03-0.08.
- *Levers:* more/stronger rewarded placements (revive, 2×); raise interstitial frequency
  *up to the retention cliff*; add a starter pack to lift the IAP component. Move both halves.

**Ad-ARPDAU vs IAP-ARPDAU** — non-payers generate ~$0.08-0.15 via rewarded; payers add
$0.30+ IAP on top.
- *Ad levers:* more rewarded engagement/session; higher-eCPM formats (rewarded > interstitial
  > banner); mediation/waterfall optimization.
- *IAP levers:* introduce a buyable booster/currency the rewarded coins also feed into.

**Conversion rate** (% who ever pay) — light puzzle is low; ~60-70% of F2P players *never*
pay.
- *Levers:* a well-priced **starter pack shown early/once**; **over-deliver on the first
  purchase** (drives the *repeat* rate — the real engine); **remove-ads as a low-friction
  first buy**; ad friction itself (annoy non-payers just enough that $2.99 to remove ads
  feels worth it).

**ARPPU** (avg revenue per *paying* user) — among top puzzle games ARPPU dipped slightly YoY
in 2025, but average first-purchase price rose ~46%.
- *Levers:* price ladders / larger packs; piggy bank (raises basket size); battle/season
  pass; LTOs. ⚠️ Needs a real economy — later-stage work.

**LTV** = ARPDAU × average lifetime (retention-driven).
- *Levers:* **retention is the biggest LTV lever** (longer lifetime multiplies daily
  revenue) — don't over-monetize at the cost of D7. Modern guidance: stop "hunting whales,"
  build an engine that converts *every* player's time.

**Whale concentration** — top 5% of payers ≈ 48% of IAP revenue; top 10% ≈ 64%. Healthier
games have a *flatter* spread.
- *Levers:* high-ceiling offers (big packs, VIP, pass tiers) capture whales — but for a solo
  dev with no whale-courting LiveOps, **bias to the flat spread** (broad cheap offers +
  ads) so revenue isn't fragile.

## Benchmark table (2025-2026, US/tier-1 where noted)

| Metric | Hybrid-casual | Pure puzzle | Hypercasual |
|---|---|---|---|
| Blended ARPDAU | $0.15-0.50 | ~$0.08 | $0.03-0.08 |
| Ad-ARPDAU (non-payers) | $0.08-0.15 | — | — |
| IAP/ads split | ~45/55 | ~30/70 (IAP-light) | 5-15 / 85-95 |
| D7 retention | 18-22% | ~20% | 6-9% |
| D30 retention | ~10% | ~10% | — |
| Rewarded eCPM (US) | $15-20 (up to $40) | same | same |
| Interstitial eCPM (US) | $6-14 | same | same |
| Banner eCPM (US) | <$2 | same | same |
| Rewarded share of ad rev | ~62% | — | — |
| Never-pay share | ~60-70% | — | — |
| Whale: top 5% of payers | ~48% of IAP rev | — | — |
| Rewarded views/user/day (start) | 3-4 | — | — |
| Interstitials/user/day (start) | 5-7 | — | — |

## How to use this
1. **Instrument before monetizing** (GameAnalytics or similar) — you can't tune ARPDAU vs
   retention blind.
2. **Gate monetization depth behind retention** — if D7 < ~15%, fix the loop/meta before
   adding IAP systems.
3. **Diagnose with the lever map** — identify the weak metric, pull its specific lever, A/B
   it, watch D7 doesn't drop. Monetization changes that cost retention usually lose net LTV.

## Sources
Game Growth Advisor 2026 · Gamigion 2025 · AppMagic Monetization Report 2025 · GameAnalytics
(good monetization, Apr 2026) · Juego (ARPDAU benchmarks) · Tenjin 2025/2026 · Udonis · MAF.
Full URLs in CHANGELOG notes.
