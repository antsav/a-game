---
date: 2026-06-29
type: lesson
tags: [hybrid-casual, ads, iap, sequencing, solo-dev]
---

**Lesson:** For a solo v1 hybrid-casual puzzle/sort/block game, the money is in **ads**,
not IAP. Ship an ads-first stack and add IAP only once a meta layer exists.

**Evidence:** Block Blast (pure block puzzle, no meta) earns ~$17.5M/month from ads vs
~$66K *lifetime* IAP despite 200M+ monthly players (Balancy, Mar 2025; Udonis 2026). The
"45% IAP / 55% ads" hybrid split is achieved only by games with authored levels, a lives
economy, and LiveOps (e.g. Color Block Jam). A thin-meta game **cannot force IAP** — there
is nothing to buy power for. Cross-confirmed by all six research streams (2025-2026).

**How to apply:** v1 = mediation SDK + rewarded revive + delayed interstitial + remove-ads
+ one starter pack. Defer the whole IAP economy until a meta layer exists and D7 retention
clears ~15%. Treat "45/55" as a destination, not a launch assumption.

**Related:** [[ad-monetization]] · [[economy-design]] · [[design-to-metrics]] ·
[[patterns/rewarded-revive]]
