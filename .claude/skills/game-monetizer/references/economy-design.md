# Economy Design

The virtual economy that monetization sells into: currencies, faucets/sinks, gacha,
energy/timers, progression gates, and the meta-game that manufactures the *need*. Pair
with `monetization-models.md` (what you sell) and `spend-psychology.md` (why it works).

## The meta-game is the engine (read this first)

**Monetization sells the solution to a need the meta-game manufactures.** The core loop
is fun for free; the meta-game creates the long-term goals (and friction) that IAP and
ads resolve. The chain:

> Meta-game creates a goal (complete the collection / upgrade the gear / finish the
> pass) → progress is gated by currency/energy/time → **that gate is the need** → IAP
> sells the resource, ads offer a slower free alternative, the pass packages a season.

**No meta-game = no manufactured need = nothing to sell.** This is why pure hyper-casual
collapsed to ads-only and hybrid-casual (with a meta) now dominates. **Block Blast**
(pure block puzzle, no meta) earns ~$17.5M/mo from ads but only ~$66K *lifetime* IAP —
proof a thin-meta game *cannot* force IAP. The 2026 formula: **Casual core loop +
mid-core meta progression + LiveOps.**

**Solo-dev rule:** before designing any IAP, design **one meta progression system** (a
collection, an upgrade tree, a base to build) that gives players a reason to return
tomorrow. Build the *need* first, then the *purchase* that satisfies it. Until a meta
exists, ship **ads-first** (see `ad-monetization.md`).

## Currencies

- **Soft currency** — low-value, earned by playing (coins/gold). Runs routine sinks
  (upgrades, retries).
- **Hard / premium currency** — scarce, high-value, **the primary thing you sell**
  (gems/diamonds). Trickled free, bought in bulk; gates the best content and gacha.

**Count systems:** single (simplest, limits price discrimination, hard to obscure value)
· **dual (soft + hard) = the F2P standard** (soft for the loop, hard for monetization) ·
triple+ (adds event/seasonal/guild currencies — powerful for LiveOps and obscuring value
but a **complexity tax**; only add when a feature needs its own loop).

**The currency-layer trick** (why premium currency obscures real money): real money →
gems → item inserts a psychological buffer; players track "gems," not dollars. Three
deliberate effects: (1) **decoupling** real money from spend (less pain), (2) **false
sense of wealth** (big gem numbers feel abundant), (3) **leftover-balance trap** — pack
sizes never match item prices, so a dangling remainder ("you have 50, this costs 60")
nudges the next purchase.

## Faucets & sinks

- **Faucet/tap** = where currency enters (level rewards, daily login, ad rewards, IAP).
- **Sink** = where it leaves (upgrades, gacha, retries, cosmetics, timer-skips).
- Healthy when **sources ≈ sinks** at the intended earn/buy ratio: give *just enough*
  free resource to make sinks attractive, *scarce enough* to motivate play + purchase.
- **Inflation** = faucets outpace sinks → players hoard, currency loses meaning, IAP
  value collapses. Control by scaling sinks as players progress (exponential upgrade
  costs, new content) and gating with premium currency so soft-currency inflation never
  touches real revenue. Keep **hard-currency faucets stingy and predictable.**
- **Model before launch:** even a spreadsheet projecting "currency earned vs spent over
  30 levels" catches most balance bugs. (Tools: Machinations.io.)

## Core monetization mechanics

**The convenience → cosmetics → P2W spectrum** (your ethical/retention dial):
- **Pay for convenience/acceleration** (skip timers, refill energy, instant complete) —
  lowest backlash, doesn't break fairness. **Best default for casual.**
- **Pay for cosmetics** — beloved, low-backlash, but monetizes well only with identity/
  social investment (weak in solo casual).
- **Pay-to-win** — highest ceiling in competitive games, **highest churn/backlash**;
  avoid for a first casual/hybrid title.

**Gacha / loot boxes + pity:** randomized reward purchases. **Pity is now standard and
legally required in several markets:** *soft pity* (drop rate ramps after a threshold,
e.g. ~pull 75), *hard pity* (guaranteed at a ceiling, e.g. pull 90). Pity caps bad luck
(protects players, reduces refunds/regulatory heat) and — counterintuitively — makes
players pull *more* because the bounded downside feels safe. **If you use gacha,
implement pity + disclose odds from day one** (Apple/Google require it; see
`ethics-compliance-and-platform-rules.md`). For a first title, approach gacha cautiously.

**Energy / lives / timers:** a meter depletes per play/fail and recharges over real
time; when empty you wait, watch an ad, or pay. Monetizes **impatience** (hyperbolic
discounting), forms habit (come back when refilled), and paces content. **But:** energy
*caps engagement, which also caps your ad impressions* — "monetization alone is a bad
reason to add energy." In hybrid-casual it's mainly useful as a clean **ad-watch-moment
generator** (refill via rewarded video).

**Progression gates/walls:** points where the free path slows and the paid/ad path
accelerates past. Effective but **the #1 churn risk** if unfair — tune so the wall
*nudges*, doesn't *block*.

## Solo-dev economy stack (v1)
Dual currency (soft runs the loop, premium is what you sell, pack sizes deliberately
mismatched) → one meta progression system as the need-generator → convenience-only
spend (timer skips, extra lives, boosters) with a rewarded-ad alternative to every paid
skip → track faucets vs sinks in a spreadsheet before tuning live. Defer multi-currency,
gacha, and deep economies until the meta and retention are proven.

## Sources
GameDeveloper (currency types, premium currency, "A Cake Recipe") · Machinations.io ·
Mobile Free To Play (energy) · MWM/dotgg (pity) · arXiv:2312.10205 (monetizing
impatience) · Airflux/Game Growth Advisor (meta-systems) · Balancy/Udonis (Block Blast).
Full URLs in CHANGELOG notes.
