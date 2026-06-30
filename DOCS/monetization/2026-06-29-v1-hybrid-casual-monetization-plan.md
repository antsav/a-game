# v1 Monetization Plan — Hybrid-Casual Sort/Block Puzzle — 2026-06-29

*First run of the `game-monetizer` skill. Scope: the minimum-viable monetization for a
solo, iOS-first v1 of the target genre (puzzle/sort/block). Build-now vs later separated.
Numbers are 2025-2026 aggregator-sourced — directional, verify on your own dashboard.*

## TL;DR

- **v1 money is in ADS, not IAP.** A thin-meta puzzle can't force IAP (Block Blast:
  ~$17.5M/mo ads vs ~$66K *lifetime* IAP). Build a clean ad stack first; add a tiny IAP
  layer second; defer the IAP *economy* until a meta layer exists and D7 ≥ ~15%.
- **The entire v1 stack is 6 things.** Mediation SDK → rewarded revive → delayed
  interstitial → remove-ads → one starter pack → analytics. Nothing more.
- **Gate everything on retention.** If D7 < ~15%, stop and fix the loop/meta — monetization
  can't save a leaky game.
- **The one compliance rule for v1:** ship **no paid randomization** (no loot box/gacha/
  prize wheel). That alone avoids loot-box law and the new min-PEGI-16 (EU) / "M" (AU)
  ratings, and removes your biggest App Store rejection risk.

## v1 build stack (do all, in this order — nothing else)

| # | Build | Price / tuning | Metric it moves | Effort |
|---|---|---|---|---|
| 1 | **Mediation SDK** (AppLovin MAX / Unity LevelPlay / AdMob — pick one) | — | all ad revenue | plumbing, do first |
| 2 | **Rewarded: Continue/Revive** after a fail (opt-in) | cap ~1/session | ad-ARPDAU (#1 lever) | low |
| 3 | **Interstitial** at level transitions | **first-ad delay** (none until ~level 2), start 1/session | ad-ARPDAU | low |
| 4 | **Remove-ads IAP** (non-consumable) | **$2.99-4.99** | conversion (self-sorts payers) | low |
| 5 | **One starter pack** at a planted moment-of-need | **$0.99-4.99**, one-time, over-deliver value | first-purchase conversion | low-med |
| 6 | **Analytics** (GameAnalytics or similar) wired before tuning | retention + funnel events | enables everything | low |

Why this order: ads need zero economy design and pay from day one; remove-ads + starter
pack are the only two IAP types that sell in a thin-meta puzzle; the first IAP self-sorts
payers so you can mute their ads.

See [patterns/rewarded-revive](../../.claude/skills/game-monetizer/patterns/rewarded-revive.md)
and [starter-pack](../../.claude/skills/game-monetizer/patterns/starter-pack.md).

## Defer to Tier 2 (after retention is proven)

- Rewarded **2× rewards** on the win screen (>70% opt-in).
- **Piggy bank** ($4.99) — high ROI, low build, proven in sort games (Hexa Sort). See
  [patterns/piggy-bank](../../.claude/skills/game-monetizer/patterns/piggy-bank.md).
- Optional banner (menus only).

## Defer hard to Tier 3 (needs a meta + LiveOps you don't have solo)

Coin/booster economy · battle/season pass · no-ads subscription · live events / segmented
offers · any whale-courting. These need a meta layer and LiveOps muscle one person can't
run. Don't build them for v1 — it's the scope-creep trap.

## Ad tuning guardrails

- Rewarded: **always opt-in, framed as a gift** ("Watch to revive"); never forced. Start
  ~3-4 rewarded views/user/day.
- Interstitial: short-session puzzles tolerate frequent interstitials, but **always use a
  first-ad delay** (+5-8% D1 at negligible revenue cost). Start ~1/session, step up only
  where retention and revenue grow together.
- **Suppress interstitials + banners for anyone who paid** (remove-ads or any IAP).

## Compliance notes (the guardrails that keep you shippable)

- **No paid randomization in v1** — avoids loot-box law + min PEGI-16/"M" ratings + the
  Apple 3.1.1 odds-disclosure rejection risk entirely.
- **Remove-ads & starter pack via Apple IAP**, currency must not expire, provide restore.
- If you later add a **subscription**: ≥7 days, price shown before purchase, no
  bait-and-switch trial, easy cancel (Apple 3.1.2 — top rejection cause).
- **No disguised ads / fake close buttons / forced reviews.** No *fake* scarcity on the
  starter pack (it must genuinely be one-time).
- The test before each release: *"would the player feel tricked if I explained this out
  loud?"* See
  [ethics-compliance-and-platform-rules](../../.claude/skills/game-monetizer/references/ethics-compliance-and-platform-rules.md).

## Targets to validate against (directional)

Hybrid-casual blended ARPDAU $0.15-0.50; ad-ARPDAU (non-payers) $0.08-0.15; D7 ~18-22%;
rewarded eCPM US ~$15-20. If D7 < ~15%, fix the loop before adding any Tier-2/3 system.

*Next: once a meta progression system (collection / upgrade loop) is designed, revisit for
the Tier-2/3 IAP economy and a piggy-bank + pass plan.*
