# Pricing & Offers

The in-game store as a conversion funnel: price points, decoys, first-purchase offers,
LTOs, bundles, subscriptions, personalization, and store UX. Its #1 job is turning a
non-payer into a first-time payer; #2 is growing that payer's habit. Pair with
`conversion-funnel.md` and `spend-psychology.md`.

> **Validation gate:** none of this matters until you have retention. If D1 < ~25-27%
> (2024 casual avg), fix the loop first. Monetization amplifies a working loop; it can't
> create one.

## Price points & the currency ladder

**Charm pricing** (.99 endings) — Apple's tiers give it for free. The canonical 5-7 rung
ladder casual games converge on:

| USD | Role |
|---|---|
| $0.99 | Entry / first-purchase floor (the cheapest rung is almost always the most-bought) |
| $1.99 / $4.99 / $9.99 | **Workhorses** — $4.99-9.99 is the value sweet spot |
| $19.99 / $49.99 | Mid/whale |
| $99.99 | **Anchor** — almost exclusively whales; its real job is to make $9.99-19.99 look cheap |

**Gift ratio:** bigger packs give better coin-per-dollar, framed as a "gift." Always
show a high anchor in the layout even if it converts near-zero.

## Decoy & value-framing

- **"Best Value" / "Most Popular" badges** — steering tools, not reports (in a survey,
  only 1 of 8 "Most Popular" badges marked the actually-most-bought pack). Put one badge
  on the rung *you* want sold.
- **Decoy packs** — a deliberately poor-value middle option makes the target look smart.
- **Bonus-coin framing (+20% / +150%)** — arrange base+bonus to maximize the honest %.
  Lead with the biggest truthful number.
- **First-time double** — "DOUBLE the coins at the SAME price," one-time per pack on first
  purchase. Very effective.

## First-purchase offers — the most important section

The first $0.99 conversion matters far more than its revenue: it **anchors all future
spend**, and a player who buys once is **5-10× more likely** to buy again. Well-designed
first-purchase offers correlate with **3-5× higher** payer conversion (vendor-cited,
directional).

- **The $0.99-4.99 starter pack** — obviously superior value, shown early/once (premium
  currency + a booster + sometimes a rare unit).
- **Remove-ads offer** — often the #1 first IAP in hybrid/ad-supported games. 2025 trend:
  *temporary* remove-ads (a duration) alongside permanent.
- **First-time-buyer-only deals** — flagged "one time only."
- **Pricing trap:** devs over-index on conversion and price starters *too low* (DoF: 96%
  would price under $10). Counter-view: under-price the first upgrade and **upsell later**
  — but leave high-tier anchors in the catalog.
- **Timing:** most first purchases land on the **2nd-3rd store visit** — design to bring
  the player back, not to close on visit one.

## LTOs & FOMO

LTOs appear in nearly every top-200 grossing game. Patterns:
- **Countdown timers / flash sales** — a visible closing window.
- **Progressive offers** — each tier unlocks only after buying the prior (Lily's Garden).
- **Scarcity sales** — fixed quantity, vanishes when sold out (Dragon City).
- **Milestone "one-time only" packs** after a level/achievement.
- **Festival/holiday packs** — seasonal, a major LiveOps revenue driver.

Don't build a full *Monopoly GO* event engine for v1 — one recurring timed offer + one
milestone one-time pack is enough.

## Starter packs, bundles & the piggy bank

- **Starter pack** — must-build (see above).
- **Value/growth bundles** — currency + boosters at a framed discount vs buying parts.
- **Piggy bank / coin-accumulator** — premium currency accrues passively through play;
  player **pays real money to "smash" and claim it.** The visible growing total creates
  loss-aversion pressure. Found in ~45% of top puzzle games; proven in *sort* games
  (Hexa Sort $4.99). Mostly a counter + a buy button — **very buildable solo, high ROI.**
  Monopoly GO personalizes both capacity and unlock price per player.

## Subscriptions, VIP & pass pricing

- **Monthly card** (casual workhorse) — **$4.99-9.99/mo**, daily currency drip + perks,
  tuned so the drip slightly exceeds the price → feels free to keep.
- **Battle/season pass** — free + paid track, **$4.99-9.99/season**, in ~60% of top-20%
  grossing games.
- **VIP** — spend-based escalating perks, up to ~$29.99/mo (casino/RPG); don't build a
  multi-tier VIP for v1. iOS auto-renewing subs need StoreKit + App Review scrutiny.

## Personalization & PPP

- **Rules-based segmentation** (achievable solo, high ROI): define 3-4 segments
  (non-payer / minnow / dolphin / whale, or just "has-paid vs not") and swap which offer
  surfaces. That's `if`-statements over local analytics, **not ML.** Do this.
- **Full AI/ML dynamic pricing** — over-engineering for v1; skip.
- **PPP / regional pricing** — Apple auto-converts but **ignores purchasing power**,
  leaving India/Brazil/SEA/Turkey 2-3× too high. Manually set lower tiers there
  (`country_price ≈ (PPP_country/PPP_base) × base_price`, rounded to a valid tier); devs
  commonly cut 80-85%. One-time config, outsized conversion upside, genuinely solo-sized.

## Store UX

The **contextual "moment of need" pop-up is the highest-converting placement** — surface
a coins/booster bundle **right after a loss/death** (out of moves, lost a battle, out of
lives). *Royal Match* runs on exactly this (IAP ARPDAU ~$0.17 vs Candy Crush ~$0.11). The
post-death offer is usually a *bundle* (currency + the exact booster that would've
helped), not raw currency. Seed reasons to reopen the store (free daily gift) since first
buys land on visit 2-3.

## Solo-dev build order (anti-scope-creep)
1. $0.99 starter pack + remove-ads (highest ROI, smallest build)
2. Canonical ladder + "Best Value" badge + first-time-double
3. Contextual "out of moves → buy" pop-up (the core monetization moment)
4. Piggy bank
5. $4.99 monthly card or battle pass (once retention proven)
6. Manual PPP pricing (config, not code)
7. Rules-based "has-paid vs not" offer swapping
**Defer:** AI/ML pricing, full event engines, multi-tier VIP, build-your-own-bundle.

## Sources
DoF Starter Pack Pricing (Apr 2024) · Naavik Royal Match · GameRefinery IAP mechanics ·
Game Developer (currency pricing trends, IAP packs) · Gamigion (10 monetization
features) · Theria/Pocket Tactics (Monopoly GO piggy bank) · Liftoff 2025 · Adjust (AI) ·
Apple/PricePush/Mirava (pricing tiers, PPP) · Appcharge · AdrianCrook (subs). Full URLs
in CHANGELOG notes.
